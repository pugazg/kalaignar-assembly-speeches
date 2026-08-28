# Visual-fidelity audit — நமது நிலை

## Baseline

The **user-supplied word-to-word transcription in the source-intake prompt** is the first-pass transcription baseline for this PDF.

It is **not authoritative**. Every word, numeral, heading, speaker label and clearly printed punctuation/compound form must be checked directly against the rendered scan. OCR-like material from library stamps, handwriting and other later marks is not canonical publication text.

This audit is being performed at the **source level** while the exact dated/House-level canonical speech split remains unresolved. It is a visual-fidelity verification of the supplied first pass; it does not by itself mark a canonical speech `verified` under Gate E.

## Audit method

For each bounded batch:

1. compare the supplied first-pass text against the rendered scan word by word;
2. preserve source anomalies rather than silently correcting them;
3. record every confirmed discrepancy before applying any canonical correction;
4. distinguish substantive/orthographic discrepancies from mere physical line wrapping;
5. do not treat Connemara Public Library stamps, handwriting or scan artefacts as publication text.

## Batch 1 — scan pp. 1–10 / printed front matter + pp. 1–8

Status: **complete**.

### Scan p. 1 — cover

- Cover title and attribution visually confirmed: `நமது நிலை`; `தமிழக முதல்வர் கலைஞர் மு.கருணாநிதி`.
- The large `10 JUN 1971` / Connemara Public Library stamp is later library matter. Any OCR text derived from that stamp in the supplied extraction is **not** part of the publication transcription.

### Scan p. 2 — unnumbered front matter

**Confirmed discrepancy 1**

- First pass: `துல்லியமான, விளக்குபான விடை அளித்தார்கள்.`
- Scan: `துல்லியமான, விளக்கமான விடை அளித்தார்கள்.`
- Type: OCR/letter substitution.
- Action for corrected source text: `விளக்குபான` → `விளக்கமான`.

No other word-level discrepancy was confirmed on this page in this pass. Library handwriting crossing the lower paragraph is later annotation and must not enter the transcription.

### Scan p. 3 / printed p. 1

**Confirmed discrepancy 2**

- First pass: `ஆளுநர் சந்தார் உஜ்ஜல்சிங்`
- Scan: `ஆளுநர் சர்தார் உஜ்ஜல்சிங்`
- Type: name/letter error.
- Action: `சந்தார்` → `சர்தார்`.

No other word-level discrepancy was confirmed on this page.

### Scan p. 4 / printed p. 2

**Confirmed discrepancy 3**

In the section `ஜனநாயக மரபு`:

- First pass: `அதுதான் ஜனநாயகத்திலே போற்றிப் பாராட்டவேண்டிய ஒன்று.`
- Scan: `அதுதான் ஜனநாயகத்திலே போற்றிப் பாராட்டவேண்டிய நல்ல மரபாகும்.`
- Type: substantive phrase substitution/omission in first pass.
- Action: replace `ஒன்று` with source-supported `நல்ல மரபாகும்`.

No other word-level discrepancy was confirmed on this page in this pass.

### Scan p. 5 / printed p. 3

No substantive word-level discrepancy was confirmed in this pass.

The scan does preserve several compound/spacing forms that should be respected during final source transcription (for example forms around `ஒரு போதும்` / `வழக்காடப் போவதாக`). These will be handled in the dedicated spacing/punctuation normalization check rather than silently modernised.

### Scan p. 6 / printed p. 4

**Confirmed discrepancy 4**

- First pass: `குறைகளுக்கும் குற்றங்களுக்கும் இடையே உள்ள வேறுபாட்டை ஆழ்ந்து கவனிக்கவேண்டும்.`
- Scan: `குறைகளுக்கும் குற்றங்களுக்கும் இடையே உள்ள வேறுபாட்டை நாம் ஆழ்ந்து கவனிக்கவேண்டும்;`
- Type: omitted word.
- Action: restore `நாம்` after `வேறுபாட்டை`.

### Scan p. 7 / printed p. 5

**Confirmed discrepancy 5**

Under `சேலம் நிகழ்ச்சி; ஒரு விளக்கம்!`:

- First pass: `சேலத்தில் நடைபெற்ற சம்பவங்களை யாரும் ஏற்றுக் கொள்ள இயலாது.`
- Scan: `சேலத்தில் நடைபெற்ற சம்பவங்கள் யாரும் ஏற்றுக் கொள்ள இயலாது.`
- Type: source anomaly silently normalised by first pass.
- Action: preserve the printed `சம்பவங்கள்`; do **not** improve it to the grammatically expected `சம்பவங்களை`.

The later phrase `என்று நான் கேட்கவில்லை.` was rechecked visually and the supplied first pass is correct there; no correction is required.

### Scan p. 8 / printed p. 6

**Confirmed discrepancy 6**

Under `தவறைச் செய்து காட்டுவது முறையா?`:

- First pass: `அப்படிபட்ட நேரத்தில் அதைப் புகைப்படமும் எடுத்து விடுகிறான் ஒருவன்.`
- Scan: `அப்படி அடிபட்ட நேரத்தில் அதைப் புகைப்படமும் எடுத்து விடுகிறான் ஒருவன்.`
- Type: word loss/merger.
- Action: `அப்படிபட்ட` → `அப்படி அடிபட்ட`.

### Scan p. 9 / printed p. 7

**Confirmed discrepancy 7**

- First pass: `1965-ஆம் ஆண்டு`
- Scan: `1965-ம் ஆண்டு`
- Type: source orthography/number suffix normalised in first pass.
- Action: preserve `1965-ம் ஆண்டு`.

**Confirmed discrepancy 8**

- First pass: `'மாலை மணி' பத்திரிக்கை மீது`
- Scan: `'மாலை மணி' பத்திரிகை மீது`
- Type: spelling.
- Action: `பத்திரிக்கை` → `பத்திரிகை` in this occurrence.

**Confirmed discrepancy 9**

- First pass: `'பெரியார் பொன்மொழி'`
- Scan: `'பெரியார் பொன் மொழி'`
- Type: printed compound spacing.
- Action: preserve the two-word printed form `பொன் மொழி`.

**Confirmed discrepancy 10**

- First pass: `பத்திரிக்கைச் சுதந்திரம் பறி போயிற்று`
- Scan: `பத்திரிகைச் சுதந்திரம் பறி போயிற்று`
- Type: spelling.
- Action: `பத்திரிக்கைச்` → `பத்திரிகைச்`.

### Scan p. 10 / printed p. 8

No word-level discrepancy was confirmed in this pass.

## Batch 1 totals

- Physical scan pages visually checked: **10 / 60** (including cover and front matter).
- Printed speech pages visually checked: **1–8**.
- Confirmed first-pass discrepancies: **10**.
- Unresolved readings in this batch: **0**.
- Canonical text modified: **no** — this file records discrepancies first, as requested.

## Exact continuation point

Continue the same word-by-word visual comparison at:

- **scan p. 11 / printed p. 9**,
- beginning with the continuation of `அரசியலும் கொலைகளும்.`

Report newly confirmed discrepancies before applying them to any canonical transcript.
