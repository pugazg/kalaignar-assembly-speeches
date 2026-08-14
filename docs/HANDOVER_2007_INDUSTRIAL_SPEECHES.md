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
- Gate E: **in progress — Batches 1 and 2 passed, 30/42 pages audited**
- Gate-E corrections so far: **5**
- unresolved/`[REVIEW]`: **0**
- Tamil status: **transcribed, not verified**
- English: **blocked until Gate E passes**

## Gate E Batch 1 — passed

Audited **scan pp.199–213 / printed pp.198–212**. Three canonical corrections were applied in commit `4c42c979f087a78cdaeef3e96a12506bcdd7693e`:

1. p.202 `விற்கப்படுகின்ற` → `விற்கப்படுகிற`;
2. p.205 `தெரிவித்து உண்மை` → `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கின்றேன்` → `சுட்டிக் காட்டியிருக்கிறேன்`.

## Gate E Batch 2 — passed

Audited **scan pp.214–228 / printed pp.213–227** directly against rendered scan images. Two canonical corrections were applied in transcript commit `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693`:

1. **scan p.214 / printed p.213** — Hyundai allotment `552 ஏக்கர்` → `532 ஏக்கர்`;
2. **scan p.227 / printed p.226** — `புயூஜிகுரா லிமிடெட்` → `ப்யூஜிகுரா லிமிடெட்`.

No other definite canonical correction was identified on pp.215–226 or 228 in this pass. Unusual source forms were retained and helper-OCR alternatives were not treated as authority.

After Batch 2:

- audited pages: **30/42**, scan pp.199–228 / printed pp.198–227;
- cumulative Gate-E corrections: **5**;
- unresolved readings: **0**;
- exact next scan page: **229**.

Batch-2 checkpoints:

- canonical transcript correction commit: `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693`
- metadata: `0dde50ee34d942d81eb233923c0b9ee374955ae3`
- README: `3016e1b9bd61509307cae00ac593c23bb915a0ce`
- source notes: `5974d9ac73ca2db8bc1e2dc9f83902d8fa8556ec`
- verification log: `fe553776f0eabe2e4079b60606f5e05b81b7a116`

## Exact next activity — Speech 7 Gate E Batch 3

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`, and `sources/2007-industrial-speeches/mapping.md`.
2. Continue the existing canonical Speech-7 files; do not restart transcription or Gate E.
3. Re-open the controlling scan at **scan p.229 / printed p.228**.
4. Audit the remaining Speech-7 range **scan pp.229–240 / printed pp.228–239** page by page.
5. Check Tamil characters/word forms, names, figures, dates, money, percentages, acreage/units, printed English, speaker/intervention labels, contextual markers, punctuation where legible and cross-page continuity.
6. The scan image is authoritative; OCR is helper only. Preserve unusual/historical printed forms.
7. Apply only source-supported corrections to canonical `transcript.md`; itemise every correction in `verification-log.md`.
8. Record uncertainty explicitly rather than guessing.
9. Stop at the p.240 Speech-7 closing boundary. Do **not** enter p.241 / Speech 8.
10. If all remaining 12 pages pass, perform Gate-E full-speech closure checks over all 42 pages. Only then may Tamil status become verified.
11. Do not begin English before full Gate E passes.

At the end, refresh this handover and the next-chat prompt with Gate-E closure status and relevant commit SHA(s).

## New-window source requirement

The controlling PDF is not stored in GitHub. If unavailable in a new chat, attach `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf` before scan-level verification continues.

## End-of-handoff state

Speeches 1–6 remain released and untouched. Speech 7 is the active unit. **Gate E Batches 1–2 passed through scan p.228; resume exactly at scan p.229 for the final Gate-E Batch 3, pp.229–240.**
