# Verification log — உரை : 8 / 29.04.1999

## Source preflight and boundary re-confirmation

Controlling PDF:

- actual pages: **329**;
- file size: **217,124,211 bytes**;
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`;
- Speech-8 scan range: **241–277**;
- printed range: **240–276**.

Before Gate C started, the locked boundaries were re-confirmed directly from the rendered scan:

- p.241 begins `உரை : 8`, `நாள் : 29.04.1999`;
- p.277 is the Speech-8 closing page;
- p.278 begins `உரை : 9`, `நாள் : 8.05.2000`, and is excluded.

## Gate C — Tamil first-pass transcription

**Complete — 37/37 mapped pages.**

### Batch 1 — scan pp.241–255 / printed pp.240–254

- pages: **15**;
- canonical source-page range: **241–255**;
- unresolved/`REVIEW` readings: **0**.

### Batch 2 — scan pp.256–270 / printed pp.255–269

- pages: **15**;
- canonical source-page range: **256–270**;
- canonical Batch-2 merge checkpoint: `1da567dc66d89847bfa10704254d8bf9e3c8b46a`;
- unresolved/`REVIEW` readings: **0**.

### Batch 3 — scan pp.271–277 / printed pp.270–276

- pages: **7**;
- canonical source-page range: **271–277**;
- unresolved/`REVIEW` readings: **0**;
- canonical Gate-C completion checkpoint: `d0fd3ea71f29838299eb5d7008e4149b7399498c`.

## Gate D — Tamil completeness/page-marker audit

**Passed.** The complete canonical Tamil layer contains all 37 source-page markers in exact sequence 241–277, with no gaps, duplicates, reordering or Speech-9 spillover. Opening, interventions and final p.277 closing structure are intact. Unresolved `REVIEW` markers: **0**.

Tamil status after Gate D: **reviewed, not verified**. Character-level and source-fidelity verification still requires Gate E.

## Gate E — strict Tamil visual/source-fidelity verification

**In progress.**

### Batch 1 — scan pp.241–245 / printed pp.240–244

Pages checked directly against rendered scan images: **5/5**.

Definite corrections applied to canonical `transcript.md`:

1. p.241 `நிதிமன்றத்திலே` → `நீதிமன்றத்திலே`;
2. p.243 first `பொது ஒப்பந்த முறையில்` → `பொது ஒப்பந்த முறைப்படி`;
3. p.243 second `பொது ஒப்பந்த முறையில்` → `பொது ஒப்பந்த முறைப்படி`;
4. p.243 `நிதிமன்ற இடைக்காலத் தடையை` → `நீதிமன்ற இடைக்காலத் தடையை`;
5. p.244 `நடைபெற்றிருக்கிறது` → `நடைபெற்றிருக்கின்றது`.

Batch-1 canonical correction checkpoint: `201b5eff42382bcb6192475be75e01a6865ed921`.

Batch-1 result: verified **5/37** pages; corrections **5**; unresolved readings **0**.

### Batch 2 — scan pp.246–250 / printed pp.245–249

Pages checked directly against rendered scan images: **5/5**.

Checks covered wording and individual characters, names, numerals and figures, punctuation where legible, printed English/Latin-script forms, and the p.245→246, p.249→250 and p.250→251 transitions.

Definite corrections applied to canonical `transcript.md`:

1. p.246 `ஊழல்களை எல்லாம்` → `ஊழல்களை யெல்லாம்`;
2. p.246 `எடுத்து வருகிறார்` → `எடுத்து வருகின்றார்`;
3. p.247 `முதலமைச்சர்கூட` → `முதலமைச்சரேகூட`;
4. p.247 `நாளாக` → `நானாக`;
5. p.248 `மிக வெற்று` → `மிகை வெற்று`;
6. p.249 `அது தொடர்பான தேவையான கச்சாப் பொருட்கள்` → `அது தொடர்ந்து நடப்பதற்குத் தேவையான கச்சாப்பொருட்கள்`.

Scan p.250 definite corrections: **0**.

Boundary/continuation checks:

- p.245→246: `அது ஊழல் விசாரிப்புக் குழுவிற்கு` → `அனுப்பப்பட்டு...` — intact;
- p.249→250: `தமிழகத்திற்குத் தேவையான, நல்ல வேலைகளை` → `நல்லத் தொழிற்சாலைகளை...` — intact;
- p.250→251: `10.72 சதவிகிதம் கட்டுமானம் உள்ள குஜராத்தில்` → `கரும்பு விலை ஒரு டன் 648 ரூபாய்.` — intact.

Batch-2 canonical correction checkpoint: `bcddfa24237941596f5acaab0531974b783e7b77`.

Batch-2 result:

- verified scan range: **246–250**;
- verified printed range: **245–249**;
- verified pages in batch: **5/5**;
- corrections applied in batch: **6**;
- unresolved readings: **0**.

### Batch 3 — scan pp.251–255 / printed pp.250–254

Pages checked directly against rendered scan images: **5/5**.

Checks covered wording and individual characters, names, numerals/percentages/monetary values, printed English and abbreviations, punctuation/spacing where source-significant, and the p.250→251 and p.255→256 transitions.

Definite corrections applied to canonical `transcript.md`:

1. p.251 `நிதிமன்றத்திற்குச்` → `நீதிமன்றத்திற்குச்`;
2. p.251 `இடைக்காலத்தடையை` → `இடைக் காலத்தடையை`;
3. p.251 `ஏஜென்சியால்` → `ஏஜென்ஸியால்`;
4. p.251 `தாமதமாகும்போலக்கூட` → `தாமதமாகும்போல்கூட`;
5. p.253 `நிபந்தனைகளுக்கு குறைவான` → `நிபந்தனைகளுக்குக் குறைவான`;
6. p.253 `முன்வருமானால்` → `முன் வருமானால்`;
7. p.254 `இருக்கின்றதா` → `இருக்கிறதா`;
8. p.254 `வளருவதற்கு காரணமாக` → `வளருவதற்குக் காரணமாக`;
9. p.255 `அந்த காலகட்டத்திலேதான்` → `அந்தக் காலகட்டத்திலேதான்`;
10. p.255 `அந்தத் திட்ட வரவை` → `அந்தத் திட்ட வரைவை`;
11. p.255 `நிதியமைச்சராக` → `நிதிஅமைச்சராக`;
12. p.255 `தெரிவித்துக்கொள்கிறேன்` → `தெரிவித்துக் கொள்கிறேன்`.

Scan p.252 definite corrections: **0**.

Boundary/continuation checks:

- p.250→251: `10.72 சதவிகிதம் கட்டுமானம் உள்ள குஜராத்தில்` → `கரும்பு விலை ஒரு டன் 648 ரூபாய்.` — intact;
- p.255→256: Speech-history passage closes on p.255 and p.256 begins `இந்தக் காலகட்டத்திலேதான் ஆலங்குளம் சிமெண்ட் தொழிற்சாலையும் அமைக்கப்பட்டது.` — intact.

Batch-3 canonical correction checkpoint: `856297ff79dcb3f2539ac569941e09a27aaeccde`.

Batch-3 result:

- verified scan range: **251–255**;
- verified printed range: **250–254**;
- verified pages in batch: **5/5**;
- corrections applied in batch: **12**;
- unresolved readings: **0**.

### Gate-E cumulative state after Batch 3

- verified scan range: **241–255**;
- verified printed range: **240–254**;
- verified pages: **15/37**;
- cumulative definite corrections: **23**;
- unresolved readings in verified range: **0**.

Tamil status remains **reviewed, not fully verified**. Gate E must cover all 37 pages before Tamil can be marked verified.

## Gates not yet complete

- Gate E strict Tamil visual/source-fidelity verification: **in progress — 15/37 pages verified**.
- Gate F English translation: **blocked**.
- Gate G English fidelity verification: **not started**.
- Gate H release/index: **not started**.

## Next activity

Continue **Gate E Batch 4 — scan pp.256–260 / printed pp.255–259**. Compare canonical Tamil directly against the rendered scan and apply/log only definite source-supported corrections. Do not begin English.
