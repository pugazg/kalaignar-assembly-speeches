# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 15 Gate C.5 applicability determination

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–14 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Fixed repository iteration rule

Per explicit user instruction, `docs/ARCHIVAL_WORKFLOW.md` now controls:

- **Gate C — 10 source pages per iteration**
- **Gate E — 10 source pages per iteration**
- only the final remainder of a speech may contain fewer than 10 pages;
- do not exceed 10 source pages in a Gate-C or Gate-E iteration unless the user explicitly overrides the rule.

This rule supersedes any earlier whole-speech exception for Gates C and E.

## Speech 15 current state

Working entry:

`speeches/1977/1977-08-03-financial-statement-debate/`

- source label/date — `உரை : 15 / 03.08.1977`
- mapped unit — **scans 320–355 / printed pp.319–354 / 36 pages**
- incoming boundary **319→320** — **PASS / visually reconfirmed**
- outgoing boundary **355→356** — **PASS / visually reconfirmed**
- source coverage — **36/36 / no gap / no overlap**
- Gate C — **COMPLETE / 36 of 36 first-pass**
- source-page markers — **320→355 / 36 / exactly once / ordered**
- first-pass unresolved readings — **0 currently flagged**
- Tamil — **NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 — **NOT STARTED**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- Gate F — **BLOCKED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**
- Speech 16 — **NOT STARTED**
- outside wording imported — **0**

Speech 15 Gate C was already complete on live `main` before the new fixed 10-page rule was locked. Do not rewrite that completed history merely to simulate 10-page batches.

## Planned Speech-15 Gate-E cadence

When Gate E is reached:

- Batch 1 — **scans 320–329 / printed pp.319–328 / 10 pages**
- Batch 2 — **scans 330–339 / printed pp.329–338 / 10 pages**
- Batch 3 — **scans 340–349 / printed pp.339–348 / 10 pages**
- Final Batch 4 — **scans 350–355 / printed pp.349–354 / 6 pages**

## Exact next activity

Perform **Speech 15 Gate C.5 applicability determination — scans 320–355**.

Requirements:

1. use the controlling 2007 anthology pixels only;
2. determine whether this modern 2007 typeset witness requires a separate historical-Tamil-glyph audit;
3. inspect enough source pages to support a defensible applicability decision, including the known reform-sensitive glyph families defined in `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`;
4. if no legacy/historical glyph condition applies, record Gate C.5 **N/A / CLOSED** with the basis;
5. if historical forms are present, perform or schedule the required Gate C.5 audit without normalising source wording;
6. make no Gate-E verification claim in this activity;
7. do not mark Tamil verified;
8. do not begin Gate E until Gate C.5 is PASS/N/A and Gate D is complete;
9. preserve the fixed **10-source-page** rule for all later Gate-C and Gate-E iterations;
10. do not reopen Speech 14 or begin Speech 16.
