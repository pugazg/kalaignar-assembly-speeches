# Next-chat prompt — Speech 9 Gate C Batch 5 / 8.05.2000

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speeches **1–8** from the 2007 industrial-speeches anthology are fully released through Gate H with verified Tamil and verified English. **Do not restart, retranscribe or modify those released entries.** Speech 9 is active and Gate C Batches 1–4 are complete.

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

Gate C Batches 1–4 are complete:

- transcribed source/scan pages: **278–297**
- corresponding printed pages: **277–296**
- cumulative coverage: **20/26 pages**
- page markers: **278–297**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next source page: **298**
- Batch-4 canonical transcript commit: `dcc52ef8fcc7a48517dfa924f5dc297e7a96867d`
- metadata checkpoint: `4d166a5f5b59bd79f79fcad682602903dbecfcb6`
- README checkpoint: `52507b64a83fac54432fa40a24473a803bacf519`
- source-notes checkpoint: `bc80283fe01b0ea7fe2de978c03312927be7b5c6`
- verification-log checkpoint: `d88ee0575563db9c61368cd40cb8f83b51d56d5b`

The Batch-4 transcript diff was inspected and contains only the Gate-C coverage-note update plus appended source pp.293–297. Completed pp.278–292 were not rewritten.

Important Batch-4 source-sensitive forms include:

- p.293 high-resolution reread supports `இன்னொன்றியில் சென்னை வர்த்தக மையம்;`;
- `(TIDCO)`, `(ITPO)`, `20.000 சதுர மீட்டர்`, `5000 சதுர மீட்டர்`, `30-1-2000`, `2000 நவம்பரில்`;
- `Bio-Technology`, `உயிரியல் தொழில் நுட்பவியல் ஊக்க மூலதன நிதி`, `வழங்கப்பட விருக்கிறது`;
- p.293→294 split after `அதிவேகப் பயன்பாட்டிற்கு`, then `உகந்த டீசல்`;
- `ப்ராக்சேர் இந்தியா பிரைவேட் லிமிடெட்`, `industrial gases`, `செயிண்ட் கோபைன்`, `பென்னார் ரிபைனர்ஸ் லிமிடெட்`;
- `கவிதி மலைப் பகுதிகளிலும்`, `இரும்புத் துண்டங்களை`, `நாம்தா டெக்ஸ்டைல்ஸ்`;
- p.296 explicitly prints **`24-3-2001`** despite the speech date `8.05.2000`; preserve it exactly and do not fact-correct;
- p.297 `பேசவில்லை யானாலும்`, repeated `விற்காது, விற்காது`, and the no-privatisation assurance.

Source p.297 ends mid-sentence after exactly:

`ஆனால், தினமும்`

## Exact next activity — Gate C Batch 5

Process **source/scan pp.298–302 / printed pp.297–301**.

1. Inspect rendered scan p.298 and continue directly from the unfinished p.297 sentence; do not reconstruct the continuation from memory or outside knowledge.
2. Transcribe pp.298–302 directly from the scan, preserving wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and printed English.
3. Do not silently modernise, reconstruct, fact-correct or reconcile internally unusual source wording. Physical line wraps alone may be normalised into readable paragraphs.
4. Add explicit source markers `<!-- source-page: 298 -->` through `<!-- source-page: 302 -->`, each exactly once and in order.
5. Record every genuinely uncertain reading explicitly rather than guessing.
6. Append only to the current Tamil first-pass transcript; do not rewrite completed pp.278–297 unless a concrete source-supported transcription mistake is discovered and explicitly documented.
7. Update Speech-9 metadata, README, source notes and verification log after the batch.
8. If all five pages complete cleanly, cumulative Gate-C coverage becomes **25/26 pages, source pp.278–302 / printed pp.277–301**, and next source page becomes **303**.
9. Gate C remains only a first-pass transcription. Do not mark Tamil `verified`; Gates D and E remain later full-speech stages.
10. Do not include p.303 in this batch; it is the final Speech-9 page and should be handled in the next bounded activity unless the user explicitly changes priority.
11. Do not begin English translation and do not begin Speech 10.

After this bounded activity, the expected next activity is **Speech 9 Gate C final Batch 6 — source p.303 / printed p.302**, followed by Gate D only after Gate C is fully complete.
