import { useState, type FormEvent } from "react";
import { formatFieldValue } from "../data";
import type { TrainingCard } from "../types";
import { addDays, parseDay, validDay } from "./model";
import type { BlockLevel, BlockSchedule } from "./model";

function recommendedDuration(card: TrainingCard, level: BlockLevel) {
  const field = level === "micro" ? "recommended_duration_days" : "recommended_duration_weeks";
  const text = formatFieldValue(field, card[field]).replace(/(\d)\s*[-–]\s*(\d)/g, "$1–$2");
  const numbers = [...text.matchAll(/\d+(?:\.\d+)?/g)].map((match) => Number(match[0]));
  const midpoint = numbers.length > 1 ? Math.round((numbers[0] + numbers[1]) / 2) : numbers[0];
  return { text, midpoint: Number.isFinite(midpoint) ? midpoint : "" };
}

function calendarMonthAfter(date: Date) {
  const next = new Date(date);
  const originalDay = date.getDate();
  next.setDate(1);
  next.setMonth(next.getMonth() + 1);
  next.setDate(Math.min(originalDay, new Date(next.getFullYear(), next.getMonth() + 1, 0).getDate()));
  return next;
}

function durationBreakdown(start: string, end: string) {
  if (!validDay(start) || !validDay(end) || end < start) return "";
  let cursor = parseDay(start);
  const endExclusive = parseDay(addDays(end, 1));
  let months = 0;
  while (calendarMonthAfter(cursor) <= endExclusive) {
    cursor = calendarMonthAfter(cursor);
    months += 1;
  }
  const remainingDays = Math.round((endExclusive.getTime() - cursor.getTime()) / 86400000);
  return `${months}M : ${Math.floor(remainingDays / 7)}W : ${remainingDays % 7}D`;
}

function displayDate(day: string) {
  return validDay(day) ? parseDay(day).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "Choose an end date";
}

export function BlockScheduleForm({ card, level, defaultStart, saved, minDate, maxDate, disabled, onSave }: {
  card: TrainingCard;
  level: BlockLevel;
  defaultStart: string;
  saved?: BlockSchedule;
  minDate?: string;
  maxDate?: string;
  disabled: boolean;
  onSave: (schedule: BlockSchedule) => void;
}) {
  const unit = level === "micro" ? "days" : "weeks";
  const recommendation = recommendedDuration(card, level);
  const initial = saved?.cardId === card.id && saved.unit === unit ? saved : undefined;
  const [start, setStart] = useState(initial?.start ?? defaultStart);
  const [duration, setDuration] = useState(initial?.duration ? String(initial.duration) : String(recommendation.midpoint));
  const [customEnd, setCustomEnd] = useState(initial?.customEnd ?? false);
  const [endDate, setEndDate] = useState(initial?.end ?? "");
  const [error, setError] = useState("");
  const durationValue = Number(duration);
  const end = customEnd ? endDate : validDay(start) && Number.isInteger(durationValue) && durationValue > 0
    ? addDays(start, durationValue * (unit === "weeks" ? 7 : 1) - 1)
    : "";
  const withinParent = (!minDate || start >= minDate) && (!maxDate || end <= maxDate);
  const valid = validDay(start) && validDay(end) && end >= start && withinParent;

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!validDay(start) || !validDay(end) || end < start) {
      setError("Choose a valid start and end date.");
      return;
    }
    if (!withinParent) {
      setError("Keep this block within its parent dates.");
      return;
    }
    onSave({ cardId: card.id, start, end, unit, duration: customEnd ? null : durationValue, customEnd });
  }

  return <form className="plan-schedule-form" onSubmit={submit}>
    <div className="plan-schedule-heading">
      <span>{level === "macro" ? "Macro phase" : level === "mezzo" ? "Mezzo block" : "Micro week"}</span>
      <h3>Set dates and duration</h3>
    </div>
    <p className="plan-schedule-recommendation">{recommendation.text ? <>Recommended from this card: <strong>{recommendation.text}</strong></> : "This card has no recommended duration."}</p>
    <div className="plan-schedule-fields">
      <label>From<input type="date" value={start} min={minDate} max={maxDate} onChange={(event) => { setStart(event.target.value); setError(""); }} required /></label>
      {!customEnd ? <label>Duration in {unit}<input type="number" min="1" step="1" value={duration} onChange={(event) => { setDuration(event.target.value); setError(""); }} required /></label>
        : <label>Custom end date<input type="date" value={endDate || end} min={start} max={maxDate} onChange={(event) => { setEndDate(event.target.value); setError(""); }} required /></label>}
    </div>
    <div className="plan-schedule-method" role="group" aria-label="Choose how to set the block end">
      <button className="text-action" type="button" aria-pressed={!customEnd} onClick={() => { setCustomEnd(false); setError(""); }}>Use duration</button>
      <button className="text-action" type="button" aria-pressed={customEnd} onClick={() => { setEndDate(end || (validDay(start) ? addDays(start, 6) : "")); setCustomEnd(true); setError(""); }}>Use custom end date</button>
    </div>
    <div className="plan-schedule-preview" aria-live="polite">
      <span>End date</span><strong>{displayDate(end)}</strong>
      {valid && <small>M : W : D &nbsp; {durationBreakdown(start, end)}</small>}
    </div>
    {error && <p className="plan-error" role="alert">{error}</p>}
    <button className="button plan-schedule-save" type="submit" disabled={disabled || !valid}>Save duration and continue</button>
  </form>;
}
