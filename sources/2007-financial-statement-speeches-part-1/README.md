# நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — பாகம் 1

This source package preserves the 2007 anthology **`நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`** as a new controlling source witness.

## Gate A — source preflight

Status: **PASS / COMPLETE**.

### Controlling scan

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- actual physical PDF pages: **546**
- file size: **393,027,493 bytes**
- SHA-256: `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- usable parsed text layer: **none**
- controlling textual authority: **rendered scan pixels**
- interface note: the file viewer exposed only the first 150 rendered pages, but the actual PDF contains 546 pages; the PDF byte-level page count controls.

### Publication evidence from the scan

- printed title: `நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`
- author attribution: `கலைஞர் மு. கருணாநிதி`
- publisher: `தமிழ்க்கனி பதிப்பகம்`, சென்னை - 600 004
- sales-rights imprint: `பூம்புகார் பதிப்பகம்`, 127 (ப.எண். 63), பிரகாசம் சாலை (பிராட்வே), சென்னை - 600 108
- first edition: **மே, 2007**
- printed price: **ரூ. 300/-**
- rights: **ஆசிரியருக்கே**
- printer / binder: **Eagle Press, Chennai - 600 013**

### Physical structure

- scans **1–17** — publication/front matter and internal title matter;
  - scan 1 — cover;
  - scan 2 — title/publisher page;
  - scan 3 — edition/price/printer page;
  - scans 4–9 — `என்னுரை`;
  - scans 10–14 — `பதிப்புரை`;
  - scans 15 and 17 — blank/verso leaves with heavy reverse show-through; no new speech body admitted;
  - scan 16 — internal section title;
- scans **18–545** — 19 numbered `உரை` units;
- scan **546** — closing portrait/back matter.

From scan 18 through scan 545, the printed-page relation is stable:

`printed page = PDF scan page - 1`.

### Source condition

The scan is image-only. Most speech pages are readable at source resolution. There is intermittent bleed-through and library stamping/handwriting that must be distinguished from printed text. The 2007 anthology is modern typesetting despite reprinting historical speeches; Gate C.5 historical-glyph review is therefore **provisionally N/A for this edition**, subject to reopening if a page-specific legacy typeform anomaly is actually encountered.

## Gate B — anthology structural mapping

Status: **PASS / COMPLETE / LOCKED**.

All **19** printed speech units were mapped and then boundary-rechecked. See:

[`mapping.md`](./mapping.md)

Speeches **1–11 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Speech 12 / 07.03.1973 is established separately at `speeches/1973/1973-03-07-financial-statement-debate/` as an **independent parallel witness** to the already released `1973-03-07-financial-statement-reply`. Speech 12 Gate C is **COMPLETE / 40 of 40**; Gate C.5 is **N/A / CLOSED**; Gate D is **PASS / COMPLETE / 40 of 40 / 0 completeness corrections**; Gate E is **PASS / COMPLETE / 40 of 40 — 25 correction entries / 30 correction occurrences / 0 unresolved**. Tamil is **VERIFIED** with `verified_against_scan=true`. Gate F is **COMPLETE / 40 of 40**; English is **TRANSLATED / NOT VERIFIED AGAINST TAMIL** with `verified_against_tamil=false`; Gate G is next.

## Whole-speech batching policy

For ongoing anthology processing, use a **maximum of 25 source-scan pages per activity**.

- process only **complete speech units**;
- add consecutive speeches while the cumulative source-page count remains **≤25**;
- **never split a speech** merely to fill the page allowance;
- if the next complete speech would push the activity above 25 pages, defer that **entire speech** to the next activity;
- if a single speech itself exceeds 25 pages, process it separately as one intact speech unit rather than splitting or dropping it.

Speech 7 Gate C used the user-supplied 25-page split covering global scans 76–100. Local pages 1–14 map to global scans **76–89**; local page 15 / scan 90 begins Speech 8 and remains excluded.

## Parallel-witness / released-material rule

This anthology contains dates already represented elsewhere in the repository:

- **29.03.1971 / உரை 9** overlaps the existing `நமது நிலை` event/provenance record;
- **29.06.1971 / உரை 10** overlaps the existing `நமது விளக்கம்` event/provenance record;
- **07.03.1973 / உரை 12** overlaps the already **RELEASED** canonical entry `1973-03-07-financial-statement-reply`.

These are separate source witnesses. Do **not** overwrite or silently normalize any previously released canonical Tamil/English from this 2007 anthology. Any overlap must be handled explicitly as parallel-witness evidence.

## Speech 1 current state

Reader/work entry:

[`../../speeches/1958/1958-03-05-financial-statement-debate/`](../../speeches/1958/1958-03-05-financial-statement-debate/)

- Gate C — **COMPLETE / 7 of 7 pages**
- source markers — **18→24 exactly once in first-pass transcript**
- unresolved first-pass readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate D — **PASS / COMPLETE — 7/7 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 7/7 pages; 9 source-fidelity corrections; 0 unresolved readings**
- Gate F English — **COMPLETE / 7 of 7 pages**
- Gate G — **PASS / COMPLETE — 7/7 pages; 10 refinements; 0 blockers**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- Speech 1 release — **RELEASED / CLOSED**

## Speech 1 Tamil verification closure

Gate C and Gate D remain complete. Gate E is **PASS / COMPLETE — 7/7 pages**.

- Gate-E source-fidelity corrections — **9**
- unresolved readings — **0**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED for this modern 2007 typesetting; no legacy-glyph anomaly observed**

Correction sites: scan 19 ×2, scan 20 ×4, scan 23 ×1, scan 24 ×2. Full details are in the speech `verification-log.md`.

## Gate F / Gate G closure for Speech 1

Gate F is **COMPLETE — 7/7 pages**.

Gate G is **PASS / COMPLETE — 7/7 pages**:

- English refinements — **10**
- blocking fidelity issues — **0**
- verified-Tamil changes — **0**
- English `verified_against_tamil=true`
- outside wording — **none**

The detailed Gate-G ledger is in `speeches/1958/1958-03-05-financial-statement-debate/translation-review.md`.

## Speech 1 Gate H closure

**PASS / COMPLETE — RELEASED / CLOSED.**

Canonical bilingual transcript and repository indexes are synchronized. No verified wording changed during Gate H.

## Speech 2 current state

Reader/work entry:

[`../../speeches/1959/1959-03-04-financial-statement-debate/`](../../speeches/1959/1959-03-04-financial-statement-debate/)

- Gate C — **COMPLETE / 9 of 9 pages**
- source markers — **25→33 exactly once**
- unresolved first-pass readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED for Speech 2**
- Gate D — **PASS / COMPLETE — 9/9 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 9/9 pages; 6 source-fidelity corrections; 0 unresolved readings**
- Gate F English — **COMPLETE / 9 of 9 pages**
- Gate G — **PASS / COMPLETE — 9/9 pages; 12 refinements; 0 blockers**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- Speech 2 release — **RELEASED / CLOSED**

## Speech 2 Gate D result

**PASS / COMPLETE — 9/9 pages; 0 completeness corrections.**

Markers 25→33 are unique/ordered; start/end boundaries, the scan-26 intervention, quotations, figures and all page transitions are structurally complete. Tamil remains not verified.

## Speech 2 Gate E closure

**PASS / COMPLETE — 9/9 pages; Tamil VERIFIED.**

Gate E applied **6 source-fidelity corrections** with **0 unresolved readings**. Full correction details are in the Speech 2 verification log.

## Speech 2 Gate F / Gate G / Gate H closure

- Gate F — **COMPLETE / 9 of 9 pages**
- Gate G — **PASS / COMPLETE / 12 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- release — **RELEASED / CLOSED**

Canonical bilingual transcript and dated indexes are synchronized. Full English audit: `speeches/1959/1959-03-04-financial-statement-debate/translation-review.md`.

## Speech 3 current state

Reader/work entry:

[`../../speeches/1960/1960-03-16-financial-statement-debate/`](../../speeches/1960/1960-03-16-financial-statement-debate/)

- Gate C — **COMPLETE / 9 of 9 pages**
- source markers — **34→42 exactly once**
- unresolved first-pass readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED for Speech 3**
- Gate D — **PASS / COMPLETE — 9/9 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 9/9 pages; 3 source-fidelity corrections; 0 unresolved readings**
- Gate F English — **COMPLETE / 9 of 9 pages**
- Gate G — **PASS / COMPLETE — 9/9 pages; 17 refinements; 0 blockers**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- Speech 3 release — **RELEASED / CLOSED**

Gate C preserved the C. Subramaniam intervention, J. Madhava Gowder intervention, Deputy Speaker interventions including printed English, the quoted letter with embedded English administrative terms, figures, humour and page-spanning continuations.

## Speech 3 Gate D result

**PASS / COMPLETE — 9/9 pages; 0 completeness corrections.**

Markers 34→42 are unique/ordered; start/end boundaries, all speaker interventions, printed-English blocks, quoted-letter structure, figures and all page transitions are structurally complete. Tamil remains not verified.

## Speech 3 Gate E closure

**PASS / COMPLETE — 9/9 pages; Tamil VERIFIED.**

Gate E applied **3 source-fidelity corrections** with **0 unresolved readings**. Full details are in the Speech 3 verification log.

## Speech 3 Gate F / Gate G / Gate H closure

- Gate F — **COMPLETE / 9 of 9 pages**
- Gate G — **PASS / COMPLETE / 17 refinements / 0 blockers / 0 Tamil changes**
- source-printed English — **preserved exactly**
- English — **VERIFIED AGAINST TAMIL**
- Gate H — **PASS / COMPLETE**
- release — **RELEASED / CLOSED**

Canonical bilingual transcript and dated indexes are synchronized. Full English audit: `speeches/1960/1960-03-16-financial-statement-debate/translation-review.md`.

## Speech 4 Gate-H closure

**PASS / COMPLETE — RELEASED / CLOSED.**

- scans **43–48 / 6 pages**
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 6 of 6 English pages**
- Gate G — **PASS / COMPLETE — 6 refinements / 0 blockers / 0 Tamil changes**
- source-printed English scan 48 — **preserved verbatim**
- Gate H — **PASS / COMPLETE**
- canonical bilingual `transcript.md` — complete
- `translation.md` — retired pointer
- release — **RELEASED / CLOSED**

## Speech 5 Gate-H closure

**PASS / COMPLETE — RELEASED / CLOSED.**

- scans **49–59 / 11 pages**
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 11 of 11 English pages**
- Gate G — **PASS / COMPLETE — 11 refinements / 0 blockers / 0 Tamil changes**
- `பூவாங்க` — **Poovanga**, no outside identification
- `தும்பை விட்டுவிட்டு வாலைப் பிடிக்கும்` — conservative **thumbai** rendering, no outside gloss
- Gate H — **PASS / COMPLETE**
- canonical bilingual `transcript.md` — complete
- `translation.md` — retired pointer
- release — **RELEASED / CLOSED**

## Speeches 4–5 Gate-H closure

The paired 17-page activity is **PASS / COMPLETE**.

- hard speech boundary **48→49** — preserved;
- canonical Tamil/English ranges — **43→48** and **49→59**, complete and ordered;
- cumulative Gate-G refinements — **17**;
- blocking fidelity issues — **0**;
- verified-Tamil changes — **0**;
- Gate-H verified-English wording changes — **0**;
- root dated index / `data/speeches.json` — synchronized;
- outside wording from OCR / booklet pixels / web / Official Reports / alternate anthologies — **none**.

## Speech 6 Gate-H closure

Reader/work entry:

[`../../speeches/1963/1963-03-07-financial-statement-debate/`](../../speeches/1963/1963-03-07-financial-statement-debate/)

- scans **60–75 / printed pp.59–74**
- Gates C–H — **COMPLETE**
- Tamil / English — **VERIFIED**
- release — **RELEASED / CLOSED**
- hard boundary **75→76** — preserved

## Speech 7 Gate-H closure

Reader/work entry:

[`../../speeches/1964/1964-03-07-financial-statement-debate/`](../../speeches/1964/1964-03-07-financial-statement-debate/)

- source label/date — `உரை : 7 / 7.3.1964`
- scans **76–89 / printed pp.75–88**
- Gates C–E — **COMPLETE / Tamil VERIFIED**
- Gate E — **19 source-fidelity corrections / 0 unresolved**
- Gate F — **COMPLETE / 14 of 14 English pages**
- Gate G — **PASS / COMPLETE / 16 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual `transcript.md` — complete
- `translation.md` — retired pointer
- root dated index / `data/speeches.json` — synchronized
- hard boundaries **75→76** and **89→90** — preserved
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- outside wording — **none**

## Speech 8 Gate-H closure

Reader/work entry:

[`../../speeches/1966/1966-03-04-financial-statement-debate/`](../../speeches/1966/1966-03-04-financial-statement-debate/)

- source label/date — `உரை : 8 / 4.3.1966`
- scans **90–112 / printed pp.89–111**
- Gate D — **PASS / COMPLETE / retrospectively amended to 1 completeness correction**
- Gate E — **PASS / COMPLETE / 43 corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / 23 of 23 English pages**
- Gate G — **PASS / COMPLETE / 16 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — complete
- `translation.md` — retired pointer
- root dated index / `data/speeches.json` — synchronized
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- boundaries **89→90** and **112→113** — preserved
- outside wording — **none**


## Speech 9 Gate-H closure

Reader/work entry:

[../../speeches/1971/1971-03-29-financial-statement-debate/](../../speeches/1971/1971-03-29-financial-statement-debate/)

- source label/date — `உரை : 9 / 29.3.1971`
- scans **113–116 / printed pp.112–115**
- Gate C — **COMPLETE / 4 of 4 pages**
- source markers — **113→116 exactly once and in order**
- first-pass unresolved readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate C.5 — **N/A / CLOSED — modern 2007 typesetting; no legacy-glyph anomaly found**
- Gate D — **PASS / COMPLETE — 4/4 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 4/4 pages; 4 source-fidelity corrections; 0 unresolved readings**
- Gate F — **COMPLETE / 4 of 4 English pages**
- Gate G — **PASS / COMPLETE — 4/4 pages; 11 refinements; 0 blockers; 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- hard boundaries **112→113** and **116→117** — preserved
- scan 117 visually confirmed as `உரை : 10 / நாள் : 29.6.71` and excluded
- relationship to `நமது நிலை` — **PARALLEL WITNESS / NO OVERWRITE**
- outside wording from OCR / web / Official Reports / `நமது நிலை` / alternate anthologies — **none**

Gate E corrected scan 115 directly from the anthology pixels to `அதன் மூலமாக எல்லாவிதமான ஹீட்டும் குறையும்.`; scan 116 `அவைகளை யெல்லாம்` was confirmed exactly as printed. The source-printed repeated two-sentence sequence on scan 115 remains retained. No cross-witness normalisation was used.

Gate F translated **4/4 pages** only from the final Gate-E-verified Tamil. Conservative source-bound forms include **Munnetra Kazhagam**, **‘Sunflower’**, **heat** for `ஹீட்டும்`, **Southern Structurals**, and the retained scan-115 repetition. Blocking questions: **0**. Tamil changes: **0**. No `நமது நிலை` English was imported.

Gate G reviewed all **4/4 pages** against the verified Tamil and applied **11 English refinements** with **0 blocking fidelity issues / 0 Tamil changes**. Source-page order, the scan-115 repetition, names, figures, `(Laughter).`, and all conservative source-bound choices remain intact.

English is **VERIFIED AGAINST TAMIL / verified_against_tamil=true**.

Gate H is **PASS / COMPLETE — RELEASED / CLOSED**. The canonical `transcript.md` now contains verified Tamil + verified English; `translation.md` is retired to a pointer; root and machine-readable dated indexes are synchronized. Gate-H wording changes: **0 Tamil / 0 English**. The `நமது நிலை` source layer remains unchanged.

## Speech 10 Gate-H closure

Working entry: `speeches/1971/1971-06-29-financial-statement-debate/`

Locked unit: **117–151 / printed 116–150 / 35 pages**.

Final state:

- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 35 of 35 English pages**
- Gate G — **PASS / COMPLETE / 21 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- root / machine-readable indexes — **SYNCHRONIZED**
- parallel witness to `நமது விளக்கம்` — **PRESERVED / NO OVERWRITE**

## Speech 11 Gate-H closure

Working entry: [`../../speeches/1972/1972-03-10-financial-statement-debate/`](../../speeches/1972/1972-03-10-financial-statement-debate/)

Locked unit: **152–190 / printed 151–189 / 39 pages**.

Final state:

- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 39 of 39**
- Gate G — **PASS / COMPLETE / 23 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- canonical bilingual transcript — **COMPLETE**
- `translation.md` — **retired pointer**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- root / machine-readable indexes — **SYNCHRONIZED**

## Speech 12 Gate-E closure

Working entry: [`../../speeches/1973/1973-03-07-financial-statement-debate/`](../../speeches/1973/1973-03-07-financial-statement-debate/)

Locked unit: **191–230 / printed 190–229 / 40 pages**.

- source coverage — **40/40 COMPLETE**
- hard boundaries **190→191 / 230→231 — PASS**
- Gate C — **COMPLETE / 40 of 40**
- source markers — **191→230 exactly once and in order**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE — 40/40 pages; 39/39 transitions; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 40/40 pages**
- correction ledger — **25 entries / 30 occurrences**
- unresolved readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- scan 222 source-visible repetition — **retained twice**
- scan 228→229 poem continuation — **confirmed / preserved**
- scan 230 final close — **confirmed**
- released `1973-03-07-financial-statement-reply` — **UNCHANGED**
- parallel-witness / no-overwrite / no-normalization rule — **PRESERVED**
- English / Gate F — **COMPLETE / 40 of 40 / TRANSLATED / NOT VERIFIED AGAINST TAMIL**
- Gate G — **NOT STARTED / next**
- Gate H — **NOT STARTED**

No OCR, web copy, Official Report, released 1973 wording, alternate anthology or another witness supplied Gate-E wording. Final before→after details are in the Speech 12 verification log and metadata.

## Exact next activity

Perform **Speech 12 Gate G strict English-vs-verified-Tamil review for all 40 pages / scans 191–230**. Record every refinement and blocker, keep verified Tamil unchanged unless a genuine source issue is found, and do not begin Gate H or Speech 13 in the same activity.
