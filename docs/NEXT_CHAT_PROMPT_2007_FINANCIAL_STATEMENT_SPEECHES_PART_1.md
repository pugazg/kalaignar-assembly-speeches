# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 16 Gate H canonical bilingual merge / release closure

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–15 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Speech 16 current state

Working entry:

`speeches/1978/1978-03-01-financial-statement-debate/`

- source label/date — **உரை : 16 / 1.3.1978**
- scans — **356–388 / printed pp.355–387 / 33 pages**
- Gates C–E — **COMPLETE**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate-E corrections — **24 / 0 unresolved**
- Gate F — **COMPLETE / 33 of 33**
- English source-page sections — **356→388 / 33 / exactly once / ordered**
- Gate G — **PASS / COMPLETE / 33 of 33**
- Gate-G refinements — **9**
- Gate-G blockers — **0**
- verified-Tamil changes — **0**
- source-printed-English changes — **0**
- outside English imported — **0**
- English — **VERIFIED AGAINST TAMIL**
- `verified_against_tamil=true`
- Gate H — **READY / NOT STARTED / NOT RELEASED**
- Speech 17 — **NOT STARTED**

## Exact next activity

Perform **Speech 16 Gate H — canonical bilingual merge / release closure**.

Requirements:

1. merge the already verified Tamil and Gate-G-verified English into the canonical bilingual `transcript.md`;
2. preserve Tamil source-page markers **356→388** and English source-page sections **356→388**, each exactly once and ordered;
3. do not alter verified Tamil or Gate-G-verified English merely for polishing;
4. preserve source-page boundaries, speaker labels/intervention, figures, repetitions, source-bound oddities and source-printed English;
5. retire `translation.md` to the standard released pointer only after the canonical bilingual record passes;
6. record any Gate-H wording change explicitly; expected wording changes are **0 Tamil / 0 English**;
7. synchronize Speech-16 controls, anthology controls, root dated speech table and `data/speeches.json` if the unique-date indexing checks pass;
8. set Speech 16 **RELEASED / CLOSED** only after all Gate-H checks pass;
9. advance exact next to **Speech 17 source-boundary + Gate-C setup** only after Speech 16 release closure;
10. do not begin Speech 17 in the same activity.
