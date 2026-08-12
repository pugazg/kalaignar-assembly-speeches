# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1981/1981-04-16-industries-debate/`

Treat those files as controlling instructions. The scan image is authoritative; OCR is not canonical.

## Current state

Speech 1 (`1963-03-21-industries-debate`) is fully released with verified Tamil and English and must remain untouched.

Speech 2:

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Full scan range: **27–61**
- Printed pages: **26–60**

### Completed

The Tamil first-pass transcription is complete for **all scan pp.27–61**, in three batches: 27–41, 42–56, and 57–61.

The full-speech Tamil completeness audit has passed:

- 35 source-page markers, 27–61 inclusive;
- unique and monotonic;
- no mapped page skipped or duplicated;
- opening and ending align with the locked map;
- printed speaker changes/interventions are represented;
- no explicit unreadable/`[REVIEW]` placeholder remains;
- scan p.61 ends Speech 2 with Kalaignar's final intervention and a decorative ornament;
- scan p.62 begins `உரை : 3 / நாள் : 03.05.1989`.

Current Tamil status is **`transcribed`**, not `verified`.

A direct visual reading corrected the old p.57 continuation note: the scan reads `பட்டிருக்கிறார்கள். இது ஒன்றும் புதிதும் அல்ல.`

English translation remains **blocked / not started**. Do not update the root release index or `data/speeches.json` yet.

## Next action — strict Tamil verification

Proceed directly with **Gate E: strict page-by-page visual/source-fidelity verification of Speech 2, scan pp.27–61**.

Compare the complete canonical Tamil transcript directly against every scan image. At minimum check:

- words and individual Tamil characters;
- names and initials;
- numerals, dates, percentages, monetary amounts and units;
- printed English passages;
- headings and speaker labels;
- interventions/interruptions;
- punctuation where legible;
- page-transition omissions or repetitions.

Apply corrections to the canonical transcript and document them in `verification-log.md`.

Do **not** mark Tamil `verified` until the full 35-page visual audit is genuinely complete. Do **not** begin English translation before that point.

Preserve source wording, period spelling, printer errors and historical claims rather than silently correcting them. Mark genuinely unreadable text for review rather than guessing. Do not infer the speaker's historical office from general knowledge.

At the end provide an exact handover: pages visually verified, corrections made, unresolved readings, Tamil status, English status, files changed, commit SHA, and exact next action.

---
