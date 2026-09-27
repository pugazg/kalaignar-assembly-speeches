# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 source intake + Gate C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–18 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 18 durable closure

Working entry:

`speeches/1980/1980-07-09-financial-statement-debate/`

- source label/date — **உரை : 18 / 09.07.1980**
- scans — **482–510 / printed pp.481–509 / 29 pages**
- Tamil — **VERIFIED / 29/29 / verified_against_scan=true**
- English — **VERIFIED AGAINST TAMIL / 29/29 / verified_against_tamil=true**
- Gate-E corrections — **20 / 0 unresolved**
- Gate-G refinements — **6 / 0 blockers / 0 Tamil changes**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired release pointer**
- `data/speeches.json` / root dated table — **indexed**
- hard boundary **510→511 — PASS**
- Speech 18 is now **LOCKED**

## Speech 19 mapped source state

Planned working entry:

`speeches/1982/1982-03-06-financial-statement-debate/`

Source map:

- source label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- incoming boundary **510→511 — PASS**
- outgoing boundary **545→546 — PASS**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**
- anthology Gate B — **PASS / COMPLETE / LOCKED**

## Exact next activity

Perform **Speech 19 source intake + Gate C setup only**.

Requirements:

1. confirm live-main source mapping and existing-work overlap before creating or changing the Speech-19 entry;
2. establish/confirm the controlling source split(s) available for scans **511–545** and their page/hash metadata where already recorded;
3. create or synchronize the Speech-19 working entry and source-control files without importing outside wording;
4. preserve hard boundaries **510→511 / 545→546** and keep Speech 18 / back matter excluded;
5. set Gate C batching according to the repository's established fixed cadence of **10 source pages per iteration**, with only the final remainder allowed to be fewer;
6. expected Gate-C batches for 35 pages: **511–520 / 521–530 / 531–540 / 541–545 FINAL** unless live-main control documents already establish a different source-backed split;
7. Gate C.5 should remain provisionally N/A for this modern 2007 typesetting unless an actual legacy-type anomaly is observed;
8. do **not** begin Gate-C transcription in the same setup activity;
9. do **not** reopen Speech 18;
10. exact next after setup: **Speech 19 Gate C Batch 1 — scans 511–520 / exactly 10 pages**.
