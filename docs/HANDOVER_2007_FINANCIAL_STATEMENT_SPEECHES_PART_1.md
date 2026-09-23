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

Latest released unit: Speech 9 / 29.3.1971 = **RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Speech 9 closed with **4 Gate-E corrections / 11 Gate-G refinements / 0 blockers / 0 Tamil changes / 0 Gate-H wording changes** and remains an independent parallel witness to `நமது நிலை`. Speeches 1–9 are now released. Speech 10 / 29.6.71 has **Gate C COMPLETE across all 35 pages**; Tamil is **TRANSCRIBED / NOT VERIFIED** with `verified_against_scan=false`.

## Existing-source overlaps

Do not modify released or existing source layers merely because this anthology overlaps them.

- Speech 9 / 29.03.1971 — overlaps the `நமது நிலை` event/provenance record.
- Speech 10 / 29.06.1971 — overlaps the `நமது விளக்கம்` event/provenance record.
- Speech 12 / 07.03.1973 — parallel witness to the already released canonical `1973-03-07-financial-statement-reply`.

Treat this 2007 anthology as its own witness.

## Current gates

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / COMPLETE / LOCKED**
- Gate C — **Speeches 1–15 COMPLETE; Speech 16 IN PROGRESS / Batch 1 COMPLETE / 10 of 33; speeches 17–19 not started**
- Gate C.5 — **N/A / CLOSED for Speeches 1–15**
- Gate D — **PASS / COMPLETE for Speeches 1–15**
- Gate E — **PASS / COMPLETE / Tamil VERIFIED for Speeches 1–15; speeches 16–19 not started**
- Gate F — **COMPLETE for Speeches 1–15; speeches 16–19 not started**
- Gate G — **PASS / COMPLETE / English VERIFIED for Speeches 1–15; speeches 16–19 not started**
- Gate H — **Speeches 1–15 PASS / COMPLETE — RELEASED / CLOSED; speeches 16–19 not started**
- Speech 12 parallel-witness protection — **ACTIVE / released `1973-03-07-financial-statement-reply` unchanged**
- Speech 13 — **RELEASED / CLOSED / indexed / canonical bilingual complete**
- Speech 14 — **RELEASED / CLOSED / indexed / canonical bilingual complete**
- Speech 15 — **Gate H PASS / COMPLETE — RELEASED / CLOSED / indexed / canonical bilingual complete**
- Speech 16 — **Gate C IN PROGRESS / 10 of 33 / Tamil NOT VERIFIED**
- speeches 17–19 — **NOT STARTED**

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
- Gate E — **READY / NOT STARTED**
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
- Speech 8 is **RELEASED / CLOSED through Gate H**; Speech 9 is the next active unit as a parallel witness

No OCR, scan pixels, web research, Official Reports or alternate anthologies supplied English wording.

## Speech 8 durable Gate-H closure

Canonical entry:

`speeches/1966/1966-03-04-financial-statement-debate/`

- scans **90–112 / printed pp.89–111**
- Gate D — **PASS / COMPLETE / retrospectively amended to 1 completeness correction**
- Gate E — **PASS / COMPLETE / 43 corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / 23/23**
- Gate G — **PASS / COMPLETE / 16 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — complete
- `translation.md` — retired pointer
- root / machine-readable indexes — synchronized
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- boundaries **89→90** and **112→113** — preserved


## Speech 9 durable Gate-H closure

Working entry:

`speeches/1971/1971-03-29-financial-statement-debate/`

- source label/date — `உரை : 9 / 29.3.1971`
- source split — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_005_pages_101-125.pdf`
- split SHA-256 — `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`
- local pages **13–16** = global scans **113–116**
- printed pages **112–115**
- Gate C — **COMPLETE / 4 of 4 pages**
- source markers **113→116** — exactly once and in order
- first-pass unresolved readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE — 4/4 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 4/4 pages; 4 source-fidelity corrections; 0 unresolved readings**
- Gate F — **COMPLETE / 4 of 4 English pages**
- Gate G — **PASS / COMPLETE — 4/4 pages / 11 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- root / `data/speeches.json` — **synchronized**
- hard boundaries **112→113** and **116→117** — preserved
- scan 117 visually confirmed as `உரை : 10 / நாள் : 29.6.71` and excluded
- parallel-witness rule — the 2007 anthology is independent of `நமது நிலை`; no earlier-source wording was copied, merged, normalised or used to repair this first pass
- no OCR, web, Official Report or alternate anthology supplied wording

Gate C retained first-pass source readings for later same-scan verification. Gate E corrected scan 115 to `அதன் மூலமாக எல்லாவிதமான ஹீட்டும் குறையும்.` directly from the anthology pixels; scan 116 `அவைகளை யெல்லாம்` was confirmed exactly as printed. No cross-witness correction was used.

## Speech 9 Gate-D result

- Gate D — **PASS / COMPLETE — 4/4 pages**
- completeness corrections — **0**
- markers **113→116** — unique and ordered
- transitions **113→114 / 114→115 / 115→116** — PASS
- hard boundaries **112→113 / 116→117** — PASS
- scan-115 source-printed repetition — retained, not treated as a transcription duplication
- Tamil wording changes at Gate D — **0**
- Tamil state at Gate D — **TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- parallel-witness / no-overwrite rule — preserved

## Speech 9 Gate-E result

- Gate E — **PASS / COMPLETE — 4/4 pages**
- source-fidelity corrections — **4**
- scan 114 — **2 corrections**
- scan 115 — **2 corrections**
- unresolved readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED**
- scan-115 source-printed repetition — confirmed and retained
- scan-116 `அவைகளை யெல்லாம்` — confirmed exactly as printed
- outside-witness wording imported — **0**
- parallel-witness / no-overwrite rule — preserved

Gate-E correction summary:

1. `புறக்கணிப்பட்டுக்கூடாது` → `புறக்கணிப்படக்கூடாது`
2. `பார்த்துக் கொள்வதற்கும்;` → `பார்த்து கொள்வதற்கும்,`
3. `பயிரிடப்படுவதில்லை` → `பயிரிடப்போவதில்லை`
4. `வீட்டும்` → `ஹீட்டும்`

## Speech 9 Gate-F result

- Gate F — **COMPLETE / 4/4 English pages**
- translation authority — final Gate-E-verified Tamil only
- blocking translation questions — **0**
- verified-Tamil changes — **0**
- source-page sequence **113→116** — preserved
- scan-115 source-printed repetition — retained in English
- `‘சன்பிளவர்’` — **‘Sunflower’**
- verified `ஹீட்டும்` — **heat**, without outside medical gloss
- `முன்னேற்றக் கழகம்` — **Munnetra Kazhagam**, not expanded through another witness
- `சதர்ன் ஸ்ட்ரக்சரல்ஸ்` — **Southern Structurals**
- outside / `நமது நிலை` English imported — **0**
- English — **VERIFIED AGAINST TAMIL**
- `verified_against_tamil=true`

## Speech 9 Gate-G result

- Gate G — **PASS / COMPLETE — 4/4 pages**
- refinements — **11**
- blocking fidelity issues — **0**
- verified-Tamil changes — **0**
- English source-page sequence **113→116** — PASS
- scan-115 source-printed repetition — retained twice
- conservative source-bound terms — PASS
- outside / `நமது நிலை` English imported — **0**
- English — **VERIFIED AGAINST TAMIL**
- `verified_against_tamil=true`

The complete before → after ledger is in `translation-review.md`.

## Speech 9 Gate-H result

- Gate H — **PASS / COMPLETE**
- release — **RELEASED / CLOSED**
- canonical bilingual `transcript.md` — complete
- `translation.md` — retired to pointer
- verified Tamil markers **113→116** — preserved
- verified English sections **113→116** — preserved
- Gate-H wording changes — **0 Tamil / 0 English**
- hard boundaries **112→113 / 116→117** — preserved
- root dated index / `data/speeches.json` — synchronized
- existing `நமது நிலை` source layer — unchanged
- parallel-witness / no-overwrite rule — preserved

## Speech 10 durable Gate-H closure

Working entry: `speeches/1971/1971-06-29-financial-statement-debate/`

Locked unit: **117–151 / printed 116–150 / 35 pages**.

Final state:

- Tamil Gates C–E — **COMPLETE / VERIFIED**
- `verified_against_scan=true`
- Gate F — **COMPLETE / 35 of 35 English pages**
- Gate G — **PASS / COMPLETE / 21 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- root / `data/speeches.json` — **SYNCHRONIZED**
- independent `நமது விளக்கம்` parallel witness — **PRESERVED**

## Speech 11 durable Gate-H closure

Canonical entry: `speeches/1972/1972-03-10-financial-statement-debate/`

Locked unit: **152–190 / printed 151–189 / 39 pages**.

Final state:

- Tamil Gates C–E — **COMPLETE / VERIFIED**
- `verified_against_scan=true`
- Gate F — **COMPLETE / 39 of 39 English pages**
- Gate G — **PASS / COMPLETE / 23 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- root / `data/speeches.json` — **SYNCHRONIZED**

## Speech 12 durable Gate-H closure

Canonical anthology entry: `speeches/1973/1973-03-07-financial-statement-debate/`

Locked unit: **191–230 / printed 190–229 / 40 pages**.

Controlling coverage:

- part008 local 16–25 = scans 191–200 — **10 pages** — SHA-256 `a7e186a1f4f415410d462f39f50c75475a27ef3d1c386a8cf557ef39701dab47`
- part009 local 1–25 = scans 201–225 — **25 pages** — SHA-256 `fe1df9ca2d41fd52219cd1fc97d0b6036f69b08aaad022ba2135c599088c40a7`
- part010 local 1–5 = scans 226–230 — **5 pages** — SHA-256 `257b862a7ebe21d768f8e5a2f2d2f9e8bb6c4e7ca7f704800a6453f40d0a9b90`
- total — **40/40 COMPLETE**

Final state:

- hard boundaries **190→191 / 230→231 — PASS**
- Tamil source markers **191→230 — 40/40 / exactly once / ordered**
- Gate C — **COMPLETE / 40 of 40**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE / 40 of 40 / 39 of 39 transitions / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / 40 of 40**
- Gate-E ledger — **25 correction entries / 30 correction occurrences**
- unresolved readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / 40 of 40**
- Gate G — **PASS / COMPLETE / 40 of 40 / 12 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual `transcript.md` — **COMPLETE**
- English source-page sections **191→230 — 40/40 / ordered**
- `translation.md` — **retired to released pointer**
- Gate-H wording changes — **0 Tamil / 0 English**
- source-printed English changes — **0**
- scan 222 repeated cinema sentence — **preserved twice**
- scan 228→229 poem — **preserved**
- release — **RELEASED / CLOSED**
- outside wording imported — **0**

Parallel-witness/index treatment:

- separately released same-date record — `speeches/1973/1973-03-07-financial-statement-reply/`
- relationship — **INDEPENDENT PARALLEL WITNESS / NO OVERWRITE / NO NORMALIZATION**
- same-date released record — **UNCHANGED**
- `data/speeches.json` — **UNCHANGED INTENTIONALLY**
- root dated speech table — **UNCHANGED INTENTIONALLY**
- reason — the repository's dated machine-readable index currently has one canonical entry per date; a second `1973-03-07` entry was not created. The released anthology witness remains discoverable through the anthology package and repository status sections.

## Speech 13 durable release state

Canonical entry:

`speeches/1974/1974-03-14-financial-statement-debate/`

- `உரை : 13 / 14.03.1974`
- scans **231–262 / printed pp.230–261 / 32 pages**
- Tamil / English — **VERIFIED**
- Gates C–H — **COMPLETE**
- release — **RELEASED / CLOSED**
- canonical bilingual transcript — **COMPLETE**
- Gate-H wording changes — **0 Tamil / 0 English**
- indexed — **YES**

## Speech 14 — Tamil Gates C–E COMPLETE / VERIFIED

Working entry:

`speeches/1975/1975-03-10-financial-statement-debate/`

Mapped unit:

- source label/date — `உரை : 14 / 10.03.1975`
- scans **263–319 / printed pp.262–318 / 57 pages**
- hard start boundary — **262→263 PASS / visually reconfirmed**
- hard end boundary — **319→320 PASS / visually reconfirmed from part013 local 19→20**
- scan 320 — **உரை : 15 / நாள் : 03.08.1977 / excluded from Speech 14**

Controlling split coverage:

- part011 local **13–25 = scans 263–275**
  - SHA-256 — `27c9c96d3c0bdb53480f8d1634300bf9d7dc57be17d3f83c66397ef78863712d`
- part012 local **1–25 = scans 276–300**
  - SHA-256 — `2010012bd354bc4f9354d0d547097c6ae9b2c2a7eb225d854018ebc482173cdc`
- part013 local **1–19 = scans 301–319**
  - SHA-256 — `26f0a480bf6c7b6f3f8638aadc77d0528f15b61def73937fad1627060f31c61b`

Tamil gate state:

- Gate C — **COMPLETE / 57 of 57**
- source markers — **263→319 / 57 / exactly once / ordered**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE — 57/57 pages; 56/56 internal transitions; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 57/57**
- Gate-E verified range — **263–319 / printed 262–318**
- Gate-E corrections — **32 entries / 32 occurrences**
- Gate-E affected scans — **20**
- unresolved readings — **0**
- final scan 319 close — **verified through `வணக்கம்.`**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- source-printed English — **preserved**
- outside wording imported — **0**

Gate-E final Batch 6:

- scans **313–319 / printed pp.312–318 / 7 pages**
- status — **PASS / STRICTLY VERIFIED**
- corrections — **2 entries / 2 occurrences**
- affected scan — **313**
- scan 313 — `போராட்டம் ஆரம்பித்தது இப்போது, ஆனால்` → `போராட்டம் ஆரம்பித்தது இப்போது; ஆனால்`
- scan 313 — `Rajamannar Committee’s` → `Rajammannar Committee’s`
- source-visible oddities retained where printed, including `Soverign`, `முதலவர்`, `Gujaritis`, `Beharies`, and scan-319 `அச்சாரமாக`

Downstream:

- Gate F / English — **COMPLETE — scans 263–319 / 57 of 57 translated / 0 blockers / verified_against_tamil=false**
- Gate G — **PASS / COMPLETE — scans 263–319 / 57 of 57 reviewed / 23 cumulative refinements / 0 blockers / 0 Tamil changes / 0 source-printed-English changes / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- canonical bilingual `transcript.md` — **COMPLETE**
- `translation.md` — **retired pointer**
- `data/speeches.json` / root dated table — **indexed**
- Gate-H wording changes — **0 Tamil / 0 English**
- Speech 15 — **Gate H PASS / COMPLETE — RELEASED / CLOSED**

## Gate F closure — Batches 1–3 COMPLETE

- translation authority — **Gate-E-verified Tamil only**
- translated scans — **263–319 / printed pp.262–318**
- translated pages — **57/57**
- Batch 1 — **263–287 / 25 pages / COMPLETE**
- Batch 2 — **288–312 / 25 pages / COMPLETE**
- Final Batch 3 — **313–319 / 7 pages / COMPLETE**
- source-page sequence — **263→319 / 57 sections / exactly once / ordered**
- blocking translation questions — **0**
- verified-Tamil changes — **0**
- outside English / outside-witness wording imported — **0**
- source-printed English — **preserved verbatim**
  - scans **313–314** — Jayaprakash Narayan / autonomy quotation
  - scans **316–317** — DMK Parliament quotation
  - scans **317–318** — 1942 CPI-resolution quotation
  - scan **318** — A.I.C.C. 8th August Resolution 1942 quotation
- English — **TRANSLATED / NOT VERIFIED AGAINST TAMIL**
- `verified_against_tamil=false`
- working file — `translation.md`
- review ledger — `translation-review.md`

## Gate G closure — COMPLETE / 57 of 57

- fidelity authority — **Gate-E-verified Tamil only**
- reviewed scans — **263–319 / printed pp.262–318 / 57 pages**
- Batch 1 — **263–287 / 25 pages / PASS / 6 refinements**
- Batch 2 — **288–312 / 25 pages / PASS / 12 refinements**
- Final Batch 3 — **313–319 / 7 pages / PASS / 5 refinements**
- cumulative English refinements — **23**
- blocking fidelity issues — **0**
- verified-Tamil changes — **0**
- source-printed-English changes — **0**
- outside English / other-witness wording imported — **0**
- source-page sequence — **263→319 / 57 sections / exactly once / ordered**
- source-printed English — **verified verbatim throughout**
- final scan 319 close — **verified through `Vanakkam.`**
- Tamil — **VERIFIED / verified_against_scan=true**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **READY / NOT STARTED**
- Speech 15 — **Gate H PASS / COMPLETE — RELEASED / CLOSED**

Batch-2 refinements are recorded in `translation-review.md` on pages **290, 291, 293, 294, 296, 297, 298, 300, 301, 302, 303, 306**.

Final-Batch refinements are recorded in `translation-review.md` on pages **313, 314, 317, 319**; page **317** has two separate refinements.

## Gate H closure — PASS / COMPLETE / RELEASED

- canonical bilingual record — **COMPLETE**
- Tamil source-page markers — **263→319 / 57/57 / exactly once / ordered**
- English source-page sections — **263→319 / 57/57 / exactly once / ordered**
- Tamil — **VERIFIED / verified_against_scan=true**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate-E corrections — **32 entries / 32 occurrences**
- Gate-G refinements — **23**
- Gate-G blockers — **0**
- Gate-H wording changes — **0 Tamil / 0 English**
- source-printed English — **preserved verbatim**
- hard boundaries — **262→263 PASS / 319→320 PASS**
- final closes — **Tamil `வணக்கம்.` / English `Vanakkam.`**
- `translation.md` — **retired to released pointer**
- `data/speeches.json` — **indexed**
- root dated speech table — **indexed**
- release — **RELEASED / CLOSED**

## Speech 15 Gate-H closure — PASS / COMPLETE / RELEASED

- working entry — `speeches/1977/1977-08-03-financial-statement-debate/`
- source label/date — **உரை : 15 / 03.08.1977**
- scans — **320–355 / printed pp.319–354 / 36 pages**
- boundaries — **319→320 PASS / 355→356 PASS**
- Tamil source markers — **320→355 / 36/36 / exactly once / ordered**
- English source sections — **320→355 / 36/36 / exactly once / ordered**
- Gate C — **COMPLETE**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE**
- Gate E — **PASS / COMPLETE / 53 corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / 36 of 36**
- Gate G — **PASS / COMPLETE / 36 of 36 / 6 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- canonical bilingual `transcript.md` — **COMPLETE**
- `translation.md` — **retired release pointer**
- `translation-review.md` — **COMPLETE**
- Gate-H wording changes — **0 Tamil / 0 English**
- `data/speeches.json` — **indexed**
- root dated speech table — **indexed**
- Speech 16 — **Gate C IN PROGRESS / Batch 1 COMPLETE / 10 of 33 / Tamil NOT VERIFIED**

## Speech 16 active Gate-C state

Canonical entry:

`speeches/1978/1978-03-01-financial-statement-debate/`

- source label/date — **உரை : 16 / 1.3.1978**
- scans — **356–388 / printed pp.355–387 / 33 pages**
- incoming boundary **355→356** — **PASS / visually reconfirmed**
- outgoing boundary **388→389** — **PASS / visually reconfirmed**
- part015 local **6–25 = scans 356–375** — SHA-256 `cc81c3d6e9496012e10a39f2a0ad3666d522f9a7b2b58f25f484a7f5a3682344`
- part016 local **1–13 = scans 376–388** — SHA-256 `cc1067f556825a36fd7558316df12ed09ca92e498374e9b23d1ebb7a2aa28e47`
- source coverage — **33/33 COMPLETE / no gap / no overlap**
- Gate C Batch 1 — **COMPLETE / scans 356–365 / 10 pages**
- marker sequence — **356→365 / exactly once / ordered**
- unresolved first-pass readings — **0**
- source-visible oddities retained — scan 362 `183,85`; scan 363 `கட்டப்பட்ட விருக்கின்றன`
- Tamil — **TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C.5 / D / E / F / G / H — **NOT STARTED**
- Speech 17 — **NOT STARTED**

## Exact next activity — Speech 16 Gate C Batch 2

Process **scans 366–375 / printed pp.365–374 / exactly 10 source pages** from part015 local pages **16–25**.

Use only rendered controlling anthology pixels. Preserve source wording, punctuation, numerals, printed English, labels and visible repetition. Do not exceed 10 Gate-C pages and do not begin downstream gates in the same activity.
