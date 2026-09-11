# Historical Tamil glyph audit — 8-3-1973 Legislative Council reply

## Gate

**Gate C.5 — HISTORICAL TAMIL GLYPH AUDIT**

Status: **PASS / COMPLETE**

Controlling source: `TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

Locked Council range: scan pages **41–62** / printed pages **40–61**.

Controlling method: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Audit rule

Read character identity, not modern visual resemblance. This audit decodes historical Tamil typeforms into correct modern Unicode identity; it does not authorize modernization of spelling, grammar, vocabulary, punctuation, compounds or spacing.

Mandatory families checked on every audited page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Source pixels are controlling; same-edition comparison is used when uncertain; global replacement is forbidden.

## Progress

| Scan range | Printed pages | Status | Glyph corrections | Unresolved clusters |
|---|---|---|---:|---:|
| 41–50 | 40–49 | **PASS — HG1** | **1** | **0** |
| 51–60 | 50–59 | **PASS — HG2** | **1** | **0** |
| 61–62 | 60–61 | **PASS — HG3 / FINAL** | **0** | **0** |

## Correction ledger

| Scan | Printed page | Earlier/apparent reading | Source-supported reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 44 | 43 | `வழக்கத்திற்கு மாறுக நடனம்` | `வழக்கத்திற்கு மாறாக நடனம்` | `றா` | enlarged source pixels; same-edition comparison with clear `றா` forms including Unit-1 `மாறாக` precedent | corrected |
| 58 | 57 | `அப்போது நடந்த வேலதான் மிகுந்த சங்கடமானது` | `அப்போது நடந்த வேலைதான் மிகுந்த சங்கடமானது` | `லை` | enlarged source pixels; complete historical `லை` form is visibly printed in `வேலைதான்` | corrected |

## HG1 page-level coverage

| Scan | Printed | All 13 families checked | Representative identities | Corrections | Unresolved |
|---:|:---:|---|---|---:|---:|
| 41 | 40 | YES | `கருணாநிதி` (`ணா`), `நிதிநிலை` (`லை`), `கருத்துக்களை` (`ளை`) | 0 | 0 |
| 42 | 41 | YES | `தவறான` (`றா`), `பேசவில்லையோ` (`லை`), `அவர்களை` (`ளை`) | 0 | 0 |
| 43 | 42 | YES | `நிலைமை` (`லை`), `நாரதர்` (`னா`), `அவர்களை` (`ளை`) | 0 | 0 |
| 44 | 43 | YES | `மாறாக` / `விளக்கியிருக்கிறார்கள்` (`றா`) | **1** | 0 |
| 45 | 44 | YES | `இல்லையோ` / `நிதிநிலை` (`லை`) | 0 | 0 |
| 46 | 45 | YES | `மாற்றியமைத்திருக்கிறார்கள்` (`றா`), `தொலைதூர` (`லை`) | 0 | 0 |
| 47 | 46 | YES | `தவறான` (`றா`), `கல்வி மானியத்தின் கீழ்` (`லை`) | 0 | 0 |
| 48 | 47 | YES | `நிலைமைகள்` (`லை`), inflectional `ளை` forms checked | 0 | 0 |
| 49 | 48 | YES | `நிலைமை` (`லை`), neighboring old-type clusters checked | 0 | 0 |
| 50 | 49 | YES | `நிலையத்தில்` (`லை`), neighboring `ண` families checked | 0 | 0 |

Families without a positive occurrence requiring action were still explicitly checked on each page.

## HG1 result

- audited scans: **41–50**
- pages audited: **10**
- historical-glyph corrections: **1**
- unresolved glyph clusters: **0**
- global replacements: **0**
- Gate C remains complete
- `transcription.verified_against_scan=false` remains unchanged
- Gate D remains blocked

## HG2 page-level coverage

| Scan | Printed | All 13 families checked | Representative identities | Corrections | Unresolved |
|---:|:---:|---|---|---:|---:|
| 51 | 50 | YES | `நிலையம்` / `தலைமையில்` (`லை`), `அவைகளை` (`ளை`), `தனியார்` (`னா`) | 0 | 0 |
| 52 | 51 | YES | `விலக்கிவிடலாமென்று` (`லை`), `தவறாகப்` (`றா`), `அனைவருக்கும்` (`னை`) | 0 | 0 |
| 53 | 52 | YES | `இணைந்திருக்கின்ற` (`ணை`), `புரியவில்லை` (`லை`), `ஆனால்` (`னா`) | 0 | 0 |
| 54 | 53 | YES | `அண்ணா` (`ணா`), `மாநிலங்களும்` (`னா`), neighboring clusters checked | 0 | 0 |
| 55 | 54 | YES | `அண்ணா` (`ணா`), `மாநில` (`னா`), neighboring `லை` forms checked | 0 | 0 |
| 56 | 55 | YES | `நாலு` (`னா`), `அண்ணா` (`ணா`), neighboring old-type clusters checked | 0 | 0 |
| 57 | 56 | YES | `நாராயணசாமி` (`னா`), `அவைகளைக்` (`ளை`) | 0 | 0 |
| 58 | 57 | YES | `வேலைதான்` / `நிலத்தை` (`லை`), `மனை` / `சென்னை` (`னை`), `நிச்சயமாக` (`னா`) | **1** | 0 |
| 59 | 58 | YES | `தன்னைச்` (`னை`), `நிலம்` (`லை`), `தவறான` (`றா`) | 0 | 0 |
| 60 | 59 | YES | `நாணயம்` (`ணா`), `சூழ்நிலையை` (`ளை`), `நாங்களும்` (`னா`) | 0 | 0 |

Families without a positive occurrence requiring action were still explicitly checked on every HG2 page. No historical character identity required correction in scans 51–60.

## HG2 result

- audited scans: **51–60**
- audited printed pages: **50–59**
- pages audited in HG2: **10**
- HG2 historical-glyph corrections: **1**
- cumulative Gate-C.5 corrections: **2**
- unresolved glyph clusters: **0**
- global replacements: **0**
- Gate C remains complete
- `transcription.verified_against_scan=false` remains unchanged
- Gate D remains blocked

## HG3 page-level coverage

| Scan | Printed | All 13 families checked | Representative identities | Corrections | Unresolved |
|---:|:---:|---|---|---:|---:|
| 61 | 60 | YES | `சொன்னதில்லை` / `தெரியவில்லை` (`லை`), `மாற்றப்பட்டிருக்கிறார்` (`றா`), `நானாக` (`னா`), `சென்னையிலே` (`னை`), `இன்னொரு` (`னொ`) | 0 | 0 |
| 62 | 61 | YES | `நிலைமைகளை` (`லை` / `ளை`), `உரிமைகளை` (`ளை`), `சான்றோர்கள்` (`றோ`), `அனைவரும்` (`னை`) | 0 | 0 |

Families without a positive occurrence requiring action were still explicitly checked on both final pages.

## HG3 result

- audited scans: **61–62**
- audited printed pages: **60–61**
- pages audited in HG3: **2**
- HG3 historical-glyph corrections: **0**
- unresolved glyph clusters: **0**
- global replacements: **0**
- Gate C remains complete
- `transcription.verified_against_scan=false` remains unchanged
- Gate D was **not** started in this iteration

## Gate C.5 final result

**PASS / COMPLETE — scans 41–62 / printed pp.40–61.**

- pages audited: **22 / 22**
- HG1 corrections: **1**
- HG2 corrections: **1**
- HG3 corrections: **0**
- cumulative historical-glyph corrections: **2**
- unresolved historical-glyph clusters: **0**
- all 13 mandatory families checked on every mapped Unit-2 page
- source pixels remained controlling
- global replacements: **0**
- ordinary spelling/grammar modernization: **0**
- Gate D: **unblocked / next**

Exact next activity: **Gate D Tamil completeness audit — D1 scans 41–50 / printed pp.40–49**. Do not begin Gate E in the same iteration.
