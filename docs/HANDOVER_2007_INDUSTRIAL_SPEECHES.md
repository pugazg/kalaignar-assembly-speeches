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
- Speech-8 boundary confirmed at source p.277; source p.278 begins Speech 9; **no spillover**

## English Gate G

- Gate G: **complete — 37/37 pages**
- reviewed source/scan pages: **241–277**
- reviewed printed pages: **240–276**
- definite Gate-G fidelity corrections applied cumulatively: **1**
- Batch-1 corrections: **1**
- Batches 2–8 corrections: **0**
- unresolved fidelity issues: **0**
- next Gate-G source page: **none**
- English overall status: **verified against final Tamil**
- Gate-G review record: `speeches/1999/1999-04-29-industries-debate/translation-review.md`
- final reviewed canonical English blob: `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`

Batch 1 applied the only definite English fidelity correction on source p.245: Gate F's over-literal `You are taking the nameplate and going away with it.` was corrected to **`You are taking the credit for it.`** for `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்`. Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`.

Batches 2–7 required no further canonical English correction.

Final Batch 8 reviewed source pp.276–277 and also required no canonical English edit. It reconfirmed the continuing printed High Court quotation, `8-ஏ` / 8-A, `டாமின்` / TAMIN public-auction passage, Kalaignar's close, the Speaker → Thiru So. Balakrishnan intervention, 5,000 acres / Rs.29 / Rs.429 / Rs.1½ crore, and the final `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay. Source p.277 closes Speech 8; source p.278 begins Speech 9. Gate G therefore passed all **37/37** pages with **1 cumulative correction and 0 unresolved issues**.

## Exact next activity — Gate H

Release/index **Speech 8**.

Requirements:

1. Inspect the current Gate-H implementation used for released Speech 7 before writing.
2. Read current `data/speeches.json` and the repository root `README.md` / speech index surfaces.
3. Add or update only the Speech-8 release/index entry; do not alter Speech 7 content.
4. Ensure the released entry agrees exactly with Speech-8 `metadata.json`, `source-notes.md`, locked mapping and verified statuses.
5. Ensure Tamil and English artifacts are represented as verified, with source pp.241–277 / printed pp.240–276 and no Speech-9 spillover.
6. Inspect all Gate-H commit diffs before marking Speech 8 released.
7. Update Speech-8 README/metadata/release notes if the established Gate-H pattern requires a released status marker.
8. Update this handover and `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md` so the exact next activity becomes Speech 9 only after Gate H is complete.
9. Do not begin Speech 9 until Speech 8 Gate H has been completed and audited unless the user explicitly changes priority.
