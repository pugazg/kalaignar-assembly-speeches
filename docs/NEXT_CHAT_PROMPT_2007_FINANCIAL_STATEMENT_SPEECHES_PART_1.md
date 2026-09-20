# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 8 Gate F

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–7 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen Speeches 1–7 merely for stylistic polishing.

## Speech 8 durable Gates C–E state

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
- Gate D — **PASS / COMPLETE / retrospectively amended to 1 completeness correction**
- Gate-D retrospective note — Gate E restored the omitted scan-90 phrase `விந்தையாக இருக்கிறது,`
- Gate E — **PASS / COMPLETE / 23 of 23 pages / 43 source-fidelity corrections / 0 unresolved readings**
- source markers **90→112 exactly once and in order**
- cross-split transition **100→101 — PASS**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED** for modern 2007 typesetting; no historical/reform-sensitive glyph anomaly found
- English — **NOT STARTED / Gate F exact next**
- release — **WORKING / NOT RELEASED**
- Speech 9 — **NOT STARTED**

Gate E re-read all 23 pages directly against rendered source pixels. No OCR, web copy, Official Report or alternate anthology supplied Tamil wording.

The complete **43-item** Gate-E correction ledger is in:

`speeches/1966/1966-03-04-financial-statement-debate/verification-log.md`

## Exact next activity

Perform **Speech 8 / 4.3.1966 — Gate F English first-pass translation**, scans **90–112 / 23 pages**.

Gate-F authority is strictly the **final Gate-E-verified Tamil in `transcript.md`**. Do not use OCR, scan pixels, web research, Official Reports or alternate anthologies to supply or correct English wording.

Requirements:

1. translate all **23/23** verified Tamil source-page sections **90→112**;
2. preserve source-page sections **90→112** in `translation.md`, each exactly once and in order;
3. produce a faithful reading translation that preserves source names, dates, numerals, rupee amounts, commodity-price figures, statistical blocks, quotations, interventions, humour, analogies and rhetorical force;
4. preserve the scan-93 Speaker source-printed English `He is so well known.` exactly rather than retranslating it;
5. do not normalize or outside-correct source-bound names, historical references, political labels, policy claims or institutional terms;
6. keep uncertain/source-bound terms conservative; transliterate rather than import an outside identification or gloss when necessary;
7. record translation choices and any blocking questions in `translation-review.md`;
8. create/update `translation.md`, `translation-review.md`, `metadata.json`, speech README, source notes and verification log;
9. synchronize anthology README, mapping, handover and root status summary;
10. after Gate F, English status must be **FIRST-PASS / NOT YET VERIFIED AGAINST TAMIL** with `verified_against_tamil=false`;
11. Gate-F blocking questions must be recorded explicitly; do not silently resolve them from outside sources;
12. do not alter the verified Tamil during Gate F;
13. do not add Speech 8 to the released root dated index or `data/speeches.json`;
14. do not begin Gate G or Speech 9 in the same iteration.

Source-bound passages requiring conservative handling include the tax / “empty gun” analogy; food-production and nutrition discussion; commodity-price list; Chennai / Tiruchirappalli / Thanjavur / Coimbatore water-supply discussion; Tenali Raman analogy; Tuticorin thermal-power project; Salem steel-plant chronology; backward-region discussion; audit / housing / pesticide / `கேந்திர கிராமம்` expenditure examples; ministerial-economy proposals; and the 1967 election closing.

Expected continuation after successful Gate F: **Speech 8 Gate G full English fidelity and voice review, scans 90–112 / 23 pages**.
