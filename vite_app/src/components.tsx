import { useEffect, useRef, type ReactNode } from "react";
import DOMPurify from "dompurify";
import { marked } from "marked";
import {
  asList,
  asText,
  displayLabel,
  displayText,
  formatFieldValue,
  orderedProfiles,
  philosophyName,
} from "./data";
import type { CardType, TrainingCard, WebLibraryData } from "./types";

const PIP_COUNTS: Record<CardType, number> = { macro: 4, mezzo: 3, micro: 2, session: 1 };

export function CardPips({ type }: { type: CardType }) {
  return (
    <span className="preview-card-pips" aria-hidden="true">
      {Array.from({ length: PIP_COUNTS[type] }, (_, index) => (
        <span className="preview-card-pip" key={index}>★</span>
      ))}
    </span>
  );
}

export function TagLabels({
  tags,
  selectedTags,
  onToggle,
  footer = false,
}: {
  tags: string[];
  selectedTags: string[];
  onToggle: (tag: string) => void;
  footer?: boolean;
}) {
  if (!tags.length) return null;
  return (
    <div className={footer ? "preview-footer-tags" : "preview-tag-labels"}>
      {tags.map((tag) => (
        <button
          type="button"
          key={tag}
          className={`tag-link ${selectedTags.includes(tag) ? "is-active" : ""}`}
          onClick={() => onToggle(tag)}
          title={`Filter by ${displayText(tag)}`}
        >
          {footer ? displayLabel(tag) : displayLabel(tag)}
        </button>
      ))}
    </div>
  );
}

export function CardPreview({
  card,
  data,
  onOpen,
  onSelect,
  selectLabel,
  selectedTags,
  onToggleTag,
  compact = false,
}: {
  card: TrainingCard;
  data: WebLibraryData;
  onOpen: (card: TrainingCard) => void;
  onSelect?: (card: TrainingCard) => void;
  selectLabel?: string;
  selectedTags: string[];
  onToggleTag: (tag: string) => void;
  compact?: boolean;
}) {
  const fields = [
    "summary",
    "purpose",
    "suitable_levels",
    "goal_race_context",
    "training_profile",
    "philosophy_profile_ids",
  ].filter((field) => data.display_config.preview_fields.includes(field));
  return (
    <article className={`preview-card card-${card.card_type} ${compact ? "preview-card-compact" : ""}`}>
      <div className="preview-card-title">
        <span className="preview-card-title-text">{card.title}</span>
        <CardPips type={card.card_type} />
      </div>
      <div className="preview-action-row">
        <div className={`preview-card-meta preview-card-type-${card.card_type}`}>
          {displayLabel(card.card_type)}
        </div>
        <div className="preview-actions">
          {onSelect && (
            <button className="button button-small" type="button" onClick={() => onSelect(card)}>
              {selectLabel ?? "Select"}
            </button>
          )}
          <button className="text-action" type="button" onClick={() => onOpen(card)}>
            {compact ? "Open full card" : "Open card"}
          </button>
        </div>
      </div>
      {fields.map((field) => {
        const value = card[field];
        if (field === "summary") {
          return value ? <p className="preview-summary" key={field}>{asText(value)}</p> : null;
        }
        if (field === "philosophy_profile_ids") {
          const names = orderedProfiles(data, asList(value)).map((id) => philosophyName(data, id));
          if (!names.length) return null;
          return <PreviewField key={field} label={fieldLabel(data, field)} value={names.join(", ")} />;
        }
        const values = asList(value);
        const text = values.length ? values.map((item) => field === "suitable_levels" ? displayLabel(item) : item).join(", ") : asText(value);
        return text ? <PreviewField key={field} label={fieldLabel(data, field)} value={text} /> : null;
      })}
      <TagLabels tags={card.tags ?? []} selectedTags={selectedTags} onToggle={onToggleTag} footer />
    </article>
  );
}

function PreviewField({ label, value }: { label: string; value: string }) {
  return (
    <div className="preview-field">
      <span className="preview-field-label">{label}:</span>
      <span className="preview-field-value">{value}</span>
    </div>
  );
}

export function CardsGrid({
  cards,
  data,
  onOpen,
  onSelect,
  selectLabel,
  selectedTags,
  onToggleTag,
}: {
  cards: TrainingCard[];
  data: WebLibraryData;
  onOpen: (card: TrainingCard) => void;
  onSelect?: (card: TrainingCard) => void;
  selectLabel?: string;
  selectedTags: string[];
  onToggleTag: (tag: string) => void;
}) {
  return (
    <div className="card-grid">
      {cards.map((card) => (
        <CardPreview
          key={card.id}
          card={card}
          data={data}
          onOpen={onOpen}
          onSelect={onSelect}
          selectLabel={selectLabel}
          selectedTags={selectedTags}
          onToggleTag={onToggleTag}
        />
      ))}
    </div>
  );
}

export function Pagination({
  total,
  pageSize,
  page,
  onChange,
}: {
  total: number;
  pageSize: number;
  page: number;
  onChange: (next: number) => void;
}) {
  const paginationRef = useRef<HTMLDivElement>(null);
  const pageCount = Math.max(1, Math.ceil(total / pageSize));
  const start = total ? page * pageSize + 1 : 0;
  const end = Math.min((page + 1) * pageSize, total);
  const changePage = (next: number) => {
    onChange(next);
    paginationRef.current?.closest("[data-page-start]")?.scrollIntoView({ block: "start" });
  };
  return (
    <div className="pagination" ref={paginationRef}>
      <div className="pagination-status">
        <span>Showing {start}-{end}</span><strong>{total} cards</strong>
      </div>
      <button className="button button-small" type="button" onClick={() => changePage(Math.max(0, page - 1))} disabled={page <= 0}>Previous</button>
      <span className="pagination-page">Page {page + 1} / {pageCount}</span>
      <button className="button button-small" type="button" onClick={() => changePage(Math.min(pageCount - 1, page + 1))} disabled={page >= pageCount - 1}>Next</button>
    </div>
  );
}

export function ProfileFilter({
  data,
  value,
  onChange,
}: {
  data: WebLibraryData;
  value: string[];
  onChange: (ids: string[]) => void;
}) {
  const label = value.length
    ? value.map((id) => philosophyName(data, id)).join(", ")
    : "All coaching philosophies";
  const pickerRef = useRef<HTMLDetailsElement>(null);
  useEffect(() => {
    const dismiss = (event: PointerEvent) => {
      if (pickerRef.current && !pickerRef.current.contains(event.target as Node)) pickerRef.current.open = false;
    };
    const escape = (event: KeyboardEvent) => {
      if (event.key === "Escape" && pickerRef.current?.open) {
        pickerRef.current.open = false;
        pickerRef.current.querySelector("summary")?.focus();
      }
    };
    document.addEventListener("pointerdown", dismiss);
    document.addEventListener("keydown", escape);
    return () => {
      document.removeEventListener("pointerdown", dismiss);
      document.removeEventListener("keydown", escape);
    };
  }, []);
  return (
    <details className="profile-picker" ref={pickerRef}>
      <summary title="Filter by coaching philosophy">{label}</summary>
      <div className="profile-picker-menu">
        {Object.entries(data.philosophies).map(([id, profile]) => (
          <label key={id}>
            <input
              type="checkbox"
              aria-label={profile.name}
              checked={value.includes(id)}
              onChange={(event) => onChange(event.target.checked ? [...value, id] : value.filter((item) => item !== id))}
            />
            <span>{profile.name}</span>
          </label>
        ))}
        {value.length > 0 && <button className="plain-button" type="button" onClick={() => onChange([])}>Clear selection</button>}
      </div>
    </details>
  );
}

export function ActiveFilters({
  tags,
  onRemoveTag,
  terms = [],
  onRemoveTerm,
}: {
  tags: string[];
  onRemoveTag: (tag: string) => void;
  terms?: string[];
  onRemoveTerm?: (term: string) => void;
}) {
  if (!tags.length && !terms.length) return null;
  return (
    <div className="active-filters">
      {tags.map((tag) => <button className="filter-chip" type="button" key={`tag-${tag}`} onClick={() => onRemoveTag(tag)}>{displayText(tag)} ×</button>)}
      {terms.map((term) => <button className="filter-chip" type="button" key={`term-${term}`} onClick={() => onRemoveTerm?.(term)}>{term} ×</button>)}
    </div>
  );
}

export function MarkdownContent({ source, className = "" }: { source: string; className?: string }) {
  const html = DOMPurify.sanitize(marked.parse(source) as string, { USE_PROFILES: { html: true } });
  return <div className={`markdown-content ${className}`} dangerouslySetInnerHTML={{ __html: html }} />;
}

export function Modal({
  children,
  onClose,
  wide = false,
  contentKey,
}: {
  children: ReactNode;
  onClose: () => void;
  wide?: boolean;
  contentKey?: string;
}) {
  const dialogRef = useRef<HTMLDivElement>(null);
  const panelRef = useRef<HTMLDivElement>(null);
  const bodyRef = useRef<HTMLDivElement>(null);
  const closeRef = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (bodyRef.current) bodyRef.current.scrollTop = 0;
  }, [contentKey]);
  useEffect(() => {
    const previousFocus = document.activeElement as HTMLElement | null;
    const oldOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    closeRef.current?.focus();
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
      if (event.key === "Tab") {
        const controls = panelRef.current?.querySelectorAll<HTMLElement>('button:not(:disabled), a[href], input, summary, [tabindex="0"]');
        if (!controls?.length) return;
        const first = controls[0];
        const last = controls[controls.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
      }
    };
    window.addEventListener("keydown", handleKey);
    return () => {
      document.body.style.overflow = oldOverflow;
      window.removeEventListener("keydown", handleKey);
      previousFocus?.focus({ preventScroll: true });
    };
  }, [onClose]);
  return (
    <div className="modal-backdrop" onMouseDown={(event) => { if (event.target === dialogRef.current) onClose(); }} ref={dialogRef}>
      <div className={`modal-panel ${wide ? "modal-wide" : ""}`} role="dialog" aria-modal="true" aria-label="Card library details" ref={panelRef}>
        <button className="modal-close" type="button" aria-label="Close dialog" onClick={onClose} ref={closeRef}>×</button>
        <div className="modal-body" ref={bodyRef}>{children}</div>
      </div>
    </div>
  );
}

export function fieldLabel(data: WebLibraryData, field: string): string {
  return data.display_config.field_labels[field] ?? field.split("_").map((part) => part[0]?.toUpperCase() + part.slice(1)).join(" ");
}

export function formatDetailValue(field: string, value: unknown, data: WebLibraryData): string | string[] {
  if (field === "philosophy_profile_ids") {
    return orderedProfiles(data, asList(value)).map((id) => philosophyName(data, id));
  }
  if (Array.isArray(value)) {
    return value.map((item) => field === "suitable_levels" ? displayLabel(item) : asText(item));
  }
  return formatFieldValue(field, value);
}
