import { CARD_TYPES, type TrainingCard, type WebLibraryData } from "./types";

const cache = new WeakMap<WebLibraryData, Map<string, Map<string, string>>>();

export function normalizeSearch(value: string): string {
  return value.toLowerCase().replaceAll(/[_-]/g, " ").replaceAll(/\s+/g, " ").trim();
}

// Index only real hierarchy edges within each philosophy's accepted library.
// A shared session can have different phase context in different philosophies.
function buildContexts(data: WebLibraryData): Map<string, Map<string, string>> {
  const result = new Map<string, Map<string, string>>();
  const cards = new Map(data.cards.map((card) => [card.id, card]));
  const reuse = [
    [data.macro_mezzo_reuse, "macro_card_id", "reused_mezzo_card_id"],
    [data.mezzo_micro_reuse, "mezzo_card_id", "reused_micro_card_id"],
    [data.micro_session_reuse, "micro_card_id", "reused_session_card_id"],
  ] as const;

  for (const profile of Object.keys(data.philosophies)) {
    const members = new Set(data.cards.filter((card) => card.philosophy_profile_ids.includes(profile)).map((card) => card.id));
    for (const level of CARD_TYPES) {
      for (const entry of data.card_library_index.levels[level]?.[profile] ?? []) members.add(entry.card_id);
    }
    const parents = new Map<string, Set<string>>();
    const add = (parentId: string, childId: string) => {
      const parent = cards.get(parentId);
      const child = cards.get(childId);
      if (!parent || !child || !members.has(parentId) || !members.has(childId)) return;
      if (CARD_TYPES.indexOf(child.card_type) !== CARD_TYPES.indexOf(parent.card_type) + 1) return;
      if (!parents.has(childId)) parents.set(childId, new Set());
      parents.get(childId)!.add(parentId);
    };
    for (const card of data.cards) {
      for (const reference of card.references ?? []) {
        if (reference.relationship === "parent") add(reference.card_id, card.id);
        if (reference.relationship === "child") add(card.id, reference.card_id);
      }
    }
    for (const [config, parentField, childField] of reuse) {
      for (const entry of config.entries) {
        if (entry.philosophy_profile_id === profile) add(String(entry[parentField]), String(entry[childField]));
      }
    }
    const contexts = new Map<string, string>();
    for (const id of members) {
      const ancestors = new Set<string>();
      const pending = [...(parents.get(id) ?? [])];
      while (pending.length) {
        const ancestor = pending.pop()!;
        if (ancestors.has(ancestor)) continue;
        ancestors.add(ancestor);
        pending.push(...(parents.get(ancestor) ?? []));
      }
      contexts.set(id, normalizeSearch([...ancestors].map((ancestor) => {
        const card = cards.get(ancestor)!;
        return [card.title, card.slug, ...card.tags].join(" ");
      }).join(" ")));
    }
    result.set(profile, contexts);
  }
  return result;
}

export function cardSearchContext(data: WebLibraryData, card: TrainingCard, profiles: string[]): string {
  if (!cache.has(data)) cache.set(data, buildContexts(data));
  const contexts = cache.get(data)!;
  return (profiles.length ? profiles : [...contexts.keys()])
    .map((profile) => contexts.get(profile)?.get(card.id) ?? "").join(" ");
}
