# Handover — 2007 financial-statement speeches anthology, Part 1

Repository: `pugazg/kalaignar-assembly-speeches`, branch `main`.

## Controlling source

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

Locked source identity:

- printed title — `நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`;
- author — கலைஞர் மு. கருணாநிதி;
- publisher — தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004;
- first edition — மே, 2007;
- physical PDF pages — **546**;
- file size — **393,027,493 bytes**;
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`;
- usable text layer — **none**;
- authority — rendered scan pixels.

The source viewer initially exposed only 150 pages, but the actual PDF has 546 pages. Do not reintroduce the 150-page cap into metadata.

## Physical source state

- scans 1–17 — front matter / title matter;
- scans 18–545 — **19** numbered `உரை` units;
- scan 546 — closing portrait/back matter;
- printed page = scan page - 1 through the speech body.

Gate A: **PASS / COMPLETE**.

## Gate B

**PASS / COMPLETE / LOCKED.**

Full inventory is in:

`sources/2007-financial-statement-speeches-part-1/mapping.md`

Speech starts are scans:

**18, 25, 34, 43, 49, 60, 76, 90, 113, 117, 152, 191, 231, 263, 320, 356, 389, 482, 511**.

The focused second boundary check covered every transition plus 545→546; no boundary changed.

## Locked speech dates

1. 5.3.1958
2. 4.3.1959
3. 16.3.1960
4. 6.3.1961
5. 2.7.1962
6. 7.3.1963
7. 7.3.1964
8. 4.3.1966
9. 29.3.1971
10. 29.6.71
11. 10.3.1972
12. 07.03.1973
13. 14.03.1974
14. 10.03.1975
15. 03.08.1977
16. 1.3.1978
17. 22 & 23.3.1979
18. 09.07.1980
19. 06.03.1982

Speech 17 is deliberately held as a **multi-date source unit**; do not invent one canonical date.

## Whole-speech batching policy

Use a **maximum 25 source-scan pages per activity** while preserving whole-speech boundaries.

- add consecutive complete speeches while cumulative pages stay ≤25;
- do not split a speech merely to fill the batch;
- if the next speech would exceed 25 pages, defer that whole speech;
- if a single speech itself exceeds 25 pages, process it separately as one intact unit rather than dropping it.

Latest released unit: Speech 7 / 7.3.1964 = **RELEASED / CLOSED through Gate H** with verified Tamil and English. Active unit: Speech 8 / 4.3.1966 = **Gates C–E COMPLETE / 23 pages / scans 90–112 / 43 Gate-E corrections / 0 unresolved / Tamil VERIFIED**. Gate D is retrospectively amended to **1 completeness correction** because Gate E restored the omitted scan-90 phrase `விந்தையாக இருக்கிறது,`. Exact next: Speech 8 Gate F.

## Existing-source overlaps

Do not modify released or existing source layers merely because this anthology overlaps them.

- Speech 9 / 29.03.1971 — overlaps the `நமது நிலை` event/provenance record.
- Speech 10 / 29.06.1971 — overlaps the `நமது விளக்கம்` event/provenance record.
- Speech 12 / 07.03.1973 — parallel witness to the already released canonical `1973-03-07-financial-statement-reply`.

Treat this 2007 anthology as its own witness.

## Current gates

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / COMPLETE / LOCKED**
- Gate C — **Speeches 1–7 CLOSED; Speech 8 COMPLETE / 23 of 23 / NOT VERIFIED; speeches 9–19 not started**
- Gate C.5 — **N/A / CLOSED for Speeches 1–8 — modern 2007 typesetting; no historical/reform-sensitive glyph anomaly found in Speech 8**
- Gate D — **Speeches 1–7 PASS / COMPLETE with 0 completeness corrections; Speech 8 PASS / COMPLETE, retrospectively amended to 1 completeness correction**
- Gate E — **Speeches 1–8 PASS / COMPLETE / Tamil VERIFIED — correction counts 9 / 6 / 3 / 6 / 10 / 20 / 19 / 43; unresolved 0**
- Gate F — **Speeches 1–7 COMPLETE — English page counts 7 / 9 / 9 / 6 / 11 / 16 / 14**
- Gate G — **Speeches 1–7 PASS / COMPLETE — refinements 10 / 12 / 17 / 6 / 11 / 15 / 16; 0 blockers; English VERIFIED**
- Gate H — **Speeches 1–7 PASS / COMPLETE — RELEASED / CLOSED**

## Speech 1 durable Gate-C state

Canonical working entry:

`speeches/1958/1958-03-05-financial-statement-debate/`

Gate C is **COMPLETE**:

- scans **18–24 / printed pp.17–23**
- **7/7 pages**
- source markers **18→24**
- unresolved first-pass readings — **0**
- Tamil status — **VERIFIED**
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting; reopen only if actual glyph evidence requires it
- Gate D — **PASS / COMPLETE — 7/7 pages, 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 7/7 pages; 9 corrections; 0 unresolved readings**
- English — **VERIFIED AGAINST TAMIL**

The first pass preserved the speaker label, all three C. Subramaniam interventions, quotations, figures, and page-spanning continuations. No outside source supplied wording.

## Speech 1 Gate-D result

Gate D is **PASS / COMPLETE**.

- markers **18→24** — exactly once and in order;
- start/end boundaries — PASS;
- all three C. Subramaniam interventions — represented;
- quotations / figures / paragraph order — structurally complete;
- transitions **18→19, 19→20, 20→21, 21→22, 22→23, 23→24** — PASS;
- completeness corrections — **0**;
- Tamil — **VERIFIED / verified_against_scan=true**.

## Speech 1 Gate-E result

Gate E is **PASS / COMPLETE**.

- scans **18–24 / printed pp.17–23**
- verified pages — **7/7**
- source-fidelity corrections — **9**
- unresolved readings — **0**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED** for this modern 2007 typesetting; no legacy-glyph anomaly found

Corrections:
- scan 19 — two `திட்டமிட்டிருந்தோமென்றும்` joined forms;
- scan 20 — `வருஷமே`, `விதிக்கப் பட்டிருக்கின்றன`, `சென்ற வருஷம்`, `இவ்வளவாவது`;
- scan 23 — `சுவிட்ஜர்லாண்டை`;
- scan 24 — `வடக்கு என்ற வள்ளி வேண்டாம்`, `தெரிவித்துக் கொண்டு`.

## Speech 1 Gate-F / Gate-G result

Gate F is **COMPLETE — 7/7 pages**.

Gate G is **PASS / COMPLETE — 7/7 pages**.

- refinements — **10**
- blocking fidelity issues — **0**
- Tamil changes — **0**
- English `verified_against_tamil=true`
- all three C. Subramaniam interventions — PASS
- quotations, figures, page transitions and source claims — PASS
- humour/wordplay — PASS
- outside wording — **none**

The detailed audit is in `speeches/1958/1958-03-05-financial-statement-debate/translation-review.md`.

## Speech 1 Gate-H result

Speech 1 / 5.3.1958 is **RELEASED / CLOSED**.

- canonical bilingual transcript — complete;
- Tamil — verified;
- English — verified against Tamil;
- Gate-G refinements — 10;
- Gate-H wording changes — 0;
- root and machine-readable indexes — synchronized;
- `translation.md` — retired pointer.

## Speech 2 durable Gate-C state

Canonical working entry:

`speeches/1959/1959-03-04-financial-statement-debate/`

- scans **25–33 / printed pp.24–32**
- Gate C — **COMPLETE / 9 of 9 pages**
- source markers — **25→33**
- unresolved first-pass readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting
- Gate D — **NOT STARTED / next**
- Gate E — **NOT STARTED**
- English — **Speech 1 verified/released; Speech 2 NOT STARTED / Gate F next**

Gate C preserved the C. Subramaniam intervention, quoted material, all printed figures, and every page-spanning continuation through the scan-33 close.

## Speech 2 Gate-D result

Gate D is **PASS / COMPLETE**.

- markers **25→33** — exactly once and in order;
- start/end boundaries — PASS;
- scan-26 C. Subramaniam intervention — represented;
- quotations / figures / paragraph order — structurally complete;
- transitions **25→26, 26→27, 27→28, 28→29, 29→30, 30→31, 31→32, 32→33** — PASS;
- completeness corrections — **0**;
- Tamil remains **NOT VERIFIED**.

## Speech 2 Gate-E result

Gate E is **PASS / COMPLETE**.

- scans **25–33 / printed pp.24–32**
- verified pages — **9/9**
- source-fidelity corrections — **6**
- unresolved readings — **0**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED** for modern 2007 typesetting; no legacy-glyph anomaly found

Corrections:
- scan 26 — `குறிப்பிடும்`;
- scan 27 — source semicolon `திட்டமும்; கொள்கையும்!`;
- scan 28 — comma after `ஒப்புவித்து`;
- scan 29 — `செய்கின்ற காரியங்கள்`;
- scan 30 — `அந்த நிலையில்`;
- scan 32 — `19 இலட்சமாக`.

## Speech 2 Gate-F / Gate-G / Gate-H result

Speech 2 / 4.3.1959 is **RELEASED / CLOSED**.

- Gate F — complete 9/9;
- Gate G — PASS / COMPLETE, 12 refinements, 0 blockers, 0 Tamil changes;
- English `verified_against_tamil=true`;
- Gate H — PASS / COMPLETE;
- canonical bilingual transcript — complete;
- root and machine-readable dated indexes — synchronized;
- Gate-H wording changes — 0.

## Speech 3 durable Gate-C state

Canonical working entry:

`speeches/1960/1960-03-16-financial-statement-debate/`

- scans **34–42 / printed pp.33–41**
- Gate C — **COMPLETE / 9 of 9 pages**
- source markers — **34→42**
- unresolved first-pass readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- Gate C.5 — **provisionally N/A** for modern 2007 typesetting
- Gate D — **NOT STARTED / next**
- Gate E — **NOT STARTED**
- English — **BLOCKED**

Gate C preserved:
- C. Subramaniam intervention on scan 39;
- J. Madhava Gowder intervention spanning scans 41→42;
- Deputy Speaker interventions on scan 42, including printed English;
- the quoted letter and embedded English administrative terms;
- all figures and the scan-42 close.

## Speech 3 Gate-D result

Gate D is **PASS / COMPLETE**.

- markers **34→42** — exactly once and in order;
- start/end boundaries — PASS;
- scan-39 C. Subramaniam intervention — represented;
- scans 41→42 J. Madhava Gowder intervention — continuous;
- scan-42 Deputy Speaker interventions / printed English — represented;
- quoted letter / embedded English administrative terms — structurally complete;
- figures / quotations / humour / analogies — structurally complete;
- transitions **34→35, 35→36, 36→37, 37→38, 38→39, 39→40, 40→41, 41→42** — PASS;
- completeness corrections — **0**;
- Tamil remains **NOT VERIFIED**.

## Speech 3 Gate-E result

Gate E is **PASS / COMPLETE**.

- scans **34–42 / printed pp.33–41**
- verified pages — **9/9**
- source-fidelity corrections — **3**
- unresolved readings — **0**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED** for modern 2007 typesetting; no historical-glyph anomaly found

Corrections:
- scan 37 — `கட்டுப்படுத்தவேண்டுமென்று`;
- scan 41 — source mixed-script spacing `D.H.O -வுக்கு`;
- scan 42 — `சிமெண்டு கட்டிப் பிடித்துக்கொண்டிருக்கிறது`.

All interventions, printed English, quoted-letter English terms, figures, dates and transitions passed after correction.

## Speech 3 Gate-F / Gate-G / Gate-H result

Speech 3 / 16.3.1960 is **RELEASED / CLOSED**.

- Gate F — complete 9/9;
- Gate G — PASS / COMPLETE, 17 refinements, 0 blockers, 0 Tamil changes;
- source-printed English — preserved exactly;
- English `verified_against_tamil=true`;
- Gate H — PASS / COMPLETE;
- canonical bilingual transcript — complete;
- root and machine-readable dated indexes — synchronized;
- Gate-H wording changes — 0.

## Speech 4 Gate-H closure

Canonical entry:

`speeches/1961/1961-03-06-financial-statement-debate/`

- scans **43–48 / 6 pages**
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 6/6**
- Gate G — **PASS / COMPLETE / 6 refinements / 0 blockers / 0 Tamil changes**
- source-printed English scan 48 — **preserved exactly**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — complete
- `translation.md` — retired pointer
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**

## Speech 5 Gate-H closure

Canonical entry:

`speeches/1962/1962-07-02-financial-statement-debate/`

- scans **49–59 / 11 pages**
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 11/11**
- Gate G — **PASS / COMPLETE / 11 refinements / 0 blockers / 0 Tamil changes**
- `பூவாங்க` / **Poovanga** — source-bound; no outside identification
- `தும்பை விட்டுவிட்டு வாலைப் பிடிக்கும்` / **thumbai** — conservative; no outside gloss
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — complete
- `translation.md` — retired pointer
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**

## Paired Gate-H closure

Speeches 4–5 are closed as one **17-page** activity.

- hard boundary **48→49** — preserved;
- Speech 4 source-printed English — verbatim;
- combined Gate-G state — **17/17 pages / 17 refinements / 0 blockers / 0 Tamil changes**;
- root README / anthology surfaces / machine-readable dated index — synchronized;
- no OCR, booklet pixels, web, Official Report or alternate anthology supplied English wording.

## Speech 6 durable Gate-H closure

Canonical entry:

`speeches/1963/1963-03-07-financial-statement-debate/`

- scans **60–75 / printed pp.59–74**
- Gates C–H — **COMPLETE**
- Tamil / English — **VERIFIED**
- release — **RELEASED / CLOSED**
- hard boundary **75→76** — preserved

## Speech 7 durable Gate-H closure

Canonical entry:

`speeches/1964/1964-03-07-financial-statement-debate/`

- scans **76–89 / printed pp.75–88**
- Gate C — **COMPLETE / 14 of 14**
- Gate D — **PASS / COMPLETE / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / 19 source-fidelity corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**
- Gate F — **COMPLETE / 14 of 14 English pages**
- Gate G — **PASS / COMPLETE / 16 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — complete
- `translation.md` — retired pointer
- root / machine-readable dated indexes — synchronized
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- hard boundaries **75→76** and **89→90** — preserved
- Speech 8 is now the active unit; Gates C–E are complete and Tamil is verified

No OCR, scan pixels, web research, Official Reports or alternate anthologies supplied English wording.

## Speech 8 durable Gate-E state

Working entry:

`speeches/1966/1966-03-04-financial-statement-debate/`

Source:

- global scans **90–112 / printed pp.89–111**
- split 004 local pages **15–25** = global scans **90–100**
- split 005 local pages **1–12** = global scans **101–112**
- split 005 local page **13** / global scan 113 begins Speech 9

Gate state:

- Gate C — **COMPLETE / 23 of 23 pages**
- source markers — **90→112 exactly once and in order**
- Gate D — **PASS / COMPLETE / retrospectively amended to 1 completeness correction**
- Gate-E retrospective note — scan 90 restored omitted **`விந்தையாக இருக்கிறது,`**
- Gate E — **PASS / COMPLETE / 23 of 23 pages / 43 source-fidelity corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**
- English — **NOT STARTED / Gate F exact next**
- hard boundaries **89→90** and **112→113** — preserved
- outside wording — **none**

No OCR, web copy, Official Report or alternate anthology supplied Tamil wording.

## Exact next activity

Perform **Speech 8 / 4.3.1966 — Gate F English first-pass translation**, scans **90–112 / 23 pages**, using only the final Gate-E-verified Tamil.

Do not begin Gate G or Speech 9 in the same iteration. Do not reopen released Speeches 1–7 merely for stylistic polishing.
