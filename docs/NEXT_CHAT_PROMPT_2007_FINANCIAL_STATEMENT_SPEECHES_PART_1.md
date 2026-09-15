# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speeches 4–5 Gate H

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Whole-speech batching policy

Maximum **25 source-scan pages per activity**, preserving complete speech units.

Current batch:

- Speech 4 / 6.3.1961 — **6 pages / scans 43–48**
- Speech 5 / 2.7.1962 — **11 pages / scans 49–59**
- total — **17 pages**
- Speech 6 / 7.3.1963 — deferred

## Durable state

### Speech 4
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 6 of 6 English pages**
- Gate G — **PASS / COMPLETE — 6/6 pages**
- Gate-G refinements — **6**
- blockers — **0**
- verified-Tamil changes — **0**
- source-printed English scan 48 — **preserved verbatim**
- English `verified_against_tamil=true`
- Gate H — **NOT STARTED / next**

### Speech 5
- Tamil Gates C–E — **COMPLETE / VERIFIED**
- Gate F — **COMPLETE / 11 of 11 English pages**
- Gate G — **PASS / COMPLETE — 11/11 pages**
- Gate-G refinements — **11**
- blockers — **0**
- verified-Tamil changes — **0**
- `பூவாங்க` — **Poovanga**, no outside identification
- `தும்பை விட்டுவிட்டு வாலைப் பிடிக்கும்` — conservative **thumbai** rendering, no outside gloss
- English `verified_against_tamil=true`
- Gate H — **NOT STARTED / next**

Combined Gate-G state: **17/17 pages / 17 refinements / 0 blockers / 0 Tamil changes**.

## Gate-G authority rule

Gate G used only:

- final Gate-E-verified Tamil;
- Gate-F English.

No OCR, booklet pixels, web research, Official Reports or alternate anthologies supplied English wording.

## Exact next activity

Perform **Gate H canonical merge / index / release closure for both Speech 4 and Speech 5**.

Requirements:

1. inspect the established Gate-H release convention already used for Speeches 1–3;
2. do not reopen or rewrite verified Tamil or Gate-G English unless a concrete internal inconsistency is found;
3. merge verified Tamil followed by verified English into each canonical `transcript.md`;
4. retire each `translation.md` to a pointer to canonical English;
5. preserve Speech 4 source-printed English exactly;
6. preserve the hard speech boundary **48→49**;
7. preserve Speech 5 conservative **Poovanga** / **thumbai** renderings without outside identification or gloss;
8. synchronize `metadata.json`, speech READMEs, source notes, verification logs, anthology README/mapping, handover, root README and machine-readable dated index;
9. add dated index entries for **1961-03-06** and **1962-07-02** according to repository convention;
10. if all closure checks pass, mark both **Gate H PASS / COMPLETE — RELEASED / CLOSED**;
11. do **not** begin Speech 6 in the same iteration.

Expected continuation after successful closure: **Speech 6 / 7.3.1963 — next whole-speech batch**, subject to the ≤25-page policy.
