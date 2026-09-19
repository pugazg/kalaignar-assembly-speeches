# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 7 Gate C

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–6 are RELEASED / CLOSED through Gate H**.

Do not reopen Speeches 1–6 merely for stylistic polishing.

Speech 6 final closure:

- source — scans **60–75 / printed pp.59–74**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **20 corrections / 0 unresolved**
- Gate F — **COMPLETE / 16/16**
- Gate G — **PASS / COMPLETE / 15 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- hard boundary **75→76** — preserved

## Whole-speech batching policy

Maximum **25 source-scan pages per activity**, preserving complete speech units.

Current exact unit:

- Speech 7 / **7.3.1964**
- scans **76–89**
- printed pages **75–88**
- page count — **14**
- previous boundary — scan 75 closes Speech 6
- scan 76 begins `உரை : 7 / நாள் : 7.3.1964`
- scan 89 closes Speech 7
- scan 90 begins Speech 8 / 4.3.1966

Speech 8 is **23 pages / scans 90–112** and must remain deferred because Speech 7 (14) + Speech 8 (23) exceeds the 25-page activity limit.

## Source authority

Use only the controlling source:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

Rendered scan pixels are authoritative.

Do not use OCR, web copies, Official Reports or alternate anthologies to supply wording.

## Exact next activity

Perform **Speech 7 / 7.3.1964 — Gate C Tamil first-pass transcription, scans 76–89 / 14 pages**.

Requirements:

1. create the working entry at `speeches/1964/1964-03-07-financial-statement-debate/` using the established neutral archival slug pattern;
2. transcribe all **14/14** source scans directly from rendered pixels;
3. preserve source spelling, punctuation, numerals, quotations, names, speaker labels/interventions and any source-printed English exactly as printed;
4. normalize only physical line wrapping into readable paragraphs; do not modernize or silently regularize wording;
5. add explicit source-page markers **76→89**, each exactly once and in order;
6. preserve the hard boundaries **75→76** and **89→90**; scan 75 belongs to released Speech 6 and scan 90 belongs to Speech 8;
7. record unresolved readings explicitly rather than guessing;
8. create/update the speech README, metadata, source notes and verification log for Gate-C state;
9. treat Gate C.5 as **provisionally N/A** for modern 2007 typesetting unless page-specific legacy-glyph evidence appears;
10. after Gate C, Tamil must remain **TRANSCRIBED / NOT VERIFIED** and `verified_against_scan=false`;
11. synchronize anthology README, mapping and handover;
12. do not begin Gate D, Gate E, English translation or Speech 8 in the same iteration.

Expected continuation after successful Gate C: **Speech 7 Gate D completeness audit, scans 76–89 / 14 pages**.
