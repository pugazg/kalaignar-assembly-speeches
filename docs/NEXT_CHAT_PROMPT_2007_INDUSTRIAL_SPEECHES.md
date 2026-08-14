# Next-chat prompt — Speech 7 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Start **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely before doing any work.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the repository and confirm `speeches/1998/1998-05-14-industries-debate/` has not already been started. If work exists, continue it rather than creating duplicates.
5. Inspect the actual controlling PDF scan before creating metadata or transcription. Do not rely on the filename, OCR, extracted text, or prior prose summaries.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- OCR/extracted text is only a helper
- do not silently modernise, correct, normalise, reconstruct, or improve printed Tamil

The PDF itself is not stored in the repository. If it is not available in this new chat, ask me to attach:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Do not begin scan-level transcription without the controlling PDF.

## Released anthology state

Speeches **1–6** are fully released with verified Tamil and verified English. Do not modify them absent a separately justified correction.

Speech-6 Gate-H canonical release commit: `188a79e1b9de76b6bf2bbe037185aef2b6ffe7b1`.

## Speech 7 locked identity

- source label: `உரை : 7`
- printed date: `14.05.1998`
- ISO date: `1998-05-14`
- canonical ID: `1998-05-14-industries-debate`
- scan pages: **199–240**
- printed pages: **198–239**
- total mapped pages: **42**
- scan page = printed page + 1
- scan p.198 closes released Speech 6
- scan p.199 begins Speech 7 with `உரை : 7`, `நாள் : 14.05.1998`
- locked structural map ends Speech 7 at scan p.240
- scan p.241 begins Speech 8 dated `29.04.1999`

## Exact first activity — Speech 7 Gate C Batch 1

1. Directly re-confirm the p.198→199 and p.240→241 boundaries from the controlling scan.
2. Create the standard Speech-7 canonical folder/files if absent:
   - `README.md`
   - `metadata.json`
   - `source-notes.md`
   - `transcript.md`
   - `verification-log.md`
3. Transcribe **scan pp.199–213 / printed pp.198–212** as the first bounded Tamil batch unless the source structure gives a strong reason to stop earlier.
4. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as supported by the scan. Only physical line wrapping may be normalised.
5. Record exact pages completed, first/last continuation words, unresolved readings and the next scan page.
6. Keep Tamil status `in-progress`; do not mark `transcribed` or `verified` after a partial batch.
7. Do not start English. English remains blocked until the complete Tamil passes Gates D and E.
8. Do not begin Speech 8.

At the end of the session, refresh the handover and next-chat prompt with the exact continuation point and relevant commit SHA(s).
