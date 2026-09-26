# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 17 Gate H archival/release audit

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–16 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Speech 17 state

Working entry:

`speeches/1979/1979-03-22-and-23-financial-statement-debate/`

Source:

- source label/date — **உரை : 17 / 22 & 23.3.1979**
- scans — **389–481 / printed pp.388–480 / 93 pages**
- source date status — **one continuous multi-date source unit**
- canonical single date — **not assigned**
- explicit internal date divider — **none found**
- hard boundaries **388→389 / 481→482 — PASS**
- scan **481** — **Speech 17 close / included**
- scan **482** — **Speech 18 / உரை : 18 / 09.07.1980 start / excluded**

Gate state:

- Gate C — **COMPLETE / 93 of 93**
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE**
- Gate E — **PASS / COMPLETE / 93 of 93 source-verified / 37 corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / 93 of 93 translated**
- Gate G — **PASS / COMPLETE / 93 of 93 reviewed**
- Gate-G batches — **389–418 / 419–448 / 449–478 / 479–481 FINAL**
- Gate-G refinements — **43 cumulative — 12 + 16 + 10 + 5**
- Gate-G blockers — **0**
- Gate-G verified-Tamil changes — **0**
- Gate-G source-printed-English changes — **0**
- Gate-G outside English imported — **0**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **READY / NOT STARTED / NOT RELEASED**
- Speech 18 — **NOT STARTED**

Final Gate-G remainder:

- scans **479–481 / exactly 3 pages**
- refinements — **5**
- **478→479** continuation — **PASS / preserved**
- **480→481** continuation — **restored / PASS**
- scan **481** source close / ornament — **PASS / preserved**
- source-visible `1-1-58க்குள்` — **preserved without normalization**
- English scans **389–478** changed in final-remainder activity — **0**

## Gate-H authority and safeguards

Gate H is an **archival/release audit**, not another translation or polishing pass.

- treat the Gate-E-verified Tamil and Gate-G-verified English in `transcript.md` as the authoritative bilingual pair;
- make no Tamil or English wording change unless a separate source-backed defect is discovered;
- preserve all **93 Tamil** and **93 English** source-page markers and page order;
- preserve source-printed English, speaker labels, interventions, figures, repetitions, source-bound oddities and source structure;
- preserve the source's single **multi-date unit** `22 & 23.3.1979`;
- do **not** invent an internal 22/23 March split;
- do **not** assign a single canonical date merely for indexing;
- preserve **481→482** as the hard Speech-17/Speech-18 boundary;
- import no wording from web, Official Reports, alternate anthologies, released speeches or other outside witnesses.

## Exact next activity

Perform **Speech 17 Gate H archival/release audit**.

Requirements:

1. audit the complete **93/93 Tamil + 93/93 English** source-page sequence and confirm exact ordered coverage **389→481**;
2. verify Tamil remains `verified_against_scan=true` and English remains `verified_against_tamil=true`;
3. verify the final **478→479 / 480→481** continuations and **481→482** terminal boundary;
4. verify scan 482 / Speech 18 content has not entered the Speech-17 record;
5. audit metadata, README, source notes, verification log, translation review and anthology mapping for the multi-date policy and Gate-G totals;
6. establish the canonical bilingual release form using the existing repository convention, including the standard `translation.md` release-pointer treatment if applicable;
7. synchronize repository/source-package/root status and any machine-readable index only in a way compatible with the multi-date/no-single-canonical-date policy — **do not invent a dated index entry**;
8. Gate-H wording changes should be **0 Tamil / 0 English** unless an independently source-backed defect is found and explicitly recorded;
9. if all checks pass, mark Speech 17 **Gate H PASS / COMPLETE — RELEASED / CLOSED**, canonical bilingual complete, while retaining the multi-date source-unit policy;
10. exact next after successful Gate-H closure: **Speech 18 source intake / Gate C setup — scans 482–510 / printed pp.481–509 / உரை : 18 / 09.07.1980**;
11. do not begin Speech 18 in the same activity.
