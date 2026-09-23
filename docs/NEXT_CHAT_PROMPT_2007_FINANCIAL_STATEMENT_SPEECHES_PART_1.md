# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 16 source-boundary + Gate-C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–15 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

Speech 15 / 03.08.1977 final state:

- scans — **320–355 / printed pp.319–354 / 36 pages**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate-E corrections — **53 entries / 53 occurrences / 0 unresolved**
- Gate F — **COMPLETE / 36 of 36**
- Gate G — **PASS / COMPLETE / 36 of 36 / 6 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- canonical bilingual transcript — **COMPLETE**
- Gate-H wording changes — **0 Tamil / 0 English**
- indexed — **YES**

## Fixed repository iteration rule

- **Gate C — 10 source pages per iteration**
- **Gate E — 10 source pages per iteration**
- only the final remainder may contain fewer than 10 pages;
- do not exceed 10 source pages in Gate C or Gate E unless the user explicitly overrides the rule.

## Speech 16 locked mapping

- source label/date — **உரை : 16 / 1.3.1978**
- canonical date — **1978-03-01**
- canonical path — `speeches/1978/1978-03-01-financial-statement-debate/`
- mapped scans — **356–388**
- printed pages — **355–387**
- mapped page count — **33**
- incoming boundary — **355→356**
- outgoing boundary — **388→389**
- Speech 17 begins at scan **389**
- current state — **NOT STARTED**

## Exact next activity

Perform **Speech 16 source-boundary + Gate-C setup**.

Requirements:

1. refetch live `main` before editing;
2. use only rendered controlling anthology pixels for source wording;
3. reconfirm **355→356** and **388→389** visually;
4. establish which split PDFs/local pages cover scans **356–388** and record filename, byte size and SHA-256 when available;
5. create or reuse `speeches/1978/1978-03-01-financial-statement-debate/` with source notes, metadata, README, transcript and verification log;
6. preserve source spelling, punctuation, numerals, headings, speaker labels/interventions, printed English and visible repetition;
7. import no wording from OCR, web, Official Reports, alternate anthologies, released speeches or other witnesses;
8. keep Tamil **NOT VERIFIED / verified_against_scan=false** during Gate C;
9. once transcription begins, process **Gate C Batch 1 — scans 356–365 / exactly 10 pages**;
10. do not exceed 10 Gate-C pages in this iteration;
11. do not begin Gate E, Gate F, Gate G, Gate H or Speech 17.
