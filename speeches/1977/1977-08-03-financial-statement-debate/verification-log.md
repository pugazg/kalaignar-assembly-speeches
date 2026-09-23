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

## Gate C — first-pass transcription

**COMPLETE — scans 320–355 / printed pp.319–354 / 36 of 36 pages.**

- source-page markers — **320→355 / 36 / exactly once / ordered**
- first-pass unresolved readings — **0 currently flagged**
- heading/date/speaker labels — **captured**
- speaker interventions — **preserved where printed**
- source spelling / punctuation / numerals — **preserved at first-pass level**
- source-printed English — **preserved**
- page-spanning continuations — **represented**
- outside wording imported — **0**
- Tamil verification state — **NOT VERIFIED**
- `verified_against_scan=false`

Gate C completion is not a Gate-E word-for-word source verification claim.

## Fixed iteration rule — Gate C and Gate E

Per explicit user instruction:

- Gate C — **10 source pages per iteration**
- Gate E — **10 source pages per iteration**
- final remainder — may be **fewer than 10** only when fewer than 10 source pages remain in the current speech;
- no Gate-C or Gate-E iteration may exceed 10 source pages unless the user explicitly overrides the rule.

This rule supersedes the earlier whole-speech exception for Gate C and Gate E. Speech 15 Gate C was already complete on live `main` before the rule was locked.

Planned Speech-15 Gate-E cadence:

- Batch 1 — **320–329 / 10 pages**
- Batch 2 — **330–339 / 10 pages**
- Batch 3 — **340–349 / 10 pages**
- Final Batch 4 — **350–355 / 6 pages**

## Gate C.5 — historical-glyph applicability

**N/A / CLOSED.**

Decision basis:

- source edition — **May 2007 modern-typeset anthology**;
- representative direct-pixel review — **scans 320, 326, 335, 345, 355**;
- known reform-sensitive families considered — `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- observed typography — **modern post-reform Tamil forms**;
- legacy/historical metal-type identity requiring separate decoding — **not observed**;
- historical-glyph corrections — **0**;
- unresolved historical-glyph readings — **0**.

This applicability closure is not a Tamil source-fidelity verification. `verified_against_scan=false` remains unchanged.

## Downstream gate state

- Gate C.5 — **N/A / CLOSED**
- Gate D — **READY / NOT STARTED**
- Gate E — **NOT STARTED**
- Gate F — **BLOCKED**
- Gate G — **NOT STARTED**
- Gate H — **NOT STARTED / NOT RELEASED**

## Exact next activity

Perform **Gate D completeness audit — scans 320–355 / printed pp.319–354 / 36 pages**.

Gate D must verify complete structural representation only: markers **320→355** exactly once and ordered, no page gaps/duplicates, locked start/end boundaries, page-spanning continuity, and all printed speaker/intervention structure represented. Do not mark Tamil verified.

After Gate D passes, Gate E must follow the fixed 10-page cadence:

- **320–329**
- **330–339**
- **340–349**
- **350–355** final remainder
