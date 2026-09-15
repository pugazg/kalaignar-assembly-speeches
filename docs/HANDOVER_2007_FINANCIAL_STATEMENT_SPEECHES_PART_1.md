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

## Existing-source overlaps

Do not modify released or existing source layers merely because this anthology overlaps them.

- Speech 9 / 29.03.1971 — overlaps the `நமது நிலை` event/provenance record.
- Speech 10 / 29.06.1971 — overlaps the `நமது விளக்கம்` event/provenance record.
- Speech 12 / 07.03.1973 — parallel witness to the already released canonical `1973-03-07-financial-statement-reply`.

Treat this 2007 anthology as its own witness.

## Current gates

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / COMPLETE / LOCKED**
- Gate C — **Speech 1 COMPLETE — 7/7 pages, scans 18–24**
- Gate C.5 — **N/A / CLOSED for Speech 1**
- Gate D — **Speech 1 PASS / COMPLETE**
- Gate E — **Speech 1 PASS / COMPLETE / Tamil VERIFIED**
- Gate F — **Speech 1 COMPLETE — 7/7 English pages**
- Gate G — **Speech 1 PASS / COMPLETE — 7/7 pages; 10 refinements; 0 blockers; English VERIFIED**
- Gate H — **NOT STARTED**

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

## Exact next activity

Perform **Gate H canonical merge / index / release closure for Speech 1**. Do not begin Speech 2 in the same iteration.
