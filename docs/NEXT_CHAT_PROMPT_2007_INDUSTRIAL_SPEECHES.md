# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- root `README.md`
- `data/speeches.json`
- `speeches/1990/1990-04-18-industries-debate/` as the latest released structural precedent

Treat those repository files as controlling instructions. The scan image is authoritative for Tamil transcription; OCR is only a helper and is never canonical.

## Completed released work

Speeches 1–4 from this anthology are fully released with verified Tamil and verified English:

- `1963-03-21-industries-debate` — scan pp.18–26
- `1981-04-16-industries-debate` — scan pp.27–61
- `1989-05-03-industries-debate` — scan pp.62–98
- `1990-04-18-industries-debate` — scan pp.99–135

Speech 4 completed Gates C–H. Its canonical `transcript.md` contains verified Tamil first and verified English after it. The temporary translation companion was retired after canonical integration.

Important source anomalies intentionally retained in Speech 4 include printed `financed`, `constitute and Inter-Ministerial Committee`, `cilicon`, `stainlees`, `Spensioner Mill`, `ancilary`, the separate p.120/p.121 `கேஸ்டிக்`/`காஸ்டிக்` forms, and p.128 `ஆலங்குடி 3, 1, அறந்தாங்கி 4`.

## Important Speech 3 correction already completed

On Speech-3 source p.94 the verified Tamil reads `சிப்காட், டிக் நிறுவனங்களிடமிருந்து...` and must remain `டிக்` in the Tamil source layer. The final English uses **`SIPCOT and TIIC`** as an explicitly documented institutional identification. Do not revert it to `TIC`.

## Current active work — Speech 5

- Source label: `உரை : 5`
- Printed date: `14.08.1996`
- Canonical ID: `1996-08-14-industries-debate`
- Full scan range: **136–171**
- Printed pages: **135–170**
- Total mapped scan pages: **36**
- Gate C: **not started**
- Tamil status: **not started**
- English: **blocked until Tamil Gates C–E are complete**
- Speech 5 folder: **not yet created**

Boundary is already locked: scan p.135 ends Speech 4; scan p.136 / printed p.135 begins `உரை : 5`, dated `14.08.1996`.

## Next action — Speech 5 Gate C Batch 1

Begin Tamil first-pass transcription for **scan pp.136–150 / printed pp.135–149**.

1. Reconfirm the Speech-5 opening on scan p.136 directly from the rendered page.
2. Create `speeches/1996/1996-08-14-industries-debate/` with the standard five files:
   - `README.md`
   - `metadata.json`
   - `source-notes.md`
   - `transcript.md`
   - `verification-log.md`
3. Transcribe scan pp.136–150 directly from the scan images. OCR may assist but must not be treated as canonical text.
4. Preserve printed wording, period spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as far as the scan permits.
5. Add one explicit `<!-- source-page: N -->` marker for every scan page transcribed.
6. Mark genuinely unreadable text explicitly for review rather than guessing.
7. At the end of scan p.150, record the exact continuation words/boundary and set `next_scan_page` to **151**.
8. Keep Speech 5 `in-progress`; Gate D is not eligible until all scan pages **136–171** are represented.
9. Do not start English translation, Speech 6, or modify already released Speeches 1–4 except for necessary index consistency.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with the Batch-1 range, continuation point, unresolved readings, files changed, commit SHAs and exact next action.

---
