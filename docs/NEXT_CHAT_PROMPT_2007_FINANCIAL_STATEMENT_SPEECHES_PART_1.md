# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 6 Gate G

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–5 are RELEASED / CLOSED through Gate H**.

Do not reopen Speeches 1–5 merely for stylistic polishing.

## Speech 6 durable state

Working entry:

`speeches/1963/1963-03-07-financial-statement-debate/`

Source boundary:

- source label — `உரை : 6`
- printed date — `7.3.1963`
- scans — **60–75**
- printed pages — **59–74**
- hard boundary **59→60** — preserved
- hard boundary **75→76** — preserved
- scan 76 begins Speech 7 and remains excluded

Tamil:

- Gate C — **COMPLETE / 16 of 16 pages**
- Gate D — **PASS / COMPLETE / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / 20 source-fidelity corrections / 0 unresolved readings**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**

English:

- Gate F — **COMPLETE / 16 of 16 pages**
- translation source — final Gate-E-verified Tamil only
- English — **FIRST-PASS / NOT YET VERIFIED AGAINST TAMIL**
- source-printed English on scan 73 — **preserved verbatim**
- Gate-F blocking translation questions — **0**
- Gate G — **NOT STARTED / exact next**
- release — **WORKING / NOT RELEASED**

Gate-F working files:

- `translation.md`
- `translation-review.md`

No OCR, web copy, Official Report or alternate anthology supplied English wording.

## Whole-speech batching policy

Maximum **25 source-scan pages per activity**, preserving whole speech units.

Speech 7 / 7.3.1964 is **14 pages / scans 76–89** and remains deferred. Do not start it in this iteration.

## Exact next activity

Perform **Gate G full English fidelity and voice review for Speech 6 / 7.3.1963, scans 60–75 (16/16 pages)**.

Review authority is strictly:

1. final Gate-E-verified Tamil in `transcript.md`;
2. Gate-F English in `translation.md`.

Requirements:

1. compare all 16 English source-page sections **60→75** against the corresponding verified Tamil;
2. check omissions, additions, mistranslations, altered emphasis, humour, rhetorical tone, quotations, names, dates, figures, quantities and page-spanning syntax;
3. preserve the source-printed English on scan 73 **exactly**:
   - `The Hon. Member has already taken 25 minutes.`
   - `Then it will be against the rules and regulations.`
4. do not use OCR, scan pixels, web research, Official Reports or alternate anthologies to supply English wording;
5. do not modify verified Tamil;
6. record every English refinement by scan and before→after wording in `translation-review.md`;
7. record per-page Gate-G result and total refinements / blockers / Tamil changes;
8. if all pages pass, set English `verified_against_tamil=true`;
9. do not begin Gate H in the same iteration;
10. do not begin Speech 7 in the same iteration.

Expected continuation after successful Gate G: **Speech 6 Gate H canonical merge / index / release closure**.
