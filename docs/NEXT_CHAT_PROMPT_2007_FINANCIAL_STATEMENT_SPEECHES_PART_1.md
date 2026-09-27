# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 19 Gate E Batch 2 — scans 521–530

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable released state

Speeches **1–18 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Do not reopen any released speech unless a separate source-backed defect is discovered.

## Speech 19 authoritative state

Working entry:

`speeches/1982/1982-03-06-financial-statement-debate/`

Source:

- label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- hard boundaries **510→511 / 545→546 — PASS**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**

Current gates:

- Gate C — **PASS / COMPLETE / 35 of 35 first-pass**
- Gate C.5 — **N/A / CLOSED — modern 2007 typesetting / 0 historical-glyph corrections**
- Gate D — **PASS / COMPLETE — 35/35 pages / 34/34 internal transitions / 0 completeness corrections**
- Gate E Batch 1 — **PASS / COMPLETE — scans 511–520 / 10 of 35 source-verified**
- Batch-1 corrections — **3 entries / 3 occurrences / 2 affected scans**
- Batch-1 unresolved — **0**
- Tamil — **PARTIALLY VERIFIED / verified_against_scan=false**
- Gates F–H — **NOT STARTED**

Batch-1 correction ledger:

1. scan **518** — `1½ நாள் எடுத்து கொண்டு` → `1½ நாள் எடுத்துக் கொண்டு`
2. scan **520** — `எதிர்பார்க்கப்படுகிறது` → `எதிர்பார்க்கப் படுகிறது`
3. scan **520** — `கட்டி முடிக்கப்பட்டன` → `கட்டிமுடிக்கப்பட்டன`

Structural state:

- source-page markers — **511→545 / 35 / exactly once / ordered**
- missing / duplicate / empty page sections — **0 / 0 / 0**
- working-split transition **525→526 — PASS**
- source-printed English on scans **523–525 / 535 / 542** — **represented**
- source-printed `foundation, weir pie` on scan **539** — **represented as printed**
- outside wording imported — **0**

## Controlling sources for Gate E Batch 2

Full anthology:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- authority — **rendered scan pixels only**
- usable text layer — **none**

Batch 2 crosses the working-split boundary.

Part021:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`

- **25 pages / 18,938,935 bytes**
- SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- Batch-2 coverage — local **21–25 = scans 521–525**

Part022:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`

- **21 pages / 15,522,557 bytes**
- SHA-256 — `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`
- Batch-2 coverage — local **1–5 = scans 526–530**
- working-split transition — **525→526 / part021→part022 / already structurally PASS; recheck source fidelity across it**

## Gate-E cadence

1. Batch 1 — **511–520 / 10 pages / PASS-COMPLETE / 3 corrections**
2. Batch 2 — **521–530 / 10 pages / exact next**
3. Batch 3 — **531–540 / 10 pages**
4. Batch 4 FINAL — **541–545 / 5 pages**

## Exact next activity

Perform **Speech 19 Gate E Batch 2 — scans 521–530 / exactly 10 pages**.

Requirements:

1. compare the canonical Tamil directly against rendered source pixels for **every page 521–530**;
2. use no outside wording: no OCR, web, Official Reports, alternate anthologies, released speeches or other witnesses may supply or normalize text;
3. do not alter already source-verified scans **511–520** unless a separate concrete source-backed defect is discovered and documented;
4. check every legible word/character, names/initials, numerals/dates/money/units, embedded English, quotations, speaker/interruption markers, punctuation where legible, omissions, repetitions and page-spanning continuations;
5. explicitly verify the **520→521** continuation and the **525→526 / part021→part022** source transition;
6. preserve the source-printed English passages on scans **523–525** exactly as printed;
7. preserve source spelling, grammar, vocabulary, compounds and punctuation; correct only source-backed transcription defects;
8. maintain a page-specific correction ledger with exact before→after readings;
9. record unresolved readings rather than guessing;
10. preserve markers **511→545** unchanged / exactly once / ordered;
11. do not source-verify or alter scan **531** in this activity;
12. process exactly **10 pages / 521–530** and no more;
13. after Batch 2, Tamil remains **PARTIALLY VERIFIED / verified_against_scan=false**;
14. update Speech README, metadata, transcript, source-notes, verification-log, anthology mapping/source README, handover, root README and this continuation prompt;
15. exact next after Batch 2 — **Speech 19 Gate E Batch 3 — scans 531–540 / exactly 10 pages**;
16. do not begin Batch 3 in the same activity.

Do not begin Gate F until all **35/35** pages have passed Gate E and Tamil is marked **VERIFIED / verified_against_scan=true**.
