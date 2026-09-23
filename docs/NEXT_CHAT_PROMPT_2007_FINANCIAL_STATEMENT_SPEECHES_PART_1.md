# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 15 Gate D completeness audit

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–14 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Fixed repository iteration rule

Per explicit user instruction:

- **Gate C — 10 source pages per iteration**
- **Gate E — 10 source pages per iteration**
- only the final remainder may contain fewer than 10 pages;
- do not exceed 10 source pages in Gate C or Gate E unless the user explicitly overrides the rule.

## Speech 15 current state

Working entry:

`speeches/1977/1977-08-03-financial-statement-debate/`

- source label/date — `உரை : 15 / 03.08.1977`
- mapped unit — **scans 320–355 / printed pp.319–354 / 36 pages**
- boundaries — **319→320 PASS / 355→356 PASS**
- Gate C — **COMPLETE / 36 of 36 first-pass**
- source-page markers — **320→355 / 36 / exactly once / ordered**
- first-pass unresolved readings — **0 currently flagged**
- Gate C.5 — **N/A / CLOSED**
- Gate C.5 basis — **May 2007 modern typesetting; representative direct-pixel review at scans 320, 326, 335, 345, 355; 0 historical-glyph corrections / 0 unresolved**
- Gate D — **READY / NOT STARTED**
- Gate E — **NOT STARTED**
- Tamil — **NOT VERIFIED / verified_against_scan=false**
- Gate F — **BLOCKED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**
- Speech 16 — **NOT STARTED**
- outside wording imported — **0**

## Exact next activity

Perform **Speech 15 Gate D completeness audit — scans 320–355 / printed pp.319–354 / all 36 pages**.

Requirements:

1. inspect canonical `transcript.md` structurally against the locked source map;
2. confirm all **36** source-page markers **320→355** are present exactly once and ordered;
3. confirm no source page is omitted or duplicated;
4. confirm start/end align with locked boundaries **319→320** and **355→356**;
5. confirm split continuations **325→326** and **350→351** are represented without mechanical omission/duplication;
6. confirm all printed speaker labels/interventions represented in the first-pass transcript;
7. confirm first/last Speech-15 text aligns with the locked source unit;
8. record any completeness correction separately; do not perform Gate-E word-for-word polishing;
9. keep Tamil **NOT VERIFIED / verified_against_scan=false**;
10. if Gate D passes, set exact next activity to **Gate E Batch 1 — scans 320–329 / exactly 10 pages**;
11. do not begin Gate E in the same activity unless separately instructed;
12. do not reopen Speech 14 or begin Speech 16.
