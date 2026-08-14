# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English must be translated from and verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Locked map: `sources/2007-industrial-speeches/mapping.md`

## Released anthology state

Speeches **1–6** are fully released with verified Tamil and verified English. Leave them untouched absent a separately justified correction.

## Active unit — Speech 7

- source label: `உரை : 7`
- date: `14.05.1998`
- canonical ID: `1998-05-14-industries-debate`
- locked scan range: **199–240**
- locked printed range: **198–239**
- mapped pages: **42**
- Gate C: **complete — 42/42**
- Gate D: **passed**
- Gate E: **in progress — Batch 1 passed, 15/42 pages audited**
- Gate-E corrections so far: **3**
- unresolved/`[REVIEW]`: **0**
- Tamil status: **transcribed, not verified**
- English: **blocked until Gate E passes**

## Gate E Batch 1 — passed

Audited **scan pp.199–213 / printed pp.198–212** directly against rendered scan images.

Canonical corrections applied in commit `4c42c979f087a78cdaeef3e96a12506bcdd7693e`:

1. p.202 `விற்கப்படுகின்ற` → `விற்கப்படுகிற`;
2. p.205 `தெரிவித்து உண்மை` → `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கின்றேன்` → `சுட்டிக் காட்டியிருக்கிறேன்`.

A preliminary correction note had incorrectly treated two already-present passages as omissions. The current canonical blob was fetched before modification, confirming that the p.202 administered-price paragraph and p.209 Economic Intelligency Unit introduction were already present. No duplicate text was inserted; `gate-e-batch1-corrections.md` was corrected accordingly.

Batch-1 status checkpoints:

- canonical transcript corrections: `4c42c979f087a78cdaeef3e96a12506bcdd7693e`
- corrected Gate-E Batch-1 record: `b268d0d6b62ce8366258260303915e7052bd41c7`
- metadata: `cfa53dec9a3febc14269a1127a3cc7928d86381b`
- verification log: `7e8164170d29c53ce837a21625c4bda73387e845`
- README: `4d7fc9162bbc777d39d6dcf829c28e41d784c424`

## Exact next activity — Speech 7 Gate E Batch 2

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`, and `sources/2007-industrial-speeches/mapping.md`.
2. Continue the existing canonical Speech-7 files; do not restart transcription or Gate E.
3. Re-open the controlling scan at **scan p.214 / printed p.213**.
4. Audit **scan pp.214–228 / printed pp.213–227** page by page against the scan.
5. Check Tamil characters/word forms, names, figures, dates, money, percentages, acreage/units, printed English, interventions, punctuation where legible and cross-page continuity.
6. Scan image is authoritative; OCR is helper only.
7. Apply only source-supported corrections to canonical `transcript.md`; itemise every correction in `verification-log.md`.
8. Record uncertainty explicitly rather than guessing.
9. After Batch 2, Gate E will still have scan pp.229–240 remaining.
10. Do not begin English before Gate E passes all 42 pages.
11. Do not begin Speech 8.

## New-window source requirement

The controlling PDF is not stored in GitHub. If unavailable in a new chat, attach `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf` before scan-level verification continues.

## End-of-handoff state

Speeches 1–6 remain released and untouched. Speech 7 is the active unit. **Gate E Batch 1 passed through scan p.213; resume exactly at scan p.214 for Batch 2 (pp.214–228).**
