# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter its verified Tamil or English while processing the next unit.

## Active unit — Speech 8

Locked source mapping:

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- relationship: scan page = printed page + 1
- previous boundary: scan p.240 closes Speech 7
- next boundary: scan p.278 begins Speech 9 (`8.05.2000`)

The opening and closing boundaries were re-confirmed directly from the controlling scan: p.241 begins `உரை : 8 / நாள் : 29.04.1999`; p.277 closes Speech 8 with the printed ornament; p.278 begins Speech 9.

## Gate C progress

### Batch 1 — complete and canonical

- scan pages: **241–255**
- printed pages: **240–254**
- page count: **15**

### Batch 2 — complete and canonical

- scan pages: **256–270**
- printed pages: **255–269**
- page count: **15**
- canonical merge commit: `1da567dc66d89847bfa10704254d8bf9e3c8b46a`

### Batch 3 — transcribed and staged

- scan pages: **271–277**
- printed pages: **270–276**
- page count: **7**
- staging file: `speeches/1999/1999-04-29-industries-debate/gate-c-batch3-pp271-277.md`
- staging commit: `c1caa09e674f62525f25a1a41ccf34be442ed07d`
- unresolved/`[REVIEW]` readings: **0**

The final batch was transcribed directly from rendered scan images. It preserves the `தமிழ்நெட் 1999` / Unicode / `Tamil Virtual University` passages, school-computer-training court material, granite Rule 39 and High Court quotations, the source form `8-ஏ`, all speaker changes, and the p.277 salt-pan closing exchange.

The staged text stops at p.277 after:

`உப்பளத் தொழில் மாத்திரம் அல்ல, தமிழகத்தில் அப்பளத் தொழிலும் கெடாமல் இந்த அரசு பார்த்துக் கொள்ளும். (மேசையைத் தட்டும் ஒலி).`

Rendered p.278 begins Speech 9 (`உரை : 9`, `நாள் : 8.05.2000`) and was not entered.

## Current canonical state

- canonical path: `speeches/1999/1999-04-29-industries-debate/`
- canonical `transcript.md`: **scan pp.241–270 / printed pp.240–269 — 30/37 pages**
- final pp.271–277: **transcribed and staged, pending merge**
- Tamil status: **in-progress, not verified**
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked**

Current Batch-3 staging/status checkpoints:

- staging file: `c1caa09e674f62525f25a1a41ccf34be442ed07d`
- README: `2f49271e9e04452eb514381d3e0509efb343bed3`
- metadata: `1c1fd641bfb1cad6ceb21ce193b1f2c5e2d30e37`
- source notes: `7432b72b08ad8ff7dd04ff11ada6c3f1e996e648`
- verification log: `62c2361a5219f73d7082288fcb17a23cb7242e74`

## Exact next activity — merge final Gate C batch

1. Fetch the current canonical `transcript.md` and current staging file; do not overwrite concurrent changes.
2. Merge staged **scan pp.271–277 / printed pp.270–276** after canonical p.270.
3. Confirm exact source-page markers **241–277**, in order, with 37 pages, no gaps/duplicates/reordering and no p.278/Speech-9 spillover.
4. Confirm the p.277 closing intervention and Kalaignar reply remain intact.
5. Update the archival note and metadata to Gate C **complete / 37/37**, with Tamil status **transcribed, not verified**.
6. Remove `gate-c-batch3-pp271-277.md` only after the canonical merge is verified.
7. Reconcile README/source notes/verification log/handover/prompt.
8. The next gate after merge is **Gate D full-speech completeness/page-marker audit**. Do not begin English. Gate E must still follow Gate D before English is unblocked.
