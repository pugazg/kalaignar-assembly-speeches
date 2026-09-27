# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 Gate C Batch 1 — scans 511–520

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
- incoming boundary **510→511 — PASS**
- outgoing boundary **545→546 — PASS**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**
- source intake — **PASS / COMPLETE**
- Gate C setup — **PASS / COMPLETE**
- Gate C transcription — **NOT STARTED / 0 of 35**
- Tamil — **NOT TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**

## Controlling source / split coverage

Full source:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- authority — **rendered scan pixels only**
- usable text layer — **none**

Batch 1 source lies wholly inside:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`

- split total — **25 pages**
- bytes — **18,938,935**
- SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- Speech-19 coverage — local **11–25 = global scans 511–525**
- Batch 1 mapping — local **11–20 = global scans 511–520**
- boundary witness — local **10 = scan 510 / Speech 18 close / excluded**; local **11 = scan 511 / Speech 19 heading / included**

Later split:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`

- split total — **21 pages**
- Speech-19 coverage — local **1–20 = scans 526–545**
- local 21 = scan 546 / closing portrait-back matter / excluded
- exact split byte size / SHA-256 — **not recorded in live-main controls; do not invent**
- transition **525→526** must be audited during Batch 2

## Gate-C cadence

Fixed rule: **10 source pages per iteration**, except final remainder.

- Batch 1 — **511–520 / 10 pages**
- Batch 2 — **521–530 / 10 pages**
- Batch 3 — **531–540 / 10 pages**
- Batch 4 FINAL — **541–545 / 5 pages**

## Exact next activity

Perform **Speech 19 Gate C Batch 1 — scans 511–520 / exactly 10 pages**.

Requirements:

1. use only the controlling 2007 anthology pixels; no OCR/web/Official Reports/alternate anthologies/released speeches/outside witnesses may supply wording;
2. transcribe exactly **10 pages: 511–520**, no more;
3. add source-page markers **511→520**, each exactly once and in order;
4. preserve source heading/date, speaker labels/interventions, spelling, punctuation, figures, repetitions and source-printed English;
5. preserve page-spanning continuations conservatively;
6. do not import any wording from scan 521;
7. record unresolved readings rather than guessing;
8. keep `verified_against_scan=false` after Gate C; this is first-pass transcription, not Gate E verification;
9. leave Gate C.5 only **PROVISIONALLY N/A** unless an actual legacy-type anomaly is observed;
10. update Speech-19 README, metadata, transcript, source-notes, verification-log, anthology source controls, handover and this continuation prompt;
11. exact next after Batch 1: **Speech 19 Gate C Batch 2 — scans 521–530 / exactly 10 pages**;
12. do not begin Batch 2 in the same activity.
