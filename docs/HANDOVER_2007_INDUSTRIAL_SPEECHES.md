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
- final Batch-8 staging file has been deleted after clean merge: deletion commit `006b846958383f354dd27e3fe8066c4982261d69`
- Speech-8 boundary confirmed at source p.277; source p.278 begins Speech 9; **no spillover**

## English Gate G

- Gate G: **in progress**
- Batch 1 reviewed source/scan pp. **241–245** / printed pp. **240–244**
- reviewed pages: **5/37**
- definite Gate-G fidelity corrections applied: **1**
- unresolved fidelity issues: **0**
- next Gate-G source page: **246**
- English overall status: **complete, not yet verified**
- Gate-G review record: `speeches/1999/1999-04-29-industries-debate/translation-review.md`

Batch 1 confirmed the opening, Ranganathan and south-district passages, Subbarayan/TANCEM/athirasam material, TWAD tender figures and terms, Tiruppur court-stay discussion, Singapore/Malaysia/Colachel/flying-road passage, Nellore comparison, Sundaram's three-instalment joke, Ford/MoU/1996 passage and the p.245→246 Pugalur continuation.

One definite English fidelity correction was applied on source p.245. Gate F had translated `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்` as `You are taking the nameplate and going away with it.` Gate G corrected this to **`You are taking the credit for it.`** Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`. The diff contains only this English change.

## Exact next activity — Gate G Batch 2

Review **source/scan pp.246–250 / printed pp.245–249** against the final verified Tamil.

Requirements:

1. Fetch the final verified Tamil and current canonical English for the exact bounded range.
2. Compare page-by-page for omissions, additions, meaning shifts, cross-page continuations, speaker/context markers, names, dates, figures, units, technical/company names and humour/idiom.
3. Preserve source-specific claims; do not fact-correct from outside knowledge.
4. Apply only definite English fidelity corrections.
5. Inspect every canonical translation diff before advancing reviewed coverage.
6. Update `translation-review.md`, metadata, README, handover and next prompt truthfully.
7. English remains **not fully verified** until all source pp.241–277 pass Gate G.
8. Do not begin Speech 9 or Gate H until Speech 8 Gate G passes unless the user explicitly changes priority.
