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
- a fully released anthology speech folder such as `speeches/1989/1989-05-03-industries-debate/` as the structural precedent

Treat those repository files as controlling instructions. The scan image is authoritative; OCR is only a helper and is never canonical.

## Completed released work

Speeches 1, 2 and 3 from this anthology are fully released with verified Tamil and verified English and must remain untouched unless separately requested:

- `1963-03-21-industries-debate` — scan pp.18–26
- `1981-04-16-industries-debate` — scan pp.27–61
- `1989-05-03-industries-debate` — scan pp.62–98

Speech 3 Gate H is complete. Release commits:

- root README: `3e3dfe207435dd8d78ef263d472798e2acc248e5`
- `data/speeches.json`: `a83d671fb6d313e30c3846658f38546eff049796`
- Speech 3 final README release state: `3cef665ace36720a29b06710799810e985a59143`
- Speech 3 final source notes: `94a5fd5610157440e0cc0630dab4493f26790b22`
- Speech 3 final verification log: `8c5dac2bf2d563d9fbb4f50bc69c65706e67ac0c`

The machine-readable index was validated as valid JSON after the Speech 3 append, and the pre-existing released records were unchanged.

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
9. Do not start English translation, Speech 5, or modify any already released speech/index record.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with the Batch-1 page range, continuation point, unresolved readings, files changed, commit SHAs and exact next action.

---
