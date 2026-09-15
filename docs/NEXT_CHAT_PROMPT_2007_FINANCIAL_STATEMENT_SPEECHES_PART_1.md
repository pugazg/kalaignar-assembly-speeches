# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 3 Gate E

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

## Durable anthology state

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / COMPLETE / LOCKED**
- mapped speeches — **19**
- Speech 1 / 5.3.1958 — **RELEASED / CLOSED**
- Speech 2 / 4.3.1959 — **RELEASED / CLOSED**
- Speech 3 / 16.3.1960 — Gate C COMPLETE; Gate D PASS
- speeches 4–19 — not started

## Speech 3 durable state

Path: `speeches/1960/1960-03-16-financial-statement-debate/`

- source label — `உரை : 3`
- printed date — `16.3.1960`
- scans — **34–42**
- printed pages — **33–41**
- Gate C — **COMPLETE / 9 of 9 pages**
- Gate D — **PASS / COMPLETE / 0 completeness corrections**
- source markers — **34→42 exactly once and in order**
- first-pass unresolved readings — **0**
- Tamil — **REVIEWED STRUCTURALLY / NOT VERIFIED**
- Gate C.5 — **provisionally N/A for modern 2007 typesetting**
- Gate E — **NOT STARTED / next**
- English — **BLOCKED**

## Exact next activity

Perform **Gate E strict page-by-page visual source-fidelity verification** for scans **34–42 / printed pp.33–41**.

Requirements:

1. compare every Tamil word/character directly with the rendered scan pixels;
2. check source spelling, spacing/compounds, punctuation, names, numerals, quantities and quotations;
3. verify the C. Subramaniam intervention on scan 39;
4. verify J. Madhava Gowder's intervention across scans 41→42;
5. verify both Deputy Speaker interventions and preserve their printed English exactly;
6. verify all embedded English in the quoted letter exactly as printed;
7. inspect transitions **34→35, 35→36, 36→37, 37→38, 38→39, 39→40, 40→41, 41→42**;
8. preserve source forms; do not modernise or silently correct grammar;
9. if an actual historical/reform-sensitive glyph issue appears, reopen Gate C.5 for that item;
10. record every fidelity correction in `verification-log.md`;
11. if all nine pages pass with no unresolved reading, set Tamil `verified_against_scan=true`;
12. do **not** begin English or Speech 4 in the same iteration.

Expected continuation after a clean Gate E: **Speech 3 Gate F English translation from verified Tamil**.
