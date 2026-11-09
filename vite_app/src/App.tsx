import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  ActiveFilters,
  CardPreview,
  CardsGrid,
  MarkdownContent,
  Modal,
  Pagination,
  ProfileFilter,
} from "./components";
import { CardDetail } from "./detail";
import {
  APP_MODES,
  APP_TITLE,
  CARD_TYPES,
  LIBRARY_PAGE_SIZE,
  MODE_INFO,
  PAGE_SIZE,
  type AppMode,
  type CardType,
  type LibraryEntry,
  type TrainingCard,
  type WebLibraryData,
} from "./types";
import {
  cardMatchesSearch,
  cardsOfType,
  displayLabel,
  getChildCards,
  loadLibrary,
  matchesAllTerms,
  matchesPhilosophies,
  philosophyName,
  sortCards,
} from "./data";

type ModalState =
  | { type: "card"; cardId: string }
  | { type: "preview"; cardId: string }
  | { type: "philosophy"; profileId: string }
  | { type: "sources"; profileId: string }
  | null;

const LEVEL_LABELS = ["All", "Macro", "Mezzo", "Micro", "Session"];
const PATHWAY_LABELS: Record<CardType, string> = {
  macro: "Macro",
  mezzo: "Mezzo",
  micro: "Micro",
  session: "Session",
};

export default function App() {
  const [data, setData] = useState<WebLibraryData | null>(null);
  const [loadError, setLoadError] = useState("");
  const [mode, setMode] = useState<AppMode>(APP_MODES[0]);
  const [modal, setModal] = useState<ModalState>(null);
  const [cardHistory, setCardHistory] = useState<string[]>([]);

  const [scope, setScope] = useState("All");
  const [search, setSearch] = useState("");
  const [profiles, setProfiles] = useState<string[]>([]);
  const [tags, setTags] = useState<string[]>([]);
  const [todayTerms, setTodayTerms] = useState<string[]>([]);
  const [todayInput, setTodayInput] = useState("");
  const [pathwayTerms, setPathwayTerms] = useState<string[]>([]);
  const [pathwayInput, setPathwayInput] = useState("");
  const [pathway, setPathway] = useState<Record<CardType, string | null>>({
    macro: null,
    mezzo: null,
    micro: null,
    session: null,
  });
  const [libraryLevel, setLibraryLevel] = useState("All");
  const [librarySearch, setLibrarySearch] = useState("");
  const [expandedProfiles, setExpandedProfiles] = useState<string[]>([]);
  const [pages, setPages] = useState<Record<string, number>>({});
  const modeInfoRef = useRef<HTMLDetailsElement>(null);

  useEffect(() => {
    const dismiss = (event: PointerEvent) => {
      if (modeInfoRef.current && !modeInfoRef.current.contains(event.target as Node)) modeInfoRef.current.open = false;
    };
    const escape = (event: KeyboardEvent) => {
      if (event.key === "Escape" && modeInfoRef.current?.open) {
        modeInfoRef.current.open = false;
        modeInfoRef.current.querySelector("summary")?.focus();
      }
    };
    document.addEventListener("pointerdown", dismiss);
    document.addEventListener("keydown", escape);
    return () => {
      document.removeEventListener("pointerdown", dismiss);
      document.removeEventListener("keydown", escape);
    };
  }, []);

  useEffect(() => {
    loadLibrary().then(setData).catch((error: unknown) => {
      setLoadError(error instanceof Error ? error.message : "The card library could not be loaded.");
    });
  }, []);

  const cardsById = useMemo(
    () => new Map((data?.cards ?? []).map((card) => [card.id, card])),
    [data],
  );
  const currentCard = modal?.type === "card" ? cardsById.get(modal.cardId) : undefined;
  const previewCard = modal?.type === "preview" ? cardsById.get(modal.cardId) : undefined;
  const activeHistory = cardHistory.map((id) => cardsById.get(id)).filter((card): card is TrainingCard => Boolean(card));

  const setPage = (key: string, page: number) => setPages((current) => ({ ...current, [key]: page }));
  const pageFor = (key: string) => pages[key] ?? 0;
  const resetPages = () => setPages({});

  const openCard = (card: TrainingCard) => {
    setCardHistory([]);
    setModal({ type: "card", cardId: card.id });
  };
  const closeModal = useCallback(() => {
    setModal(null);
    setCardHistory([]);
  }, []);
  const changeMode = (next: AppMode) => {
    setMode(next);
    closeModal();
  };
  const toggleTag = (tag: string) => {
    setTags((current) => current.includes(tag) ? current.filter((item) => item !== tag) : [...current, tag]);
    resetPages();
  };
  const removeTag = (tag: string) => setTags((current) => current.filter((item) => item !== tag));
  const addSearchTerm = (kind: "today" | "pathway") => {
    const currentInput = kind === "today" ? todayInput : pathwayInput;
    const term = currentInput.trim();
    if (!term) return;
    if (kind === "today") {
      setTodayTerms((current) => current.includes(term) ? current : [...current, term]);
      setTodayInput("");
    } else {
      setPathwayTerms((current) => current.includes(term) ? current : [...current, term]);
      setPathwayInput("");
    }
    resetPages();
  };

  if (!data) {
    return (
      <main className="load-state">
        <h1>{APP_TITLE}</h1>
        {loadError ? <div className="load-error"><p>{loadError}</p><code>pnpm prepare:data</code></div> : <p>Loading the training-card library…</p>}
      </main>
    );
  }

  const counts = {
    All: data.cards.length,
    Macro: cardsOfType(data.cards, "macro").length,
    Mezzo: cardsOfType(data.cards, "mezzo").length,
    Micro: cardsOfType(data.cards, "micro").length,
    Session: cardsOfType(data.cards, "session").length,
  };
  const countLine = `All ${counts.All} · Macro ${counts.Macro} · Mezzo ${counts.Mezzo} · Micro ${counts.Micro} · Session ${counts.Session}`;

  const filtered = (items: TrainingCard[], query: string, andTerms: string[] = [], parentId?: string) =>
    sortCards(data, items.filter((card) =>
      cardMatchesSearch(data, card, query) &&
      matchesAllTerms(data, card, andTerms) &&
      (tags.length === 0 || tags.every((tag) => card.tags?.includes(tag))) &&
      matchesPhilosophies(data, card, profiles, parentId),
    ));

  const renderCards = (
    items: TrainingCard[],
    key: string,
    onSelect?: (card: TrainingCard) => void,
    selectLabel?: string,
  ) => {
    const pageCount = Math.max(1, Math.ceil(items.length / PAGE_SIZE));
    const page = Math.min(pageFor(key), pageCount - 1);
    const pageItems = items.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);
    if (items.length === 0) return <p className="empty-state">No cards match the current filters.</p>;
    return <div className="paginated-cards" data-page-start>
      <CardsGrid cards={pageItems} data={data} onOpen={openCard} onSelect={onSelect} selectLabel={selectLabel} selectedTags={tags} onToggleTag={toggleTag} />
      <Pagination total={items.length} pageSize={PAGE_SIZE} page={page} onChange={(next) => setPage(key, next)} />
    </div>;
  };

  const renderBrowse = () => {
    const scopeType = scope === "All" ? null : scope.toLowerCase() as CardType;
    const items = filtered(data.cards.filter((card) => !scopeType || card.card_type === scopeType), search);
    return <>
      <section className="mode-toolbar browse-toolbar">
        <nav className="scope-tabs" aria-label="Card level">
          {LEVEL_LABELS.map((level) => <button type="button" key={level} className={scope === level ? "scope-tab is-selected" : "scope-tab"} onClick={() => { setScope(level); resetPages(); }}>{level}</button>)}
        </nav>
        <div className="toolbar-controls">
          <input aria-label="Search cards" value={search} onChange={(event) => { setSearch(event.target.value); resetPages(); }} placeholder="Search cards" />
          <ProfileFilter data={data} value={profiles} onChange={(next) => { setProfiles(next); resetPages(); }} />
        </div>
        <ActiveFilters tags={tags} onRemoveTag={removeTag} />
      </section>
      {items.length ? renderCards(items, "browse_cards") : <p className="empty-state">No cards match the current filters.</p>}
    </>;
  };

  const renderToday = () => {
    const sessions = filtered(cardsOfType(data.cards, "session"), "", todayTerms);
    return <>
      <section className="mode-toolbar">
        <div className="toolbar-controls">
          <form className="search-with-add" onSubmit={(event) => { event.preventDefault(); addSearchTerm("today"); }}>
            <input aria-label="Search session cards" value={todayInput} onChange={(event) => setTodayInput(event.target.value)} placeholder="Search today's session" />
            <button className="plain-button" type="submit" disabled={!todayInput.trim()}>Add</button>
          </form>
          <ProfileFilter data={data} value={profiles} onChange={(next) => { setProfiles(next); resetPages(); }} />
        </div>
        <ActiveFilters tags={tags} onRemoveTag={removeTag} terms={todayTerms} onRemoveTerm={(term) => setTodayTerms((current) => current.filter((item) => item !== term))} />
      </section>
      {sessions.length ? renderCards(sessions, "today_sessions") : <p className="empty-state">No session cards match the current search.</p>}
    </>;
  };

  const selectedPathway = Object.fromEntries(
    CARD_TYPES.map((level) => [level, pathway[level] ? cardsById.get(pathway[level]!) ?? null : null]),
  ) as Record<CardType, TrainingCard | null>;
  const nextLevel = CARD_TYPES.find((level) => !selectedPathway[level]);
  const previousLevel = nextLevel ? CARD_TYPES[CARD_TYPES.indexOf(nextLevel) - 1] : null;
  const parentCardId = previousLevel ? selectedPathway[previousLevel]?.id : undefined;

  const renderPathway = () => {
    const candidates = nextLevel
      ? previousLevel && selectedPathway[previousLevel]
        ? getChildCards(data, data.cards, selectedPathway[previousLevel]!, nextLevel)
        : cardsOfType(data.cards, nextLevel)
      : [];
    const visible = filtered(candidates, "", pathwayTerms, parentCardId);
    const choosePathwayCard = (card: TrainingCard) => {
      setPathway((current) => {
        const next = { ...current, [card.card_type]: card.id };
        for (const level of CARD_TYPES.slice(CARD_TYPES.indexOf(card.card_type) + 1)) next[level] = null;
        return next;
      });
      setPathwayTerms([]);
      setPathwayInput("");
      resetPages();
    };
    const clearPathwayFrom = (level: CardType) => setPathway((current) => {
      const next = { ...current };
      for (const item of CARD_TYPES.slice(CARD_TYPES.indexOf(level))) next[item] = null;
      return next;
    });
    return <>
      <section className="pathway-selection">
        <div className="pathway-steps">
          {CARD_TYPES.map((level) => {
            const card = selectedPathway[level];
            return <div className={`pathway-step pathway-step-${level}`} key={level}>
              <div className="pathway-level-label">{PATHWAY_LABELS[level]}</div>
              <div className="pathway-level-rule" />
              {card ? <>
                <div className="pathway-selected-title">{card.title}</div>
                <div className="pathway-step-actions"><button className="text-action" type="button" onClick={() => openCard(card)}>Open card</button><button className="text-action" type="button" onClick={() => clearPathwayFrom(level)}>Remove</button></div>
              </> : <div className="pathway-empty">Not selected</div>}
            </div>;
          })}
        </div>
        <div className="pathway-summary-footer-rule" />
        <button className="plain-button clear-pathway" type="button" disabled={!CARD_TYPES.some((level) => pathway[level])} onClick={() => setPathway({ macro: null, mezzo: null, micro: null, session: null })}>Clear pathway</button>
      </section>
      {nextLevel ? <>
        <section className="mode-toolbar">
          <div className="toolbar-controls">
            <form className="search-with-add" onSubmit={(event) => { event.preventDefault(); addSearchTerm("pathway"); }}>
              <input aria-label="Search current cards" value={pathwayInput} onChange={(event) => setPathwayInput(event.target.value)} placeholder={`Search ${nextLevel} cards`} />
              <button className="plain-button" type="submit" disabled={!pathwayInput.trim()}>Add</button>
            </form>
            <ProfileFilter data={data} value={profiles} onChange={(next) => { setProfiles(next); resetPages(); }} />
          </div>
          <ActiveFilters tags={tags} onRemoveTag={removeTag} terms={pathwayTerms} onRemoveTerm={(term) => setPathwayTerms((current) => current.filter((item) => item !== term))} />
        </section>
        {visible.length ? renderCards(visible, `pathway_${nextLevel}`, choosePathwayCard, "Select") : <p className="empty-state">No {nextLevel} cards match the current pathway search.</p>}
      </> : <>
        <p className="pathway-complete">Pathway complete. Open any selected card to inspect details, or remove a step to revise the pathway.</p>
        <h2 className="card-group-title">Chosen pathway cards</h2>
        {renderCards(CARD_TYPES.map((level) => selectedPathway[level]!).filter(Boolean), "completed_pathway")}
      </>}
    </>;
  };

  const renderLibrary = () => {
    const levels = libraryLevel === "All" ? CARD_TYPES : [libraryLevel.toLowerCase() as CardType];
    const profileEntries = Object.keys(data.philosophies).map((profileId) => {
      const merged = new Map<string, LibraryEntry>();
      for (const level of levels) {
        for (const entry of data.card_library_index.levels[level]?.[profileId] ?? []) merged.set(entry.card_id, entry);
      }
      const entries = [...merged.values()].filter((entry) => {
        const haystack = [entry.title, entry.description, entry.card_id, entry.source, entry.source_profile].join(" ").toLowerCase();
        return haystack.includes(librarySearch.toLowerCase());
      });
      return [profileId, entries] as const;
    }).filter(([, entries]) => entries.length > 0);
    const toggleExpanded = (id: string) => setExpandedProfiles((current) => current.includes(id) ? current.filter((item) => item !== id) : [id]);

    return <>
      <div className="library-toolbar">
        <nav className="scope-tabs" aria-label="Card level">
          {LEVEL_LABELS.map((level) => <button type="button" key={level} className={libraryLevel === level ? "scope-tab is-selected" : "scope-tab"} onClick={() => { setLibraryLevel(level); setExpandedProfiles([]); resetPages(); }}>{level}</button>)}
        </nav>
        <input aria-label="Search library" value={librarySearch} onChange={(event) => setLibrarySearch(event.target.value)} placeholder="Search titles, descriptions, IDs, or source" />
      </div>
      {profileEntries.length === 0 ? <p className="empty-state">No cards match the current library filters.</p> : <>
        <div className="library-profile-grid">
          {profileEntries.map(([profileId, entries]) => <div className="library-group" key={profileId}>
            <button className="library-group-toggle" type="button" onClick={() => toggleExpanded(profileId)} aria-expanded={expandedProfiles.includes(profileId)}>
              <span>{expandedProfiles.includes(profileId) ? "⌄" : "›"}</span>{philosophyName(data, profileId)} · {entries.length} cards
            </button>
          </div>)}
        </div>
        {profileEntries.filter(([profileId]) => expandedProfiles.includes(profileId)).map(([profileId, entries]) => <LibraryGroup
          key={profileId}
          profileId={profileId}
          entries={entries}
          data={data}
          page={pageFor(`library_${profileId}`)}
          onPage={(page) => setPage(`library_${profileId}`, page)}
          onOpen={(id) => setModal({ type: "preview", cardId: id })}
        />)}
      </>}
    </>;
  };

  const renderPhilosophies = () => {
    const philosophyIds = Object.keys(data.philosophies);
    return <div className="philosophy-grid">
      {philosophyIds.map((profileId) => {
        const profile = data.philosophies[profileId];
        const lines = profile.summary.split(/\r?\n/);
        const firstHeading = lines.findIndex((line) => line.startsWith("# "));
        const title = firstHeading >= 0 ? lines[firstHeading].slice(2).trim() : profile.name;
        const body = firstHeading >= 0 ? lines.slice(firstHeading + 1).join("\n").trim() : profile.summary;
        const website = body.match(/^\[[^\]]+\]\(https?:\/\/[^\s)]+\)/)?.[0] ?? "";
        const summary = website ? body.slice(website.length).trim() : body;
        const count = data.cards.filter((card) => card.philosophy_profile_ids?.includes(profileId)).length;
        return <article className="philosophy-card" key={profileId}>
          <h2 className="philosophy-card-title">{title}</h2>
          <div className="philosophy-card-actions">
            <div className="philosophy-card-count">{count} cards in this profile</div>
            <div className="philosophy-actions">
              <button className="plain-button" type="button" onClick={() => { setMode("Browse cards"); setScope("All"); setProfiles([profileId]); closeModal(); }}>Show cards</button>
              <button className="plain-button" type="button" onClick={() => setModal({ type: "philosophy", profileId })}>Read full philosophy</button>
              <button className="plain-button" type="button" onClick={() => setModal({ type: "sources", profileId })}>View sources</button>
            </div>
          </div>
          <div className="philosophy-website">{website && <MarkdownContent source={website} />}</div>
          <div className="philosophy-summary-content"><MarkdownContent source={summary} /></div>
        </article>;
      })}
    </div>;
  };

  const renderMode = () => {
    if (mode === "Browse cards") return renderBrowse();
    if (mode === "Today session") return renderToday();
    if (mode === "Card library") return renderLibrary();
    if (mode === "Build pathway") return renderPathway();
    return renderPhilosophies();
  };

  const referenceCard = (card: TrainingCard) => {
    setCardHistory((history) => [...history, modal?.type === "card" ? modal.cardId : ""].filter(Boolean));
    setModal({ type: "card", cardId: card.id });
  };

  return <>
    <main className="app-shell">
      <header className="app-header">
        <h1>{APP_TITLE}</h1>
        <div className="app-card-count">{countLine}</div>
        <div className="mode-navigation-row">
          <nav className="mode-navigation" aria-label="App mode">
            {APP_MODES.map((item) => <button type="button" key={item} className={mode === item ? "mode-tab is-selected" : "mode-tab"} onClick={() => changeMode(item)}>{item}</button>)}
          </nav>
          <details className="mode-info" ref={modeInfoRef}>
            <summary aria-label={`About ${mode}`} title={`About ${mode}`}>ⓘ</summary>
            <div className="mode-info-copy"><strong>{mode}</strong><p>{MODE_INFO[mode].intro}</p><ul>{MODE_INFO[mode].bullets.map((line) => <li key={line}>{line}</li>)}</ul></div>
          </details>
        </div>
      </header>
      <section className="app-content">{renderMode()}</section>
      <footer className="author-footer">
        <span className="author-footer-label">Contact</span>
        <a href="mailto:pecek.urh@gmail.com"><MailIcon /> <span>pecek.urh@gmail.com</span></a>
        <a href="https://github.com/1312Bravo/Trail-Running-Training-Cards" target="_blank" rel="noreferrer"><GitHubIcon /> <span>GitHub</span></a>
      </footer>
    </main>

    {currentCard && <Modal onClose={closeModal} contentKey={currentCard.id}>
      <CardDetail
        card={currentCard}
        data={data}
        cardsById={cardsById}
        history={activeHistory}
        onBack={() => {
          const previousId = cardHistory[cardHistory.length - 1];
          if (!previousId) return;
          setCardHistory((history) => history.slice(0, -1));
          setModal({ type: "card", cardId: previousId });
        }}
        onReference={referenceCard}
        onToggleTag={toggleTag}
        selectedTags={tags}
      />
    </Modal>}

    {previewCard && <Modal onClose={closeModal}>
      <div className="library-preview-wrap">
        <CardPreview card={previewCard} data={data} onOpen={() => setModal({ type: "card", cardId: previewCard.id })} compact selectedTags={tags} onToggleTag={toggleTag} />
      </div>
    </Modal>}

    {modal?.type === "philosophy" && <Modal onClose={closeModal} wide>
      <MarkdownContent source={data.philosophies[modal.profileId]?.detail ?? ""} className="philosophy-detail" />
    </Modal>}

    {modal?.type === "sources" && <Modal onClose={closeModal} wide>
      <div className="source-note"><p className="source-note-caption">Reviewed sources used to inform this library's interpretation.</p><MarkdownContent source={data.philosophies[modal.profileId]?.sources ?? ""} /></div>
    </Modal>}
  </>;
}

function LibraryGroup({
  profileId,
  entries,
  data,
  page,
  onPage,
  onOpen,
}: {
  profileId: string;
  entries: LibraryEntry[];
  data: WebLibraryData;
  page: number;
  onPage: (page: number) => void;
  onOpen: (id: string) => void;
}) {
  const pageCount = Math.max(1, Math.ceil(entries.length / LIBRARY_PAGE_SIZE));
  const safePage = Math.min(page, pageCount - 1);
  const directCount = entries.filter((entry) => entry.source === "direct").length;
  const reusedCount = entries.length - directCount;
  return <div className="library-expanded" data-page-start>
    <div className="library-expanded-title">{philosophyName(data, profileId)}</div>
    <p className="library-entry-count">{directCount} direct · {reusedCount} reused</p>
    <div className="library-table">
      <div className="library-table-head"><span>Card</span><span>Description</span><span>Level</span><span>Source</span></div>
      {entries.slice(safePage * LIBRARY_PAGE_SIZE, (safePage + 1) * LIBRARY_PAGE_SIZE).map((entry) => {
        const level = data.cards.find((card) => card.id === entry.card_id)?.card_type ?? "";
        const source = entry.source === "reused" && entry.source_profile
          ? `From ${philosophyName(data, entry.source_profile)}`
          : "Direct";
        return <div className="library-table-row" key={entry.card_id}>
          <button className="plain-button library-card-link" type="button" onClick={() => onOpen(entry.card_id)}>{entry.title}</button>
          <span className="library-description">{entry.description}</span>
          <span className="library-meta">{displayLabel(level)}</span>
          <span className="library-meta">{source}</span>
        </div>;
      })}
    </div>
    <Pagination total={entries.length} pageSize={LIBRARY_PAGE_SIZE} page={safePage} onChange={onPage} />
  </div>;
}

function MailIcon() {
  return <svg className="contact-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm-.4 4.25-7.07 4.42a1 1 0 0 1-1.06 0L4.4 8.25 5.46 6.55 12 10.64l6.54-4.09 1.06 1.7Z" /></svg>;
}

function GitHubIcon() {
  return <svg className="contact-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z" /></svg>;
}
