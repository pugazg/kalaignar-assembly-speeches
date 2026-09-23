# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 15 source-boundary + Gate-C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–14 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

Speech 14 / `10.03.1975` final state:

- working entry — `speeches/1975/1975-03-10-financial-statement-debate/`
- scans — **263–319 / printed pp.262–318 / 57 pages**
- Tamil — **VERIFIED / verified_against_scan=true**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate E — **32 corrections / 0 unresolved**
- Gate G — **23 refinements / 0 blockers / 0 Tamil changes**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- Gate-H wording changes — **0 Tamil / 0 English**
- `data/speeches.json` and root dated table — **indexed**

## Speech 15 mapped unit

- source label/date — `உரை : 15 / 03.08.1977`
- global scans — **320–355**
- printed pages — **319–354**
- page count — **36**
- incoming boundary — **319→320** — mapped as Speech 14 close → Speech 15 start
- outgoing boundary — **355→356** — mapped as Speech 15 close → Speech 16 start
- proposed working entry — `speeches/1977/1977-08-03-financial-statement-debate/`
- Speech 15 — **NOT STARTED**

## Exact next activity

Perform **Speech 15 source-boundary + Gate-C setup** for the full mapped unit **scans 320–355 / printed pp.319–354 / 36 pages**.

Requirements:

1. inspect live `main` and the anthology source inventory first;
2. establish the exact controlling split-file coverage for scans **320–355** and record file names, local-page mappings, sizes and SHA-256 values from the available source files;
3. directly inspect the hard boundaries **319→320** and **355→356** from source pixels;
4. confirm scan 320 begins `உரை : 15 / நாள் : 03.08.1977`;
5. confirm scan 355 is the final Speech-15 page and scan 356 begins Speech 16 / `1.3.1978`;
6. create or synchronize the Speech-15 working entry, source notes, metadata, README, verification log and control documents;
7. use only rendered controlling anthology pixels; no OCR/web/Official Report/alternate-anthology/other-witness wording may supply the text;
8. do not reopen Speech 14;
9. do not begin downstream verification/translation gates before the Speech-15 source unit and Gate-C controls are established;
10. follow the live repository batching rules unless the user gives a new Speech-15 cadence.
