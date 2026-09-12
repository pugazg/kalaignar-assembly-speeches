# Crop-recovery audit — 7-3-1973 Assembly reply

## Purpose

The controlling publication scan, `TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`, has physical gutter loss on scans 4–5, 10–11, 20–21, 25–27 and 34–35. Earlier archival work correctly preserved those losses as `⟦scan-crop⟧` rather than guessing.

A newly supplied **official Tamil Nadu Legislative Assembly Debates** PDF for **7 March 1973** now provides an independent primary-source witness for the same speech. This permits evidence-based recovery of text that is physically missing from the booklet scan.

## Recovery source

- file: `927193.pdf`
- record: **Tamil Nadu Legislative Assembly Debates**
- sitting date: **7 March 1973**
- PDF pages: **119**
- bytes: **184,860,788**
- SHA-256: `b56b0e2d70fb64ec026312ca62d925cb2ef7df32feb8a9578848df97461c54b4`
- Karunanidhi's budget reply begins near PDF p.86 / printed proceedings p.484 and continues to the close of the sitting.

## Authority rule

1. The `இருளும் ஒளியும்` scan remains controlling wherever its pixels are legible.
2. TNLA proceedings may supply **only material physically absent at the cropped gutter**.
3. Visible booklet wording is never silently replaced merely because the TNLA printing/OCR differs.
4. Recovery must match both surrounding visible booklet text and the official TNLA passage.
5. No grammar-only, memory-based or contextual reconstruction is permitted.
6. English is repaired only after Tamil crop recovery is complete.
7. The prior Unit-1 release is temporarily reopened until Tamil, English and canonical integrity are revalidated.

## CR1 — scans 4–5 and 10–11

Status: **PASS / COMPLETE**

- scans recovered: **4, 5, 10, 11**
- actual Tamil `⟦scan-crop⟧` placeholders removed: **99**
- unresolved crop placeholders on these four scans: **0**
- global replacements: **0**
- source-page boundaries retained
- scan-5 illustration note retained
- remaining actual Tamil crop placeholders after CR1: **226**

### Evidence map

| Booklet scan | Printed p. | TNLA evidence | Result |
|---:|:---:|---|---|
| 4 | 3 | TNLA PDF pp.86–87 / proceedings pp.484–485; opening reply, 81/175/38/58/43 figures and start of Thangamani passage | recovered |
| 5 | 4 | TNLA PDF p.87 / proceedings p.485; Hande/Ananthanayaki/Ponnappa Nadar continuation and 62-day Palayamkottai passage | recovered |
| 10 | 9 | TNLA PDF pp.91–92 / proceedings pp.489–490; Kasiraman land-tax comparison and agricultural-income-tax explanation | recovered |
| 11 | 10 | TNLA PDF pp.92–93 / proceedings pp.490–491; Gopal industrial-development figures and transition to James | recovered |

### Recovery-specific observations

- On scan 4, the source pixels themselves preserve the final `க்` in `சுதந்திரக்`; scan 5 continues `கட்சியின் சார்பில்...`. TNLA confirms the cross-page phrase.
- Scan 5 still ends at the source-supported page boundary `பாளையங்`; scan 6 begins `கோட்டைச் சிறைச்சாலையில்...`.
- Numerical/source forms already visible in the booklet — including `6·56`, `4·48`, `7·50`, `6·3`, and source spacing such as `குறைக்க வில்லை` — were retained rather than normalized.

## Remaining crop-recovery work

- **CR2:** scans **20–21 and 25–27**
- **CR3:** scans **34–35**
- then: whole-Tamil recovery audit
- then: English repair/retranslation for recovered spans
- then: English fidelity recheck and Gate-H canonical revalidation/re-release.

## Page-by-page revalidation

The recovery workflow is now proceeding **one booklet page at a time**. A page is not considered revalidated merely because an earlier bulk recovery removed its placeholders.

### Booklet scan 4 / printed p.3

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **4**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF pp. **86–87** / proceedings pp. **484–485**;
- the TNLA witness confirms the same opening reply, the **81 / 175 / 38 / 58 / 43** figures, the first procedural paragraph, and the opening of the Thangamani discussion;
- visible booklet wording remains controlling wherever legible.

Review result:

- old page-4 `⟦scan-crop⟧` markers reviewed: **38**;
- page-4 markers remaining: **0**;
- source line breaks: **preserved**;
- direct missing-fragment recoveries: **10**;
- other edge markers required no additional textual fragment after the official witness confirmed the continuation;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct recovered fragments:

1. `மாமன்ற` → `மாமன்றத்`
2. `காங்கிர` → `காங்கிரஸ்`
3. `அவர்க` → `அவர்கள்`
4. `கழ` → `கழக`
5. first `உறுப்பினர` → `உறுப்பினர்`
6. `அவரவர்க` → `அவரவர்கள்`
7. `இரு` → `இருந்`
8. second `உறுப்பினர` → `உறுப்பினர்`
9. `பாராட்டுதல` → `பாராட்டுதலை`
10. final `சுதந்திர` → `சுதந்திரக்`

Cross-page boundary is now explicit and source-supported:

- scan 4 ends: `... எனக்கு அது புரிந்தது. சுதந்திரக்`
- scan 5 begins: `கட்சியின் சார்பில் ...`

Exact next page-by-page activity: **booklet scan 5 / printed p.4**.

### Booklet scan 5 / printed p.4

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **5** / printed p. **4**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF p. **87** / proceedings p. **485**;
- the witness confirms the Hande / Ananthanayaki / Ponnappa Nadar continuation, the Congress-governance comparison, **20 ஆண்டுக் காலம்**, and the **62 நாட்கள்** Palayamkottai passage;
- visible booklet wording remains controlling wherever legible.

Marker accounting:

- the pre-recovery scan-5 block contains **16 literal** `⟦scan-crop⟧` occurrences;
- **15** are source-loss placeholders at the left edge of printed lines;
- **1** is the literal token quoted inside the explanatory scan-condition note;
- page-level source-loss positions revalidated: **15 / 15**;
- source-loss markers remaining on scan 5: **0**;
- source line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct missing-fragment recoveries, in physical line order:

1. `கட்` + `சியின்` → `கட்சியின்`
2. `எ` + `னக்குப்` → `எனக்குப்`
3. `தி` + `ருமதி` → `திருமதி`
4. `வ` + `ர்கள்` → `வர்கள்`
5. `ப` + `ழைய` → `பழைய`
6. `நா` + `டார்` → `நாடார்`
7. `அ` + `து` → `அது`
8. `கட்` + `சியோ` → `கட்சியோ`
9. `கி` + `ரஸ்` → `கிரஸ்` after the preceding line's visible `காங்`
10. `ஆ` + `ட்சிப்` → `ஆட்சிப்`
11. `கட்` + `சிகள்` → `கட்சிகள்`
12. `அ` + `வர்களுடைய` → `அவர்களுடைய`
13. `கா` + `லம்` → `காலம்`
14. `ந` + `ம்முடைய` → `நம்முடைய`
15. missing line opening before visible `பொன்னப்ப நாடார்...` → `திரு. `, confirmed by the official witness's `தலைவர் திரு. பொன்னப்ப நாடார்` sequence.

Page-level correction to earlier bulk CR1:

- the bulk pass had collapsed the last two booklet lines into `... கட்சியின் தலைவரான பொன்னப்ப நாடார் ...`;
- high-resolution booklet reinspection does **not** support that join at the cropped edge;
- the booklet visibly ends the preceding line with `தலைவர்`;
- TNLA p.87 / proceedings p.485 independently gives `தலைவர் திரு. பொன்னப்ப நாடார்`;
- canonical Tamil is therefore restored as the physical two-line sequence:
  - `நம்முடைய நிறுவன காங்கிரஸ் கட்சியின் தலைவர்`
  - `திரு. பொன்னப்ப நாடார் அவர்கள் என்னை 62 நாட்கள் பாளையங்`.

Page-boundary evidence:

- incoming boundary remains: scan 4 ends `சுதந்திரக்`; scan 5 begins `கட்சியின் சார்பில்...`;
- scan 5 ends exactly `பாளையங்`;
- scan 6 begins `கோட்டைச் சிறைச்சாலையில்...`;
- no text from scan 6 was moved backward into scan 5.

Illustration text retained from the booklet:

- `சட்டசபைத் தொடரின் போது (1965)`
- `62`
- `நாட்கள் பாளையச் சிறையில்`

Exact next page-by-page activity: **booklet scan 10 / printed p.9**. Do not process scan 11 in the same iteration.

