# Next-chat prompt — Speech 9 Gate C Batch 2 / 8.05.2000

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speeches **1–8** from the 2007 industrial-speeches anthology are fully released through Gate H with verified Tamil and verified English. **Do not restart, retranscribe or modify those released entries.** Speech 9 has now been started and Gate C Batch 1 is complete.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current Speech-9 `metadata.json`, `README.md`, `source-notes.md`, `transcript.md` and `verification-log.md`.
5. Continue the existing `speeches/2000/2000-05-08-industries-debate/` entry; do not create a duplicate.
6. Use the controlling scan as the textual authority. OCR or parsed text may assist but must not override the rendered scan.

## Speech 9 locked mapping

- source label: `உரை : 9`
- printed date: `8.05.2000`
- ISO date: `2000-05-08`
- canonical ID: `2000-05-08-industries-debate`
- scan/source pages: **278–303**
- printed pages: **277–302**
- scan p.277 closes Speech 8
- scan p.278 begins Speech 9
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`)

The p.277→278 and p.303→304 boundaries were re-confirmed directly from the controlling scan at Speech-9 startup. The working PDF also matched the locked 329-page count, file size and SHA-256.

## Current Speech-9 state

Gate C Batch 1 is complete:

- transcribed source/scan pages: **278–282**
- corresponding printed pages: **277–281**
- cumulative coverage: **5/26 pages**
- page markers: **278–282**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next source page: **283**
- current transcript checkpoint: `dbdcdab67fee3085607bd8929d5cf0b524a8ed85`
- current verification-log checkpoint: `cb6711a21e876b9c5601d63e4e5c79cf11fd0690`

A post-write scan reread corrected one definite Gate-C transcription error on source p.282: `முக்கிய களமாக` → `முக்கிய தளமாக`. The correction commit changed only that word; it does not constitute Gate-E verification.

Important source-sensitive forms already preserved:

- p.280 `22-4-200` versus later `22-4-2000`;
- p.280 `1,14,893 கோடி ரூபாய்` versus p.281 `1,41,893 + 15,000 = 1,56,893 கோடி ரூபாய்`;
- the printed-English *Economic Times* passage on p.282;
- embedded English export-category labels on p.281.

Source p.282 ends mid-sentence after exactly:

`இந்த 1999-2000-ல்`

## Exact next activity — Gate C Batch 2

Process **source/scan pp.283–287 / printed pp.282–286**.

1. Inspect rendered scan p.283 and continue directly from the unfinished p.282 sentence; do not reconstruct the continuation from memory or outside knowledge.
2. Transcribe pp.283–287 directly from the scan, preserving wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and printed English.
3. Do not silently modernise, reconstruct, fact-correct or reconcile internally inconsistent figures. Physical line wraps alone may be normalised into readable paragraphs.
4. Add explicit source markers `<!-- source-page: 283 -->` through `<!-- source-page: 287 -->`, each exactly once and in order.
5. Record every genuinely uncertain reading explicitly rather than guessing.
6. Append only to the current Tamil first-pass transcript; do not rewrite completed pp.278–282 unless a concrete source-supported transcription mistake is discovered and explicitly documented.
7. Update Speech-9 metadata, README, source notes and verification log after the batch.
8. If all five pages complete cleanly, cumulative Gate-C coverage becomes **10/26 pages, source pp.278–287 / printed pp.277–286**, and next source page becomes **288**.
9. Gate C remains only a first-pass transcription. Do not mark Tamil `verified`; Gates D and E remain later full-speech stages.
10. Do not begin English translation and do not begin Speech 10.

After this bounded activity, the expected next activity is **Speech 9 Gate C Batch 3 beginning source p.288**, unless the source requires a documented exception.
