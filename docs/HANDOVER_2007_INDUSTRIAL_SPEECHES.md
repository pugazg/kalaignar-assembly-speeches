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

### Batches 1–5 canonically complete

- Batch 1: scan pp.241–245 — 5 pages — 5 corrections — checkpoint `201b5eff42382bcb6192475be75e01a6865ed921`
- Batch 2: scan pp.246–250 — 5 pages — 6 corrections — checkpoint `bcddfa24237941596f5acaab0531974b783e7b77`
- Batch 3: scan pp.251–255 — 5 pages — 12 corrections — checkpoint `856297ff79dcb3f2539ac569941e09a27aaeccde`
- Batch 4: scan pp.256–260 — 5 pages — 2 corrections — checkpoint `03f32ed5460c118007693539e32db100af07ffe6`
- Batch 5: scan pp.261–265 — 5 pages — 1 correction — checkpoint `a1a90353a222507c4a14a926ce0d856b25741c65`

Canonical state after Batch 5:

- verified scan range: **241–265**
- verified printed range: **240–264**
- verified pages: **25/37**
- cumulative applied corrections: **26**
- unresolved readings: **0**

### Batch 6 visual review complete — canonical merge pending

Scan pp.**266–270** / printed pp.**265–269** were visually re-read directly against the controlling rendered scan, all 5/5 pages.

One definite source-supported correction was found:

1. p.267 `அப்போதை` → `அப்போதைய`.

The source clearly prints `அப்போதைய` in the Tamil explanation following the CDR quotation. Scan p.266 and pp.268–270 required no additional definite correction.

Checks covered the embedded `Economic Times` and `Times of India` English passages, CDR percentages, `International Real Estates`, `Jones Long Wootten`, the Vikatan editorial, and the information-technology section including `Software Professionals`, `I.T. Task Force`, `I.T.Policy`, `Hardware`, `Software` and `I.T. Super Highway`.

Boundary checks passed:

- p.265→266: `Economic Times` lead-in dated `28-4-1999` → `Tamil Nadu followed closely by Gujarat...`;
- p.270→271: `வேர்ல்ட்டெல்` / internetisation passage → `தமிழ்நெட் 1999`.

Batch-6 unresolved readings: **0**.

For safety, the correction is staged in:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch6-pp266-270.md`

Staging commit: `5dbe646ada65968165c4465a98a8f77325036336`.

Do **not** count Batch 6 as canonically verified until the p.267 correction has been merged into the large `transcript.md` and its diff has been checked. Therefore current canonical verified state remains **25/37 pages / 26 applied corrections**.

Current Tamil status: **reviewed, not fully verified**. English remains **blocked**.

## Exact next activity — close Gate E Batch 6

1. Fetch the current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
2. Merge exactly one source correction on scan p.267: `அப்போதை` → `அப்போதைய`.
3. Update only the archival note from verified through scan p.265 / printed p.264 to verified through **scan p.270 / printed p.269**.
4. Inspect the resulting commit diff and confirm there are no unrelated Tamil changes.
5. Then update metadata/README/source notes/verification log to **30/37 pages verified**, **27 cumulative corrections**, next scan page **271**, unresolved **0**.
6. Delete `gate-e-batch6-pp266-270.md` only after the successful canonical merge and status closure.
7. Only after Batch 6 is canonically closed, proceed to **Gate E Batch 7 — scan pp.271–275 / printed pp.270–274**.
8. Keep English blocked until all **37/37** Tamil pages pass Gate E.
