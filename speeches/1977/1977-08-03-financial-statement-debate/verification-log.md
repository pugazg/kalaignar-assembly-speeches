# Verification log — உரை : 15 / 03.08.1977

## Source-boundary and Gate-C setup

**Status: PASS / COMPLETE — setup only**

No Speech-15 Tamil body transcription or downstream gate work was performed in this activity.

### Locked coverage

| Split | Local pages | Global scans | Printed pages | Count | SHA-256 |
|---|---:|---:|---:|---:|---|
| part013 / pages 301–325 | 20–25 | 320–325 | 319–324 | 6 | `26f0a480bf6c7b6f3f8638aadc77d0528f15b61def73937fad1627060f31c61b` |
| part014 / pages 326–350 | 1–25 | 326–350 | 325–349 | 25 | `6caec9d63d871d69f636b35aa3297345bab9e064c7e74e2f9f1bc13f1a29311e` |
| part015 / pages 351–375 | 1–5 | 351–355 | 350–354 | 5 | `cc81c3d6e9496012e10a39f2a0ad3666d522f9a7b2b58f25f484a7f5a3682344` |

Total Speech-15 source coverage: **36/36 pages**.

### Boundary checks

- **319→320 — PASS / visually reconfirmed**
  - scan 319 / printed 318 = Speech 14 final page, ending `வணக்கம்.`, excluded;
  - scan 320 / printed 319 = `உரை : 15 / நாள் : 03.08.1977`, admitted as Speech 15 start.
- **355→356 — PASS / visually reconfirmed**
  - scan 355 / printed 354 = Speech 15 final page, ending `விடைபெறுகிறேன்.` with source ornament;
  - scan 356 / printed 355 = `உரை : 16 / நாள் : 1.3.1978`, excluded.
- printed-page relationship **printed = global scan - 1** — PASS.

### Split relation checks

- part013 local **20→25 = scans 320→325** — PASS;
- part014 local **1→25 = scans 326→350** — PASS;
- part015 local **1→5 = scans 351→355** — PASS;
- split transition **325→326** — visually continuous Speech-15 text;
- split transition **350→351** — visually continuous Speech-15 text;
- no source-page gap or overlap — **PASS**.

## Source-separation check

- controlling textual authority — **rendered pixels of part013, part014 and part015 only**;
- Speech 14 reopened — **NO**;
- Speech 16 begun — **NO**;
- OCR wording imported — **0**;
- web wording imported — **0**;
- Official Report wording imported — **0**;
- alternate-anthology wording imported — **0**;
- other-witness wording imported — **0**.

## Gate state

- Gate C — **READY / NOT STARTED**
- Gate C.5 — **NOT STARTED**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- Tamil — **NOT TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate F — **BLOCKED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**

## Whole-speech exception

Speech 15 spans **36 pages**, exceeding the normal 25-page activity limit. Existing repository policy therefore permits the complete speech to be processed as a single intact Gate-C unit rather than split solely to meet the page allowance.

## Exact next activity

Perform **Gate C first-pass Tamil transcription — scans 320–355 / printed pp.319–354 / all 36 pages** from rendered controlling pixels only. Preserve source wording, spelling, punctuation, numerals, speaker labels/interventions, source-printed English and visible repetition. Gate C is not strict source verification; keep `verified_against_scan=false`.
