import { useEffect, useMemo, useState } from "react";
import { CARD_TYPES, type CardType, type TrainingCard, type WebLibraryData } from "../types";
import { PathwaySelector, type PathwayValue } from "../PathwaySelector";
import { covers, dateKey, decodeDrafts, decodePlan, descendantIds, DRAFTS_STORAGE_KEY, LEVEL_NAMES, parseDay, STORAGE_KEY, type Placement, type PlanDrafts } from "./model";
import "./plan.css";

const WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
const monthName = (date: Date) => date.toLocaleDateString("en-GB", { month: "long" });
const readableDay = (day: string) => parseDay(day).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });

export function MyPlan({ data, onOpen, selectedTags, onToggleTag, profiles, onProfilesChange, onSaveStatusChange }: {
  data: WebLibraryData;
  onOpen: (card: TrainingCard) => void;
  selectedTags: string[];
  onToggleTag: (tag: string) => void;
  profiles: string[];
  onProfilesChange: (profiles: string[]) => void;
  onSaveStatusChange: (status: string) => void;
}) {
  const [initial] = useState<{ entries: Placement[]; drafts: PlanDrafts; error: string }>(() => {
    try { return { entries: decodePlan(localStorage.getItem(STORAGE_KEY)), drafts: decodeDrafts(localStorage.getItem(DRAFTS_STORAGE_KEY)), error: "" }; }
    catch { return { entries: [], drafts: {}, error: "Your saved plan or selections could not be read. Reload to try again. Saving is paused to protect them." }; }
  });
  const [entries, setEntries] = useState(initial.entries);
  const [drafts, setDrafts] = useState(initial.drafts);
  const [storageError, setStorageError] = useState(initial.error);
  const [saveStatus, setSaveStatus] = useState("Saved in this browser");
  const [day, setDay] = useState(() => dateKey(new Date()));
  const [cursor, setCursor] = useState(() => new Date());
  const [view, setView] = useState<"month" | "year">("month");
  const [error, setError] = useState("");
  const [pathway, setPathway] = useState<PathwayValue>(() => initial.drafts[day] ?? Object.fromEntries(CARD_TYPES.map((type) => [type, initial.entries.find((entry) => entry.level === type && covers(entry, day))?.cardId ?? null])) as PathwayValue);
  const cards = useMemo(() => new Map(data.cards.map((card) => [card.id, card])), [data]);
  const unavailable = entries.filter((item) => !cards.has(item.cardId)).length;

  useEffect(() => {
    onSaveStatusChange(storageError ? "Saving paused" : saveStatus);
  }, [onSaveStatusChange, saveStatus, storageError]);

  // Accept updates from another tab without writing them back in a storage loop.
  useEffect(() => {
    const receive = (event: StorageEvent) => {
      if (event.key !== STORAGE_KEY && event.key !== DRAFTS_STORAGE_KEY && event.key !== null) return;
      try {
        if (event.key === null) {
          setEntries([]); setDrafts({});
          setPathway(Object.fromEntries(CARD_TYPES.map((type) => [type, null])) as PathwayValue);
        } else if (event.key === DRAFTS_STORAGE_KEY) {
          const next = decodeDrafts(event.newValue);
          setDrafts(next);
          setPathway(next[day] ?? Object.fromEntries(CARD_TYPES.map((type) => [type, entries.find((item) => item.level === type && covers(item, day))?.cardId ?? null])) as PathwayValue);
        } else {
          const next = decodePlan(event.newValue);
          setEntries(next);
          setPathway(drafts[day] ?? Object.fromEntries(CARD_TYPES.map((type) => [type, next.find((item) => item.level === type && covers(item, day))?.cardId ?? null])) as PathwayValue);
        }
        setStorageError(""); setSaveStatus("Updated from another tab");
      } catch { setStorageError("A saved plan update could not be read. Reload before making more changes."); }
    };
    window.addEventListener("storage", receive);
    return () => window.removeEventListener("storage", receive);
  }, [day, drafts, entries]);

  function commit(next: Placement[]) {
    if (storageError) return false;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ version: 1, placements: next }));
      setEntries(next); setSaveStatus("Saved in this browser");
      return true;
    } catch { setSaveStatus("Could not save"); setError("This browser could not save your change. Free up browser storage or allow site storage, then try again."); return false; }
  }

  function updatePathway(next: PathwayValue) {
    if (storageError) return;
    const nextDrafts = { ...drafts, [day]: next };
    try {
      localStorage.setItem(DRAFTS_STORAGE_KEY, JSON.stringify({ version: 1, drafts: nextDrafts }));
      setDrafts(nextDrafts); setPathway(next); setSaveStatus("Saved in this browser"); setError("");
    } catch {
      setSaveStatus("Could not save"); setError("This browser could not save your selection. Free up browser storage or allow site storage, then try again.");
    }
  }

  function selectDay(next: string) {
    setDay(next); setCursor(parseDay(next));
    setPathway(drafts[next] ?? Object.fromEntries(CARD_TYPES.map((type) => [type, entries.find((entry) => entry.level === type && covers(entry, next))?.cardId ?? null])) as PathwayValue);
    setError("");
  }

  function resetFrom(resetLevel: CardType) {
    const saved = entries.find((item) => item.level === resetLevel && covers(item, day));
    const next = saved
      ? entries.filter((item) => !descendantIds(entries, saved.id).has(item.id))
      : entries;
    if (saved && !commit(next)) return;
    const nextPathway = { ...pathway };
    for (const type of CARD_TYPES.slice(CARD_TYPES.indexOf(resetLevel))) nextPathway[type] = null;
    const nextDrafts = { ...drafts, [day]: nextPathway };
    try {
      localStorage.setItem(DRAFTS_STORAGE_KEY, JSON.stringify({ version: 1, drafts: nextDrafts }));
      setDrafts(nextDrafts); setPathway(nextPathway); setSaveStatus("Saved in this browser");
    } catch {
      setSaveStatus("Could not save"); setError("This browser could not save your reset. Free up browser storage or allow site storage, then try again."); return;
    }
    setError("");
  }

  function navigate(direction: number) {
    setCursor(new Date(cursor.getFullYear() + (view === "year" ? direction : 0), cursor.getMonth() + (view === "month" ? direction : 0), 1, 12));
  }

  function renderMonth(month: number, compact: boolean) {
    const first = new Date(cursor.getFullYear(), month, 1, 12);
    const offset = (first.getDay() + 6) % 7;
    const count = new Date(cursor.getFullYear(), month + 1, 0).getDate();
    return <section className={compact ? "plan-month is-compact" : "plan-month"} key={month} aria-label={`${monthName(first)} ${cursor.getFullYear()}`}>
      {compact && <button className="plan-month-title" type="button" onClick={() => { setCursor(first); setView("month"); }}>{monthName(first)}</button>}
      <div className="plan-weekdays" aria-hidden="true">{WEEKDAYS.map((name) => <span key={name}>{compact ? name[0] : name}</span>)}</div>
      <div className="plan-days">
        {Array.from({ length: offset }, (_, i) => <span className="plan-blank" key={`blank-${i}`} />)}
        {Array.from({ length: count }, (_, i) => {
          const key = dateKey(new Date(cursor.getFullYear(), month, i + 1, 12));
          const planned = entries.filter((entry) => covers(entry, key)).sort((a, b) => CARD_TYPES.indexOf(a.level) - CARD_TYPES.indexOf(b.level));
          return <button key={key} type="button" className={`plan-day${key === day ? " is-selected" : ""}${key === dateKey(new Date()) ? " is-today" : ""}`}
            aria-pressed={key === day} aria-current={key === dateKey(new Date()) ? "date" : undefined}
            aria-label={`${readableDay(key)}${planned.length ? `, ${planned.map((entry) => cards.get(entry.cardId)?.title ?? "Unavailable card").join(", ")}` : ", unplanned"}`}
            onClick={() => selectDay(key)}>
            <span className="plan-date-number">{i + 1}</span>
            {compact ? <span className="plan-dots">{CARD_TYPES.filter((type) => planned.some((entry) => entry.level === type)).map((type) => <i className={`plan-color-${type}`} key={type} />)}</span>
              : <span className="plan-day-entries">{planned.slice(0, 3).map((entry) => <span className={`plan-band plan-color-${entry.level}`} key={entry.id}>{cards.get(entry.cardId)?.title ?? "Unavailable card"}</span>)}{planned.length > 3 && <span className="plan-more">+{planned.length - 3} more</span>}</span>}
          </button>;
        })}
      </div>
    </section>;
  }

  return <div className="my-plan">
    {storageError && <p className="plan-error" role="alert">{storageError}</p>}
    {unavailable > 0 && <p className="plan-notice">{unavailable} planned card(s) are unavailable in this library. Their dates are kept.</p>}
    <PathwaySelector data={data} cardsById={cards} value={pathway} onChange={updatePathway} onOpen={onOpen}
      selectedTags={selectedTags} onToggleTag={onToggleTag} profiles={profiles} onProfilesChange={onProfilesChange}
      onResetFrom={resetFrom} showCompletedCards={false} />
    {error && <p className="plan-error" role="alert">{error}</p>}
    <div className="plan-calendar">
      <div className="plan-calendar-toolbar">
        <div className="plan-period-nav"><button className="button" type="button" aria-label={`Previous ${view}`} onClick={() => navigate(-1)}>‹</button><h3>{view === "year" ? cursor.getFullYear() : `${monthName(cursor)} ${cursor.getFullYear()}`}</h3><button className="button" type="button" aria-label={`Next ${view}`} onClick={() => navigate(1)}>›</button></div>
        <div className="plan-view-switch"><button className="button" type="button" onClick={() => selectDay(dateKey(new Date()))}>Today</button>{(["month", "year"] as const).map((item) => <button className="button" type="button" key={item} aria-pressed={view === item} onClick={() => setView(item)}>{item === "year" ? "Year" : "Month"}</button>)}</div>
      </div>
      <div className="plan-legend">{CARD_TYPES.map((type) => <span key={type}><i className={`plan-color-${type}`} />{LEVEL_NAMES[type]}</span>)}</div>
      <div className={view === "year" ? "plan-year" : ""}>{view === "year" ? Array.from({ length: 12 }, (_, month) => renderMonth(month, true)) : renderMonth(cursor.getMonth(), false)}</div>
    </div>
  </div>;
}
