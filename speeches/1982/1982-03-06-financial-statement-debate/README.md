# உரை : 19 — 06.03.1982

**காப்பக working ID:** `1982-03-06-financial-statement-debate`

## Source unit

- anthology — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`
- source label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- global scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- incoming boundary **510→511** — **PASS / locked anthology map**
- outgoing boundary **545→546** — **PASS / locked anthology map**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**

## Existing-work overlap check

- repository `speeches/` currently has **no 1982 directory / no existing Speech-19 working entry**
- `data/speeches.json` currently has **no 1982-03-06 entry**
- therefore this is a **new working entry**, not an overwrite of released material

## Controlling source / working splits

Full controlling source:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`
- physical pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- textual authority — **rendered scan pixels**
- usable text layer — **none**

Working split 1:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`
- local pages — **11–25**
- global scans — **511–525**
- printed pages — **510–524**
- Speech-19 coverage — **15 pages**
- split page count — **25**
- split bytes — **18,938,935**
- split SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- boundary witness — local **10 = scan 510 / Speech 18 close / excluded**; local **11 = scan 511 / Speech 19 heading / included**

Working split 2:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`
- local pages — **1–20**
- global scans — **526–545**
- printed pages — **525–544**
- Speech-19 coverage — **20 pages**
- split page count — **21**
- split bytes — **15,522,557**
- split SHA-256 — `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`
- boundary witness — local **20 = scan 545 / Speech 19 close / included**; local **21 = scan 546 / closing portrait-back matter / excluded**

The full controlling source hash remains authoritative. During Gate-C Batch 1, the user-supplied part022 file was available and its convenience-file integrity metadata was resolved directly: **15,522,557 bytes / SHA-256 `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`**.

## Source authority

Rendered pixels of the controlling 2007 anthology are the sole textual authority.

No OCR, web copy, Official Report, alternate anthology, released speech or other outside witness may supply, repair or normalize wording.

## Gate state

- source intake — **PASS / COMPLETE**
- Gate C setup — **PASS / COMPLETE**
- Gate C transcription — **IN PROGRESS / Batch 1 PASS-COMPLETE / scans 511–520 / 10 of 35 pages**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**
- release — **NOT RELEASED**
- Speech 18 — **RELEASED / CLOSED / locked**
- outside wording imported — **0**

## Gate-C batching

Fixed cadence: **10 source pages per iteration**; only the final remainder may be fewer.

1. Batch 1 — **511–520 / printed pp.510–519 / exactly 10 pages / PASS-COMPLETE**
2. Batch 2 — **521–530 / printed pp.520–529 / exactly 10 pages**
3. Batch 3 — **531–540 / printed pp.530–539 / exactly 10 pages**
4. Batch 4 FINAL — **541–545 / printed pp.540–544 / exactly 5 pages**

Batch 1 lies wholly inside part021. Batch 2 crosses the part021→part022 working-split boundary at **525→526**; preserve that transition explicitly when Batch 2 is processed.

## Gate C Batch 1 result

**PASS / COMPLETE — scans 511–520 / printed pp.510–519 / exactly 10 pages; cumulative 10 of 35 first-pass transcribed.**

- source-page markers — **511→520 / 10 / exactly once / ordered**
- source heading **உரை : 19 / 06.03.1982** — **preserved**
- speaker label — **preserved**
- unresolved first-pass readings — **0**
- outside wording imported — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- scan **520** — **ends mid-sentence at `இந்த`; continuation belongs to scan 521 and was not imported**
- scans **521–545** modified — **0**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- part021 Batch-1 source — **local 11–20 / global scans 511–520**
- part022 integrity metadata — **resolved from the user-supplied split: 15,522,557 bytes / SHA-256 `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`**

## Exact next activity

Perform **Speech 19 Gate C Batch 2 — scans 521–530 / exactly 10 pages**.

Batch 2 crosses the working-split boundary **525→526**. Preserve and audit that transition explicitly. Do not process scans 531 onward in the same Gate-C iteration.
