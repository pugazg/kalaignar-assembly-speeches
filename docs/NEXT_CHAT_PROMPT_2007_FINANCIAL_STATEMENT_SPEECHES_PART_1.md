# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 Gate C Batch 3 — scans 531–540

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–18 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 19 source state

Working entry:

`speeches/1982/1982-03-06-financial-statement-debate/`

- source label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- hard boundaries **510→511 / 545→546 — PASS**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**
- source intake + Gate C setup — **PASS / COMPLETE**
- Gate C Batch 1 — **PASS / COMPLETE — scans 511–520 / 10 pages**
- Gate C Batch 2 — **PASS / COMPLETE — scans 521–530 / 10 pages**
- cumulative Gate-C coverage — **511–530 / 20 of 35 pages**
- source-page markers — **511→530 / 20 / exactly once / ordered**
- unresolved first-pass readings — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**
- outside wording imported — **0**
- working-split transition **525→526 / part021→part022 — PASS / preserved**
- source-printed English on scans **523–525 — preserved**
- scan 531 wording — **not imported**

## Controlling source / split coverage

Full source:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- authority — **rendered scan pixels only**
- usable text layer — **none**

Part021:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`

- split total — **25 pages**
- bytes — **18,938,935**
- SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- Speech-19 coverage — local **11–25 = scans 511–525**
- fully consumed for Speech 19 through Gate-C Batch 2

Part022:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`

- split total — **21 pages**
- bytes — **15,522,557**
- SHA-256 — `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`
- Speech-19 coverage — local **1–20 = global scans 526–545**
- local page 21 = scan 546 / closing portrait-back matter / excluded
- Batch-3 coverage — local **6–15 = global scans 531–540**

## Gate-C cadence

Fixed rule: **10 source pages per iteration**, except final remainder.

- Batch 1 — **511–520 / 10 pages / PASS-COMPLETE**
- Batch 2 — **521–530 / 10 pages / PASS-COMPLETE**
- Batch 3 — **531–540 / 10 pages / exact next**
- Batch 4 FINAL — **541–545 / 5 pages**

## Exact next activity

Perform **Speech 19 Gate C Batch 3 — scans 531–540 / exactly 10 pages**.

Requirements:

1. use only the controlling 2007 anthology pixels; do not import wording from OCR, web, Official Reports, alternate anthologies, released speeches or outside witnesses;
2. do not alter scans **511–530** unless a separate concrete source-backed defect is discovered and documented;
3. transcribe exactly **10 pages: 531–540**, no more;
4. after Batch 3, source-page markers must cover **511→540 / 30 pages / exactly once / ordered**;
5. preserve source spelling, punctuation, figures, repetitions, speaker labels/interventions and source-printed English;
6. preserve page-spanning continuations conservatively;
7. do not import any wording from scan **541**;
8. record unresolved readings rather than guessing;
9. keep `verified_against_scan=false`; Gate C is first-pass transcription, not Gate E verification;
10. leave Gate C.5 **PROVISIONALLY N/A / not closed** unless an actual legacy-type anomaly is observed;
11. update Speech-19 README, metadata, transcript, source-notes, verification-log, anthology mapping/source README, handover, root README and this continuation prompt;
12. exact next after Batch 3: **Speech 19 Gate C Batch 4 FINAL — scans 541–545 / exactly 5 pages**;
13. do not begin the FINAL batch in the same activity.
