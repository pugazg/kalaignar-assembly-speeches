# Next-chat prompt — Speech 8 Gate G Batch 8 / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Tamil Gates C–E are complete and verified, Gate F English translation is complete for all 37 pages, and Gate G fidelity review Batches 1–7 are complete. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current `speeches/1999/1999-04-29-industries-debate/metadata.json`, `README.md`, `translation-review.md`, canonical `translation.md`, and final verified `transcript.md`.
5. Use the **final verified Tamil** in canonical `transcript.md` as the sole textual authority for Gate G. Do not use OCR or outside historical information to override it.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan/source pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E: **passed — 37/37 pages**
- Gate-E cumulative corrections: **29**
- unresolved Tamil readings: **0**
- Tamil status: **verified against scan**
- Gate F: **complete — source pp.241–277 / printed pp.240–276, 37/37 pages**
- final Gate-F merge checkpoint: `ed79a499ecb56f8fb750f5ea9d946d1b2a71fde3`
- Gate G: **in progress**
- Gate G Batches 1–7 reviewed: **source pp.241–275 / printed pp.240–274, 35/37 pages**
- Gate-G cumulative definite corrections: **1**
- Gate-G Batch-2 corrections: **0**
- Gate-G Batch-3 corrections: **0**
- Gate-G Batch-4 corrections: **0**
- Gate-G Batch-5 corrections: **0**
- Gate-G Batch-6 corrections: **0**
- Gate-G Batch-7 corrections: **0**
- Gate-G unresolved fidelity issues: **0**
- next Gate-G source page: **276**
- English overall status: **complete, not yet verified**
- current canonical English blob: `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`

## Gate-G corrections so far

Batch 1, source p.245: Gate F rendered `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்` as `You are taking the nameplate and going away with it.` Gate G corrected this definite over-literalisation to **`You are taking the credit for it.`** Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`.

Batches 2–7, source pp.246–275: **no further definite canonical English correction required**. Batch 7 reconfirmed `தமிழ்நெட் 1999`, Unicode Consortium associate membership, July Tamil formats, `Tamil Virtual University`, the 1,200-school / approximately 48,000-student computer-training scheme and court passage; then Rule 39, Government Order No.97 dated 8-3-1993, 125 leases / 9 districts / 196.80 hectares / Rs.95 crore and the printed High Court English quotations through p.275, including the p.274→275 quotation continuation.

## Exact next activity — Gate G Batch 8

Review **source/scan pp.276–277 / printed pp.275–276** against the final verified Tamil.

1. Fetch the exact Tamil and English final-two-page ranges before review.
2. Compare page-by-page for omissions, additions, mistranslations, meaning shifts and cross-page continuations.
3. Preserve unusual source claims, spellings and printed English; do not fact-correct or modernise from outside knowledge.
4. Check the printed High Court quotation continuing onto source p.276 exactly.
5. Check the `8-ஏ` / 8-A granite-rule amendment, `டாமின்` / TAMIN land and public-auction passage, Kalaignar's closing and desk-thumping marker.
6. Check the Speaker → Thiru So. Balakrishnan intervention, the salt-pan-industry material, 5,000 acres / Rs.29 / Rs.429 / Rs.1½ crore figures and the final `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay.
7. Reconfirm that p.277 closes Speech 8 and p.278 begins Speech 9 (`8.05.2000`); no Speech-9 spillover.
8. Apply only definite English fidelity corrections. If a correction is made, inspect the canonical `translation.md` commit/diff before closing Gate G. If none is needed, record the unchanged canonical blob checkpoint.
9. If both pages pass, close Gate G at **37/37 pages**, mark English translation **verified**, set `verified_against_tamil: true`, `gate_g_status: complete`, next Gate-G source page null, and record final correction/unresolved counts.
10. Update `translation-review.md`, metadata, README, handover and this prompt truthfully.
11. Only after Gate G passes should the next activity become **Gate H — index/release for Speech 8**.
12. Do not begin Speech 9 until Speech 8 Gate H is complete unless the user explicitly changes priority.

Batch 8 begins on source p.276 with `".... the money due to the Government has been siphoned off by them..."` and ends on source p.277 with the salt-pan / `appalam` exchange and the locked Speech-8 boundary.
