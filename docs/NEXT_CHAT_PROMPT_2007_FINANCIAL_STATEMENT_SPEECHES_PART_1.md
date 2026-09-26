# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 18 Gate C Batch 1 — scans 482–491

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–17 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen released speeches unless a separate source-backed defect is discovered.

## Speech 18 setup state

Working entry:

`speeches/1980/1980-07-09-financial-statement-debate/`

Source:

- source label/date — **உரை : 18 / 09.07.1980**
- canonical date — **1980-07-09**
- global scans — **482–510**
- printed pages — **481–509**
- page count — **29**
- incoming boundary **481→482 — PASS**
- outgoing boundary **510→511 — PASS**
- scan 511 — **Speech 19 / உரை : 19 / 06.03.1982 start / excluded**

Controlling working splits:

1. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_020_pages_476-500.pdf`
   - bytes — **18,623,915**
   - SHA-256 — `74d09c34f8ee6293e91895dbcc20fe651c314fe8f89f3241585e290a8674e1df`
   - Speech-18 coverage — **local 7–25 / global scans 482–500 / 19 pages**
   - local 6 / scan 481 — **Speech 17 close / excluded**

2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`
   - bytes — **18,938,935**
   - SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
   - Speech-18 coverage — **local 1–10 / global scans 501–510 / 10 pages**
   - local 11 / scan 511 — **Speech 19 start / excluded**

The separately supplied `part_022_pages_526-546.pdf` is downstream of Speech 18 and is not needed for this Gate-C batch.

## Gate state

- source intake — **COMPLETE**
- Gate-C setup — **COMPLETE**
- Gate C — **NOT STARTED / 0 of 29**
- Tamil — **NOT TRANSCRIBED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- Gate F / English — **NOT STARTED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**
- Speech 19 — **NOT STARTED**

## Gate-C fixed cadence

- Batch 1 — **482–491 / printed pp.481–490 / 10 pages**
- Batch 2 — **492–501 / printed pp.491–500 / 10 pages**
- Batch 3 FINAL — **502–510 / printed pp.501–509 / 9 pages**

Batch/split alignment:

- Batch 1 = part020 local **7–16**
- Batch 2 = part020 local **17–25** + part021 local **1**
- Batch 3 = part021 local **2–10**

## Source authority

Use only the controlling **2007 anthology pixels**.

Do not import wording from web sources, Official Reports, alternate anthologies, released speeches, other witnesses, or OCR output used as a substitute for reading the rendered source.

Preserve source spelling, punctuation, numerals, repetitions, speaker labels/interventions, printed English, and source-page boundaries.

## Exact next activity

Perform **Speech 18 Gate C Batch 1 — scans 482–491 / exactly 10 pages**.

Requirements:

1. transcribe scans **482–491** manually from the rendered source pages;
2. create exactly one `<!-- source-page: N -->` marker for each scan;
3. preserve the scan-482 heading **உரை : 18 / 09.07.1980** and all source-visible structural content;
4. preserve speaker labels/interventions, figures, printed English and page-spanning continuations;
5. record uncertain readings conservatively rather than silently normalizing them;
6. import **0 outside wording**;
7. update Tamil state to **TRANSCRIBED / NOT VERIFIED** for the completed first-pass range only; do not set `verified_against_scan=true`;
8. leave scans **492–510** untouched;
9. synchronize Speech-18 and anthology controls after success;
10. exact next after Batch 1: **Gate C Batch 2 — scans 492–501 / exactly 10 pages**;
11. do not begin Batch 2 in the same activity.
