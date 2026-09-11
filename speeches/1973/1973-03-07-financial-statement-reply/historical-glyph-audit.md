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
| 14–40 | 13–39 | NOT YET AUDITED | 0 | not yet assessed |

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

## Exact next activity

Continue the Gate C.5 source-pixel audit with **scan pp.14–18 / printed pp.13–17**. Check all 13 families on every page, apply only individually proven glyph-identity corrections, synchronize this ledger and `verification-log.md`, and do not start Gate D until scans 4–40 have passed.
