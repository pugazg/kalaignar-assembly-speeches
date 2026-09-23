# NEXT CHAT PROMPT — 2007 financial-statement speeches Part 1 / Speech 15 Gate C first-pass transcription

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable release state

Speeches **1–14 are RELEASED / CLOSED through Gate H** with verified Tamil and verified English. Do not reopen them unless a separate source-backed defect is discovered.

## Speech 15 setup state

Working entry:

`speeches/1977/1977-08-03-financial-statement-debate/`

- source label/date — `உரை : 15 / 03.08.1977`
- mapped unit — **scans 320–355 / printed pp.319–354 / 36 pages**
- source-boundary + Gate-C setup — **PASS / COMPLETE**
- incoming boundary **319→320** — **PASS / visually reconfirmed**
- outgoing boundary **355→356** — **PASS / visually reconfirmed**
- scan 320 — `உரை : 15 / நாள் : 03.08.1977`
- scan 355 — final Speech-15 page / ends `விடைபெறுகிறேன்.` / source ornament
- scan 356 — `உரை : 16 / நாள் : 1.3.1978` / excluded
- source coverage — **36/36 / no gap / no overlap**
- split transitions **325→326 / 350→351** — **PASS / visually continuous**
- Gate C — **READY / NOT STARTED**
- Tamil — **NOT TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C.5 / D / E — **NOT STARTED**
- Gate F — **BLOCKED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**
- Speech 16 — **NOT STARTED**

## Controlling splits

1. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_013_pages_301-325.pdf`
   - local **20–25 = scans 320–325**
   - printed **319–324**
   - size **17,775,750 bytes**
   - SHA-256 `26f0a480bf6c7b6f3f8638aadc77d0528f15b61def73937fad1627060f31c61b`

2. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_014_pages_326-350.pdf`
   - local **1–25 = scans 326–350**
   - printed **325–349**
   - size **19,044,518 bytes**
   - SHA-256 `6caec9d63d871d69f636b35aa3297345bab9e064c7e74e2f9f1bc13f1a29311e`

3. `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_015_pages_351-375.pdf`
   - local **1–5 = scans 351–355**
   - printed **350–354**
   - size **18,255,463 bytes**
   - SHA-256 `cc81c3d6e9496012e10a39f2a0ad3666d522f9a7b2b58f25f484a7f5a3682344`
   - local page **6 = scan 356 / Speech 16 boundary witness / excluded**

## Whole-speech exception

The repository's normal activity allowance is **25 source pages**, but Speech 15 itself is **36 pages**. Under the existing whole-speech exception, process the complete speech as one intact unit rather than splitting it merely to satisfy the allowance.

The Speech-14-specific 10-page Gate-C/Gate-E cadence does **not** carry forward to Speech 15.

## Exact next activity

Perform **Speech 15 Gate C first-pass Tamil transcription — scans 320–355 / printed pp.319–354 / all 36 pages**.

Requirements:

1. use only rendered controlling anthology pixels;
2. transcribe all **36/36** pages as one intact Speech-15 unit;
3. add source-page markers **320→355**, exactly once and ordered;
4. preserve source wording, spelling, punctuation, numerals, headings, speaker labels/interventions, source-printed English and visible repetition;
5. preserve page-spanning continuations across **325→326** and **350→351**;
6. do not import wording from OCR, web, Official Reports, alternate anthologies, released speeches or another witness;
7. record any genuinely uncertain first-pass reading explicitly rather than normalizing or guessing;
8. Gate C is first-pass transcription only — keep Tamil **NOT VERIFIED / verified_against_scan=false**;
9. synchronize Speech-15 and anthology control documents after the complete first pass;
10. do not begin Gate C.5, Gate D, Gate E, English, Gate H or Speech 16 in the same activity unless separately instructed.
