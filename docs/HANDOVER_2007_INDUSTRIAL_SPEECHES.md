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

Batch 6 applied the source-supported p.267 correction:

`அப்போதை` → `அப்போதைய`

The canonical commit diff was inspected and contains only the archival status-note update plus that one Tamil correction; no unrelated Tamil change was introduced. Scan p.266 and pp.268–270 required no additional definite correction. The p.265→266 and p.270→271 continuations are intact. The temporary Batch-6 staging file was removed after successful canonical merge.

### Current Gate-E state

- verified scan range: **241–270**
- verified printed range: **240–269**
- verified pages: **30/37**
- cumulative applied corrections: **27**
- unresolved readings in verified range: **0**
- next verification scan page: **271**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

Batch-6 closure checkpoints:

- canonical transcript: `2d43d163d6c7ac9e470ae08299d0d20e91ebe089`
- metadata: `1b20d2313b8cf444bbfc1a39860b36665eee99ae`
- README: `27ed2bfaf991055b1458e08908076bf3dd058c52`
- source notes: `de119d2181e0c3dcd11b49fee02cb4d10493bf3a`
- verification log: `63f01b67c388977254bb81272cfb3012396d0341`
- staging-file deletion: `d65b2baa601805bb643854d3508f97cb35d518d5`

## Exact next activity — Speech 8 Gate E Batch 7

1. Fetch the current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
2. Visually verify **scan pp.271–275 / printed pp.270–274** directly against the controlling rendered scan.
3. Check words/characters, names/initials, numerals, dates, printed English, punctuation, speaker/context markers and cross-page continuations.
4. Pay particular attention to `தமிழ்நெட் 1999`, Unicode Consortium, `Tamil Virtual University`, the 1,200-school / 48,000-student passage, Rule 39 / granite material, and the printed High Court English quotations.
5. Preserve historical/source forms; do not modernise or reconcile against outside knowledge.
6. Apply only definite scan-supported corrections to canonical Tamil and record every correction in `verification-log.md`.
7. Record unresolved readings explicitly instead of guessing.
8. Update metadata/README/source notes/verification log/handover/prompt after the bounded batch.
9. After Batch 7, continue Gate E from **scan p.276**.
10. Keep Tamil **not fully verified** and English blocked until all **37/37** pages pass Gate E.
