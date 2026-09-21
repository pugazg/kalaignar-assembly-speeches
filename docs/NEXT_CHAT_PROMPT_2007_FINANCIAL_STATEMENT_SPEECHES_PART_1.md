# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 10 Gate C.5 + Gate D readiness

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–9 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them merely for stylistic polishing.

Speech 10 / `29.6.71` has now completed **Gate C across all 35 source pages**.

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
   - local pages **17–25** = global scans **117–125**
   - SHA-256 `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`
2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_006_pages_126-150.pdf`
   - local pages **1–25** = global scans **126–150**
   - SHA-256 `67f71bd3d4bce3c2fe9c258daaa307e29b3a5a195c848b4597c4844066ca8043`
3. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_007_pages_151-175.pdf`
   - local page **1** = global scan **151**
   - SHA-256 `e6fc152ccc1953d829438fafb6bdcfe5865633033662924518366c05a844f906`

Total controlling coverage remains **35/35 pages**.

## Parallel-witness rule

Speech 10 is an **independent 2007-anthology witness** overlapping the existing `நமது விளக்கம்` source layer.

- do not overwrite or normalize to `நமது விளக்கம்`;
- do not use `நமது விளக்கம்`, Official Reports, OCR, web copies or alternate anthologies to supply or repair wording;
- use only the controlling 2007 anthology pixels for source checks;
- leave the existing `நமது விளக்கம்` source layer unchanged.

## Gate C durable result

- `transcript.md` — **CREATED**
- represented source pages — **35/35**
- markers — **117→151 / exactly once / in order — PASS**
- boundary leakage — **none**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- first-pass unresolved readings — **0 explicitly flagged**
- page-boundary reconciliation — **123–125 / 136–138 corrected before canonical assembly**
- definite Gate-C pixel readings reconciled — scans **120, 127, 139, 142, 144, 149**
- outside-source wording imported — **0**

These Gate-C reconciliations are **not Gate-E verification corrections**.

## Current Speech 10 state

- source-boundary setup — **PASS / COMPLETE**
- Gate C — **COMPLETE**
- Gate C.5 — **NOT STARTED**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- English / Gates F–G — **BLOCKED / NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**

## Exact next activity

1. Decide **Gate C.5 applicability** from the actual 2007 anthology typography.
2. If Gate C.5 is **N/A / CLOSED**, perform the **Gate D structural completeness audit** across the intact 35-page Speech-10 unit / scans **117–151**.
3. At Gate D, audit all 35 page markers and transitions **117→118 ... 150→151**, hard boundaries, speaker labels/interventions, quotations, parenthetical reactions, source-printed English, figures/dates, source-visible repetition, truncation, duplicated blocks and missing source content.
4. Gate D may make completeness-only fixes if required and must record each fix.
5. Keep Tamil **TRANSCRIBED / NOT VERIFIED** and `verified_against_scan=false` after Gate D.
6. Do **not** perform Gate E word-for-word fidelity verification, English translation, Gate H, or Speech 11 in the same activity.

Expected continuation after Gate D: **Speech 10 Gate E word-for-word Tamil scan verification — scans 117–151 / 35 pages**, using only the controlling anthology pixels.
