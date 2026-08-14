# Next-chat prompt — Speech 7 Gate E Batch 1 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart transcription. Gate C is complete and Gate D has passed.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely before doing any work.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the existing canonical folder `speeches/1998/1998-05-14-industries-debate/` and continue the existing files.
5. Inspect the actual controlling PDF scan before making any Gate-E correction. OCR/extracted text and the existing transcript are helpers; the rendered scan image controls.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- OCR/extracted text is helper-only
- do not silently modernise, correct, normalise, reconstruct or improve printed Tamil

If the controlling PDF is unavailable in a new chat, attach:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Do not perform Gate-E verification without the scan.

## Released anthology state

Speeches **1–6** are fully released with verified Tamil and verified English. Do not modify them absent a separately justified correction.

Speech-6 Gate-H release commit: `188a79e1b9de76b6bf2bbe037185aef2b6ffe7b1`.

## Speech 7 locked identity

- source label: `உரை : 7`
- printed date: `14.05.1998`
- ISO date: `1998-05-14`
- canonical ID: `1998-05-14-industries-debate`
- scan pages: **199–240**
- printed pages: **198–239**
- total mapped pages: **42**
- scan page = printed page + 1
- p.198 closes Speech 6
- p.199 begins Speech 7
- p.240 closes Speech 7
- p.241 begins Speech 8 dated `29.04.1999`

## Completed Speech-7 state

- Gate C: **complete — 42/42 pages**, scan pp.199–240;
- Gate D: **passed**;
- Tamil status: **transcribed, not verified**;
- Gate E: **not started**;
- unresolved/`[REVIEW]` readings: **0**;
- English: **blocked**.

Gate-D structural audit confirmed exact source-page coverage **199–240**, no gaps/duplicates/reordering, no p.241 marker, correct opening/closing boundaries, closing speaker/intervention sequence, printed English Venkatasamy passage, and no Speech-8 spillover.

Relevant checkpoints:

- complete Gate-C transcript: `4432eaa5e584d881e38cd606b3f6b7f5306b76ef`
- Gate-D metadata: `bad345777cd6f49a7f002a623680376392cc23ce`
- Gate-D README: `7407681b41a4df9b1aad56bd2933766391065980`
- Gate-D source notes: `6463e1ee8d6972d9c8992ac76b1951bbbcb3bfc1`
- Gate-D verification log: `7b8408cb5f5b39322d52acb7dd96bbb28147015b`
- refreshed handover: `3ee32418c68fc7239c803efd11ff5bcae4692d76`

## Exact next activity — Speech 7 Gate E Batch 1

1. Re-open the controlling scan at **scan p.199 / printed p.198**.
2. Strictly verify **scan pp.199–213 / printed pp.198–212** against canonical `transcript.md`.
3. Check every page for individual Tamil words/characters, names and initials, dates, percentages, monetary values, acreage/units, headings, speaker labels, interventions/context markers, embedded/printed English, punctuation where legible and cross-page continuity.
4. The scan wins over OCR, extracted text, external knowledge and plausible reconstruction.
5. Preserve unusual/historical/source forms. Do not modernise or silently fix source errors.
6. Apply each source-supported transcription correction to canonical `transcript.md` and itemise it in `verification-log.md` with scan page / printed page.
7. Record unresolved readings explicitly rather than guessing.
8. Update `README.md`, `metadata.json`, `source-notes.md` and `verification-log.md` with Gate-E Batch-1 progress.
9. After this batch, Tamil remains **transcribed, not verified**. Gate E will still have scan pp.214–240 to audit.
10. Do not begin English until Gate E passes for all 42 pages.
11. Do not begin Speech 8.

At the end of the session, refresh the handover and this next-chat prompt with the exact Gate-E continuation page and relevant commit SHA(s).
