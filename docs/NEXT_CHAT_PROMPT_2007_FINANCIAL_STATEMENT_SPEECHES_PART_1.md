# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 8 Gate E

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–7 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen Speeches 1–7 merely for stylistic polishing.

## Speech 8 durable Gates C–D state

Working entry:

`speeches/1966/1966-03-04-financial-statement-debate/`

Source identity:

- source label — `உரை : 8`
- printed date — `4.3.1966`
- global scans — **90–112**
- printed pages — **89–111**
- page count — **23**
- split 004 `...part_004_pages_76-100.pdf`
  - local pages **15–25** = global scans **90–100**
  - SHA-256 `249a5cfee267acc49efc222d13408e2c3570f02ee67de7bc3ce583a8e453c9d2`
- split 005 `...part_005_pages_101-125.pdf`
  - local pages **1–12** = global scans **101–112**
  - SHA-256 `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`

Boundaries:

- scan 89 closes released Speech 7;
- scan 90 begins `உரை : 8 / நாள் : 4.3.1966`;
- scan 112 closes Speech 8 with `வணக்கம்.`;
- scan 113 / split 005 local page 13 begins `உரை : 9 / நாள் : 29.3.1971`;
- hard boundaries **89→90** and **112→113** are preserved.

Gate state:

- Gate C — **COMPLETE / 23 of 23 pages**
- Gate D — **PASS / COMPLETE / 23 of 23 pages / 0 completeness corrections**
- source markers **90→112 exactly once and in order**
- all transitions **90→91 through 111→112 — PASS**
- cross-split transition **100→101 — PASS**
- first-pass unresolved readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting
- Gate E — **NOT STARTED / exact next**
- English — **NOT STARTED**
- release — **WORKING / NOT RELEASED**

Gate D directly checked all 23 rendered source pages, including the scan-91/92/95 M. Bhaktavatsalam interventions, scan-93 Speaker source-printed English `He is so well known.`, quotations, dates, numerals, rupee amounts, commodity prices, statistical figures, named references and all page boundaries. No OCR, web copy, Official Report or alternate anthology supplied wording.

## Exact next activity

Perform **Speech 8 / 4.3.1966 — Gate E strict page-by-page Tamil source-fidelity verification**, scans **90–112 / 23 pages**.

Gate-E requirements:

1. compare every Gate-C Tamil page directly against the rendered source pixels, scan by scan **90→112**;
2. preserve source spelling, punctuation, numerals, quotations, names, speaker labels/interventions, source-printed English and page fragments exactly as printed;
3. make only source-supported fidelity corrections; do not normalize, modernize or rewrite from outside knowledge;
4. record every correction in `verification-log.md` by scan with exact before → after wording;
5. keep source-page markers **90→112** exactly once and in order;
6. preserve hard boundaries **89→90** and **112→113**; scan 113 remains excluded;
7. explicitly re-check the M. Bhaktavatsalam interventions on scans **91, 92 and 95**, the Speaker source-printed English on scan **93**, quotations, dates, rupee amounts, commodity-price list, statistical blocks and the final `வணக்கம்.`;
8. explicitly re-check the cross-split **100→101** continuation;
9. if any legacy/reform-sensitive glyph issue is actually encountered, reopen Gate C.5 only for that page and record it; otherwise close Gate C.5 as N/A after the full visual audit;
10. record unresolved readings rather than guessing;
11. if all 23 pages pass with 0 unresolved readings, set Tamil status to **VERIFIED / verified_against_scan=true**;
12. update transcript banner, `metadata.json`, speech README, source notes, verification log, root anthology summary, anthology README, mapping, handover and this next-chat prompt;
13. do not begin English Gate F or Speech 9 in the same iteration.

Expected continuation after successful Gate E: **Speech 8 Gate F English first-pass translation, scans 90–112 / 23 pages**.
