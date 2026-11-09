export type JsonRecord = Record<string, unknown>;

export interface TrainingCard extends JsonRecord {
  id: string;
  slug: string;
  title: string;
  card_type: CardType;
  summary: string;
  purpose: string;
  tags: string[];
  philosophy_profile_ids: string[];
  suitable_levels: string[];
  references: CardReference[];
}

export type CardType = "macro" | "mezzo" | "micro" | "session";

export interface CardReference {
  card_id: string;
  relationship: string;
  tags?: string[];
}

export interface PhilosophyProfile {
  name: string;
  summary: string;
  detail: string;
  sources: string;
}

export interface LibraryEntry extends JsonRecord {
  card_id: string;
  title: string;
  description: string;
  source: "direct" | "reused";
  source_profile?: string;
}

export interface WebLibraryData {
  manifest: JsonRecord & { schema_version: string; library_version: string };
  display_config: JsonRecord & {
    field_labels: Record<string, string>;
    card_type_labels: Record<CardType, string>;
    preview_fields: string[];
  };
  macro_mezzo_reuse: { entries: JsonRecord[] };
  mezzo_micro_reuse: { entries: JsonRecord[] };
  micro_session_reuse: { entries: JsonRecord[] };
  card_library_index: {
    levels: Record<string, Record<string, LibraryEntry[]>>;
  };
  cards: TrainingCard[];
  philosophies: Record<string, PhilosophyProfile>;
}

export const APP_TITLE = "Run & Train with Deck of Cards";
export const APP_MODES = [
  "Browse cards",
  "Today session",
  "Card library",
  "Build pathway",
  "Coaching philosophies",
] as const;
export type AppMode = (typeof APP_MODES)[number];

export const CARD_TYPES: CardType[] = ["macro", "mezzo", "micro", "session"];
export const PAGE_SIZE = 8;
export const LIBRARY_PAGE_SIZE = 10;

export const DETAIL_SECTION_ORDER = [
  "summary",
  "purpose",
  "suitable_levels",
  "recommended_duration_weeks",
  "recommended_duration_days",
  "typical_duration",
  "timing_guidance",
  "placement_guidance",
  "goal_race_context",
  "training_profile",
  "session_family",
  "week_structure",
  "key_sessions",
  "load_pattern",
  "workout_blocks",
  "expected_adaptations",
  "recovery_requirements",
  "watchouts",
  "progression_rules",
  "regression_rules",
  "philosophy_profile_ids",
  "tags",
  "additional_information",
  "references",
];

export const MODE_INFO: Record<AppMode, { intro: string; bullets: string[] }> = {
  "Browse cards": {
    intro: "A flexible deck view for exploring cards across every training level or finding a specific idea quickly.",
    bullets: [
      "Filter by card level, coaching philosophy, or tags.",
      "Search across titles, summaries, purposes, tags, notes, and levels.",
      "Open a card to inspect the full coaching details.",
    ],
  },
  "Today session": {
    intro: "A focused view for choosing a single workout-style session card without browsing the full deck.",
    bullets: [
      "Search session cards by goal, terrain, intensity, or theme.",
      "Add multiple search terms when you want more specific results.",
      "Filter by coaching philosophy or active tag selections.",
      "Open a card when you want the full session structure.",
    ],
  },
  "Card library": {
    intro: "A structured library view for checking how cards are distributed across coaching philosophies and levels.",
    bullets: [
      "Browse cards grouped by coaching philosophy.",
      "Filter by all cards, macro, mezzo, micro, or session cards.",
      "Expand a philosophy group to scan cards and preview details.",
    ],
  },
  "Build pathway": {
    intro: "A guided builder for linking cards into a macro-to-session training sequence.",
    bullets: [
      "Choose one card at each level, from macro to session.",
      "Each step shows related options based on your previous choice.",
      "Use search, tags, and philosophy filters to shape the next choice.",
    ],
  },
  "Coaching philosophies": {
    intro: "A reference view for understanding the coaching philosophies used to organize and interpret the cards.",
    bullets: [
      "Read short summaries of each coaching philosophy.",
      "Use Show cards to browse cards connected to a philosophy.",
      "Open full notes or reviewed sources when you want deeper context.",
    ],
  },
};
