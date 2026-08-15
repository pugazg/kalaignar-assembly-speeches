# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 8

Speeches 1–8 of the anthology are fully released through Gate H. Do not restart or modify their verified Tamil/English content while processing Speech 9.

## Active unit — Speech 9

- source label: `உரை : 9`
- printed date: `8.05.2000`
- ISO date: `2000-05-08`
- canonical ID: `2000-05-08-industries-debate`
- PDF scan pages: **278–303**
- printed pages: **277–302**
- page relationship: scan page = printed page + 1
- scan p.277 closes Speech 8
- scan p.278 begins Speech 9
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`)

Both locked boundaries were re-confirmed directly from the controlling scan before Speech 9 transcription began. The working PDF matched the locked **329 pages**, **217,124,211 bytes**, and SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Speech 9 Gate C progress

- Batch 1: pp.278–282 / printed 277–281; cumulative 5/26; post-write p.282 correction `முக்கிய களமாக` → `முக்கிய தளமாக`, commit `dbdcdab67fee3085607bd8929d5cf0b524a8ed85`.
- Batch 2: pp.283–287 / printed 282–286; cumulative 10/26; transcript commit `3fc93b8b3bb7860db225ead53511a747149a0ebd`.
- Batch 3: pp.288–292 / printed 287–291; cumulative 15/26; transcript commit `8de59961b972844acffb7f831d1867d2193cbf9d`.
- Batch 4: pp.293–297 / printed 292–296; cumulative 20/26; transcript commit `dcc52ef8fcc7a48517dfa924f5dc297e7a96867d`.
- **Batch 5: pp.298–302 / printed 297–301; cumulative 25/26; complete.**

Current Speech-9 state after Batch 5:

- cumulative source coverage: **278–302 / 25 of 26 pages**
- cumulative printed coverage: **277–301**
- source-page markers: **278–302**, once and in strict order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next and final Gate-C source page: **303**
- initial Batch-5 transcript commit: `ed2ade25fb1f3808a8cb8f6bfd0918ca1be7f3a5`
- corrected canonical transcript commit: `8ed2c3685857e16b368139252386b623875284ab`
- corrected transcript blob: `67b1cc071ce4c8c04c1ea6748a65e0ffd1d91d3b`
- metadata commit: `d644f57d18ce8c15b6925528a3130cb5b7da9e8f`
- README commit: `7746597e74e8b2b69dcb91771351895fca753318`
- source-notes commit: `160ecfcb0d9985850573b863772487388914a7cf`
- verification-log commit: `7ae977e13f78e05ca4059685be67bbc19d130e9c`

### Batch-5 post-write corrections

A high-resolution reread found four definite Gate-C transcription corrections. Commit `8ed2c3685857e16b368139252386b623875284ab` was inspected and contains exactly these four textual changes:

1. p.298 `பழனிசாமி ஏற்றுக்கொள்கிறாரோ` → `பழனிசாமி ஏற்றுக் கொள்கிறாரோ`;
2. p.298 `டி. மணி ஏற்றுக்கொள்கிறாரோ` → `டி. மணி ஏற்றுக் கொள்கிறாரோ`;
3. p.300 `சிமெண்ட் தயார்செய்வதன்` → `சிமெண்ட் தயார் செய்வதன்`;
4. p.300 `குறைந்த விலையில் தயார்செய்து` → `குறைந்த விலையில் தயார் செய்து`.

These are first-pass Gate-C corrections, **not** Gate-E verification corrections.

### Batch-5 source-sensitive forms

Preserve without external reconciliation:

- p.298 `ரைட்` and the source-varying `ஏற்றுக்கொள்கிறாரோ` / `ஏற்றுக் கொள்கிறாரோ` forms;
- p.299 `'TANCEM'`, `12-12-1994`, the printed English Counter Affidavit and the source Tamil paraphrase `மூன்றாவது பிரதிவாதியான டான்செம் நிறைவேற்றவில்லை.`;
- p.300 the two printed Government English sentences and So. Balakrishnan's `தயார் செய்வதன்` / `தயார் செய்து` wording;
- p.301 production figures: 3,33,000; 4,13,000; 4,34,000; 3,77,000; 4,29,000; 4,63,000; 5,38,000; 4,87,000; 4,46,000 tons for 1991-92 through 1999-2000;
- p.302 `அம்புஜா`, Rs.85 / Rs.145, `50 சதவிகிதத்திலே`, Chief Secretary committee and 111 cut motions.

Source p.302 ends **mid-sentence** after exactly:

`வெட்டுத் தீர்மானங்களுடைய எண்ணிக்கை 111. நம்பர்`

## Exact next activity — Speech 9 Gate C final Batch 6

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `sources/2007-industrial-speeches/mapping.md`, and current Speech-9 files before writing.
2. Process **source/scan p.303 / printed p.302 only**.
3. Begin with the exact continuation after `111. நம்பர்`; do not reconstruct from memory or outside knowledge.
4. Transcribe p.303 directly from the rendered scan, preserving all wording, punctuation, numerals, speaker labels, interventions and any printed English.
5. Add `<!-- source-page: 303 -->` exactly once.
6. Confirm that p.303 contains the Speech-9 close/ornament and that **no p.304 / Speech-10 material** is included.
7. Record any genuinely uncertain reading explicitly rather than guessing.
8. If p.303 completes cleanly, Gate C becomes **26/26 pages, source pp.278–303 / printed pp.277–302**. The Tamil transcription status may then become `transcribed`, but **not verified**.
9. After Gate C closure, **Gate D completeness/page-marker audit is the next activity**. Do not begin Gate E or English translation in the same bounded activity unless explicitly requested.
