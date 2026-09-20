# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 7 Gate E

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–6 are RELEASED / CLOSED through Gate H**.

Do not reopen Speeches 1–6 merely for stylistic polishing.

## Speech 7 durable Gates C–D state

Working entry:

`speeches/1964/1964-03-07-financial-statement-debate/`

Source identity:

- source label — `உரை : 7`
- printed date — `7.3.1964`
- global scans — **76–89**
- printed pages — **75–88**
- page count — **14**
- working split — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_004_pages_76-100.pdf`
- split local pages — **1–14**
- split local page 15 / global scan 90 begins Speech 8
- working split pages — **25**
- working split SHA-256 — `249a5cfee267acc49efc222d13408e2c3570f02ee67de7bc3ce583a8e453c9d2`

Boundaries:

- scan 75 closes released Speech 6;
- scan 76 begins `உரை : 7 / நாள் : 7.3.1964`;
- scan 89 closes Speech 7 with `வணக்கம்.`;
- scan 90 begins `உரை : 8 / நாள் : 4.3.1966`;
- hard boundaries **75→76** and **89→90** are preserved.

Gate state:

- Gate C — **COMPLETE / 14 of 14 pages**
- Gate D — **PASS / COMPLETE / 14 of 14 pages / 0 completeness corrections**
- source markers **76→89 exactly once and in order**
- all transitions **76→77 through 88→89 — PASS**
- first-pass unresolved readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting
- Gate E — **NOT STARTED / exact next**
- English — **NOT STARTED**
- release — **WORKING / NOT RELEASED**

Gate D confirmed the M. Bhaktavatsalam intervention on scan 77, `(சிரிப்பு)` on scan 77, `(மணி அடிக்கப்பட்டது.)` on scan 88, all boundaries, quotations, dates, numerals, rupee amounts, figures, names and page order. No OCR, web copy, Official Report or alternate anthology supplied wording.

## Exact next activity

Perform **Speech 7 / 7.3.1964 — Gate E strict page-by-page Tamil source-fidelity verification**, scans **76–89 / 14 pages**.

Gate-E requirements:

1. compare every Gate-C Tamil page directly against the rendered source pixels, scan by scan **76→89**;
2. preserve source spelling, punctuation, numerals, quotations, names, speaker labels/interventions, parenthetical stage notes and page fragments exactly as printed;
3. make only source-supported fidelity corrections; do not normalize, modernize or rewrite from outside knowledge;
4. record every correction in `verification-log.md` by scan with exact before → after wording;
5. keep source-page markers **76→89** exactly once and in order;
6. preserve hard boundaries **75→76** and **89→90**; scan 90 remains excluded;
7. explicitly re-check the M. Bhaktavatsalam intervention and `(சிரிப்பு)` on scan 77, the bell note on scan 88, quoted material, dates, rupee amounts and the final `வணக்கம்.`;
8. if any legacy/reform-sensitive glyph issue is actually encountered, reopen Gate C.5 only for that page and record it; otherwise close Gate C.5 as N/A after the full visual audit;
9. record unresolved readings rather than guessing;
10. if all 14 pages pass with 0 unresolved readings, set Tamil status to **VERIFIED / verified_against_scan=true**;
11. update transcript banner, `metadata.json`, speech README, source notes, verification log, anthology README, mapping, handover and this next-chat prompt;
12. do not begin English Gate F or Speech 8 in the same iteration.

Expected continuation after successful Gate E: **Speech 7 Gate F English first-pass translation, scans 76–89 / 14 pages**.
