# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 2 Gate E

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

## Durable anthology state

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / COMPLETE / LOCKED**
- mapped speeches — **19**
- Speech 1 / 5.3.1958 — **RELEASED / CLOSED**
- Speech 2 / 4.3.1959 — Gate C COMPLETE; Gate D PASS
- speeches 3–19 — not started

## Speech 2 durable state

Path: `speeches/1959/1959-03-04-financial-statement-debate/`

- source label — `உரை : 2`
- printed date — `4.3.1959`
- scans — **25–33**
- printed pages — **24–32**
- Gate C — **COMPLETE / 9 of 9 pages**
- Gate D — **PASS / COMPLETE / 0 completeness corrections**
- source markers — **25→33 exactly once and in order**
- first-pass unresolved readings — **0**
- Tamil — **REVIEWED STRUCTURALLY / NOT VERIFIED**
- Gate C.5 — **provisionally N/A for modern 2007 typesetting**
- Gate E — **NOT STARTED / next**
- English — **BLOCKED**

## Exact next activity

Perform **Gate E strict page-by-page visual source-fidelity verification** for scans **25–33 / printed pp.24–32**.

Requirements:

1. compare every Tamil word/character directly with the rendered scan pixels;
2. check source spelling, spacing/compounds, punctuation, names, numerals, quantities and quotations;
3. inspect the C. Subramaniam intervention on scan 26;
4. inspect transitions **25→26, 26→27, 27→28, 28→29, 29→30, 30→31, 31→32, 32→33**;
5. preserve source forms; do not modernise or silently correct grammar;
6. if an actual historical/reform-sensitive glyph issue appears, reopen Gate C.5 for that item;
7. record every fidelity correction in `verification-log.md`;
8. if all nine pages pass with no unresolved reading, set Tamil `verified_against_scan=true`;
9. do **not** begin English or Speech 3 in the same iteration.

Expected continuation after a clean Gate E: **Speech 2 Gate F English translation from verified Tamil**.
