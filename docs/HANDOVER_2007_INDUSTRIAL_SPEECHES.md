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
- Batches 1–7 reviewed source/scan pp. **241–275** / printed pp. **240–274**
- reviewed pages: **35/37**
- definite Gate-G fidelity corrections applied cumulatively: **1**
- Batch-2 corrections: **0**
- Batch-3 corrections: **0**
- Batch-4 corrections: **0**
- Batch-5 corrections: **0**
- Batch-6 corrections: **0**
- Batch-7 corrections: **0**
- unresolved fidelity issues: **0**
- next Gate-G source page: **276**
- English overall status: **complete, not yet verified**
- Gate-G review record: `speeches/1999/1999-04-29-industries-debate/translation-review.md`
- current canonical English blob: `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`

Batch 1 applied one definite English fidelity correction on source p.245. Gate F had translated `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்` as `You are taking the nameplate and going away with it.` Gate G corrected this to **`You are taking the credit for it.`** Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`; the inspected diff contains only that English change.

Batches 2–6 reviewed source pp.246–270 and required **no further canonical English correction**.

Batch 7 reviewed source pp.271–275 and also required **no canonical English correction**. It reconfirmed `தமிழ்நெட் 1999` / Unicode Consortium associate membership and July Tamil-format material; `Tamil Virtual University`; the 1,200-school / 40-student / approximately 48,000-student computer-training scheme and court-judgment passage; Rule 39 / Government Order No.97, Industries Department, dated 8-3-1993; 125 leases / 9 districts / 196.80 hectares / Rs.95 crore; Thiru Chinnasamy; and all printed High Court English quotations through source p.275. The p.274→275 quotation beginning `The persons to whom the granite leases have been granted...` was verified as a continuous quotation across the page marker. The canonical English blob remains `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`.

## Exact next activity — Gate G Batch 8

Review **source/scan pp.276–277 / printed pp.275–276** against the final verified Tamil.

Requirements:

1. Fetch the final verified Tamil and current canonical English for the exact final two-page range.
2. Compare page-by-page for omissions, additions, meaning shifts, cross-page continuations, speaker labels/interventions, names, dates, figures, technical terms, printed English and humour/wordplay.
3. Preserve the printed High Court English quotation opening p.276 exactly as represented in the verified Tamil.
4. Check `8-ஏ` / 8-A, `டாமின்` / TAMIN, the public-auction passage, Kalaignar's closing, the Speaker → Thiru So. Balakrishnan intervention, 5,000 acres / Rs.29 / Rs.429 / Rs.1½ crore figures and the final `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay through source p.277.
5. Confirm again that source p.277 closes Speech 8 and source p.278 begins Speech 9; no Speech-9 material may enter Gate G.
6. Apply only definite English fidelity corrections. Inspect any canonical translation diff before closing Gate G.
7. If both pages pass, mark Gate G **complete — 37/37**, set English translation status to **verified**, `verified_against_tamil: true`, next Gate-G page null, and record the final cumulative correction count and zero unresolved issues if still true.
8. Update `translation-review.md`, metadata, README, handover and next prompt truthfully.
9. Only after Gate G passes may the next activity become **Gate H — index/release for Speech 8**.
10. Do not begin Speech 9 until Speech 8 Gate H is complete unless the user explicitly changes priority.

Batch 8 starts on source p.276 with the continuation of the High Court quotation and ends on source p.277 with the salt-pan / `appalam` exchange and Speech-8 close.
