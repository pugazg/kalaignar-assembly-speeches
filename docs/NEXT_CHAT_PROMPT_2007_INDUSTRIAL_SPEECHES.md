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
- `speeches/1989/1989-05-03-industries-debate/` as the released structural precedent

Treat those repository files as controlling instructions. The scan image is authoritative for Tamil transcription; OCR is only a helper and is never canonical.

## Completed released work

Speeches 1, 2 and 3 from this anthology are fully released with verified Tamil and verified English:

- `1963-03-21-industries-debate` — scan pp.18–26
- `1981-04-16-industries-debate` — scan pp.27–61
- `1989-05-03-industries-debate` — scan pp.62–98

Speech 3 Gate H release commits:

- root README: `3e3dfe207435dd8d78ef263d472798e2acc248e5`
- `data/speeches.json`: `a83d671fb6d313e30c3846658f38546eff049796`

## Important Speech 3 correction already completed

On source p.94 the verified Tamil scan/transcription reads `சிப்காட், டிக் நிறுவனங்களிடமிருந்து...` and must remain `டிக்` in the Tamil source layer.

The final English, however, must use **`SIPCOT and TIIC`**. A previous Gate-G choice had rendered this as `TIC` merely to mirror the Tamil letters, but the project owner clarified that the intended Tamil Nadu industrial institution is TIIC, not TIC.

This is an explicitly documented editorial/institutional identification in English and must **not** be reverted to `TIC`.

Correction commits:

- Speech 3 `transcript.md`: `822bb9ca97d43655f80ec222b2a4572a898c3e58`
- Speech 3 `README.md`: `0adad93cd31e71a88900cad5a35180b619974f5e`
- Speech 3 `source-notes.md`: `0eadb079ed213a14517f437e49f0483ce9c9c750`
- Speech 3 `verification-log.md`: `5b2016282588dcec121e2354c567711eda4e47da`
- updated handover: `3c8c799799959d7ef6d07bc44171d35d9b83b441`

## Current active work — Speech 4

- Source label: `உரை : 4`
- Printed date: `18.04.1990`
- Canonical ID: `1990-04-18-industries-debate`
- Full scan range: **99–135**
- Printed pages: **98–134**
- Total mapped scan pages: **37**
- Gate C: **not started**
- Tamil status: **not started**
- English: **blocked until Tamil Gates C–E are complete**
- Speech 4 folder: **not yet created**

Boundary already locked: scan p.98 ends Speech 3; scan p.99 / printed p.98 begins `உரை : 4`, dated `18.04.1990`.

## Next action — Speech 4 Gate C Batch 1

Begin the Tamil first-pass transcription for **scan pp.99–113 / printed pp.98–112**.

1. Reconfirm the Speech 4 opening on scan p.99 directly from the rendered page.
2. Create `speeches/1990/1990-04-18-industries-debate/` with the standard five files:
   - `README.md`
   - `metadata.json`
   - `source-notes.md`
   - `transcript.md`
   - `verification-log.md`
3. Transcribe scan pp.99–113 directly from the scan images. OCR may assist but must not be treated as canonical text.
4. Preserve printed wording, period spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as far as the scan permits.
5. Add one explicit `<!-- source-page: N -->` marker for every scan page transcribed.
6. Mark genuinely unreadable text explicitly for review rather than guessing.
7. At the end of scan p.113, record the exact continuation words/boundary and set `next_scan_page` to **114**.
8. Keep Speech 4 `in-progress`; Gate D is not eligible until all scan pages **99–135** are represented.
9. Do not start English translation, Speech 5, or modify already released speeches/index entries.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with the Batch-1 range, continuation point, unresolved readings, files changed, commit SHAs and exact next action.

---
