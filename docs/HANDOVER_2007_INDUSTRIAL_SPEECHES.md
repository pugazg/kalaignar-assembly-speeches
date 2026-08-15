# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter it while processing Speech 8.

## Active unit — Speech 8

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Tamil gates

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E: **passed — 37/37 pages directly verified against scan**
- cumulative Gate-E corrections: **29**
- unresolved Tamil readings: **0**
- Tamil status: **verified**
- canonical Gate-E completion checkpoint: `7ddf8745a4c3417750c0c7130ae20edb8b4cca62`

## English Gate F

- Gate F: **complete — 37/37 pages**
- translated source/scan pages: **241–277**
- corresponding printed pages: **240–276**
- unresolved Gate-F translation questions: **0**
- final Gate-F canonical merge checkpoint: `ed79a499ecb56f8fb750f5ea9d946d1b2a71fde3`
- final Batch-8 staging file deleted after clean merge: `006b846958383f354dd27e3fe8066c4982261d69`
- Speech-8 boundary confirmed at source p.277; source p.278 begins Speech 9; **no spillover**

## English Gate G

- Gate G: **in progress**
- Batches 1–4 reviewed source/scan pp. **241–260** / printed pp. **240–259**
- reviewed pages: **20/37**
- definite Gate-G fidelity corrections applied cumulatively: **1**
- Batch-2 corrections: **0**
- Batch-3 corrections: **0**
- Batch-4 corrections: **0**
- unresolved fidelity issues: **0**
- next Gate-G source page: **261**
- English overall status: **complete, not yet verified**
- Gate-G review record: `speeches/1999/1999-04-29-industries-debate/translation-review.md`
- current canonical English blob: `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`

Batch 1 applied one definite English fidelity correction on source p.245. Gate F had translated `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்` as `You are taking the nameplate and going away with it.` Gate G corrected this to **`You are taking the credit for it.`** Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`; the inspected diff contains only that English change.

Batches 2–3 reviewed source pp.246–255 and required **no further canonical English correction**.

Batch 4 reviewed source pp.256–260 and also required **no canonical English correction**. It reconfirmed the Alangulam cement factory; Ranipet 729 acres / 107 industries / Rs.168 crore; Hosur 1,236 acres / 186 factories / Rs.500 crore; 293 industries / approximately 20,000 jobs; the 1989–90 factory list; the source-specific p.257 **Rs. 1.125 crore** versus p.258 **Rs. 1,125 crore** distinction; the 21-versus-28 factory comparison; Rs.6,067 crore / 9,626 jobs / further 28 projects / Rs.22,946 crore / 11,000 jobs; Irungattukottai 1,829 acres; Hyundai / Mitsubishi / Ford / Iljin; and the component-industry entries through source p.260, including the Mayilsamy Gounder → Mayilanandam passage. Source company-name forms were preserved rather than normalised externally.

## Exact next activity — Gate G Batch 5

Review **source/scan pp.261–265 / printed pp.260–264** against the final verified Tamil.

Requirements:

1. Fetch the final verified Tamil and current canonical English for the exact bounded range.
2. Compare page-by-page for omissions, additions, meaning shifts, cross-page continuations, names, dates, figures, units, technical/company names, printed English and humour/idiom.
3. Preserve source-specific claims and internally unusual figures; do not fact-correct from outside knowledge.
4. Pay special attention to the industrial-project/company list, Saint-Gobain / SIPCOT / biotech / TIDEL / Pennar / SISCOL / Ennore L.N.G. / Jayankondam material and the source's internally differing Pennar **Rs.320 crore** versus **Rs.3,200 crore** statements.
5. Check the C.M.I.E. investment-ranking figures and horse-race / tug-of-war rhetoric on p.265 exactly against the verified Tamil.
6. Apply only definite English fidelity corrections.
7. Inspect every canonical translation diff before advancing reviewed coverage. If no correction is required, record the unchanged canonical blob checkpoint.
8. Update `translation-review.md`, metadata, README, handover and next prompt truthfully.
9. If Batch 5 passes, Gate G advances to **25/37 pages**, next source page **266**.
10. English remains **not fully verified** until all source pp.241–277 pass Gate G.
11. Do not begin Speech 9 or Gate H until Speech 8 Gate G passes unless the user explicitly changes priority.

Batch 5 begins on source p.261 with Karur Yarn Links / Taurus Novelties / Sriram Auto Components and related projects, continues through Saint-Gobain and the newer project list, and ends on source p.265 with the C.M.I.E. State-wise industrial-investment comparison and the `Economic Times` lead-in dated 28-4-1999.
