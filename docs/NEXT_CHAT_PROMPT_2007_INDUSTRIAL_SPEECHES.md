# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1989/1989-05-03-industries-debate/`

Treat those files as controlling instructions. The scan image is authoritative; OCR is not canonical.

## Completed released work

Speech 1 (`1963-03-21-industries-debate`) and Speech 2 (`1981-04-16-industries-debate`) are fully released with verified Tamil and verified English and must remain untouched unless separately requested.

## Current active work — Speech 3

- Source label: `உரை : 3`
- Printed date: `03.05.1989`
- Canonical ID: `1989-05-03-industries-debate`
- Full scan range: **62–98**
- Printed pages: **61–97**
- Gate C: **complete**
- Gate D: **passed**
- Tamil status: **transcribed**
- Explicit unresolved-reading markers: **0**
- Gate E: **not started**
- English: **blocked / not started**
- Final first-pass transcript commit: `d61e938659da1f41bb9188608835146e4f980556`
- Gate-D verification-log commit: `32823326403fc8560880ac21257d7c7f3ebac881`

Gate D confirmed exactly **37** source-page markers, unique and monotonic from **62 through 98**. Scan p.98 ends Speech 3 with Kalaignar's reply to `திரு. வி. கே. சின்னசாமி` followed by the decorative ending ornament; scan p.99 begins `உரை : 4 / நாள் : 18.04.1990`.

## Next action — Speech 3 Gate E

Perform a strict direct page-by-page visual/source-fidelity audit of the complete Tamil transcription against scan pp. **62–98**.

1. Fetch/read current `transcript.md`, `metadata.json`, `source-notes.md`, `verification-log.md` and `README.md` from `main` before editing.
2. Re-read every scan image p.62 through p.98 directly; scan images control every reading.
3. Compare each canonical source-page section against its scan, checking words/characters, names/initials, dates, numerals, percentages, monetary values/units, printed English/transliterations, headings, speaker labels/interventions, punctuation where legible, and page-transition continuity.
4. Apply every concrete correction to `transcript.md` and document every correction in `verification-log.md`.
5. Preserve visibly printed unusual source forms; do not silently modernise or historically correct them.
6. If a reading remains genuinely uncertain, leave an explicit review marker rather than guessing.
7. Only after all pp.62–98 are directly checked may Tamil status become `verified`; update metadata/README/source notes accordingly.
8. English translation remains blocked until Gate E passes.
9. Do not begin Speech 4.

After Gate E passes, the next workflow stage is Gate F English translation from the final verified Tamil.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with exact pages reviewed, corrections made, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.

---
