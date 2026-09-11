# Historical Tamil glyph audit — 7-3-1973 Assembly reply

## Gate

**Gate C.5 — HISTORICAL TAMIL GLYPH AUDIT**

Status: **IN PROGRESS**

Controlling source: `TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

Locked Assembly range:

- scan pages: **4–40**
- printed pages: **3–39**

Controlling method: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Audit rule

> Read character identity, not modern visual resemblance.

This audit decodes historical Tamil typeforms into the correct modern Unicode character identity. It does **not** authorize modernization of spelling, grammar, vocabulary, punctuation, compounds or spacing.

Minimum known reform-sensitive families that must be checked on **every page**:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Requirements:

- inspect the complete page first at enlarged/native resolution;
- use source pixels as authority; OCR is discovery-only;
- compare same-edition/same-font examples for uncertain clusters;
- never global-replace;
- record each correction individually with scan provenance;
- keep glyph-identity corrections separate from ordinary transcription corrections;
- if identity remains uncertain, do not guess and do not pass the gate.

## Progress

| Scan range | Printed pages | Status | Glyph corrections | Unresolved clusters |
|---|---|---|---:|---:|
| 4–8 | 3–7 | PASS — HG1 | 2 | 0 |
| 9–13 | 8–12 | PASS — HG2 | 1 | 0 |
| 14–18 | 13–17 | PASS — HG3 | 0 | 0 |
| 19–23 | 18–22 | PASS — HG4 | 0 | 0 |
| 24–28 | 23–27 | PASS — HG5 | 0 | 0 |
| 29–33 | 28–32 | PASS — HG6 | 0 | 0 |
| 34–40 | 33–39 | PASS — HG7 / FINAL | 0 | 0 |

## Correction ledger

| Scan | Printed page | Earlier/apparent reading | Source-supported reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 4 | 3 | `தொடங்கப் பெறுமல்` (first occurrence) | `தொடங்கப் பெறாமல்` | `றா` | enlarged source pixels; same-edition `றா` comparison with clear `...கிறார்கள்` forms | corrected |
| 4 | 3 | `தொடங்கப் பெறுமல்` (second occurrence) | `தொடங்கப் பெறாமல்` | `றா` | enlarged source pixels; same-edition `றா` comparison with clear `...கிறார்கள்` forms | corrected |
| 12 | 11 | `மாற்றுந்தாய்` | `மாற்றாந்தாய்` | `றா` | enlarged source pixels; same-page comparison with `தவறாகும்` and `சொல்கிறாரே` | corrected |

## HG1 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 4 | 3 | YES | `கருணாநிதி` (`ணா`), `துணைத்` (`ணை`), `நிதிநிலை` (`லை`), `கருத்துக்களைத்` (`ளை`), `...கிறார்கள்` / `பெறாமல்` (`றா`), `ஆனால்` (`னா`), `அனைத்தும்` (`னை`) | 2 | 0 |
| 5 | 4 | YES | `புரியவில்லை` (`லை`), `பாளையச்` (`ளை`), `ஆனால்` (`னா`), `என்னை` (`னை`) | 0 | 0 |
| 6 | 5 | YES | `துணையாக` (`ணை`), `சிறைச்சாலையில்` (`லை`), `விரும்புகிறாரே` (`றா`), `கோரினால்` (`னா`), `சென்னை` (`னை`) | 0 | 0 |
| 7 | 6 | YES | `ஆணைக்குழு` (`ணை`), `நிதிநிலை` (`லை`), `கூறுகிறோம்` (`றோ`), `ஆனால்` (`னா`), `வாய்ப்பினை` (`னை`) | 0 | 0 |
| 8 | 7 | YES | `ஆணைக்குழுவின்` (`ணை`), `நிலை` (`லை`), `திட்டங்களை` (`ளை`), `இருக்கிறோமேயல்லாமல்` (`றோ`), `ஆனால்` (`னா`), `அனைத்து` (`னை`) | 0 | 0 |

Families with no positive occurrence requiring action in HG1 were still explicitly checked; absence is not treated as evidence of skipping the family.

## HG2 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 9 | 8 | YES | `கருணாநிதி` (`ணா`), `இணைத்துப்` (`ணை`), `சேர்க்கவில்லை` (`லை`), `வருகிறோம்` (`றோ`), `சொன்னார்கள்` (`னா`), `இன்னொரு` (`னொ`) | 0 | 0 |
| 10 | 9 | YES | `தவணை` (`ணை`), `இல்லை` (`லை`), `ஏனென்றால்` (`றா`), `பெறுகிறோம்` (`றோ`), `வேண்டுமானால்` (`னா`) | 0 | 0 |
| 11 | 10 | YES | `நிதிநிலை` (`லை`), `வேளையாக` (`ளை`), `மாறாக` (`றா`), `வருகிறோம்` (`றோ`), `பார்ப்பார்களேயானால்` (`னா`) | 0 | 0 |
| 12 | 11 | YES | `கருணாநிதி` (`ணா`), `கருத்துக்களையெல்லாம்` (`ளை`), `தவறாகும்` / `மாற்றாந்தாய்` / `சொல்கிறாரே` (`றா`), `மறுக்கிறோம்` (`றோ`), `ஆனால்` (`னா`) | 1 | 0 |
| 13 | 12 | YES | `வரிகளைச்` (`ளை`), `விளக்கியிருக்கிறோம்` (`றோ`), `முன்னேற்றங்களினாலும்` (`னா`) | 0 | 0 |

Families with no positive occurrence requiring action in HG2 — including `ணொ / ணோ / றொ / னோ` — were still explicitly checked on every page.

## HG3 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 14 | 13 | YES | `அண்ணா` (`ணா`), `இல்லை` (`லை`), `நன்றாகப்` / `உயர்த்தியிருக்கிறார்கள்` (`றா`) | 0 | 0 |
| 15 | 14 | YES | `அண்ணா` (`ணா`), `சொல்லவில்லை` (`லை`), `நன்றாகத்` / `தவறான` (`றா`), `ஆனால்` (`னா`) | 0 | 0 |
| 16 | 15 | YES | `கொள்கைகளைப்` (`ளை`), `அப்படியென்றால்` (`றா`), `தருகிறோம்` (`றோ`), `எத்தனையோ` (`னை`) | 0 | 0 |
| 17 | 16 | YES | `விலைவாசி` (`லை`), `ஆகியவைகளைப்` (`ளை`), `தெரிவித்திருக்கிறார்கள்` (`றா`), `பிரச்சினையில்` (`னை`) | 0 | 0 |
| 18 | 17 | YES | `மலையாளத்திலும்` / `நிலைகளை` (`லை`), `கருத்துக்களை` (`ளை`), `குறிப்பிட்டிருக்கின்றார்கள்` (`றா`), `சொல்கிறோம்` (`றோ`), `பிரச்சினையை` (`னை`) | 0 | 0 |

No positive occurrence requiring correction was found for `ணொ / ணோ / றொ / னொ / னோ` in HG3; all were still checked.

## HG4 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 19 | 18 | YES | `விலைவாசி` / `நிலைக்குப்` (`லை`), `விளைவாக` (`ளை`), `மாறாக` (`றா`), `சொல்கின்றோம்` (`றோ`), `வேண்டுமானால்` (`னா`) | 0 | 0 |
| 20 | 19 | YES | `கருணாநிதி` (`ணா`), `போடுகிறார்கள்` (`றா`), `சொன்னோம்` (`னோ`), `என்னைத்` (`னை`) | 0 | 0 |
| 21 | 20 | YES | `விலைவாசி` (`லை`), `விளையாடுகிறது` (`ளை`), `பாதிக்கப்படுகிறார்கள்` (`றா`) | 0 | 0 |
| 22 | 21 | YES | `வழிகளையும்` (`ளை`), `பேசியிருக்கிறார்கள்` (`றா`), `இருக்கிறோம்` (`றோ`), `அத்தனை` / `பிரச்சினையை` (`னை`) | 0 | 0 |
| 23 | 22 | YES | `சூழ்நிலையைப்` (`லை`), `விரும்புகிறார்களோ` (`றா`), `அணுகியிருக்கிறோம்` (`றோ`), `அனைவரையும்` (`னை`) | 0 | 0 |

No positive occurrence requiring correction was found for `ணை / ணொ / ணோ / றொ / னொ` in HG4; all were still explicitly checked.

## HG5 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 24 | 23 | YES | `மூன்றாவது` / `என்றால்` (`றா`), `செய்யவில்லை` (`லை`), `பதினைந்து` (`னை`) | 0 | 0 |
| 25 | 24 | YES | `இணைப்புக்` (`ணை`), `கிடைக்கவில்லை` (`லை`), `திட்டங்களைக்` (`ளை`), `கேட்டிருக்கிறோம்` (`றோ`), `காரணத்தினால்` (`னா`), `இன்னொன்றையும்` (`னொ`) | 0 | 0 |
| 26 | 25 | YES | `கருணாநிதி` (`ணா`), `நிலையத்தை` (`லை`), `பெறாமல்` / `கொண்டிருக்கிறார்கள்` (`றா`), `வருகிறோம்` (`றோ`), `அதனை` (`னை`) | 0 | 0 |
| 27 | 26 | YES | `விசாரணைக்` (`ணை`), `தொழிற்சாலையும்` (`லை`), `அவர்களைக்` (`ளை`), `பெறாமல்` / `பெற்றாக` (`றா`), `செலவழிக்கிறோமா` (`றோ`), `ஆலோசனைக்` (`னை`) | 0 | 0 |
| 28 | 27 | YES | `கருணாநிதி` (`ணா`), `விசாரணை` (`ணை`), `செயல்படவில்லை` (`லை`), `நல்லவேளையாக` (`ளை`), `பேசியிருக்கிறார்கள்` / `குறிப்பிட்டிருக்கிறார்` (`றா`), `நினைவு` (`னை`) | 0 | 0 |

No positive occurrence requiring correction was found for `ணொ / ணோ / றொ / னோ` in HG5; all were still explicitly checked.

## HG6 page-level coverage

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 29 | 28 | YES | `வேலை` / `விலைவாசி` (`லை`), `விளைவாலும்` (`ளை`), `குறிப்பிட்டிருக்கிறார்கள்` / `சொல்கிறார்களே` (`றா`), `இன்னொன்றையும்` (`னொ`) | 0 | 0 |
| 30 | 29 | YES | `தலைவர்` (`லை`), `காரியங்களையும்` (`ளை`), `செய்துகொண்டிருக்கிறார்கள்` (`றா`), `பாதிக்கப்பட்டிருக்கிறோம்` (`றோ`), `வெட்டினால்` (`னா`) | 0 | 0 |
| 31 | 30 | YES | `கருணாநிதி` (`ணா`), `ஆலை` / `வேலை` (`லை`), `அவர்களைப்` / `சங்கடங்களைத்` (`ளை`), `ஓட்டியிருக்கிறார்கள்` (`றா`), `வருகிறோம்` (`றோ`), `என்னையும்` (`னை`) | 0 | 0 |
| 32 | 31 | YES | `காலை` / `மாலை` (`லை`), `சங்கடங்களையெல்லாம்` (`ளை`), `மூன்றாவது` (`றா`), `செய்திருக்கிறோம்` (`றோ`), `நேரத்தினை` (`னை`) | 0 | 0 |
| 33 | 32 | YES | `தொழிற்சாலைகளுக்கும்` / `தலைவர்கள்` (`லை`), `டிரான்ஸ்பார்மர்களை` (`ளை`), `கூறினார்கள்` (`னா`) | 0 | 0 |

No positive occurrence requiring correction was found for `ணை / ணொ / ணோ / றொ / னோ` in HG6; all were still explicitly checked.

## HG7 page-level coverage

Batch policy is now **10 scan pages per iteration**; this final gate batch contains the remaining 7 scans because the locked Assembly boundary is scan 40.

| Scan | Printed | All 13 families checked | Representative source-supported identities | Corrections | Unresolved glyph clusters |
|---:|:---:|---|---|---:|---:|
| 34 | 33 | YES | `கருணாநிதி` (`ணா`), `நிலையங்களின்` (`லை`), `ஏற்பாடுகளை` (`ளை`), `பார்க்கிறோமே` (`றோ`), `சென்னையிலுள்ள` (`னை`) | 0 | 0 |
| 35 | 34 | YES | `ஆட்சேபணை` / `விசாரணையில்` (`ணை`), `புகார்களைச்` (`ளை`), `உரையாற்றியிருக்கிறார்` (`றா`), `மனைப்பட்டா` (`னை`) | 0 | 0 |
| 36 | 35 | YES | `தொழிற் சாலை` / `தொழிற்சாலைகளும்` (`லை`), `பணிகளை` (`ளை`), `இருக்கிறார்கள்` (`றா`), `அளித்திருக்கின்றோம்` (`றோ`) | 0 | 0 |
| 37 | 36 | YES | `துணைத்` (`ணை`), `மலைத் தோட்டம்` / `பல்கலைக் கழக` (`லை`), `உரிமையாளனாகிவிடுகிறான்` (`றா` / `னா`) | 0 | 0 |
| 38 | 37 | YES | `அண்ணா` / `அண்ணாதுரை` (`ணா`), `இணைப்புச்` (`ணை`), `அறிவுரைகளையெல்லாம்` / `விளைவு` (`ளை`), `முடிக்கிறார்களோ` (`றா`) | 0 | 0 |
| 39 | 38 | YES | `அண்ணா` (`ணா`), `கலைஞர்` (`லை`), `நீதிகளையெல்லாம்` / `கட்டுரைகளைப்` (`ளை`), `கொண்டிருக்கிறார்கள்` (`றா`), `முனையக்கூடாது` (`னை`) | 0 | 0 |
| 40 | 39 | YES | `குணாளா` (`ணா`), `நிதிநிலை` (`லை`), `கருத்துக்களைப்` (`ளை`), `எழுதியிருக்கிறார்கள்` (`றா`), `கற்றோய்` (`றோ`), `அனைத்துக்` (`னை`) | 0 | 0 |

No positive occurrence requiring correction was found for `ணொ / ணோ / றொ / னொ / னோ` in HG7; all were still explicitly checked.

## Gate C.5 result

**PASS / COMPLETE — scans 4–40 / printed pp.3–39.**

- cumulative historical-glyph corrections: **3**;
- unresolved historical-glyph clusters: **0**;
- global replacements used: **0**;
- downstream Gate D: **unblocked**.

## Exact next activity

Begin **Gate D — Tamil completeness audit** with **scan pp.4–13 / printed pp.3–12** as the first 10-scan-page iteration. Preserve the 10-page iteration policy, but use a shorter final batch rather than crossing a gate or speech boundary.
