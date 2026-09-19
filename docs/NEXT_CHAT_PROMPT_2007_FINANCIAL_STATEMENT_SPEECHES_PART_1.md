# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 6 Gate H

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–5 are RELEASED / CLOSED through Gate H**.

Do not reopen Speeches 1–5 merely for stylistic polishing.

## Speech 6 durable state

Working entry:

`speeches/1963/1963-03-07-financial-statement-debate/`

Source boundary:

- source label — `உரை : 6`
- printed date — `7.3.1963`
- scans — **60–75**
- printed pages — **59–74**
- hard boundary **59→60** — preserved
- hard boundary **75→76** — preserved
- scan 76 begins Speech 7 and remains excluded

Tamil:

- Gate C — **COMPLETE / 16 of 16 pages**
- Gate D — **PASS / COMPLETE / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / 20 source-fidelity corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**

English:

- Gate F — **COMPLETE / 16 of 16 pages**
- Gate G — **PASS / COMPLETE / 16 of 16 pages**
- Gate-G refinements — **15**
- blocking fidelity issues — **0**
- verified-Tamil changes — **0**
- source-printed English on scan 73 — **preserved verbatim**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**

Release:

- Gate H — **NOT STARTED / exact next**
- release — **WORKING / NOT RELEASED**
- Speech 7 — **NOT STARTED**

Working English remains in `translation.md`; the Gate-F/G audit is in `translation-review.md`.

No OCR, scan pixels, web research, Official Reports or alternate anthologies supplied English wording.

## Exact next activity

Perform **Speech 6 Gate H canonical merge / index / release closure**.

Requirements:

1. preserve the verified Tamil source-page markers **60→75** exactly once and in order;
2. merge the final Gate-G-verified English after the verified Tamil in canonical `transcript.md`, preserving English source-page sections **60→75**;
3. preserve the source-printed English on scan 73 exactly;
4. retire `translation.md` to a pointer only after the verified English is safely canonical in `transcript.md`;
5. keep `translation-review.md` as the durable Gates F–G audit record and add Gate-H closure;
6. update `metadata.json`, speech README, source notes and verification log to RELEASED / CLOSED;
7. synchronize root dated speech index and `data/speeches.json` using the established neutral archival slug/date pattern;
8. synchronize anthology README, mapping and handover;
9. run final marker/range/index checks and record Gate-H wording changes separately for Tamil and English;
10. do not make stylistic changes to already verified Tamil or English during Gate H;
11. do not begin Speech 7 in the same iteration.

Expected next activity after successful Gate H: **Speech 7 / 7.3.1964 — Gate C Tamil first-pass transcription, scans 76–89 / 14 pages**.
