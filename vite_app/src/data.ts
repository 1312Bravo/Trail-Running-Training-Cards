import {
  CARD_TYPES,
  DETAIL_SECTION_ORDER,
  type CardType,
  type TrainingCard,
  type WebLibraryData,
} from "./types";

export async function loadLibrary(): Promise<WebLibraryData> {
  const response = await fetch(`${import.meta.env.BASE_URL}data/library.json`);
  if (!response.ok) {
    throw new Error(
      "The public card bundle is missing. Run pnpm prepare:data from vite_app after downloading the validated Drive library.",
    );
  }
  return response.json() as Promise<WebLibraryData>;
}

export function asText(value: unknown): string {
  if (value == null) return "";
  if (typeof value === "string") return value;
  if (typeof value === "number" || typeof value === "boolean") return String(value);
  return "";
}

export function asList(value: unknown): string[] {
  if (!Array.isArray(value)) return [];
  return value.map((item) => asText(item)).filter(Boolean);
}

export function displayText(value: unknown): string {
  return asText(value).replaceAll("_", " ");
}

const LABEL_OVERRIDES: Record<string, string> = {
  cts: "CTS",
  rpe: "RPE",
  utmb: "UTMB",
  vo2max: "VO2max",
};

export function displayLabel(value: unknown): string {
  return displayText(value)
    .replaceAll("-", " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean)
    .map((word) => LABEL_OVERRIDES[word.toLowerCase()] ?? word[0].toUpperCase() + word.slice(1))
    .join(" ");
}

export function philosophyName(data: WebLibraryData, id: string): string {
  return data.philosophies[id]?.name ?? displayLabel(id);
}

export function orderedProfiles(data: WebLibraryData, ids: string[]): string[] {
  const order = Object.keys(data.philosophies);
  return [...ids].sort((left, right) => order.indexOf(left) - order.indexOf(right));
}

export function cardTypeLabel(data: WebLibraryData, type: CardType): string {
  return data.display_config.card_type_labels[type] ?? displayLabel(type);
}

export function cardsOfType(cards: TrainingCard[], type: CardType): TrainingCard[] {
  return cards.filter((card) => card.card_type === type);
}

export function sortCards(data: WebLibraryData, cards: TrainingCard[]): TrainingCard[] {
  const profileOrder = Object.keys(data.philosophies);
  return [...cards].sort((left, right) => {
    const typeOrder = CARD_TYPES.indexOf(left.card_type) - CARD_TYPES.indexOf(right.card_type);
    if (typeOrder) return typeOrder;
    const leftProfile = orderedProfiles(data, left.philosophy_profile_ids ?? [])[0] ?? "";
    const rightProfile = orderedProfiles(data, right.philosophy_profile_ids ?? [])[0] ?? "";
    const profileDelta = profileOrder.indexOf(leftProfile) - profileOrder.indexOf(rightProfile);
    if (profileDelta) return profileDelta;
    return left.title.localeCompare(right.title) || left.id.localeCompare(right.id);
  });
}

export function cardMatchesSearch(data: WebLibraryData, card: TrainingCard, query: string): boolean {
  if (!query.trim()) return true;
  const profileIds = card.philosophy_profile_ids ?? [];
  const tags = card.tags ?? [];
  const haystack = [
    card.title,
    card.slug,
    card.card_type,
    card.summary,
    card.purpose,
    profileIds.join(" "),
    profileIds.map((id) => philosophyName(data, id)).join(" "),
    profileIds.map((id) => id.replaceAll("_", " ").replaceAll("-", " ")).join(" "),
    tags.join(" "),
    tags.map((tag) => tag.replaceAll("_", " ")).join(" "),
    asList(card.suitable_levels).join(" "),
    asText(card.additional_information),
  ]
    .join(" ")
    .toLowerCase();
  const lower = query.toLowerCase();
  return haystack.includes(lower) || haystack.includes(lower.replaceAll("_", " "));
}

export function matchesAllTerms(data: WebLibraryData, card: TrainingCard, terms: string[]): boolean {
  return terms.every((term) => cardMatchesSearch(data, card, term));
}

export function getChildCards(
  data: WebLibraryData,
  cards: TrainingCard[],
  parent: TrainingCard,
  childType: CardType,
): TrainingCard[] {
  const childIds = new Set<string>();
  for (const reference of parent.references ?? []) {
    if (reference.relationship === "child") childIds.add(reference.card_id);
  }
  for (const card of cards) {
    for (const reference of card.references ?? []) {
      if (reference.relationship === "parent" && reference.card_id === parent.id) {
        childIds.add(card.id);
      }
    }
  }

  const reuseConfig =
    childType === "mezzo"
      ? data.macro_mezzo_reuse
      : childType === "micro"
        ? data.mezzo_micro_reuse
        : data.micro_session_reuse;
  const childField =
    childType === "mezzo"
      ? "reused_mezzo_card_id"
      : childType === "micro"
        ? "reused_micro_card_id"
        : "reused_session_card_id";
  const parentField =
    childType === "mezzo" ? "macro_card_id" : childType === "micro" ? "mezzo_card_id" : "micro_card_id";
  for (const entry of reuseConfig.entries) {
    if (entry[parentField] === parent.id && typeof entry[childField] === "string") {
      childIds.add(entry[childField] as string);
    }
  }
  return sortCards(data, cards.filter((card) => card.card_type === childType && childIds.has(card.id)));
}

export function reusedCardIds(
  data: WebLibraryData,
  parentId: string | undefined,
  profileIds: string[],
  childType: CardType,
): Set<string> {
  if (!parentId || !profileIds.length) return new Set();
  const reuseConfig =
    childType === "mezzo"
      ? data.macro_mezzo_reuse
      : childType === "micro"
        ? data.mezzo_micro_reuse
        : data.micro_session_reuse;
  const parentField =
    childType === "mezzo" ? "macro_card_id" : childType === "micro" ? "mezzo_card_id" : "micro_card_id";
  const childField =
    childType === "mezzo"
      ? "reused_mezzo_card_id"
      : childType === "micro"
        ? "reused_micro_card_id"
        : "reused_session_card_id";
  return new Set(
    reuseConfig.entries
      .filter(
        (entry) => entry[parentField] === parentId && profileIds.includes(String(entry.philosophy_profile_id)),
      )
      .map((entry) => entry[childField])
      .filter((id): id is string => typeof id === "string"),
  );
}

export function matchesPhilosophies(
  data: WebLibraryData,
  card: TrainingCard,
  profileIds: string[],
  parentId?: string,
): boolean {
  if (!profileIds.length) return true;
  const childType = CARD_TYPES[Math.min(CARD_TYPES.indexOf(card.card_type), 3)] as CardType;
  const reused = reusedCardIds(data, parentId, profileIds, childType);
  return reused.has(card.id) || profileIds.some((id) => card.philosophy_profile_ids?.includes(id));
}

export function orderedDetailFields(card: TrainingCard): string[] {
  const fields = new Set([...DETAIL_SECTION_ORDER, ...Object.keys(card)]);
  const ordered = [...fields].filter(
    (field) => !["id", "slug", "title", "card_type"].includes(field) && field in card,
  );
  if (card.card_type === "session") {
    const promoted = ["session_family", "workout_blocks"].filter((field) => ordered.includes(field));
    const remaining = ordered.filter((field) => !promoted.includes(field));
    const purposeIndex = remaining.indexOf("purpose");
    remaining.splice(purposeIndex < 0 ? 0 : purposeIndex + 1, 0, ...promoted);
    return remaining;
  }
  return ordered;
}

export function formatFieldValue(field: string, value: unknown): string {
  const text = asText(value);
  if (field === "recommended_duration_weeks" && text && !/week/i.test(text)) return `${text} weeks`;
  if (field === "recommended_duration_days" && text && !/day/i.test(text)) return `${text} days`;
  return text;
}
