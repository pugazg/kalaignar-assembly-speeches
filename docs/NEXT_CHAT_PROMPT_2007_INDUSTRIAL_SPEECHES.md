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
- Gate E: **passed**
- Tamil status: **verified**
- Explicit unresolved-reading markers: **0**
- English: **not started**
- Verified transcript commit: `56716121b7535a3ba22475135e10ae93e4c3c22f`
- Gate-E final verification-log commit: `523d7cbf26b1d0e605c5abe65a85974559983cbb`

Gate E directly checked every scan page **62–98** and corrected four first-pass discrepancies:

- p.73 `கருத்தக் கூடாது` → `கருதக் கூடாது`;
- p.94 `சுவரார் அளித்த சலுகைகளும்` → `கவர்னர் அளித்த சலுகைகளும்`;
- p.96 `பரிசீலிப்பு விழாக்களில்` → `பரிசளிப்பு விழாக்களில்`;
- p.97 `கூடங்குளம் போகும்` → `கூடங்குளம் போக்கும்`.

Visibly printed unusual source forms and inconsistencies were retained rather than editorially repaired. No unresolved Tamil reading remains.

## Next action — Speech 3 Gate F English translation

Translate the **final verified Tamil only** and append the English translation after the complete Tamil source layer in `transcript.md`.

1. Fetch/read current Speech 3 `transcript.md`, `metadata.json`, `source-notes.md`, `verification-log.md` and `README.md` from `main` before editing.
2. Translate from the final verified Tamil, not OCR and not an earlier draft.
3. Preserve the complete argumentative/source sequence and parliamentary context.
4. Preserve speaker changes/interventions, quotations, names, initials, dates, numerals, percentages, monetary values, units, printed-English passages and technical/transliterated terms consistently.
5. Do not silently correct historical claims, source inconsistencies or period terminology.
6. Follow the established Speech 2 English-layer precedent, including source-page correspondence through **62–98**.
7. Complete the full English translation before starting Gate G.
8. Do not update root release/index files yet.
9. Do not begin Speech 4.

After Gate F, perform Gate G by re-reading the complete English page by page against the final verified Tamil. Only after Gate G passes may English become `verified` and Speech 3 proceed to Gate H release/index.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with English translation status, files changed, commit SHA and exact next action.

---
