# Handover — 1971 `நமது நிலை`

## Repository

`pugazg/kalaignar-assembly-speeches` — branch `main`

Source package: `sources/1971-namathu-nilai/`  
Reader-facing entry: `speeches/1971/1971-namathu-nilai/`

## Project state

**COMPLETE / VERIFIED / CLOSED.**

The Tamil booklet transcription, booklet-level reader-facing Tamil, English translation, page-by-page English fidelity review, consolidated refinement and final closure are all complete.

## Non-negotiable textual-authority rule

The **only transcription authority** is:

`ACL-CPL_01726_நமது_நிலை.pdf`

The **only English translation/review authority** is the verified Tamil derived from that same booklet.

Tamil Nadu Legislative Assembly and Legislative Council PDFs are **reference/provenance only**. Do not transcribe from, complete from, repair from, normalize toward, translate from, or merge wording from those records.

## Source identity

- title: `நமது நிலை`
- cover attribution: `தமிழக முதல்வர் கலைஞர் மு.கருணாநிதி`
- imprint: `சென்னை 22-5-1971.`
- issuing body: `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- physical pages: **60**
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

## Locked source structure

| Scan pages | Printed pages | Classification |
|---:|---:|---|
| 1–2 | — | cover / publication front matter |
| 3–37 | 1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| 38–60 | 36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

## Tamil status

**Complete and visually verified against all 60/60 booklet scan pages.**

- accepted scan-supported corrections: **175**
- unresolved source readings: **0**
- external legislative wording imported: **none**

The six source transcription files under `sources/1971-namathu-nilai/transcription/` are frozen unless a direct re-check of the controlling booklet scan proves an error.

## Provenance status

The four underlying reply events and both three-way provenance ledgers are complete and remain metadata only. The booklet must continue to be preserved as an edited two-House compilation rather than reconstructed into separate House transcripts.

## Reader-facing representation

Files under `speeches/1971/1971-namathu-nilai/`:

- `README.md`
- `metadata.json`
- `source-notes.md`
- `transcript.md`
- `translation.md`

Reader-facing Tamil covers **scan pp.3–60, 58/58 speech pages**. The publication date is source metadata only; `date: null` remains correct because the booklet has no single speech date.

The booklet-level entry is intentionally not added to the canonical dated speech table or `data/speeches.json` as one Assembly event.

## English final status

- Gate F first pass: **58/58 pages complete**
- Gate G page-by-page review: **58/58 complete**
- Editorial Unit 1 Gate G: **35/35 complete**
- Editorial Unit 2 Gate G: **23/23 complete**
- blocking fidelity issues: **0**
- consolidated refinement: **34/34 decisions complete**
- reader-facing refinement changes: **33**
- deliberate source-literal retention: **1** (`சொத்து உரிமை` → `property rights`)
- final closure check: **PASS**
- verified Tamil changes during English work: **none**
- English: **VERIFIED against the verified booklet Tamil**
- Official Report wording used: **none**

Important source-sensitive final choices remain documented in `TRANSLATION_REVIEW.md`, including p.47 `property rights`, p.57 `cut ourselves free`, p.59 `our land`, and p.60 `bring forth Rahmans in State after State`.

## Final closure checks

The completed closure confirmed:

1. complete speech-page continuity through scan pp.3–60 in Tamil and English;
2. Unit 1 → Unit 2 boundary at scan p.38 intact;
3. headings, interventions, quotations, names, dates, figures, money, percentages and units remained intact after refinement;
4. all 34 refinement decisions are implemented in reader-facing English;
5. workflow metadata/status documents are reconciled;
6. no Assembly/Council Official Report wording entered the text.

## Translation control records

Under `sources/1971-namathu-nilai/translations/en/`:

- `TRANSLATION_PLAN.md`
- `PROGRESS.md`
- `GLOSSARY.md`
- `TRANSLATION_REVIEW.md`

Actual reader-facing English remains only in:

`speeches/1971/1971-namathu-nilai/translation.md`

## Future-change rule

There is no routine next activity for this source. It is closed.

A future Tamil correction requires direct visual evidence from `ACL-CPL_01726_நமது_நிலை.pdf`. A future English correction must be derived only from the verified booklet Tamil and immediate booklet context. External legislative wording remains prohibited.
