import { useMemo } from "react";
import {
  asList,
  asText,
  displayLabel,
  formatFieldValue,
  orderedDetailFields,
  orderedProfiles,
  philosophyName,
} from "./data";
import { CardPips, TagLabels, fieldLabel } from "./components";
import type { TrainingCard, WebLibraryData } from "./types";

type DetailRecord = Record<string, unknown>;

export function CardDetail({
  card,
  data,
  cardsById,
  history,
  onBack,
  onReference,
  onToggleTag,
  selectedTags,
}: {
  card: TrainingCard;
  data: WebLibraryData;
  cardsById: Map<string, TrainingCard>;
  history: TrainingCard[];
  onBack: () => void;
  onReference: (card: TrainingCard) => void;
  onToggleTag: (tag: string) => void;
  selectedTags: string[];
}) {
  const keyFacts = useMemo(() => {
    const duration =
      asText(card.recommended_duration_weeks) ||
      asText(card.recommended_duration_days) ||
      asText(card.typical_duration);
    const durationField = card.recommended_duration_weeks
      ? "recommended_duration_weeks"
      : card.recommended_duration_days
        ? "recommended_duration_days"
        : "typical_duration";
    const philosophies = orderedProfiles(data, card.philosophy_profile_ids ?? [])
      .map((id) => philosophyName(data, id))
      .join(", ");
    return [
      ["Suitable For", asList(card.suitable_levels).map(displayLabel).join(", ")],
      ["Duration", duration ? formatFieldValue(durationField, duration) : ""],
      ["Philosophy", philosophies],
    ].filter(([, value]) => Boolean(value));
  }, [card, data]);

  const detailFields = orderedDetailFields(card).filter((field) => {
    if (["summary", "suitable_levels", "recommended_duration_weeks", "recommended_duration_days", "typical_duration", "philosophy_profile_ids"].includes(field)) return false;
    const value = card[field];
    return value != null && value !== "" && (!Array.isArray(value) || value.length > 0);
  });

  return (
    <div className={`detail-card detail-${card.card_type}`}>
      <div className={`detail-card-header detail-card-header-${card.card_type}`}>
        <div className="detail-card-title-row"><h2 className="detail-card-title">{card.title}</h2><CardPips type={card.card_type} /></div>
      </div>
      <div className="detail-card-type-line">{displayLabel(data.display_config.card_type_labels[card.card_type])}</div>
      {card.summary && <section className="detail-section detail-section-summary"><div className="detail-section-label">{fieldLabel(data, "summary")}</div><div className="detail-section-value">{card.summary}</div></section>}
      {keyFacts.length > 0 && <section className={`detail-key-facts detail-key-facts-${card.card_type}`}>
        {keyFacts.map(([label, value]) => <div className="detail-key-fact" key={label}><span className="detail-key-fact-label">{label}</span><span className="detail-key-fact-value">{value}</span></div>)}
      </section>}
      {history.length > 0 && <button className="button button-small history-back" type="button" onClick={onBack}>Back to {history[history.length - 1].title}</button>}
      {detailFields.map((field, index) => (
        <DetailSection
          key={field}
          field={field}
          value={card[field]}
          isLast={index === detailFields.length - 1}
          data={data}
          cardsById={cardsById}
          onReference={onReference}
          onToggleTag={onToggleTag}
          selectedTags={selectedTags}
        />
      ))}
    </div>
  );
}

function DetailSection({
  field,
  value,
  isLast,
  data,
  cardsById,
  onReference,
  onToggleTag,
  selectedTags,
}: {
  field: string;
  value: unknown;
  isLast: boolean;
  data: WebLibraryData;
  cardsById: Map<string, TrainingCard>;
  onReference: (card: TrainingCard) => void;
  onToggleTag: (tag: string) => void;
  selectedTags: string[];
}) {
  const sectionClass = `detail-section ${
    field === "additional_information" ? "detail-section-coaching-note" : ""
  } ${isLast ? "detail-section-last" : ""}`;

  if (field === "tags") {
    return <section className={`${sectionClass} detail-section-tags`}><div className="detail-section-label">{fieldLabel(data, field)}</div><TagLabels tags={asList(value)} selectedTags={selectedTags} onToggle={onToggleTag} /></section>;
  }

  if (field === "references") {
    const references = Array.isArray(value) ? value as DetailRecord[] : [];
    return (
      <section className={`${sectionClass} detail-section-references`}>
        <div className="detail-section-label">{fieldLabel(data, field)}</div>
        <div className="detail-reference-list">
          {references.map((reference, index) => {
            const linked = cardsById.get(asText(reference.card_id));
            const label = `${displayLabel(reference.relationship)}: ${linked?.title ?? asText(reference.card_id)}`;
            return linked
              ? <button className="button button-small" type="button" key={`${label}-${index}`} onClick={() => onReference(linked)}>{label}</button>
              : <span className="detail-reference-item" key={`${label}-${index}`}>{label}</span>;
          })}
        </div>
      </section>
    );
  }

  if (field === "session_family" && value && typeof value === "object") {
    const family = value as DetailRecord;
    return (
      <section className={`${sectionClass} detail-section-session-family`}>
        <div className="detail-section-label">{fieldLabel(data, field)}</div>
        <p className="detail-session-family-title">{asText(family.title)}</p>
        {Boolean(family.summary) && <p className="detail-session-family-summary">{asText(family.summary)}</p>}
        {Boolean(family.description) && <p className="detail-session-family-description">{asText(family.description)}</p>}
      </section>
    );
  }

  if (field === "workout_blocks" && Array.isArray(value)) {
    return <WorkoutGuide blocks={value as DetailRecord[]} isLast={isLast} />;
  }

  const values = Array.isArray(value)
    ? field === "philosophy_profile_ids"
      ? orderedProfiles(data, asList(value)).map((id) => philosophyName(data, id))
      : value.map((item) => field === "suitable_levels" ? displayLabel(item) : asText(item))
    : [field === "philosophy_profile_ids" ? "" : formatFieldValue(field, value)];
  return (
    <section className={sectionClass}>
      <div className="detail-section-label">{fieldLabel(data, field)}</div>
      <div className="detail-section-value">
        {values.length > 1 ? <ul className="detail-section-list">{values.map((item, index) => <li key={index}>{item}</li>)}</ul> : values[0]}
      </div>
    </section>
  );
}

function WorkoutGuide({ blocks, isLast }: { blocks: DetailRecord[]; isLast: boolean }) {
  return (
    <section className={`detail-section detail-section-workout-parts ${isLast ? "detail-section-last" : ""}`}>
      <div className="detail-section-label">Workout Guide</div>
      <div className="detail-workout-blocks">
        {blocks.map((block, blockIndex) => {
          const options = Array.isArray(block.options) ? block.options as DetailRecord[] : [];
          return (
            <div className="detail-workout-block" key={blockIndex}>
              <p className="detail-workout-block-title">{displayLabel(block.block_type)}</p>
              <p className="detail-workout-block-mode">{displayLabel(block.execution_mode)}</p>
              {options.map((option, optionIndex) => {
                const notes = [
                  asText(option.repeat) ? `Repeat: ${asText(option.repeat)}` : "",
                  asText(option.selection_notes) ? `Best for: ${asText(option.selection_notes)}` : "",
                  asText(option.load_notes) ? `Load: ${asText(option.load_notes)}` : "",
                ].filter(Boolean);
                const parts = Array.isArray(option.parts) ? option.parts as DetailRecord[] : [];
                return (
                  <div className="detail-workout-option" key={optionIndex}>
                    <p className="detail-workout-option-title">{asText(option.title)}</p>
                    {notes.length > 0 && <ul className="detail-workout-option-notes">{notes.map((note) => <li key={note}>{note}</li>)}</ul>}
                    <div className="detail-workout-parts">
                      {parts.map((part, partIndex) => {
                        const meta = [asText(part.duration), asText(part.rpe) ? (/^rpe/i.test(asText(part.rpe)) ? asText(part.rpe) : `RPE ${asText(part.rpe)}`) : ""].filter(Boolean);
                        return (
                          <div className="detail-workout-part" key={partIndex}>
                            <p className="detail-workout-part-title">{asText(part.title)}</p>
                            {meta.length > 0 && <p className="detail-workout-part-meta">{meta.join(" | ")}</p>}
                            {(["prescription", "selection_notes", "coaching_notes", "terrain_notes", "adjustment_notes"] as const).map((key) => {
                              if (!part[key]) return null;
                              const prefix = key === "selection_notes" ? "Best for: " : key === "coaching_notes" ? "Coach: " : key === "terrain_notes" ? "Terrain: " : key === "adjustment_notes" ? "Adjust: " : "";
                              return <p key={key} className={`detail-workout-part-line ${key === "terrain_notes" ? "detail-workout-part-terrain" : ""}`}>{prefix}{asText(part[key])}</p>;
                            })}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          );
        })}
      </div>
    </section>
  );
}
