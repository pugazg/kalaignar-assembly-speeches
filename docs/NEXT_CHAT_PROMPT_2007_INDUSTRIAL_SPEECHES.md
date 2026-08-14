# Next-chat prompt — Speech 7 Gate C Batch 2 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart Speech 7. Gate C Batch 1 is already complete through scan p.213.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely before doing any work.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the existing canonical folder `speeches/1998/1998-05-14-industries-debate/` and continue the files already there. Do not create duplicates and do not rewrite completed Batch-1 pages merely for style.
5. Inspect the actual controlling PDF scan before continuing transcription. Do not rely on OCR, extracted text, prior prose summaries or the repository transcript as source authority.

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
- scan p.240 closes Speech 7
- scan p.241 begins Speech 8 dated `29.04.1999`

Both boundaries were directly re-confirmed from the controlling scan during Batch 1; the locked map did not change.

## Completed Speech-7 state — Gate C Batch 1

The five canonical files exist under `speeches/1998/1998-05-14-industries-debate/`.

Batch 1 completed:

- scan pages: **199–213**
- printed pages: **198–212**
- completed pages: **15/42**
- remaining pages: **27**
- Tamil status: **in-progress**
- unresolved/uncertainty readings: **0**
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked**

Two post-write Gate-C typing corrections were directly checked against the scan and applied to canonical `transcript.md`:

1. p.202 `அந்த இடைப்பட்ட தொகைவை` → `அந்த இடைப்பட்ட தொகையை`;
2. p.207 `அதிகே மிகுந்த எச்சரிக்கையோடு` → `அதிலே மிகுந்த எச்சரிக்கையோடு`.

Do not treat those corrections as Gate E; the strict full-speech Tamil fidelity audit has not begun.

Relevant checkpoints:

- corrected Batch-1 canonical transcript: `e3ddee675269c65a756fe0641b20668554df732f`
- Batch-1 verification log/content checkpoint: `4fa6eb6ef84e3931b6440d78c63f2ab59982b7f7`
- refreshed handover after Batch 1: `515be2ccd4d5702490572ab916754298198f1a33`

## Exact continuation

Canonical `transcript.md` currently ends scan p.213 / printed p.212 with:

`மேலும், எண்ணெய்க் கசடு`

Direct inspection of the controlling scan shows scan p.214 / printed p.213 begins the continuation:

`வெளுகிறதே, அதிலேயிருந்து மின்சாரம் தயாரிக்கலாம், 250`

The exact next source page is therefore **scan p.214 / printed p.213**.

## Exact next activity — Speech 7 Gate C Batch 2

1. Re-open scan pp.213→214 and confirm the continuation above before appending anything.
2. Continue the existing `transcript.md` from **scan p.214 / printed p.213**.
3. Transcribe the next bounded batch **scan pp.214–228 / printed pp.213–227**, unless the source structure gives a strong reason to stop earlier.
4. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as supported by the scan. Only physical line wrapping may be normalised.
5. Append explicit `<!-- source-page: N -->` markers in order. Do not alter already completed pp.199–213 unless a separately documented source-supported correction is discovered.
6. Record exact pages completed, ending continuation words, unresolved readings and next scan page in the Speech-7 status/audit files.
7. Keep Tamil status `in-progress`; Batch 2 will still be partial if it ends at p.228.
8. Do not begin Gate D or Gate E until all mapped Speech-7 pages **199–240** have a complete first-pass Tamil transcription.
9. Do not start English. English remains blocked until the complete Tamil passes Gates D and E.
10. Do not begin Speech 8.

If Batch 2 reaches p.228 as planned, the likely final Gate-C batch is scan pp.229–240 / printed pp.228–239; verify that from the scan rather than assuming.

At the end of the session, refresh the handover and this next-chat prompt again with the exact continuation point and relevant commit SHA(s).
