# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 10 Gate C Tamil first pass

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–9 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them merely for stylistic polishing.

Speech 10 source-boundary and Gate-C setup is **PASS / COMPLETE**. No Speech-10 Tamil transcription has yet been performed.

## Speech 10 locked mapping

- source label — `உரை : 10`
- printed date — `29.6.71`
- ISO date — `1971-06-29`
- working ID — `1971-06-29-financial-statement-debate`
- global scans — **117–151**
- printed pages — **116–150**
- page count — **35**
- hard start boundary — **116→117 — PASS**
- hard end boundary — **151→152 — PASS**
- scan 152 begins Speech 11 / `உரை : 11 / நாள் : 10.3.1972` and is excluded

## Controlling split coverage

1. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_005_pages_101-125.pdf`
   - 25 pages / 18,572,668 bytes
   - SHA-256: `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`
   - local pages **17–25** = global scans **117–125**
   - local page 16 = global scan 116 / Speech 9 close, boundary-only
2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_006_pages_126-150.pdf`
   - 25 pages / 17,713,432 bytes
   - SHA-256: `67f71bd3d4bce3c2fe9c258daaa307e29b3a5a195c848b4597c4844066ca8043`
   - local pages **1–25** = global scans **126–150**
3. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_007_pages_151-175.pdf`
   - 25 pages / 18,066,473 bytes
   - SHA-256: `e6fc152ccc1953d829438fafb6bdcfe5865633033662924518366c05a844f906`
   - local page **1** = global scan **151**
   - local page 2 = global scan 152 / Speech 11 start, boundary-only

Total Speech-10 source coverage: **35/35 pages**. The supplied part008 split is outside Speech 10 and is not a controlling split for this unit.

## Parallel-witness rule

Speech 10 overlaps the existing `நமது விளக்கம்` event/provenance/source layer for 29.6.1971. The 2007 anthology is an **independent source witness**.

- do not overwrite or normalize to `நமது விளக்கம்`;
- do not use `நமது விளக்கம்`, Official Reports, OCR, web copies or alternate anthologies to supply or repair wording;
- all Gate-C wording must come directly from the rendered pixels of the three controlling 2007 anthology splits above;
- leave the existing `நமது விளக்கம்` source layer unchanged.

## Current Speech 10 state

- source-boundary / Gate-C setup — **PASS / COMPLETE**
- Tamil — **NOT STARTED / verified_against_scan=false**
- Gate C — **NOT STARTED**
- Gate C.5 — **NOT STARTED**
- Gate D / Gate E — **NOT STARTED**
- English / Gates F–G — **BLOCKED / NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**
- `transcript.md` — not yet created

## Whole-speech execution rule

The normal activity allowance is 25 source pages, but the repository policy explicitly says a single speech longer than 25 pages is processed separately as one intact unit. Therefore **Speech 10 Gate C must cover all 35 pages / scans 117–151 in this one speech activity**; do not split it merely to satisfy the allowance.

## Exact next activity

Perform **Speech 10 Gate C Tamil first-pass transcription — scans 117–151 / printed pp.116–150 / 35 pages**.

Requirements:

1. transcribe only from the rendered 2007 anthology pixels;
2. create the canonical first-pass `transcript.md` with source-page markers **117→151**, exactly once and in order;
3. preserve source wording, spelling, punctuation, numerals, speaker labels/interventions, printed English and source-visible repetitions;
4. normalize only physical line wrapping into readable paragraphs;
5. preserve the locked boundaries **116→117 / 151→152**; do not admit scan 116 or scan 152 into Speech 10;
6. mark uncertain readings explicitly rather than guessing;
7. do not consult or import wording from `நமது விளக்கம்` or any outside source;
8. after the full 35-page first pass, synchronize Speech-10 README / metadata / source-notes / verification-log and anthology control documents;
9. set Gate C to **COMPLETE** only if all 35 pages are represented; Tamil must remain **TRANSCRIBED / NOT VERIFIED** with `verified_against_scan=false`;
10. do **not** begin Gate C.5, Gate D, Gate E, English work, Gate H, or Speech 11 in this activity.

Expected continuation after Gate C: **Speech 10 Gate C.5 applicability decision / Tamil completeness audit preparation**, following the repository workflow and the actual page evidence.
