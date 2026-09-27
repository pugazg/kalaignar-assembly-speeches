# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 18 Gate H archival/release audit

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–17 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 18 source state

Working entry:

`speeches/1980/1980-07-09-financial-statement-debate/`

- source label/date — **உரை : 18 / 09.07.1980**
- canonical date — **1980-07-09**
- scans — **482–510**
- printed pages — **481–509**
- page count — **29**
- hard boundaries **481→482 / 510→511 — PASS**
- scan 511 — **Speech 19 / உரை : 19 / 06.03.1982 start / excluded**

## Durable Tamil state

- Gates C / C.5 / D / E — **COMPLETE**
- Gate E — **PASS / COMPLETE / CLOSED**
- Gate-E corrections — **20 entries / 20 occurrences / 14 affected scans**
- Gate-E unresolved — **0**
- Tamil — **VERIFIED / verified_against_scan=true**

## Durable English state

- Gate F — **COMPLETE / 29 of 29 translated**
- Gate G — **PASS / COMPLETE / 29 of 29 reviewed**
- Gate-G iteration — **one FINAL batch / scans 482–510 / 29 pages**
- Gate-G refinements — **6 entries / 6 occurrences / 6 affected scans**
- Gate-G blockers — **0**
- verified-Tamil changes — **0**
- outside English imported — **0**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- source-printed English preserved verbatim:
  - scan 492 — `Minimum Level of Consumption`
  - scan 501 — `"5 acres owning"`
  - scan 506 — `(Contractor)`
- source-page sections — **482→510 / 29 / exactly once / ordered**
- hard boundary **510→511 — PASS / Speech 19 excluded**
- detailed Gate-G ledger — `translation-review.md`

## Gate H state

- Gate H — **READY / NOT STARTED / NOT RELEASED**
- release — **NOT RELEASED**
- Speech 19 — **NOT STARTED**

## Exact next activity

Perform **Speech 18 Gate H archival/release audit**.

Requirements:

1. keep the verified Tamil unchanged and retain the complete Gate-G-verified English after it in canonical `transcript.md`;
2. verify Tamil source-page markers and English source-page sections cover **482–510 / exactly 29 pages / exactly once / ordered**;
3. recheck all **6 Gate-G refinements**, all page-spanning continuations, and hard boundaries **481→482 / 510→511** after canonical consolidation;
4. confirm source heading/date, speaker label, figures, quotations, repetitions, rhetorical questions and interventions remain intact;
5. confirm source-printed English on scans **492, 501 and 506** remains verbatim;
6. inspect all merged page transitions for mechanical duplication or omission;
7. make **0 Tamil / 0 English wording changes** during Gate H unless a separate concrete defect is discovered and documented;
8. synchronize `metadata.json`, `README.md`, `verification-log.md`, `translation-review.md`, `data/speeches.json`, root README/index, source-package controls and anthology handover;
9. if every release check passes, set Gate H **PASS / COMPLETE**, release **RELEASED / CLOSED**, canonical bilingual transcript **COMPLETE**, and indexes **SYNCHRONIZED**;
10. keep scan 511 / Speech 19 excluded;
11. exact next after successful Speech-18 release: **Speech 19 source intake / Gate C setup**;
12. do not begin Speech 19 in the same Gate-H activity.
