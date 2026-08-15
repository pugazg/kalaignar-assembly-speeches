# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter its verified Tamil or English while processing Speech 8.

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

## Gate C — complete

- canonical coverage: **241–277 / 240–276 — 37/37 pages**
- unresolved `REVIEW` readings: **0**
- Gate-C canonical completion checkpoint: `d0fd3ea71f29838299eb5d7008e4149b7399498c`

## Gate D — passed

The full-speech structural completeness/page-marker audit passed. All **37** source-page markers are present exactly once in strict sequence **241–277**, with no gaps, duplicates, reordering or Speech-9 spillover.

## Gate E — in progress

### Batches 1–6 canonically complete

- Batch 1: scan pp.241–245 — 5 pages — 5 corrections — checkpoint `201b5eff42382bcb6192475be75e01a6865ed921`
- Batch 2: scan pp.246–250 — 5 pages — 6 corrections — checkpoint `bcddfa24237941596f5acaab0531974b783e7b77`
- Batch 3: scan pp.251–255 — 5 pages — 12 corrections — checkpoint `856297ff79dcb3f2539ac569941e09a27aaeccde`
- Batch 4: scan pp.256–260 — 5 pages — 2 corrections — checkpoint `03f32ed5460c118007693539e32db100af07ffe6`
- Batch 5: scan pp.261–265 — 5 pages — 1 correction — checkpoint `a1a90353a222507c4a14a926ce0d856b25741c65`
- Batch 6: scan pp.266–270 — 5 pages — 1 correction — checkpoint `2d43d163d6c7ac9e470ae08299d0d20e91ebe089`

Canonical state after Batch 6:

- verified scan range: **241–270**
- verified printed range: **240–269**
- verified pages: **30/37**
- cumulative applied corrections: **27**
- unresolved readings: **0**

### Batch 7 visual review complete — canonical merge pending

Scan pp.**271–275** / printed pp.**270–274** were visually re-read directly against the controlling rendered scan, all 5/5 pages.

One definite source-supported correction was found:

1. p.274 `ஏராளமான தொகைகளை லஞ்சம் செய்து கொண்டு` → `ஏராளமான தொகைகளை வசூல் செய்து கொண்டு`.

The source clearly prints `வசூல் செய்து கொண்டு` in the Tamil court-summary sentence immediately before the first printed High Court English quotation. Scan pp.271–273 and p.275 required no other definite correction.

Checks covered `தமிழ்நெட் 1999`, Unicode Consortium, `Tamil Virtual University`, the 1,200-school / 48,000-student passage, Rule 39 / Government Order No. 97 / `8-3-1993`, granite lease/area/loss figures, and printed High Court English quotations through p.275.

Boundary checks passed:

- p.270→271: internetisation passage → `தமிழ்நெட் 1999`;
- p.275→276: `மேலும், நீதிபதி, தன்னுடைய தீர்ப்பில் தொடர்ந்து சொல்கிறார் :` → printed English `.... the money due to the Government has been siphoned off...`.

Batch-7 unresolved readings: **0**.

For safety, the correction is staged in:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch7-pp271-275.md`

Staging commit: `f84f49652ac589c0310be4406e541f970e21a992`.

Do **not** count Batch 7 as canonically verified until the p.274 correction has been merged into the large `transcript.md` and its diff has been checked. Therefore current canonical verified state remains **30/37 pages / 27 applied corrections**.

Current Tamil status: **reviewed, not fully verified**. English remains **blocked**.

## Exact next activity — close Gate E Batch 7

1. Fetch current canonical `transcript.md` immediately before editing.
2. Merge exactly one source correction on scan p.274: `ஏராளமான தொகைகளை லஞ்சம் செய்து கொண்டு` → `ஏராளமான தொகைகளை வசூல் செய்து கொண்டு`.
3. Update only the archival note from verified through scan p.270 / printed p.269 to verified through **scan p.275 / printed p.274**.
4. Inspect the resulting commit diff and confirm there are no unrelated Tamil changes.
5. Then update metadata/README/source notes/verification log to **35/37 pages verified**, **28 cumulative corrections**, next scan page **276**, unresolved **0**.
6. Delete `gate-e-batch7-pp271-275.md` only after successful canonical merge and status closure.
7. Then proceed to the final **Gate E Batch 8 — scan pp.276–277 / printed pp.275–276**.
8. Keep English blocked until all **37/37** Tamil pages pass Gate E.
