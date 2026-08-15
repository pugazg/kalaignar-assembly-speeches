# Next-chat prompt — Speech 9 Gate C final Batch 6 / 8.05.2000

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speeches **1–8** from the 2007 industrial-speeches anthology are fully released through Gate H with verified Tamil and verified English. **Do not restart, retranscribe or modify those released entries.** Speech 9 is active and Gate C Batches 1–5 are complete.

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

Both boundaries were re-confirmed directly from the controlling scan at Speech-9 startup. The working PDF matched the locked 329-page count, file size and SHA-256.

## Current Speech-9 state

Gate C Batches 1–5 are complete:

- transcribed source/scan pages: **278–302**
- corresponding printed pages: **277–301**
- cumulative coverage: **25/26 pages**
- page markers: **278–302**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next and final Gate-C source page: **303**
- initial Batch-5 transcript commit: `ed2ade25fb1f3808a8cb8f6bfd0918ca1be7f3a5`
- corrected canonical transcript commit: `8ed2c3685857e16b368139252386b623875284ab`
- corrected transcript blob: `67b1cc071ce4c8c04c1ea6748a65e0ffd1d91d3b`
- metadata checkpoint: `d644f57d18ce8c15b6925528a3130cb5b7da9e8f`
- README checkpoint: `7746597e74e8b2b69dcb91771351895fca753318`
- source-notes checkpoint: `160ecfcb0d9985850573b863772487388914a7cf`
- verification-log checkpoint: `7ae977e13f78e05ca4059685be67bbc19d130e9c`

The Batch-5 append diff was inspected. A subsequent high-resolution reread identified four definite source-reading corrections, and correction commit `8ed2c3685857e16b368139252386b623875284ab` was inspected to contain exactly these four changes:

- p.298 `பழனிசாமி ஏற்றுக்கொள்கிறாரோ` → `பழனிசாமி ஏற்றுக் கொள்கிறாரோ`;
- p.298 `டி. மணி ஏற்றுக்கொள்கிறாரோ` → `டி. மணி ஏற்றுக் கொள்கிறாரோ`;
- p.300 `சிமெண்ட் தயார்செய்வதன்` → `சிமெண்ட் தயார் செய்வதன்`;
- p.300 `குறைந்த விலையில் தயார்செய்து` → `குறைந்த விலையில் தயார் செய்து`.

These are Gate-C first-pass corrections, not Gate-E verification.

Important Batch-5 source-sensitive forms to preserve include p.298 `ரைட்` and the varying auxiliary spacing; p.299 `'TANCEM'`, `12-12-1994`, the printed `Counter Affidavit` English and the source Tamil phrase `மூன்றாவது பிரதிவாதியான டான்செம் நிறைவேற்றவில்லை.`; p.300 the two printed Government English sentences; p.301 the exact cement-production figures; and p.302 `அம்புஜா`, Rs.85 / Rs.145, `50 சதவிகிதத்திலே` and 111 cut motions.

Source p.302 ends mid-sentence after exactly:

`வெட்டுத் தீர்மானங்களுடைய எண்ணிக்கை 111. நம்பர்`

## Exact next activity — Gate C final Batch 6

Process **source/scan p.303 / printed p.302 only**.

1. Inspect rendered scan p.303 and continue directly after `111. நம்பர்`; do not reconstruct the continuation from memory or outside knowledge.
2. Transcribe p.303 directly from the scan, preserving wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and any printed English.
3. Add explicit source marker `<!-- source-page: 303 -->` exactly once.
4. Record every genuinely uncertain reading explicitly rather than guessing.
5. Do not rewrite pp.278–302 unless a concrete source-supported transcription mistake is discovered and explicitly documented.
6. Confirm the Speech-9 closing ornament/boundary on p.303 and **do not include scan p.304**, which begins Speech 10.
7. If p.303 completes cleanly, cumulative Gate-C coverage becomes **26/26 pages, source pp.278–303 / printed pp.277–302**. Change the Tamil first-pass status from `in-progress` to **`transcribed`**, but keep `verified_against_scan=false`; Gate E has not happened.
8. Update metadata, README, source notes and verification log to close Gate C truthfully.
9. After Gate C closure, the **next activity is Gate D — full Tamil completeness/page-marker audit**. Do not begin Gate E or English translation in this bounded activity unless explicitly requested.
10. Do not begin Speech 10.
