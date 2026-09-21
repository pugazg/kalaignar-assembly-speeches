# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 14 source-boundary + Gate-C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–13 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Speech 13 / 14.03.1974 final state:

- scans **231–262 / printed pp.230–261 / 32 pages**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **PASS / COMPLETE / 8 correction entries / 9 occurrences / 0 unresolved**
- Gate F — **COMPLETE / 32 of 32**
- Gate G — **PASS / COMPLETE / 32 of 32 / 7 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**
- canonical bilingual `transcript.md` — **COMPLETE**
- `translation.md` — **retired pointer**
- Gate-H wording changes — **0 Tamil / 0 English**
- `data/speeches.json` and root dated table — **indexed**

Do not reopen Speech 13 unless a separate source-backed defect is discovered.

## Speech 14 mapped source unit

- source label — `உரை : 14`
- printed date — `10.03.1975`
- ISO date — **1975-03-10**
- working ID — `1975-03-10-financial-statement-debate`
- global scans — **263–319**
- printed pages — **262–318**
- page count — **57**
- start boundary — **262→263**
- end boundary — **319→320**
- next source unit — Speech 15 starts at scan **320 / printed 319**

## Exact next activity

Perform **Speech 14 source-boundary + Gate-C setup** only.

Requirements:

1. refetch live main and inspect current anthology mapping / workflow controls;
2. visually confirm hard boundaries **262→263** and **319→320** from the controlling anthology pixels;
3. register the exact controlling split coverage and source hashes needed for scans **263–319**;
4. create the Speech-14 working entry and machine-readable metadata using repository conventions;
5. apply the **whole-speech exception** because the speech is **57 pages**; do not split it merely to meet the normal page limit;
6. set Tamil / Gate C to **NOT STARTED / verified_against_scan=false** after setup;
7. synchronize source README, mapping, handover and next-chat prompt;
8. do **not** begin Gate C transcription or Speech 15 in the same setup activity.
