# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 18 source intake + Gate C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–17 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

### Speech 17 special release policy

Speech 17 remains one source-preserved multi-date unit:

- source label/date — **உரை : 17 / 22 & 23.3.1979**
- scans — **389–481 / 93 pages**
- Tamil — **VERIFIED / verified_against_scan=true**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate G — **PASS / COMPLETE / 93 of 93 / 43 refinements**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- canonical bilingual transcript — **COMPLETE**
- explicit internal 22/23 March divider — **none found**
- single canonical date — **not assigned**
- root dated speech table / `data/speeches.json` — **unchanged intentionally**
- hard boundary **481→482 — PASS**
- scan 482 belongs to Speech 18 and is excluded from Speech 17.

## Speech 18 mapped source unit

Target entry:

`speeches/1980/1980-07-09-financial-statement-debate/`

Mapped source facts from the anthology controls:

- source label/date — **உரை : 18 / 09.07.1980**
- canonical date — **1980-07-09**
- global scans — **482–510**
- printed pages — **481–509**
- page count — **29**
- incoming boundary **481→482 — PASS**
- outgoing boundary **510→511 — PASS**
- scan 511 begins **Speech 19 / உரை : 19 / 06.03.1982** and is excluded
- Speech 18 status — **NOT STARTED**

## Source authority

Use the controlling **2007 anthology pixels only** for Speech 18 transcription and verification.

Do not import wording from:

- web sources;
- Official Reports;
- alternate anthologies;
- released speeches;
- other witnesses;
- OCR output used as a substitute for reading the source.

Preserve source spelling, punctuation, numerals, repetitions, speaker labels/interventions, printed English, and source-page boundaries.

## Gate-C working rule

- Gate C cadence — **10 source pages per iteration**
- Speech 18 total — **29 pages**
- expected transcription cadence after setup — **10 + 10 + 9**
- the final batch may contain fewer than 10 pages
- Gate C.5 for this modern 2007 typesetting is only provisionally N/A until Speech-18 pages are inspected; reopen only if an actual page-specific legacy typeform anomaly appears.

## Exact next activity

Perform **Speech 18 source intake + Gate C setup** for scans **482–510 / printed pp.481–509**.

Requirements:

1. re-read live source-package mapping and controls before writing;
2. establish or confirm the Speech-18 working directory and metadata;
3. identify the controlling source/split coverage for scans **482–510** from live repository/source assets without inventing file coverage;
4. reconfirm hard boundaries **481→482** and **510→511**;
5. confirm source label/date **உரை : 18 / 09.07.1980** and canonical date **1980-07-09**;
6. set Tamil state to **NOT TRANSCRIBED / verified_against_scan=false** until Gate C work actually begins;
7. set English/Gate F/G/H to **NOT STARTED**;
8. establish Gate-C batching as **482–491 / 492–501 / 502–510** if live source coverage supports those page boundaries;
9. synchronize speech-level and anthology controls;
10. exact next after successful setup: **Speech 18 Gate C Batch 1 — scans 482–491 / exactly 10 pages**;
11. do not transcribe Batch 1 in the same source-intake/setup activity unless the live control document explicitly says setup and Batch 1 are combined.
