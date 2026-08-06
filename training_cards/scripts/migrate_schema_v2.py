from __future__ import annotations

import ast
from pathlib import Path

from training_cards.json_store import load_card_library_from_json
from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY


REPO_ROOT = Path(__file__).resolve().parents[2]
CARDS_ROOT = REPO_ROOT / "training_cards" / "cards"

CARD_CLASS_NAMES = {"MacroCard", "MezzoCard", "MicroCard", "SessionCard"}


def _literal_list(node: ast.AST) -> list[str]:
    if not isinstance(node, ast.List):
        return []

    values: list[str] = []
    for item in node.elts:
        value = ast.literal_eval(item)
        if not isinstance(value, str):
            raise ValueError("Expected a list of strings in card definition.")
        values.append(value)

    return values


def _string_node(value: str) -> ast.Constant:
    return ast.Constant(value=value)


def _list_node(values: list[str]) -> ast.List:
    return ast.List(elts=[_string_node(value) for value in values], ctx=ast.Load())


def _concat_text(existing: str, additions: list[str]) -> str:
    parts = [existing.strip()] if existing.strip() else []
    parts.extend(addition.strip() for addition in additions if addition.strip())
    return "\n\n".join(parts)


def _format_string(value: str, indent: str) -> str:
    if "\n" in value:
        escaped = value.replace('"""', '\\"""')
        return f'"""{escaped}"""'

    if len(value) > 88:
        return repr(value)

    return repr(value)


def _format_expression(node: ast.AST, indent: str) -> str:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return _format_string(node.value, indent)
        return repr(node.value)

    if isinstance(node, ast.List):
        if not node.elts:
            return "[]"

        child_indent = indent + "    "
        items = ",\n".join(
            f"{child_indent}{_format_expression(item, child_indent)}"
            for item in node.elts
        )
        return "[\n" + items + "\n" + indent + "]"

    if isinstance(node, ast.Tuple):
        if not node.elts:
            return "()"

        child_indent = indent + "    "
        items = ",\n".join(
            f"{child_indent}{_format_expression(item, child_indent)}"
            for item in node.elts
        )
        trailing = "," if len(node.elts) == 1 else ""
        return "(\n" + items + trailing + "\n" + indent + ")"

    if isinstance(node, ast.Call):
        func = _format_expression(node.func, indent)
        child_indent = indent + "    "
        parts = []
        for arg in node.args:
            parts.append(_format_expression(arg, child_indent))
        for kw in node.keywords:
            assert kw.arg is not None
            parts.append(f"{kw.arg} = {_format_expression(kw.value, child_indent)}")
        if not parts:
            return f"{func}()"

        joined = ",\n".join(f"{child_indent}{part}" for part in parts)
        return f"{func}(\n{joined}\n{indent})"

    return ast.unparse(node)


def _format_module_source(tree: ast.Module) -> str:
    import_lines = []
    body_lines = []
    seen_body = False

    for statement in tree.body:
        if isinstance(statement, (ast.Import, ast.ImportFrom)) and not seen_body:
            import_lines.append(ast.unparse(statement))
            continue

        seen_body = True
        if isinstance(statement, ast.Assign) and len(statement.targets) == 1:
            target = _format_expression(statement.targets[0], "")
            value = _format_expression(statement.value, "")
            body_lines.append(f"{target} = {value}")
        else:
            body_lines.append(ast.unparse(statement))

    source_parts = []
    if import_lines:
        source_parts.append("\n".join(import_lines))
    if body_lines:
        source_parts.append("\n\n".join(body_lines))

    return "\n\n".join(source_parts) + "\n"


def _transform_card_call(call: ast.Call) -> None:
    keywords = {kw.arg: kw for kw in call.keywords if kw.arg is not None}

    goal_context = _literal_list(keywords.get("goal_race_context").value) if "goal_race_context" in keywords else []
    if "when_to_choose" in keywords:
        goal_context.extend(_literal_list(keywords["when_to_choose"].value))
        del keywords["when_to_choose"]
    if goal_context:
        keywords["goal_race_context"] = ast.keyword(arg="goal_race_context", value=_list_node(goal_context))

    training_profile = _literal_list(keywords.get("training_profile").value) if "training_profile" in keywords else []
    if "training_characteristics" in keywords:
        training_profile.extend(_literal_list(keywords["training_characteristics"].value))
        del keywords["training_characteristics"]
    if "terrain_demands" in keywords:
        training_profile.extend(_literal_list(keywords["terrain_demands"].value))
        del keywords["terrain_demands"]
    if training_profile:
        keywords["training_profile"] = ast.keyword(arg="training_profile", value=_list_node(training_profile))

    watchouts = _literal_list(keywords.get("watchouts").value) if "watchouts" in keywords else []
    for legacy_name in ("when_not_to_choose", "common_mistakes", "warning_signs"):
        if legacy_name in keywords:
            watchouts.extend(_literal_list(keywords[legacy_name].value))
            del keywords[legacy_name]
    if watchouts:
        keywords["watchouts"] = ast.keyword(arg="watchouts", value=_list_node(watchouts))

    if "detailed_description" in keywords:
        description = ast.literal_eval(keywords["detailed_description"].value)
        if not isinstance(description, str):
            raise ValueError("Expected detailed_description to be a string.")
        del keywords["detailed_description"]
        existing_info = ""
        if "additional_information" in keywords:
            existing_info = ast.literal_eval(keywords["additional_information"].value)
            if not isinstance(existing_info, str):
                raise ValueError("Expected additional_information to be a string.")
        keywords["additional_information"] = ast.keyword(
            arg="additional_information",
            value=_string_node(_concat_text(existing_info, [description])),
        )

    if any(name in keywords for name in ("intensity_guidance", "execution_notes", "recovery_requirements")):
        session_additions: list[str] = []
        for label, legacy_name in (
            ("Intensity guidance", "intensity_guidance"),
            ("Execution notes", "execution_notes"),
            ("Recovery requirements", "recovery_requirements"),
        ):
            if legacy_name in keywords:
                values = _literal_list(keywords[legacy_name].value)
                if values:
                    session_additions.append(f"{label}: " + "; ".join(values))
                del keywords[legacy_name]

        if session_additions:
            existing_info = ""
            if "additional_information" in keywords:
                existing_info = ast.literal_eval(keywords["additional_information"].value)
                if not isinstance(existing_info, str):
                    raise ValueError("Expected additional_information to be a string.")
            keywords["additional_information"] = ast.keyword(
                arg="additional_information",
                value=_string_node(_concat_text(existing_info, session_additions)),
            )

    call.keywords = list(keywords.values())


class SchemaMigrator(ast.NodeTransformer):
    def visit_Call(self, node: ast.Call) -> ast.AST:
        self.generic_visit(node)
        func_name = None
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

        if func_name in CARD_CLASS_NAMES:
            _transform_card_call(node)

        return node


def transform_card_file(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    new_tree = SchemaMigrator().visit(tree)
    ast.fix_missing_locations(new_tree)
    new_source = _format_module_source(new_tree)
    if new_source != source:
        path.write_text(new_source, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed_files: list[Path] = []
    for path in sorted(CARDS_ROOT.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        if transform_card_file(path):
            changed_files.append(path)

    from training_cards.cloud_store import export_seed_library_to_cache

    export_seed_library_to_cache()
    load_card_library_from_json(GOOGLE_DRIVE_LIBRARY.local_cache_dir)

    print(f"Updated {len(changed_files)} card files.")
    for path in changed_files:
        print(path.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
