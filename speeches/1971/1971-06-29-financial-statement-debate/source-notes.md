# Source notes — உரை : 10 / 29.6.71

## Source authority

Controlling anthology:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- title — `நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`
- first edition — **மே, 2007**
- full PDF — **546 pages / 393,027,493 bytes**
- full-PDF SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- usable parsed text layer — **none**
- textual authority — **rendered scan pixels**

Speech-10 Gate C is now complete as a 35-page first-pass transcription from the rendered anthology pixels only. The resulting Tamil remains **TRANSCRIBED / NOT VERIFIED**.

## Locked speech boundary

| Field | Value |
|---|---|
| Source label | `உரை : 10` |
| Printed date | `29.6.71` |
| Working ID | `1971-06-29-financial-statement-debate` |
| Global scans | **117–151** |
| Printed pages | **116–150** |
| Page count | **35** |
| Start boundary | **116→117 — PASS** |
| End boundary | **151→152 — PASS** |

Direct visual boundary evidence:

- global scan **116** closes released Speech 9 and is excluded;
- global scan **117** displays `உரை : 10` and `நாள் : 29.6.71`;
- global scan **151 / printed 150** closes Speech 10 with a source ornament;
- global scan **152 / printed 151** displays `உரை : 11` and `நாள் : 10.3.1972` and is excluded.

Throughout this unit, printed page = global scan page - 1.

## Controlling split files

### Part 005

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_005_pages_101-125.pdf`

- page count — **25**
- file size — **18,572,668 bytes**
- SHA-256 — `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`
- local pages **17–25** = global scans **117–125**
- Speech-10 coverage — **9 pages**
- local page 16 = global scan 116 / Speech 9 close, boundary-only

### Part 006

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_006_pages_126-150.pdf`

- page count — **25**
- file size — **17,713,432 bytes**
- SHA-256 — `67f71bd3d4bce3c2fe9c258daaa307e29b3a5a195c848b4597c4844066ca8043`
- local pages **1–25** = global scans **126–150**
- Speech-10 coverage — **25 pages**

### Part 007

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_007_pages_151-175.pdf`

- page count — **25**
- file size — **18,066,473 bytes**
- SHA-256 — `e6fc152ccc1953d829438fafb6bdcfe5865633033662924518366c05a844f906`
- local page **1** = global scan **151**
- Speech-10 coverage — **1 page**
- local page 2 = global scan 152 / Speech 11 start, boundary-only

Speech-10 coverage is therefore **9 + 25 + 1 = 35/35 pages**. The supplied part008 split covers global scans 176–200 and is not controlling for Speech 10.

## Parallel-witness policy

The repository already preserves `நமது விளக்கம்` as a separate 1971 source layer with the related record:

`sources/1971-namathu-vilakkam/events/1971-06-29-assembly-budget-reply.md`

This 2007 anthology is an **independent parallel witness**. During Speech-10 transcription and verification:

- do not overwrite, merge into, or normalize to the earlier source layer;
- do not use its Tamil or English to fill, repair or resolve anthology wording;
- do not use Official Reports, OCR, web copies or alternate anthologies to supply wording;
- use only the rendered 2007 anthology pixels as textual authority.

The earlier `நமது விளக்கம்` layer was not used for wording in this setup and remains unchanged.

## Whole-speech execution policy

The normal activity limit is 25 source pages. Speech 10 is 35 pages, and the repository's explicit exception applies: a single speech longer than 25 pages is processed separately as **one intact unit** rather than split merely to satisfy the allowance.

Gate C was completed across **all scans 117–151** as one intact 35-page speech activity.

## Gate state after Gate D

- source coverage / boundary setup — **PASS / COMPLETE**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C — **COMPLETE / 35 of 35 pages**
- source markers **117→151** — **35/35 / unique / ordered / PASS**
- first-pass unresolved readings — **0 explicitly flagged**
- Gate C.5 — **N/A / CLOSED — modern 2007 typesetting**
- Gate D — **PASS / COMPLETE / 35 of 35 / 2 completeness corrections**
- Gate E — **NOT STARTED**
- English / Gates F–G — **BLOCKED / NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**
- outside-source wording imported — **0**

The Gate-C note that **136–138** had been fully reconciled was incomplete; Gate D found and corrected a residual boundary/duplication issue.

## Gate C.5 applicability

**N/A / CLOSED.** No separate historical-glyph gate is required for this modern 2007 typesetting. This does not replace Gate E.

## Gate D structural audit

- coverage — **117–151 / 35 pages**
- markers — **35/35 / unique / ordered**
- transitions — **34/34 PASS**
- hard boundaries — **PASS**
- interventions / printed English / figures / dates / reactions / source-visible repetition — structurally represented
- missing pages — **0**
- duplicated long blocks after correction — **0**
- completeness corrections — **2**

Corrections:
1. **136→137** — moved the Anna memorial sentence completion to page 137.
2. **137→138** — removed duplicated scan-138 Muslim League/prohibition material from page 137.

No other Tamil wording changed.

## Exact next

**Gate E word-for-word Tamil scan verification — scans 117–151 / printed pp.116–150 / 35 pages**, from the controlling 2007 anthology pixels only.
