import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import ts from "typescript";
import { test } from "node:test";

// Compile these dependency-free TypeScript helpers in memory using the installed compiler.
const modules = new Map();
async function compile(name) {
  if (modules.has(name)) return modules.get(name);
  let code = ts.transpileModule(await readFile(new URL(`../src/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const dependency of ["types", "discovery"]) {
    if (code.includes(`from "./${dependency}"`)) code = code.replaceAll(`from "./${dependency}"`, `from "${await compile(dependency)}"`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(code).toString("base64")}`;
  modules.set(name, url);
  return url;
}
const { cardMatchesSearch, matchesAllTerms, matchesPhilosophies, getChildCards } = await import(await compile("data"));
const dataPath = new URL("../public/data/library.json", import.meta.url);
const data = JSON.parse(await readFile(dataPath, "utf8"));
const byId = new Map(data.cards.map((card) => [card.id, card]));
const sessions = (profile, query = "") => data.cards.filter((card) => card.card_type === "session" &&
  matchesPhilosophies(data, card, [profile]) && cardMatchesSearch(data, card, query, [profile]));

test("Browse finds mainstream base workouts and excludes unrelated quality", () => {
  const ids = sessions("mainstream_endurance", "  BASE  ").map((card) => card.id);
  for (const id of ["session_009", "session_012", "session_078"]) assert.ok(ids.includes(id), id);
  for (const id of ["session_022", "session_024", "session_026", "session_064"]) assert.ok(!ids.includes(id), id);
});

test("Every philosophy includes its explicit shared sessions", () => {
  for (const [profile, entries] of Object.entries(data.card_library_index.levels.session)) {
    assert.deepEqual(sessions(profile).map((card) => card.id).sort(), entries.map((entry) => entry.card_id).sort(), profile);
    assert.ok(sessions(profile, "base").some((card) => card.id === "session_078"), `${profile} benchmark`);
  }
  assert.ok(!sessions("mainstream_endurance").some((card) => card.id === "session_064"));
});

test("Search includes workout options, family labels, and separate AND terms", () => {
  assert.ok(cardMatchesSearch(data, byId.get("session_015"), "elliptical"));
  assert.ok(cardMatchesSearch(data, byId.get("session_028"), "treadmill"));
  assert.ok(matchesAllTerms(data, byId.get("session_009"), ["base", "easy"], ["mainstream_endurance"]));
  assert.ok(!matchesAllTerms(data, byId.get("session_009"), ["base", "elliptical"], ["mainstream_endurance"]));
});

test("A shared card does not inherit another philosophy's phase context", () => {
  const fixture = structuredClone(data);
  const phase = fixture.cards.find((card) => card.id === "macro_024");
  phase.title = "Unique Evoke Foundation";
  phase.tags = ["evoke_only_marker"];
  const shared = fixture.cards.find((card) => card.id === "session_009");
  assert.ok(cardMatchesSearch(fixture, shared, "evoke only marker", ["evoke_endurance"]));
  assert.ok(!cardMatchesSearch(fixture, shared, "evoke only marker", ["mainstream_endurance"]));
  assert.ok(!cardMatchesSearch(fixture, shared, "evoke only marker", ["cts"]));
});

test("Parent-specific filtering and non-hierarchy references preserve their meaning", () => {
  assert.ok(matchesPhilosophies(data, byId.get("session_009"), ["evoke_endurance"], "micro_124"));
  assert.ok(!matchesPhilosophies(data, byId.get("session_009"), ["evoke_endurance"], "micro_065"));
  const fixture = structuredClone(data);
  fixture.cards.find((card) => card.id === "macro_002").references.push({ card_id: "session_024", relationship: "support" });
  assert.ok(!cardMatchesSearch(fixture, fixture.cards.find((card) => card.id === "session_024"), "base", ["mainstream_endurance"]));
});

test("Every week reaches sessions and every session is reachable", () => {
  const reached = new Set();
  for (const week of data.cards.filter((card) => card.card_type === "micro")) {
    const children = getChildCards(data, data.cards, week, "session");
    assert.ok(children.length, week.id);
    children.forEach((card) => reached.add(card.id));
  }
  for (const card of data.cards.filter((card) => card.card_type === "session")) assert.ok(reached.has(card.id), card.id);
});

test("New pipeline stages and explicit shared weeks appear under the intended parents", () => {
  for (const [parent, type, child] of [
    ["macro_039", "mezzo", "mezzo_079"],
    ["mezzo_079", "micro", "micro_178"],
    ["mezzo_079", "micro", "micro_179"],
    ["mezzo_047", "micro", "micro_180"],
    ["mezzo_080", "micro", "micro_181"],
    ["mezzo_080", "micro", "micro_182"],
    ["micro_130", "session", "session_079"],
  ]) {
    assert.ok(getChildCards(data, data.cards, byId.get(parent), type).some((card) => card.id === child), `${parent} -> ${child}`);
  }
  for (const profile of Object.keys(data.card_library_index.levels.macro)) {
    assert.ok(matchesPhilosophies(data, byId.get("mezzo_080"), [profile]), `${profile} heat block`);
  }
});

test("Recovery menus exclude reviewed development sessions", () => {
  for (const [week, excluded] of [["micro_025", "session_030"], ["micro_075", "session_050"],
    ["micro_111", "session_058"], ["micro_135", "session_064"], ["micro_136", "session_064"], ["micro_147", "session_069"]]) {
    assert.ok(!getChildCards(data, data.cards, byId.get(week), "session").some((card) => card.id === excluded), `${week} excludes ${excluded}`);
  }
});

console.log(`Discovery checks use ${fileURLToPath(dataPath)} (${data.cards.length} cards).`);
