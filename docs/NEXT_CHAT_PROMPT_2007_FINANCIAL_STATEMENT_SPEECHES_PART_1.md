# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 10 Gate H release closure

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

Speeches **1–9 are RELEASED / CLOSED through Gate H**.

Speech 10 / `29.6.71` has completed Tamil Gates **C–E** and English Gates **F–G** across **35 source pages / scans 117–151**.

## Current Speech 10 state

- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **PASS / COMPLETE / 26 corrections / 0 unresolved**
- Gate F — **COMPLETE / 35 of 35**
- Gate G — **PASS / COMPLETE / 21 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H / release — **NOT STARTED / NEXT**

## Exact next activity

Perform **Speech 10 Gate H canonical bilingual merge / release readiness and index synchronization**.

Requirements:

1. merge the Gate-G-verified English from `translation.md` into the canonical `transcript.md` after the verified Tamil;
2. preserve Tamil source markers **117→151** exactly once and ordered;
3. preserve English sections **117→151** exactly once and ordered;
4. make **0 Tamil / 0 English wording changes** unless a genuine release blocker is found and explicitly recorded;
5. retire `translation.md` to the standard released pointer only after the canonical bilingual transcript is complete;
6. preserve `translation-review.md` as the Gate-F/G audit ledger;
7. verify hard source boundaries **116→117 / 151→152** and the Gate-D transitions **136→137 / 137→138**;
8. preserve the independent parallel-witness relationship to `நமது விளக்கம்`; do not overwrite or normalize that earlier source layer;
9. synchronize Speech-10 README / metadata / source-notes / verification-log, anthology README / mapping / handover / continuation prompt;
10. update root dated indexes and `data/speeches.json` only if required by the repository's release invariant;
11. if every release check passes, set Gate H **PASS / COMPLETE**, release **RELEASED / CLOSED**, and canonical bilingual transcript **COMPLETE**;
12. do **not** begin Speech 11 in the same activity.

Expected continuation after Gate H: **Speech 11 source-boundary / Gate-C setup**, using the locked anthology mapping and whole-speech batching policy.
