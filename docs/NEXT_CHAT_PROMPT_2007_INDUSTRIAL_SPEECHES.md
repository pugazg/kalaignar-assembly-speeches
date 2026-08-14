# Next-chat prompt — Speech 7 Gate C Batch 3 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart Speech 7. Gate C Batches 1 and 2 are already complete through scan p.228.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely before doing any work.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the existing canonical folder `speeches/1998/1998-05-14-industries-debate/` and continue the files already there. Do not create duplicates and do not rewrite completed pages merely for style.
5. Inspect the actual controlling PDF scan before continuing transcription. Do not rely on OCR, extracted text, prior prose summaries or the repository transcript as source authority.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- OCR/extracted text is only a helper
- do not silently modernise, correct, normalise, reconstruct, or improve printed Tamil

The PDF itself is not stored in the repository. If it is not available in a new chat, ask for:

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
- scan p.199 begins Speech 7
- scan p.240 closes Speech 7
- scan p.241 begins Speech 8 dated `29.04.1999`

Both boundaries have been directly re-confirmed from the controlling scan.

## Completed Speech-7 state — Gate C Batches 1 and 2

The five canonical files already exist under `speeches/1998/1998-05-14-industries-debate/`.

Completed:

- Batch 1: scan pp.**199–213** / printed pp.**198–212** — 15 pages;
- Batch 2: scan pp.**214–228** / printed pp.**213–227** — 15 pages;
- cumulative represented pages: **30/42**;
- remaining pages: **12**;
- Tamil status: **in-progress**;
- unresolved/uncertainty readings: **0**;
- Gate D: **not started**;
- Gate E: **not started**;
- English: **blocked**.

Relevant Batch-2 checkpoints:

- canonical transcript through p.228: `938679d94990e460d23ba0a72c7488c94f65e839`
- metadata: `a74e71a4aa9fd440563e034ed76ad0c69c453c99`
- README: `b99d6b266aea3e8b4e117207e5e8a6f6b2c420db`
- source notes: `eb7135364874cc66c2d41689fa66df8781ffd82c`
- verification log: `0926fc9939401eb5eb078604fa6ec8230a6de2f4`
- refreshed handover: `7362a4975d8fcff521120b69781c88218026bda5`

## Exact continuation

Canonical `transcript.md` currently ends scan p.228 / printed p.227 with:

`இதற்கான ஒப்பந்தம் 7-1-1998 அன்று கையெழுத்தானது.`

Direct inspection of the controlling scan shows scan p.229 / printed p.228 begins:

`PVC foamed sheets -செயற்கை மரப்பொருள் திட்டம்.`

The exact next source page is therefore **scan p.229 / printed p.228**.

## Exact next activity — Speech 7 Gate C Batch 3

1. Re-open scan pp.228→229 and confirm the continuation above before appending anything.
2. Continue the existing `transcript.md` from **scan p.229 / printed p.228**.
3. Transcribe the remaining Speech-7 range **scan pp.229–240 / printed pp.228–239**.
4. Stop at the Speech-7 closing ornament on p.240. Do not include scan p.241 / Speech 8.
5. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as supported by the scan. Only physical line wrapping may be normalised.
6. Append explicit `<!-- source-page: N -->` markers in order. Do not alter already completed pp.199–228 unless a separately documented source-supported correction is discovered.
7. Record uncertain readings rather than guessing.
8. After p.240 is transcribed, assert exact Gate-C page coverage **199–240**, with no gaps, duplicates, reordering or p.241 spillover. Only then may Tamil status become `transcribed`.
9. Perform **Gate D** as a separate full-speech completeness/page-marker audit after Gate C completes. Do not conflate Gate C completion with Gate D.
10. Do not begin Gate E until Gate D passes.
11. Do not start English. English remains blocked until the complete Tamil passes Gates D and E.
12. Do not begin Speech 8.

At the end of the session, refresh the handover and this next-chat prompt again with Gate-C completion, Gate-D status, exact next activity and relevant commit SHA(s).
