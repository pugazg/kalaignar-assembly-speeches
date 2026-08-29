# Handover — 1971 `நமது நிலை`

## Repository

`pugazg/kalaignar-assembly-speeches`

Branch: `main`

Source package: `sources/1971-namathu-nilai/`  
Reader-facing entry: `speeches/1971/1971-namathu-nilai/`

## Non-negotiable textual-authority rule

The **only transcription and translation authority** is:

`ACL-CPL_01726_நமது_நிலை.pdf`

Do not transcribe from, complete from, repair from, normalize toward, or merge wording from any Tamil Nadu Legislative Assembly or Legislative Council PDF.

Those legislative PDFs are **reference/provenance only**. The same restriction applies to English refinement and closure: use only the verified booklet Tamil and immediate booklet context.

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

## Tamil source status

**Complete and visually verified against all 60/60 booklet scan pages.**

- accepted scan-supported corrections: **175**
- unresolved source readings: **0**
- external legislative wording imported: **none**

The six source transcription files under `sources/1971-namathu-nilai/transcription/` are frozen. Do not alter them unless a direct re-check of the controlling booklet scan proves an error.

## Provenance status

The four underlying reply events and both three-way provenance ledgers have been identified/completed. They remain metadata only.

Structural conclusion:

- Unit 1 combines Assembly- and Council-associated material;
- Unit 2 interleaves Assembly- and Council-associated material multiple times;
- therefore the booklet must be preserved as printed rather than reconstructed into House transcripts.

## Reader-facing representation

Files under `speeches/1971/1971-namathu-nilai/`:

- `README.md`
- `metadata.json`
- `source-notes.md`
- `transcript.md`
- `translation.md`

This is a **booklet-level speech compilation**, not a claim that the whole text is one dated Assembly speech. Scan pp.1–2 are publication front matter/source metadata and are not inserted as spoken text.

## Current translation status

- Tamil reader-facing population: **scan pp.3–60 complete — 58/58 speech pages**
- English Gate-F first pass: **scan pp.3–60 complete — 58/58 speech pages**
- Gate F: **complete**
- Gate-G page-by-page fidelity review: **complete — scan pp.3–60, 58/58 speech pages**
- Editorial Unit 1 Gate-G review: **complete — 35/35 pages**
- Editorial Unit 2 Gate-G review: **complete — 23/23 pages**
- Gate-G blocking fidelity issues: **0**
- verified Tamil changes during Gate G: **none**
- non-blocking English refinement candidates queued: **34**
- English verified: **no — consolidated refinement and final closure remain**

## Gate-G completion

All batches are complete:

- G1 pp.3–10
- G2 pp.11–18
- G3 pp.19–26
- G4 pp.27–34
- G5 pp.35–37
- G6 pp.38–44
- G7 pp.45–51
- G8 pp.52–58
- G9 pp.59–60

G9 specifically verified the Congress-member `வணங்காதீர்கள், வளையாதீர்கள்` / `புறநானூற்றுத் தாய்` passage, State Planning Commission and ten-year-plan discussion, 1972-73 reference, `உரிமைக் குரல்`, decentralisation/State-autonomy framing, Pakistan/East Pakistan sequence and final parliamentary-method close. No blocking issue was found.

## Refinement queue

`TRANSLATION_REVIEW.md` contains **34 numbered non-blocking candidates** from G1–G9.

High-priority item:

- scan p.57 `அறுத்துக்கொள்ள வேண்டும்`, currently rendered `wrest it free`. The Tamil reflexive expression is semantically difficult in this passage. Reconsider it only from the verified booklet Tamil and immediate context. Preserve ambiguity if necessary; do not resolve it from Official Reports or outside historical reconstruction.

Other candidates concern naturalness/source closeness in headings, idioms, rhetorical phrases, source English/Tamil explanatory repetition and a few institution/term choices. None was a blocking fidelity defect in page-level Gate G.

## Translation control records

Under `sources/1971-namathu-nilai/translations/en/`:

- `TRANSLATION_PLAN.md`
- `PROGRESS.md`
- `GLOSSARY.md`
- `TRANSLATION_REVIEW.md`

Actual reader-facing English remains only in:

`speeches/1971/1971-namathu-nilai/translation.md`

Do not create a second independently editable English translation under `sources/`.

## Exact next activity

Proceed with the **consolidated English refinement pass over candidates 1–34** in `TRANSLATION_REVIEW.md`.

For each candidate:

1. compare current English only with the verified booklet Tamil and immediate booklet context;
2. decide whether to revise or retain the wording;
3. if revising, update only reader-facing `translation.md` and preserve source-page boundaries/order;
4. record the final decision for that candidate in `TRANSLATION_REVIEW.md`;
5. preserve ambiguity where the booklet itself is ambiguous;
6. do **not** use Assembly/Council Official Report wording.

After all 34 decisions, perform the final closure check of page markers, headings, names, figures, money, percentages and units. Only after that may English be marked verified.

At every step:

> **Text and translation authority = `ACL-CPL_01726_நமது_நிலை.pdf` via the verified Tamil transcription only.**
