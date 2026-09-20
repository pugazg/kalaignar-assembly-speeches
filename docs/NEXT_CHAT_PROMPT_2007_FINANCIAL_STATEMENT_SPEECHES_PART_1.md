# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 10 source-boundary + Gate-C setup

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–9 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Speech 9 / **29.3.1971** final closure:

- scans **113–116 / printed pp.112–115**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **4 corrections / 0 unresolved**
- Gate F — **COMPLETE / 4/4**
- Gate G — **PASS / COMPLETE / 11 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE**
- release — **RELEASED / CLOSED**
- Gate-H wording changes — **0 Tamil / 0 English**
- canonical bilingual transcript — complete
- root dated index / `data/speeches.json` — synchronized
- `நமது நிலை` source layer — unchanged

Do not reopen Speech 9 merely for stylistic polishing.

## Speech 10 locked mapping

Speech 10 is the next anthology unit:

- source label — `உரை : 10`
- printed date — `29.6.71`
- ISO date — `1971-06-29`
- proposed working ID — `1971-06-29-financial-statement-debate`
- global scans — **117–151**
- printed pages — **116–150**
- page count — **35**
- start boundary — **116→117**
- end boundary — **151→152**
- scan 152 begins Speech 11 / `10.3.1972`

The 35-page size exceeds the normal 25-page activity limit, but the repository's whole-speech policy explicitly requires a single speech larger than 25 pages to be processed separately as **one intact unit** rather than split merely to meet the allowance.

## Parallel-witness rule

Speech 10 overlaps the existing `நமது விளக்கம்` event/provenance/source layer for 29.6.1971. The 2007 anthology must remain an **independent source witness**.

- do not overwrite released `நமது விளக்கம்` Tamil or English;
- do not normalize the anthology to that earlier witness;
- do not use `நமது விளக்கம்`, Official Reports, OCR, web copies or alternate anthologies to supply or repair wording;
- all future Speech-10 transcription/verification must be controlled by the 2007 anthology pixels.

## Exact next activity

Perform **Speech 10 source-boundary and Gate-C setup only**.

Requirements:

1. re-confirm live-main mapping for scans **117–151 / printed pp.116–150** and hard boundaries **116→117 / 151→152**;
2. identify the exact user-supplied/source split files needed to cover the full 35-page range;
3. confirm split-to-global-page relationships and checksums for every controlling split used;
4. create the Speech-10 working folder / README / metadata / source-notes / verification-log only when source coverage is sufficient to do so accurately;
5. explicitly record the independent parallel-witness relationship to `நமது விளக்கம்`;
6. set Tamil status to **NOT STARTED** and Gate C to **NOT STARTED** unless actual transcription is performed in a later activity;
7. preserve the whole-speech policy: Speech 10 will be processed as one intact 35-page speech unit when Gate C begins;
8. synchronize anthology README, mapping, handover and this continuation prompt;
9. do not import wording from `நமது விளக்கம்` or any outside source;
10. do **not** begin Speech 10 Gate-C transcription, Gate D, English work, or Speech 11 in this setup activity.

Expected continuation after setup: **Speech 10 Gate C Tamil first-pass transcription — scans 117–151 / 35 pages**, once complete source coverage is available.
