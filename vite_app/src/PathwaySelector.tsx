import { useState } from "react";
import { ActiveFilters, CardsGrid, Pagination, ProfileFilter } from "./components";
import { cardMatchesSearch, cardsOfType, getChildCards, matchesAllTerms, matchesPhilosophies, sortCards } from "./data";
import { CARD_TYPES, PAGE_SIZE, type CardType, type TrainingCard, type WebLibraryData } from "./types";

export type PathwayValue = Record<CardType, string | null>;

export function PathwaySelector({
  data, cardsById, value, onChange, onOpen, selectedTags, onToggleTag, profiles, onProfilesChange,
  selectLabel = "Select", onSelectCard, onResetFrom, showCompletedCards = true,
}: {
  data: WebLibraryData;
  cardsById: Map<string, TrainingCard>;
  value: PathwayValue;
  onChange: (next: PathwayValue) => void;
  onOpen: (card: TrainingCard) => void;
  selectedTags: string[];
  onToggleTag: (tag: string) => void;
  profiles: string[];
  onProfilesChange: (profiles: string[]) => void;
  selectLabel?: string;
  onSelectCard?: (card: TrainingCard) => void;
  onResetFrom?: (level: CardType) => void;
  showCompletedCards?: boolean;
}) {
  const [terms, setTerms] = useState<string[]>([]);
  const [input, setInput] = useState("");
  const [pages, setPages] = useState<Record<string, number>>({});
  const selected = Object.fromEntries(CARD_TYPES.map((level) => [level, value[level] ? cardsById.get(value[level]!) ?? null : null])) as Record<CardType, TrainingCard | null>;
  const nextLevel = CARD_TYPES.find((level) => !selected[level]);
  const previousLevel = nextLevel ? CARD_TYPES[CARD_TYPES.indexOf(nextLevel) - 1] : null;
  const parent = previousLevel ? selected[previousLevel] : null;
  const candidates = nextLevel ? parent ? getChildCards(data, data.cards, parent, nextLevel) : cardsOfType(data.cards, nextLevel) : [];
  const visible = sortCards(data, candidates.filter((card) =>
    cardMatchesSearch(data, card, "") && matchesAllTerms(data, card, terms) &&
    (selectedTags.length === 0 || selectedTags.every((tag) => card.tags?.includes(tag))) &&
    matchesPhilosophies(data, card, profiles, parent?.id),
  ));
  const page = Math.min(pages[nextLevel ?? "complete"] ?? 0, Math.max(0, Math.ceil(visible.length / PAGE_SIZE) - 1));
  const items = visible.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

  function choose(card: TrainingCard) {
    const next = { ...value, [card.card_type]: card.id };
    for (const level of CARD_TYPES.slice(CARD_TYPES.indexOf(card.card_type) + 1)) next[level] = null;
    onChange(next);
    onSelectCard?.(card);
    setTerms([]); setInput(""); setPages({});
  }

  function removeFrom(level: CardType) {
    if (onResetFrom) { onResetFrom(level); return; }
    const next = { ...value };
    for (const item of CARD_TYPES.slice(CARD_TYPES.indexOf(level))) next[item] = null;
    onChange(next); setTerms([]); setPages({});
  }

  function addTerm() {
    const term = input.trim();
    if (!term) return;
    setTerms((current) => current.includes(term) ? current : [...current, term]);
    setInput(""); setPages({});
  }

  return <>
    <section className="pathway-selection">
      <div className="pathway-steps">{CARD_TYPES.map((level) => {
        const card = selected[level];
        return <div className={`pathway-step pathway-step-${level}`} key={level}>
          <div className="pathway-level-label">{level[0].toUpperCase() + level.slice(1)}</div><div className="pathway-level-rule" />
          {card ? <><div className="pathway-selected-title">{card.title}</div><div className="pathway-step-actions"><button className="text-action" type="button" onClick={() => onOpen(card)}>Open card</button><button className="text-action" type="button" onClick={() => removeFrom(level)}>Reset</button></div></> : <div className="pathway-empty">Not selected</div>}
        </div>;
      })}</div>
      <div className="pathway-summary-footer-rule" />
      <button className="plain-button clear-pathway" type="button" disabled={!CARD_TYPES.some((level) => value[level])} onClick={() => onResetFrom ? onResetFrom("macro") : onChange({ macro: null, mezzo: null, micro: null, session: null })}>Reset pathway</button>
    </section>
    {nextLevel ? <>
      <section className="mode-toolbar">
        <div className="toolbar-controls">
          <form className="search-with-add" onSubmit={(event) => { event.preventDefault(); addTerm(); }}><input aria-label={`Search ${nextLevel} cards`} value={input} onChange={(event) => setInput(event.target.value)} placeholder={`Search ${nextLevel} cards`} /><button className="plain-button" type="submit" disabled={!input.trim()}>Add</button></form>
          <ProfileFilter data={data} value={profiles} onChange={onProfilesChange} />
        </div>
        <ActiveFilters tags={selectedTags} onRemoveTag={(tag) => onToggleTag(tag)} terms={terms} onRemoveTerm={(term) => { setTerms((current) => current.filter((item) => item !== term)); setPages({}); }} />
      </section>
      {items.length ? <div className="paginated-cards" data-page-start><CardsGrid cards={items} data={data} onOpen={onOpen} onSelect={choose} selectLabel={selectLabel} selectedTags={selectedTags} onToggleTag={onToggleTag} /><Pagination total={visible.length} pageSize={PAGE_SIZE} page={page} onChange={(next) => setPages((current) => ({ ...current, [nextLevel]: next }))} /></div> : <p className="empty-state">No {nextLevel} cards match the current pathway filters.</p>}
    </> : showCompletedCards ? <><p className="pathway-complete">Pathway complete. Open a card to inspect details, or remove a step to revise it.</p><h2 className="card-group-title">Chosen pathway cards</h2><CardsGrid cards={CARD_TYPES.map((level) => selected[level]!).filter(Boolean)} data={data} onOpen={onOpen} selectedTags={selectedTags} onToggleTag={onToggleTag} /></> : <p className="pathway-complete">Pathway selection complete.</p>}
  </>;
}
