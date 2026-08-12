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
- Current gate: **Gate C — Tamil first-pass transcription**
- Completed first-pass scan pages: **62–91**
- Completed printed pages: **61–90**
- Tamil status: **in-progress**
- Explicit unresolved-reading markers: **0 currently flagged**; this does not imply verification
- Gate D: **not yet eligible**
- Gate E: **not started**
- English: **blocked / not started**
- Final batch-2 Speech-3 state commit: `9e99d34323e1c52921a5db921310e7f24d2b63df`

Important continuation evidence:

- scan p.91 ends mid-sentence with `தோல் தொழிற்சாலை`;
- scan p.92 continues `பற்றிக்கூட சொன்னார்கள். அந்த மாசுகளையும் ...`.

## Next action — Speech 3 Gate C, final first-pass batch

Continue directly with:

- scan pp. **92–98**
- printed pp. **91–97**

1. Fetch/read the existing Speech 3 `transcript.md`, `metadata.json`, `source-notes.md`, `verification-log.md` and `README.md` from current `main` before editing.
2. Render/read scan pp.92–98 from the attached source; scan images control every reading.
3. Append Tamil only, preserving explicit `<!-- source-page: N -->` markers.
4. Preserve printed wording, period spelling, punctuation, numerals, quotations, speaker changes/interventions, technical terms and printed English. Do not silently modernise or repair unusual source forms.
5. If a reading is genuinely uncertain after direct visual inspection, leave an explicit review marker rather than guessing.
6. Update Speech 3 support files to the exact completed range and ending boundary.
7. Once p.98 is transcribed, run Gate D across the full scan range **62–98**: confirm exactly **37** source-page markers, unique and monotonic; no mapped page skipped/duplicated; correct p.62 start and p.98 ending; interventions preserved; unresolved readings explicit.
8. Do not begin Gate E or English translation until Gate D is complete and the next Tamil step is explicitly established.
9. Do not begin Speech 4.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with exact pages completed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.

---
