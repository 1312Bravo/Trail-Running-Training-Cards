import { CARD_TYPES, type CardType } from "../types";

export interface Placement {
  id: string;
  cardId: string;
  level: CardType;
  start: string;
  end: string;
  parentId: string | null;
}

export const STORAGE_KEY = "run-companion-deck.plan.v1";
export const DRAFTS_STORAGE_KEY = "run-companion-deck.plan-drafts.v1";
export type SavedPathway = Record<CardType, string | null>;
export type PlanDrafts = Record<string, SavedPathway>;
export const LEVEL_NAMES: Record<CardType, string> = {
  macro: "Macro phase", mezzo: "Mezzo block", micro: "Micro week", session: "Session",
};

// Calendar dates stay in local time; UTC conversion can shift a day on some devices.
export function dateKey(date: Date): string {
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
}

export function parseDay(day: string): Date {
  const [year, month, date] = day.split("-").map(Number);
  return new Date(year, month - 1, date, 12);
}

export function validDay(value: unknown): value is string {
  return typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) && dateKey(parseDay(value)) === value;
}

export function addDays(day: string, count: number): string {
  const date = parseDay(day);
  date.setDate(date.getDate() + count);
  return dateKey(date);
}

export function covers(entry: Placement, day: string): boolean {
  return entry.start <= day && day <= entry.end;
}

export function descendantIds(entries: Placement[], id: string): Set<string> {
  const ids = new Set([id]);
  // Depth is small, but use a closure so removals also work with reordered saved data.
  let previousSize = 0;
  while (previousSize !== ids.size) {
    previousSize = ids.size;
    entries.forEach((entry) => { if (entry.parentId && ids.has(entry.parentId)) ids.add(entry.id); });
  }
  return ids;
}

export function placementError(entry: Placement, entries: Placement[]): string {
  if (!validDay(entry.start) || !validDay(entry.end) || entry.start > entry.end) return "Enter valid dates as YYYY-MM-DD, with the end on or after the start.";
  if (entry.level === "session" && entry.start !== entry.end) return "Place a session on a single day.";
  const previousLevel = CARD_TYPES[CARD_TYPES.indexOf(entry.level) - 1];
  const parent = entries.find((item) => item.id === entry.parentId);
  if (previousLevel && (!parent || parent.level !== previousLevel)) return `Add a ${LEVEL_NAMES[previousLevel].toLowerCase()} first.`;
  if (!previousLevel && entry.parentId) return "A macro phase cannot have a parent.";
  if (parent && (entry.start < parent.start || entry.end > parent.end)) return "Keep these dates within the parent period.";
  const outsideChild = entries.some((item) => item.parentId === entry.id && (item.start < entry.start || item.end > entry.end));
  if (outsideChild) return "These dates would leave planned children outside this period. Adjust their dates first.";
  if (entry.level !== "session" && entries.some((item) => item.id !== entry.id && item.level === entry.level && item.start <= entry.end && entry.start <= item.end)) return "Another period at this level already covers those dates. Choose a free range.";
  return "";
}

// Reject unreadable saves without silently overwriting them on mount.
export function decodePlan(raw: string | null): Placement[] {
  if (!raw) return [];
  const saved: unknown = JSON.parse(raw);
  if (!saved || typeof saved !== "object" || !("version" in saved) || saved.version !== 1 || !("placements" in saved) || !Array.isArray(saved.placements)) throw new Error("Unsupported saved plan.");
  const entries: Placement[] = saved.placements.map((value: unknown) => {
    if (!value || typeof value !== "object") throw new Error("Invalid placement.");
    const item = value as Placement;
    if (typeof item.id !== "string" || !item.id || typeof item.cardId !== "string" || !item.cardId || !CARD_TYPES.includes(item.level) || !validDay(item.start) || !validDay(item.end) || !(item.parentId === null || typeof item.parentId === "string")) throw new Error("Invalid placement.");
    return item;
  });
  if (new Set(entries.map((item) => item.id)).size !== entries.length || entries.some((item) => placementError(item, entries))) throw new Error("Invalid plan structure.");
  return entries;
}

export function decodeDrafts(raw: string | null): PlanDrafts {
  if (!raw) return {};
  const saved: unknown = JSON.parse(raw);
  if (!saved || typeof saved !== "object" || !("version" in saved) || saved.version !== 1 || !("drafts" in saved) || !saved.drafts || typeof saved.drafts !== "object" || Array.isArray(saved.drafts)) throw new Error("Unsupported plan selections.");
  const drafts: PlanDrafts = {};
  for (const [day, value] of Object.entries(saved.drafts)) {
    if (!validDay(day) || !value || typeof value !== "object" || Array.isArray(value)) throw new Error("Invalid plan selection.");
    const pathway = value as Partial<SavedPathway>;
    drafts[day] = Object.fromEntries(CARD_TYPES.map((type) => {
      const cardId = pathway[type] ?? null;
      if (cardId !== null && typeof cardId !== "string") throw new Error("Invalid plan selection.");
      return [type, cardId];
    })) as SavedPathway;
  }
  return drafts;
}
