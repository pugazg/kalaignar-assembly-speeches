# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 Gate H archival/release audit

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–18 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 19 authoritative pre-release state

Working entry:

`speeches/1982/1982-03-06-financial-statement-debate/`

Source:

- label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- hard boundaries **510→511 / 545→546 — PASS**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**

Current gates:

- Gate C — **PASS / COMPLETE**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE — 35/35 / 34/34 internal transitions**
- Gate E — **PASS / COMPLETE — 35/35 source-verified / 26 corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE — 35/35 translated / 0 blockers / 0 Tamil changes**
- Gate G — **PASS / COMPLETE — 35/35 English pages reviewed**
- Gate-G refinements — **14**
- Gate-G blockers — **0**
- verified-Tamil changes during Gate G — **0**
- outside English imported — **0**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **READY / NOT STARTED**
- release — **NOT RELEASED / NOT INDEXED**

Gate-G FINAL refinements were on scans **541 / 543 / 544 / 545** only. Source-printed English on scan **542** remained verbatim. Speaker labels/interventions on scans **544–545** remain preserved.

## Gate-H rule

Gate H is an **archival/release audit**. It must not rewrite verified Tamil or Gate-G-verified English merely for style.

Expected Gate-H wording changes:

- Tamil — **0**
- English — **0**

If a separate concrete defect is discovered, do not silently fix it inside Gate H. Record it and reopen the appropriate earlier gate instead.

## Exact next activity

Perform **Speech 19 Gate H archival/release audit**.

Requirements:

1. fetch live `main` and treat it as authoritative;
2. verify Tamil source-page markers **511→545 / 35 / exactly once / ordered**;
3. verify English source-page sections **511→545 / 35 / exactly once / ordered**;
4. verify Tamil is **VERIFIED / verified_against_scan=true** and English is **VERIFIED AGAINST TAMIL / verified_against_tamil=true**;
5. recheck all **34/34** merged page transitions for mechanical duplication or omission;
6. preserve key page-spanning continuations and the working-split transition **525→526**;
7. preserve source-printed English verbatim on scans **523–525 / 535 / 542**;
8. preserve scan **539** source-printed `foundation, weir pie` exactly as printed;
9. preserve speaker labels/interventions and turn-taking on scans **544–545**;
10. recheck hard boundaries **510→511 / 545→546 — PASS** and keep scans 510 / 546 excluded;
11. recheck all **26 Gate-E corrections** and all **14 Gate-G refinements** as already incorporated;
12. Gate-H wording changes should remain **0 Tamil / 0 English**;
13. confirm canonical bilingual `transcript.md` is complete: verified Tamil followed by Gate-G-verified English;
14. create/retire `translation.md` to the standard released pointer used by prior speeches, pointing to canonical `transcript.md` and `translation-review.md`;
15. update `metadata.json` release fields to **RELEASED / Gate H PASS-COMPLETE / canonical bilingual true** only after every check passes;
16. add the unique date **1982-03-06** to `data/speeches.json` exactly once, following the established Speech-18 schema and preserving chronological order;
17. add the Speech-19 row to the root dated speech table exactly once, following the established anthology-row pattern;
18. synchronize Speech README, source-notes, verification-log, translation-review, anthology mapping/source README, handover, root README and this continuation prompt;
19. confirm Speech 18 and all earlier released speeches remain unchanged;
20. after a clean audit, set Speech 19 to **RELEASED / CLOSED through Gate H**;
21. after Speech 19 closes, mark this 2007 financial-statement Part-1 anthology workflow **COMPLETE / all 19 mapped speech units processed**, while preserving the special non-single-date / parallel-witness indexing rules already recorded for earlier speeches.

Do not use OCR, web, Official Reports, alternate anthologies or other witnesses to alter archival wording during Gate H.

If all checks pass, exact resulting state:

- Tamil — **VERIFIED**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- Gate-H wording changes — **0 Tamil / 0 English**
- `translation.md` — **released pointer**
- unique-date indexes — **synchronized**
- release — **RELEASED / CLOSED**
- 2007 financial-statement speeches Part 1 — **all 19 speech units processed / workflow complete**
