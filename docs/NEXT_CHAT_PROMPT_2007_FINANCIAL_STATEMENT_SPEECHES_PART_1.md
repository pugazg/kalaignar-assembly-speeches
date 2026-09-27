# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 Gate C Batch 2 — scans 521–530

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
- Gate C Batch 1 — **PASS / COMPLETE — scans 511–520 / 10 of 35 first-pass**
- source-page markers — **511→520 / 10 / exactly once / ordered**
- unresolved first-pass readings — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**
- scan 520 ends mid-sentence at **`இந்த`**; continuation belongs to scan 521
- scan 521 wording was **not imported** during Batch 1

## Controlling source / split coverage

Full source:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- authority — **rendered scan pixels only**
- usable text layer — **none**

Working split 1:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`

- split total — **25 pages**
- bytes — **18,938,935**
- SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- Speech-19 coverage — local **11–25 = global scans 511–525**
- Batch-2 part021 coverage — local **21–25 = global scans 521–525**

Working split 2:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`

- split total — **21 pages**
- bytes — **15,522,557**
- SHA-256 — `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`
- Speech-19 coverage — local **1–20 = global scans 526–545**
- local page 21 = global scan 546 / closing portrait-back matter / excluded
- Batch-2 part022 coverage — local **1–5 = global scans 526–530**

Batch 2 therefore spans:
- **521–525** from part021 local 21–25;
- **526–530** from part022 local 1–5;
- working-split transition **525→526** must be explicitly audited and preserved.

## Gate-C cadence

Fixed rule: **10 source pages per iteration**, except final remainder.

- Batch 1 — **511–520 / 10 pages / PASS-COMPLETE**
- Batch 2 — **521–530 / 10 pages / exact next**
- Batch 3 — **531–540 / 10 pages**
- Batch 4 FINAL — **541–545 / 5 pages**

## Exact next activity

Perform **Speech 19 Gate C Batch 2 — scans 521–530 / exactly 10 pages**.

Requirements:

1. use only the controlling 2007 anthology pixels; do not import wording from OCR, web, Official Reports, alternate anthologies, released speeches or outside witnesses;
2. continue the open scan-520 sentence into scan 521 from the source pixels, without retranscribing or altering scans 511–520 unless a separate concrete source-backed defect is discovered and documented;
3. transcribe exactly **10 pages: 521–530**, no more;
4. after Batch 2, source-page markers must cover **511→530 / 20 pages / exactly once / ordered**;
5. explicitly audit and preserve the working-split transition **525→526 / part021→part022**;
6. preserve source heading context, speaker labels/interventions, spelling, punctuation, figures, repetitions and source-printed English;
7. preserve page-spanning continuations conservatively;
8. do not import any wording from scan 531;
9. record unresolved readings rather than guessing;
10. keep `verified_against_scan=false`; Gate C is first-pass transcription, not Gate E verification;
11. leave Gate C.5 **PROVISIONALLY N/A / not closed** unless an actual legacy-type anomaly is observed;
12. update Speech-19 README, metadata, transcript, source-notes, verification-log, anthology mapping/source README, handover, root README and this continuation prompt;
13. exact next after Batch 2: **Speech 19 Gate C Batch 3 — scans 531–540 / exactly 10 pages**;
14. do not begin Batch 3 in the same activity.
