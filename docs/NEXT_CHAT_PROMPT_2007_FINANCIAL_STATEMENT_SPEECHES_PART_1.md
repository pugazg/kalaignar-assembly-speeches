# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 11 Gate H release closure

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

Speeches **1–10 are RELEASED / CLOSED through Gate H**.

Speech 11 / `10.3.1972` has completed Tamil Gates **C–E** and English Gates **F–G** across the intact **39-page** unit.

## Speech 11 durable state

- global scans — **152–190**
- printed pages — **151–189**
- page count — **39**
- hard boundaries — **151→152 PASS / 190→191 PASS**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **PASS / COMPLETE / 25 corrections / 0 unresolved**
- Gate F — **COMPLETE / 39/39**
- Gate G — **PASS / COMPLETE / 23 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- source-printed English — **preserved verbatim**
- Gate H / release — **NOT STARTED / NEXT / NOT RELEASED**

## Gate H exact activity

1. re-fetch live `main` before writing;
2. merge the complete Gate-G-verified English from `translation.md` into canonical `transcript.md` **after the verified Tamil**;
3. preserve verified Tamil source markers **152→190 exactly once and ordered**;
4. preserve English source-page sections **152→190 exactly once and ordered**;
5. make **0 Tamil / 0 English wording changes** unless a genuine release blocker is found and explicitly recorded;
6. preserve source-printed English verbatim and the source-bound historical/factual readings;
7. retire `translation.md` to the standard released pointer only after canonical bilingual merge validation passes;
8. preserve the Gate-F/G audit and append Gate-H closure to `translation-review.md`;
9. synchronize Speech-11 README/metadata/source-notes/verification-log, anthology README/mapping, handover/continuation prompt, root dated index and `data/speeches.json`;
10. verify hard boundaries **151→152 / 190→191** remain preserved;
11. if all release checks pass, set Gate H **PASS / COMPLETE**, release **RELEASED / CLOSED**, `release.released=true`, `release.release_ready=true`, `release.indexed=true`, and canonical bilingual transcript true;
12. commit atomically to `main` and re-fetch live main plus key files before claiming durability;
13. do **not** begin Speech 12 in the same activity.

Expected continuation after Gate H: **Speech 12 source-boundary / Gate-C setup**, beginning at scan **191 / printed page 190 / source date 07.03.1973**, using the locked anthology mapping and whole-speech batching policy.
