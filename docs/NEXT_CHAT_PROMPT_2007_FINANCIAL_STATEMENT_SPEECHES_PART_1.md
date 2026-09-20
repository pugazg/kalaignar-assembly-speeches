# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 8 Gate D

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–7 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen Speeches 1–7 merely for stylistic polishing.

## Speech 8 durable Gate-C state

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

Gate C:

- **COMPLETE / 23 of 23 pages**
- source markers **90→112 exactly once and in order**
- first-pass unresolved readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting
- Gate D — **NOT STARTED / exact next**
- Gate E / English — **NOT STARTED**
- release — **WORKING / NOT RELEASED**

Gate C was transcribed only from rendered source pixels. No OCR, web copy, Official Report or alternate anthology supplied wording.

## Exact next activity

Perform **Speech 8 / 4.3.1966 — Gate D completeness audit**, scans **90–112 / 23 pages**.

Gate-D requirements:

1. use the Gate-C `transcript.md` as the working transcription and the rendered source pixels as the completeness authority;
2. check every source-page marker **90→112** occurs exactly once and in order;
3. verify scan 89 remains excluded, scan 90 opening is represented, scan 112 close through `வணக்கம்.` is complete, and scan 113 remains excluded;
4. check all page-spanning continuations **90→91 through 111→112** for omission, duplication or wrong ordering;
5. explicitly check the split transition **100→101** across the two PDFs;
6. check M. Bhaktavatsalam interventions on scans **91, 92 and 95**, and the Speaker source-printed English `He is so well known.` on scan **93**;
7. check quotations, dates, numerals, rupee amounts, commodity prices, statistical figures, named references and stage/intervention structure are represented;
8. Gate D is a completeness audit only: do not silently perform Gate-E word-level source corrections;
9. if a completeness defect is found, correct it and record the exact correction by scan in `verification-log.md`;
10. after Gate D, Tamil remains **NOT VERIFIED / verified_against_scan=false**;
11. update `metadata.json`, speech README, source notes, verification log, anthology README, mapping, handover and this next-chat prompt;
12. do not begin Gate E, English translation or Speech 9 in the same iteration.

Expected continuation after successful Gate D: **Speech 8 Gate E strict page-by-page Tamil source-fidelity verification, scans 90–112 / 23 pages**.
