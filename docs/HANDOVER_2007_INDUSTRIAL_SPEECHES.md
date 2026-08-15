# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 8

Speeches 1–8 of the anthology are fully released through Gate H. Do not restart or modify their verified Tamil/English content while processing Speech 9.

Latest released unit:

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- Tamil Gate E: **passed — 37/37 pages**, 29 corrections, 0 unresolved readings
- English Gate G: **passed — 37/37 pages**, 1 correction, 0 unresolved issues
- Gate H: **passed / released**
- source p.278 begins Speech 9; there is **no Speech-9 spillover** in Speech 8

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

Before Speech 9 transcription began, both locked boundaries were re-confirmed directly from the controlling scan. The attached working PDF also independently matched the locked **329 pages**, **217,124,211 bytes**, and SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Speech 9 Gate C progress

### Batch 1 — complete

- source/scan pages: **278–282**
- printed pages: **277–281**
- cumulative coverage after Batch 1: **5/26 pages**
- unresolved first-pass readings: **0**
- transcript correction checkpoint: `dbdcdab67fee3085607bd8929d5cf0b524a8ed85`

A post-write visual reread of source p.282 caught one definite first-pass error: `முக்கிய களமாக` → `முக்கிய தளமாக`. This was a Gate-C correction, not Gate-E verification.

Important Batch-1 source-sensitive forms remain locked for later Gate E: p.280 `22-4-200` versus `22-4-2000`; p.280 `1,14,893` versus p.281 `1,41,893 + 15,000 = 1,56,893`; the p.282 printed-English *Economic Times* passage; and p.281 embedded English export labels.

### Batch 2 — complete

- source/scan pages: **283–287**
- printed pages: **282–286**
- cumulative coverage: **10/26 pages, source pp.278–287 / printed pp.277–286**
- page markers: **278–287**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **in-progress; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**
- next source page: **288**
- canonical Batch-2 transcript commit: `3fc93b8b3bb7860db225ead53511a747149a0ebd`

The Batch-2 commit diff was inspected and changes only the Gate-C coverage note plus the appended source sections 283–287; pp.278–282 were not rewritten.

Batch-2 source-sensitive forms to preserve:

- p.283 printed-English *Industrial Herald* quotation beginning `Now the third largest, the Tamil Nadu economy...`;
- p.284 exact sequence `e-Mail. e-Commerce, e-Medicine, e-Value, e-biz.` followed by `e-business--, e-Stock, e-Education`, plus source `Internet` / later `internet` capitalisation;
- p.286 clearly printed but semantically unusual `இந்தக் கேமிரா கழுவும்போது இருட்டான இடங்களையும் வெளிச்சமாக்கும்.`;
- p.286 `V.S.N.L.`, `DoT`, `Thermal Energy Storage System`, `Venture Capital Fund`, TIDEL Park figures and `4-ந் தேதியன்று`;
- p.287 `தமிழ்நெட் 1999`, `Tamil Virtual University`, the 1,200-school / 600+600 / 48,000-student figures.

Source p.287 ends **inside a High Court quotation** after exactly:

`தமிழக அரசின்மீது இந்த நீதிமன்றம்`

Do not reconstruct the continuation from memory or outside sources; resume directly from rendered scan p.288.

Current Speech-9 repository state after Batch 2:

- transcript commit: `3fc93b8b3bb7860db225ead53511a747149a0ebd`
- metadata commit: `738c968d98c3d1dee17b8bd51012c7a9e89914d8`
- README commit: `302a18d6f3dc4283536c68923de44fb279438b73`
- source-notes commit: `4aab6da7724af6681c297e72b79be3f6549e20d5`
- verification-log commit: `5966c7593403b612293c2dd46180667581fa544b`

## Exact next activity — Speech 9 Gate C Batch 3

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `sources/2007-industrial-speeches/mapping.md`, and the current Speech-9 files before writing.
2. Process **source/scan pp.288–292 / printed pp.287–291**.
3. Begin p.288 with the exact continuation of the unfinished High Court quotation from p.287.
4. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and printed English. Do not silently modernise or fact-correct.
5. Use source markers `<!-- source-page: 288 -->` through `<!-- source-page: 292 -->`, each once and in order.
6. Record every genuinely uncertain reading explicitly rather than guessing.
7. Do not rewrite pp.278–287 unless a concrete source-supported transcription mistake is discovered and explicitly documented.
8. If all five pages complete cleanly, cumulative Gate-C coverage becomes **15/26 pages, source pp.278–292 / printed pp.277–291**, and next source page becomes **293**.
9. Gate C remains first-pass only. Do not mark Tamil verified; Gates D and E remain later full-speech stages.
10. Do not begin English translation or Speech 10.
