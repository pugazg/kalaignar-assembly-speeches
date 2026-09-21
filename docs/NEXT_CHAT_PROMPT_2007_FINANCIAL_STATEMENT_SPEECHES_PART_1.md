# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 13 Gate E source-fidelity verification

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–12 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Speech 13 durable state

Working entry:

`speeches/1974/1974-03-14-financial-statement-debate/`

- source label/date — `உரை : 13 / 14.03.1974`
- global scans — **231–262**
- printed pages — **230–261**
- page count — **32**
- hard boundaries — **230→231 / 262→263 — PASS**
- whole-speech exception — **APPLIED / intact 32-page unit**
- Gate C — **COMPLETE / 32 of 32**
- source-page markers — **231→262 / exactly once / ordered**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE / 32 of 32**
- Gate-D internal transitions — **31 of 31 PASS**
- Gate-D completeness corrections — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- unresolved first-pass readings — **0 currently flagged**
- Gate E — **NOT STARTED / next**
- English / Gate F / Gate G — **BLOCKED / NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**
- Speech 12 — **unchanged**
- Speech 14 — **not begun**

## Controlling source

Use only rendered pixels from:

1. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_010_pages_226-250.pdf`
   - local **6–25** = scans **231–250**
   - SHA-256 `257b862a7ebe21d768f8e5a2f2d2f9e8bb6c4e7ca7f704800a6453f40d0a9b90`
2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_011_pages_251-275.pdf`
   - local **1–12** = scans **251–262**
   - SHA-256 `27c9c96d3c0bdb53480f8d1634300bf9d7dc57be17d3f83c66397ef78863712d`

No OCR, web copy, Official Reports, alternate anthology, released speech or another witness may supply or repair Tamil wording.

## Exact next activity

Perform **Speech 13 Gate E word-for-word source-fidelity verification — all 32 pages / scans 231–262**.

Requirements:

1. compare every transcribed page directly against its controlling scan pixels;
2. log every source-fidelity correction with scan and before→after wording;
3. preserve source spelling, punctuation, numerals, speaker labels/interventions, source-printed English, figures and visible repetition;
4. resolve uncertain readings only from the same source pixels; otherwise leave them explicitly unresolved;
5. preserve all 32 source-page markers and hard boundaries;
6. after all pages are checked, synchronize transcript / metadata / README / source-notes / verification-log and anthology control documents;
7. set Tamil to **VERIFIED / verified_against_scan=true** only if **32/32 pages** pass and unresolved readings are **0**;
8. Gate C.5 and Gate D remain closed; do not reopen them merely for stylistic changes;
9. do **not** begin English / Gate F, Gate G, Gate H or Speech 14 in this activity.
