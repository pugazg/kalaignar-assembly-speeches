# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 13 Gate C Tamil first pass

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–12 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English.

Speech 12 / 07.03.1973 remains the released independent parallel witness at:

`speeches/1973/1973-03-07-financial-statement-debate/`

The separately released same-date record remains:

`speeches/1973/1973-03-07-financial-statement-reply/`

Do not overwrite, merge, normalize or reopen either witness unless a separate source-backed defect is discovered.

## Speech 13 setup state — PASS / COMPLETE

Working entry:

`speeches/1974/1974-03-14-financial-statement-debate/`

Locked map:

- source label — `உரை : 13`
- printed date — `14.03.1974`
- ISO date — `1974-03-14`
- global scans — **231–262**
- printed pages — **230–261**
- page count — **32**
- start boundary — **230→231 — PASS**
- end boundary — **262→263 — PASS**
- normal activity page limit — **25**
- whole-speech exception — **REQUIRED / keep all 32 pages intact**

## Controlling split coverage

1. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_010_pages_226-250.pdf`
   - 25 pages / **17,801,423 bytes**
   - SHA-256 `257b862a7ebe21d768f8e5a2f2d2f9e8bb6c4e7ca7f704800a6453f40d0a9b90`
   - local **6–25** = global scans **231–250** / printed pp. **230–249** / **20 speech pages**
   - local 5 = global scan 230 / Speech 12 close / boundary-only
2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_011_pages_251-275.pdf`
   - 25 pages / **17,580,247 bytes**
   - SHA-256 `27c9c96d3c0bdb53480f8d1634300bf9d7dc57be17d3f83c66397ef78863712d`
   - local **1–12** = global scans **251–262** / printed pp. **250–261** / **12 speech pages**
   - local 13 = global scan 263 / Speech 14 start / boundary-only

Total controlling coverage: **32/32 pages / no gap / no overlap**.

## Pixel boundary evidence

- scan 230 / printed 229 closes Speech 12 and is excluded;
- scan 231 / printed 230 begins `உரை : 13 / நாள் : 14.03.1974`;
- scan 262 / printed 261 closes Speech 13 with source ornament;
- scan 263 / printed 262 begins `உரை : 14 / நாள் : 10.03.1975` and is excluded.

## Source-separation rule

All Speech-13 wording must come from the rendered pixels of the two controlling 2007 anthology splits only.

- no OCR;
- no web copy;
- no Official Reports;
- no alternate anthology;
- no released speech or other witness may supply, repair or normalize wording;
- preserve uncertainty explicitly rather than guessing;
- Speech 12 remains unchanged;
- do not begin Speech 14.

## Current Speech 13 state

- source-boundary / Gate-C setup — **PASS / COMPLETE**
- Tamil — **NOT STARTED / verified_against_scan=false**
- Gate C — **NOT STARTED**
- Gate C.5 — **NOT STARTED**
- Gate D / Gate E — **NOT STARTED**
- English / Gates F–G — **BLOCKED / NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**
- `transcript.md` — **not yet created**

## Exact next activity

Perform **Speech 13 Gate C Tamil first-pass transcription — all scans 231–262 / printed pp.230–261 / 32 pages as one intact unit**.

Requirements:

1. transcribe only from the rendered pixels of part010 local 6–25 and part011 local 1–12;
2. create `transcript.md` with source-page markers **231→262**, exactly once and in order;
3. preserve source wording, spelling, punctuation, numerals, speaker labels/interventions, printed English and source-visible repetition;
4. normalize only physical line wrapping into readable paragraphs;
5. preserve hard boundaries **230→231 / 262→263**; admit neither scan 230 nor scan 263;
6. mark uncertain readings explicitly rather than guessing;
7. import wording from no other witness or outside source;
8. after all 32 pages are represented, synchronize Speech-13 README / metadata / source-notes / verification-log and anthology control documents;
9. set Gate C to **COMPLETE** only if all 32 pages are present; Tamil must remain **TRANSCRIBED / NOT VERIFIED** with `verified_against_scan=false`;
10. do **not** begin Gate C.5, Gate D, Gate E, English work, Gate H, or Speech 14 in the same activity.
