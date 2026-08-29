# நமது நிலை — booklet-only English translation plan

## Status

**PLAN COMPLETE — no English source translation has started yet.**

This plan governs the English translation of the verified 1971 booklet source package preserved under `sources/1971-namathu-nilai/`.

The controlling publication is:

`ACL-CPL_01726_நமது_நிலை.pdf`

The translation must represent **that booklet as printed**, not a reconstructed Legislative Assembly or Legislative Council speech.

---

## 1. Non-negotiable source rule

The only textual authority for this English translation is the verified Tamil source witness derived from:

`ACL-CPL_01726_நமது_நிலை.pdf`

Working Tamil files:

- `../../transcription/scan-001-010.md`
- `../../transcription/scan-011-020.md`
- `../../transcription/scan-021-030.md`
- `../../transcription/scan-031-040.md`
- `../../transcription/scan-041-050.md`
- `../../transcription/scan-051-060.md`

Those files collectively preserve the complete verified booklet text. They have already passed direct visual checking against the controlling scan, with **175** scan-supported corrections applied and **0** unresolved word/character readings.

### Prohibited translation inputs

Tamil Nadu Legislative Assembly and Legislative Council Official Reports may **not** supply English wording, missing text, paraphrases, terminology choices or corrections.

They remain reference/provenance evidence only.

Do not:

- translate from an Official Report;
- complete a booklet sentence from an Official Report;
- replace a booklet reading because an Official Report appears clearer;
- insert House-record passages omitted by the booklet;
- delete booklet passages because they derive from the other House;
- rearrange the booklet into separate Assembly/Council speeches;
- harmonise wording between the booklet and legislative records.

If a Tamil reading ever appears doubtful during translation, re-check **`ACL-CPL_01726_நமது_நிலை.pdf` itself**. Do not resolve it from another PDF.

---

## 2. Translation object

The object being translated is the **booklet publication**, including its editorial construction.

Locked source structure:

| Scan pages | Printed pages | Translation unit |
|---:|---:|---|
| 1 | — | cover/title text |
| 2 | — | publication/editorial introduction and imprint |
| 3–37 | 1–35 | Editorial Unit 1 — `நமது நிலை` / Governor-address reply compilation |
| 38–60 | 36–58 | Editorial Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

The translation must preserve this order exactly.

The House/date provenance ledgers may be cited in editorial notes outside the translated source text, but their classifications must not alter the sequence or wording of the English translation.

---

## 3. Translation objective

Produce a **faithful reading translation**, not a polished rewrite.

The English should preserve, as far as English permits:

- argumentative sequence;
- repetition and rhetorical accumulation;
- direct address to members;
- humour, irony and wordplay;
- metaphors and comparisons;
- political and parliamentary register;
- speaker changes and interventions printed by the booklet;
- headings and subheadings;
- numerals, dates, percentages, money and units;
- printed English expressions and transliterated terms;
- source-specific claims even where later knowledge or another record differs.

Do not improve historical claims, modernise political terminology, smooth away repetitions or silently explain arguments inside the translated source text.

Where literal English would destroy an idiom or joke, translate the **meaning and rhetorical function** faithfully and record difficult decisions in the review/glossary layer rather than making the main text opaque.

---

## 4. Page fidelity

Every translated page range must remain traceable to the booklet.

Use the same source-page numbering as the verified Tamil, for example:

```html
<!-- source-page: 3 -->
```

These markers refer to physical pages of `ACL-CPL_01726_நமது_நிலை.pdf`.

Do not use Official Report page numbers inside the translated source text.

Cross-page sentences should remain coherent in English, but page markers must stay at the corresponding physical source transition.

---

## 5. Heading and intervention policy

Translate all publication headings that belong to the source text while preserving their hierarchy and location.

Examples of source structures that must survive:

- booklet title;
- editorial-unit headings;
- thematic subheadings;
- speaker labels such as `முதல்வர்:`;
- named-member interventions;
- quoted speech and printed English expressions.

Do not insert editorial labels such as `[Assembly]` or `[Council]` into the translation merely because provenance research identifies a span with one House.

---

## 6. Names, institutions and political terms

Use `GLOSSARY.md` as the controlled consistency layer.

General rules:

1. Preserve the form supported by the verified Tamil source.
2. Do not silently substitute a modern institutional or party name merely because it is more familiar now.
3. For personal names, use a consistent English rendering across the booklet.
4. Preserve source abbreviations and printed English where they are already present.
5. If a term carries period-specific political meaning, prefer a faithful period-aware rendering over a modern paraphrase.
6. Do not use external legislative wording to choose between competing English phrasings.

A glossary decision may be informed by normal linguistic knowledge, but it must describe the Tamil actually printed in the booklet and must not alter the Tamil source layer.

---

## 7. Gate-F working batches

Translation will proceed in bounded source-page order and **never cross an editorial-unit boundary merely to fill a batch**.

### Front matter

- **F0:** scan pp. **1–2** — cover/title + publication introduction/imprint

### Editorial Unit 1

- **F1:** scan pp. **3–10**
- **F2:** scan pp. **11–18**
- **F3:** scan pp. **19–26**
- **F4:** scan pp. **27–34**
- **F5:** scan pp. **35–37** — complete Unit 1

### Editorial Unit 2

- **F6:** scan pp. **38–44**
- **F7:** scan pp. **45–51**
- **F8:** scan pp. **52–58**
- **F9:** scan pp. **59–60** — complete Unit 2 and physical source

Total planned coverage: **60 / 60 scan pages**.

Each batch must record:

- exact source pages completed;
- first/last safe source anchors;
- unresolved translation choices, if any;
- glossary additions/changes;
- whether a sentence continues across the next page/batch;
- commit SHA after the batch is saved.

---

## 8. Working-file design

Gate-F drafts should live under:

```text
translations/en/batches/
```

Recommended names:

```text
f00-scan-001-002.md
f01-scan-003-010.md
f02-scan-011-018.md
f03-scan-019-026.md
f04-scan-027-034.md
f05-scan-035-037.md
f06-scan-038-044.md
f07-scan-045-051.md
f08-scan-052-058.md
f09-scan-059-060.md
```

These batch files are working translation artifacts, not the final release text.

After Gate G, consolidate the reviewed English in booklet order into:

```text
translations/en/translation.md
```

Do not retire the batch files until the merged translation has been checked for complete page coverage, order, duplication and omission.

---

## 9. Gate-G English fidelity review

After Gate F covers all 60 pages, perform a **second, independent page-by-page English fidelity pass** against the final verified Tamil source files.

The Gate-G review must check:

- 60/60 source-page coverage;
- no omitted Tamil content;
- no English additions unsupported by Tamil;
- no accidental duplicate paragraphs across batches;
- no sentence loss at page/batch transitions;
- headings and intervention placement;
- names and initials;
- dates, figures, money, percentages and units;
- printed English expressions;
- humour, metaphor, idiom and rhetorical force;
- preservation of the booklet's mixed-House editorial order without reconstruction;
- absence of Official Report wording imported into the English.

Review findings should be recorded in:

```text
translations/en/TRANSLATION_REVIEW.md
```

Only after that full pass may English be marked `verified`.

---

## 10. Provenance-note separation

The English source translation and provenance commentary are separate layers.

The translated source text should reproduce what the booklet says in English.

Any explanation that:

- a span aligns to the Assembly;
- another span aligns to the Council;
- the booklet skips or reorders legislative material;
- a date was established from another primary record;

belongs in source notes, event records or provenance ledgers — **not inside the translated source text**.

Relevant provenance files remain:

- `../../unit-1-three-way-alignment-ledger.md`
- `../../unit-2-three-way-alignment-ledger.md`
- `../../events/1971-03-29-assembly-interim-budget-reply.md`
- `../../events/1971-04-02-assembly-governors-address-reply.md`

---

## 11. Tamil lock during translation

The six verified Tamil transcription files are frozen during translation.

Translation difficulty is **not** evidence that the Tamil should be changed.

A Tamil change is allowed only if a separate direct visual re-check of `ACL-CPL_01726_நமது_நிலை.pdf` proves that the current transcription is wrong. Any such correction must be documented as a new source-supported correction before the English is adjusted.

No other PDF can justify a Tamil correction.

---

## 12. Progress and consistency records

Maintain:

- `PROGRESS.md` — Gate-F/G batch completion and exact continuation point;
- `GLOSSARY.md` — recurring names, institutions, parliamentary/political terms, idioms and source-specific English choices;
- `TRANSLATION_REVIEW.md` — created when Gate G starts.

Do not mark the source English translation complete merely because all first-pass batches exist. `complete` and `verified` remain separate states.

---

## 13. Release rule

English release is permitted only when:

1. F0–F9 are complete;
2. all 60 source pages are represented once and in order;
3. Gate G has compared the complete English against the verified Tamil;
4. all definite fidelity corrections are applied;
5. `translation.md` is consolidated and mechanically checked;
6. `PROGRESS.md`, `GLOSSARY.md`, `TRANSLATION_REVIEW.md`, source README and handover agree on status;
7. no external legislative wording has entered the translation.

The release remains a translation of **`நமது நிலை` the booklet**, not of reconstructed House transcripts.

---

## Exact next activity

Before translating F0/F1, initialise `PROGRESS.md` and `GLOSSARY.md` under this directory.

Then begin Gate F in source order with **F0, scan pp.1–2**, followed by **F1, scan pp.3–10**.

At every stage:

> **Translation source = verified Tamil from `ACL-CPL_01726_நமது_நிலை.pdf` only. External Assembly/Council PDFs = provenance/reference only.**
