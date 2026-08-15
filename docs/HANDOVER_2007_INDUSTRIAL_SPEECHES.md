# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter it while processing Speech 8.

## Active unit — Speech 8

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- relationship: scan page = printed page + 1
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Gate C — complete

Canonical coverage: **241–277 / 240–276 — 37/37 pages**. Unresolved `REVIEW` readings: **0**. Gate-C checkpoint: `d0fd3ea71f29838299eb5d7008e4149b7399498c`.

## Gate D — passed

All **37** source-page markers are present exactly once in strict sequence 241–277, with no gaps, duplicates, reordering or Speech-9 spillover.

## Gate E — in progress

Batches 1–7 are now canonically complete:

- Batch 1: pp.241–245 — 5 corrections — `201b5eff42382bcb6192475be75e01a6865ed921`
- Batch 2: pp.246–250 — 6 corrections — `bcddfa24237941596f5acaab0531974b783e7b77`
- Batch 3: pp.251–255 — 12 corrections — `856297ff79dcb3f2539ac569941e09a27aaeccde`
- Batch 4: pp.256–260 — 2 corrections — `03f32ed5460c118007693539e32db100af07ffe6`
- Batch 5: pp.261–265 — 1 correction — `a1a90353a222507c4a14a926ce0d856b25741c65`
- Batch 6: pp.266–270 — 1 correction — `2d43d163d6c7ac9e470ae08299d0d20e91ebe089`
- Batch 7: pp.271–275 — 1 correction — `d3106a9d88ed7d5c801398b14e1705eff446a18c`

Batch 7 applied the source-supported p.274 correction:

`ஏராளமான தொகைகளை லஞ்சம் செய்து கொண்டு` → `ஏராளமான தொகைகளை வசூல் செய்து கொண்டு`

The canonical Batch-7 diff was inspected and contains only the archival status-note update plus this one Tamil correction; no unrelated Tamil change was introduced. Scan pp.271–273 and p.275 required no additional definite correction. The p.270→271 and p.275→276 transitions are intact. The Batch-7 staging file was removed after successful canonical merge.

### Current Gate-E state

- verified scan range: **241–275**
- verified printed range: **240–274**
- verified pages: **35/37**
- cumulative applied corrections: **28**
- unresolved readings: **0**
- next verification scan page: **276**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

Batch-7 closure checkpoints:

- canonical transcript: `d3106a9d88ed7d5c801398b14e1705eff446a18c`
- metadata: `423c1d13a46d3427e982ccfac68c523b7932c573`
- README: `b97eb039ba455f0bfeb438969d214307ad52f482`
- source notes: `a57ec3dbd93405dc0ebab5adddc75ed44e7118c5`
- verification log: `f75d2a076bdf0978190d6411da4b5b853fcc0b71`
- staging-file deletion: `82b1dc440b081ab9eba15e9326496ce49b3b2e59`

## Exact next activity — final Gate E Batch 8

1. Fetch current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
2. Visually verify **scan pp.276–277 / printed pp.275–276** directly against the controlling rendered scan.
3. On p.276, verify the opening printed High Court English quotation exactly, the Tamil continuation, the source form `8-ஏ`, the `டாமின்` passage, the speech-closing `வணக்கம்`, applause marker, and the Speaker transition.
4. On p.277, verify `திரு. சோ. பாலகிருஷ்ணன்`'s full intervention, figures `5,000`, `29`, `429`, `ஒன்றரை கோடி`, and Kalaignar's reply including `400`, `29`, and the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay.
5. Confirm the exact Speech-8 ending on p.277 and **no p.278 / Speech-9 spillover**.
6. Apply and log only definite scan-supported corrections. Record unresolved readings rather than guessing.
7. If the final two pages pass, close Gate E at **37/37 pages**, set Tamil to **verified**, and unblock Gate F only after status reconciliation.
8. Do not begin English in the same activity unless the repository workflow explicitly says Gate F starts immediately after Gate-E closure.
