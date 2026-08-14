# Next-chat prompt — Speech 7 Gate E Batch 3 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart transcription or Gate E. Gate C is complete, Gate D passed, and Gate E Batches 1–2 have passed through scan p.228.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect `speeches/1998/1998-05-14-industries-debate/` and continue the existing canonical files.
5. Inspect the actual controlling PDF scan before making any correction. The rendered scan controls; OCR/extracted text and the existing transcript are helpers only.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- do not silently modernise, normalise, reconstruct or improve printed Tamil

If the controlling PDF is unavailable in a new chat, attach:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

## Speech 7 locked identity

- source label: `உரை : 7`
- date: `14.05.1998`
- canonical ID: `1998-05-14-industries-debate`
- scan pages: **199–240**
- printed pages: **198–239**
- total mapped pages: **42**
- scan page = printed page + 1
- p.241 begins Speech 8 and must not be included

## Completed state

- Gate C: **complete — 42/42 pages**;
- Gate D: **passed**;
- Gate E Batch 1: **passed — scan pp.199–213 / printed pp.198–212**;
- Gate E Batch 2: **passed — scan pp.214–228 / printed pp.213–227**;
- Gate E audited: **30/42 pages**;
- Gate-E corrections: **5 cumulative**;
- unresolved/`[REVIEW]`: **0**;
- Tamil status: **transcribed, not verified**;
- English: **blocked**.

Batch-1 corrections are documented in the repository. Batch-2 canonical corrections in transcript commit `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693` are:

1. scan p.214 / printed p.213 — `552 ஏக்கர்` → `532 ஏக்கர்` for the Hyundai land allotment;
2. scan p.227 / printed p.226 — `புயூஜிகுரா லிமிடெட்` → `ப்யூஜிகுரா லிமிடெட்`.

Relevant Batch-2 checkpoints:

- transcript: `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693`
- metadata: `0dde50ee34d942d81eb233923c0b9ee374955ae3`
- README: `3016e1b9bd61509307cae00ac593c23bb915a0ce`
- source notes: `5974d9ac73ca2db8bc1e2dc9f83902d8fa8556ec`
- verification log: `fe553776f0eabe2e4079b60606f5e05b81b7a116`
- handover: `bbc3492b8e7b2b9735632b6df6177692f3a41db0`

## Exact next activity — Speech 7 Gate E Batch 3

1. Re-open the controlling scan at **scan p.229 / printed p.228**.
2. Strictly verify the remaining Speech-7 range **scan pp.229–240 / printed pp.228–239** against canonical `transcript.md`.
3. Check Tamil words/characters, names/initials, dates, percentages, monetary values, acreage/units, headings, speaker labels, interventions/context markers, embedded/printed English, punctuation where legible and cross-page continuity.
4. The scan wins over OCR, extracted text, outside knowledge and plausible reconstruction.
5. Preserve unusual/historical/source forms.
6. Apply each source-supported correction to canonical `transcript.md` and itemise it in `verification-log.md` with scan/printed page references.
7. Record unresolved readings explicitly rather than guessing.
8. Stop at the p.240 closing boundary. Do not include p.241 / Speech 8.
9. If all remaining 12 pages pass, perform a full Gate-E closure check over all **42/42** Speech-7 pages and update all status files accordingly.
10. Only after full Gate E passes may Tamil be marked verified and English Gate F begin.
11. Do not begin Speech 8.

At the end of the session, refresh the handover and this prompt with Gate-E closure status, exact next activity and relevant commit SHA(s).
