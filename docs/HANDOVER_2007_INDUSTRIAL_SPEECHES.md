# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 8

Speeches 1–8 of the anthology are fully released through Gate H. Do not restart or modify their verified Tamil/English content while processing Speech 9.

Latest released unit: Speech 8 (`உரை : 8`, `29.04.1999`, `1999-04-29-industries-debate`), scan pp.241–277 / printed pp.240–276. Tamil Gate E and English Gate G passed and Gate H is released. Source p.278 begins Speech 9; there is no Speech-9 spillover in Speech 8.

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

### Batch 1 — complete

- source/scan pp.278–282 / printed pp.277–281
- cumulative after Batch 1: **5/26 pages**
- post-write Gate-C correction on p.282: `முக்கிய களமாக` → `முக்கிய தளமாக`
- correction commit: `dbdcdab67fee3085607bd8929d5cf0b524a8ed85`

### Batch 2 — complete

- source/scan pp.283–287 / printed pp.282–286
- cumulative after Batch 2: **10/26 pages**
- canonical transcript commit: `3fc93b8b3bb7860db225ead53511a747149a0ebd`

### Batch 3 — complete

- source/scan pp.288–292 / printed pp.287–291
- cumulative after Batch 3: **15/26 pages**
- canonical transcript commit: `8de59961b972844acffb7f831d1867d2193cbf9d`

### Batch 4 — complete

- source/scan pages: **293–297**
- printed pages: **292–296**
- cumulative coverage: **20/26 pages, source pp.278–297 / printed pp.277–296**
- page markers: **278–297**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next source page: **298**
- canonical Batch-4 transcript commit: `dcc52ef8fcc7a48517dfa924f5dc297e7a96867d`
- metadata commit: `4d166a5f5b59bd79f79fcad682602903dbecfcb6`
- README commit: `52507b64a83fac54432fa40a24473a803bacf519`
- source-notes commit: `bc80283fe01b0ea7fe2de978c03312927be7b5c6`
- verification-log commit: `d88ee0575563db9c61368cd40cb8f83b51d56d5b`

The Batch-4 transcript diff was inspected and changes only the Gate-C coverage note plus appended source sections 293–297; completed pp.278–292 were not rewritten.

Batch 4 begins by continuing Tanflora with `ஓசூரில் 220 ஏக்கர்...`. A high-resolution reread supports the unusual printed p.293 form `இன்னொன்றியில் சென்னை வர்த்தக மையம்;`, so no uncertainty marker is needed. Preserve the source-specific forms `(TIDCO)`, `(ITPO)`, `20.000`, `Bio-Technology`, `வழங்கப்பட விருக்கிறது`, `industrial gases`, `பென்னார் ரிபைனர்ஸ் லிமிடெட்`, `கவிதி மலைப் பகுதிகளிலும்`, `இரும்புத் துண்டங்களை`, `நாம்தா டெக்ஸ்டைல்ஸ்`, and the p.296 printed date **`24-3-2001`** even though this speech is dated 8.05.2000. Do not externally reconcile that date. P.297 preserves `பேசவில்லை யானாலும்`, the repeated `விற்காது, விற்காது`, and the no-privatisation assurance concerning Ariyalur cement plant / Tamil Nadu Cements divisions.

Source p.297 ends **mid-sentence** after exactly:

`ஆனால், தினமும்`

Do not reconstruct the continuation from memory or outside sources; resume directly from rendered scan p.298.

## Exact next activity — Speech 9 Gate C Batch 5

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `sources/2007-industrial-speeches/mapping.md`, and current Speech-9 `metadata.json`, `README.md`, `source-notes.md`, `transcript.md`, `verification-log.md` before writing.
2. Process **source/scan pp.298–302 / printed pp.297–301**.
3. Begin p.298 with the exact continuation of the unfinished p.297 sentence after `ஆனால், தினமும்`.
4. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and printed English. Do not silently modernise or fact-correct.
5. Use source markers `<!-- source-page: 298 -->` through `<!-- source-page: 302 -->`, each once and in order.
6. Record every genuinely uncertain reading explicitly rather than guessing.
7. Do not rewrite pp.278–297 unless a concrete source-supported transcription mistake is discovered and explicitly documented.
8. If all five pages complete cleanly, cumulative Gate-C coverage becomes **25/26 pages, source pp.278–302 / printed pp.277–301**, and next source page becomes **303**.
9. Gate C remains first-pass only. Do not mark Tamil verified; Gate D and Gate E are later full-speech stages.
10. Do not transcribe p.303 or begin Speech 10 in the same bounded activity unless the user explicitly changes priority.
11. Do not begin English translation.
