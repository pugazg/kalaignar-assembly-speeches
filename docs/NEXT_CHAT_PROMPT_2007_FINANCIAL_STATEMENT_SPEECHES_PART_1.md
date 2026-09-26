# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 18 Gate C Batch 2 — scans 492–501

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–17 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 18 source state

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

2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`
   - bytes — **18,938,935**
   - SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
   - Speech-18 coverage — **local 1–10 / global scans 501–510 / 10 pages**
   - local 11 / scan 511 — **Speech 19 start / excluded**

The supplied `part_022_pages_526-546.pdf` is downstream of Speech 18 and remains outside the active source range.

## Current Gate-C state

- source intake — **COMPLETE**
- Gate-C setup — **COMPLETE**
- Gate C — **IN PROGRESS**
- Batch 1 — **COMPLETE / scans 482–491 / printed pp.481–490 / 10 pages**
- cumulative first-pass — **10 of 29**
- source-page markers — **482→491 / 10 / exactly once / ordered**
- first-pass unresolved readings — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**
- Speech 19 — **NOT STARTED**

Batch-1 source-visible first-pass forms retained without normalization include:

- scan 482 — `மாண்புமிகு பேரவைத் தலைவரவர்களே`, `“பொய்மான் காடு”`
- scan 485 — `982.66 கோடிய ரூபாயும்`
- scan 488 — `ஒலவக்கோடு`, `பற்றாக் குறையை`
- scans 488→489 — `கங்கை -` → `காவிரி இணைப்புத் திட்டம்...`
- scan 489 — `திட்டங்களை..`
- scan 491 — `குவாலிபிகேஷன்`
- scan 491 ends mid-sentence after `கைம்பெண்கள் உதவித்தொகை பெறுவோர்,`; its continuation belongs to scan 492 and was not imported into Batch 1.

## Fixed Gate-C cadence

- Batch 1 — **482–491 / 10 pages / COMPLETE**
- Batch 2 — **492–501 / 10 pages / NEXT**
- Batch 3 FINAL — **502–510 / 9 pages**

Batch 2 crosses the supplied split boundary:

- scans **492–500** = part020 local **17–25**
- scan **501** = part021 local **1**
- preserve the source continuation across **500→501**

## Source authority

Use only the controlling **2007 anthology pixels**.

Do not import wording from web sources, Official Reports, alternate anthologies, released speeches, other witnesses, or OCR output used as a substitute for reading the rendered source.

Preserve source spelling, punctuation, numerals, repetitions, speaker labels/interventions, printed English and source-page boundaries.

## Exact next activity

Perform **Speech 18 Gate C Batch 2 — scans 492–501 / exactly 10 pages**.

Requirements:

1. transcribe scans **492–501** manually from the rendered source pages;
2. create exactly one `<!-- source-page: N -->` marker for each scan **492→501**;
3. continue scan 491 into scan 492 exactly as supported by the source;
4. preserve the working-split transition and any textual continuation across **500→501**;
5. preserve source spellings, punctuation, figures, repetitions, speaker labels/interventions and printed English;
6. record uncertain readings conservatively rather than silently normalizing them;
7. import **0 outside wording**;
8. leave the existing scans **482–491** unchanged;
9. leave scans **502–510** untouched;
10. after success, Gate C should be **20/29 first-pass** and Tamil must remain **NOT VERIFIED / verified_against_scan=false**;
11. synchronize Speech-18 and anthology controls;
12. exact next after Batch 2: **Gate C Batch 3 FINAL — scans 502–510 / exactly 9 pages**;
13. do not begin the final batch in the same activity.
