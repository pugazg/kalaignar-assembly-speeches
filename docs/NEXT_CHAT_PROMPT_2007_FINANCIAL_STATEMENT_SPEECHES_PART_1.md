# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 9 Gate E

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–8 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them merely for stylistic polishing.

Speech 9 / **29.3.1971** is the active working entry:

`speeches/1971/1971-03-29-financial-statement-debate/`

Current state:

- source label — `உரை : 9`
- scans **113–116 / printed pp.112–115**
- Gate C — **COMPLETE / 4 of 4**
- Gate D — **PASS / COMPLETE / 4 of 4 / 0 completeness corrections**
- source markers — **113→116 exactly once and in order**
- hard boundaries **112→113** and **116→117** — PASS
- page transitions **113→114 / 114→115 / 115→116** — PASS
- first-pass unresolved readings — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 — **provisionally N/A**
- Gate E — **NOT STARTED / exact next**
- English — **NOT STARTED**
- release — **NOT RELEASED**

## Gate-D durable findings

- scan 113 heading/date and speaker label are present;
- scan **114→115** `தேவைப்படுகிற` → `தொகையைப் பெற்றுக் கொள்வதுதான்` is continuous;
- scan 115 `‘சன்பிளவர்’`, `100க்கு 90`, and `(சிரிப்பு).` are structurally present;
- the scan-115 two-sentence sequence beginning `அப்படிப்பட்ட சங்கடத்தில் அகப்பட்டிருப்பார்கள்.` and `மேடை ஏறிப் பேச ஆரம்பித்தாலே...` is **printed twice in the source itself**; do not delete it as a duplicate;
- scan 116 `14 கோடி`, `அவைகளை யெல்லாம்`, and final `கேட்டுக் கொண்டு அமர்கிறேன்.` are present;
- Gate-D Tamil wording changes — **0**.

## Parallel-witness rule

Speech 9 overlaps the existing `நமது நிலை` event/provenance record. The 2007 anthology is an **independent source witness**.

- do **not** overwrite released `நமது நிலை` Tamil or English;
- do **not** normalize this anthology to the earlier witness;
- do **not** use `நமது நிலை`, Official Reports, OCR, web copies or alternate anthologies to repair or prefer wording;
- Gate E decisions must come only from the controlling 2007 anthology pixels.

## Source authority

Use only:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_005_pages_101-125.pdf`

- local pages **13–16** = global scans **113–116**
- local page **17** = global scan **117 / Speech 10 start**
- split SHA-256 — `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade`
- rendered scan pixels are authoritative

## Exact next activity

Perform **Speech 9 Gate E strict Tamil source-fidelity verification**, scans **113–116 / 4 pages**.

Requirements:

1. re-read every line of all **4/4** scans directly from rendered pixels against the Gate-C transcript;
2. verify word-for-word source spelling, punctuation, numerals, quotations, names and spacing-sensitive source forms;
3. preserve source-page markers **113→116** and hard boundaries **112→113 / 116→117**;
4. record **every source-fidelity correction** explicitly in `verification-log.md`, with scan number and before → source form;
5. correct only what the **same 2007 anthology scan** supports; do not use another witness to choose or repair wording;
6. specifically re-check the first-pass unusual forms on scan 115 (`அதன் மூலமாக எல்லாவிதமான வீட்டும் குறையும்.`) and scan 116 (`அவைகளை யெல்லாம்`) against pixels rather than normalizing semantically;
7. retain the scan-115 source-printed repeated two-sentence sequence unless the pixels prove the first-pass capture differs from the source;
8. re-check `‘சன்பிளவர்’`, `100க்கு 90`, `(சிரிப்பு).`, `14 கோடி`, speaker label and closing sentence exactly;
9. if any source reading remains genuinely unresolved, record it explicitly and do **not** mark Tamil verified;
10. if all 4 pages resolve, close Tamil as **VERIFIED / verified_against_scan=true** and close Gate C.5 as **N/A / CLOSED** if no legacy-glyph anomaly is found;
11. update working README, metadata, source notes, verification log, transcript and synchronize anthology README, mapping, handover and this continuation prompt;
12. do **not** begin Gate F English translation or Speech 10 in the same iteration.

Expected continuation after successful Gate E: **Speech 9 Gate F English translation, scans 113–116 / 4 pages**.
