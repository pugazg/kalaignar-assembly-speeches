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

- **CR2:** scans **26–27** (scans 20–21 and 25 are now page-level closed)
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

### Booklet scan 10 / printed p.9

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **10** / printed p. **9**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF pp. **91–92** / proceedings pp. **489–490**;
- the witness confirms the Kasiraman land-tax comparison and the transition into the agricultural-income-tax explanation;
- visible booklet wording, numerals, punctuation and spacing remain controlling wherever legible.

Marker accounting:

- pre-recovery scan-10 block literal `⟦scan-crop⟧` occurrences: **29**;
- line-level right-gutter source-loss positions: **28**;
- explanatory-note literal-token occurrences: **1**;
- page-level source-loss positions revalidated: **28 / 28**;
- source-loss markers remaining on scan 10: **0**;
- booklet physical line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct missing-fragment recoveries, in physical line order:

1. `காசிராம` + `ன்` → `காசிராமன்`
2. `இல்ல` + `ா` → `இல்லா` before next-line `விட்டாலும்`
3. `வ` + `ந்` → `வந்` before next-line `திருக்கின்ற`
4. `அளிக்` + `க` → `அளிக்க`
5. `அவர்க` + `ள்` → `அவர்கள்`
6. `பாசன வ` + `ரி,` → `பாசன வரி,`
7. `எல்லா` + `ம்` → `எல்லாம்`
8. `மொத்த` + `ம்` → `மொத்தம்`
9. `தொகையு` + `ம்` → `தொகையும்`
10. `மாற்றம் இல்ல` + `ை.` → `மாற்றம் இல்லை.`
11. `நில வரியை` + `க்` → `நில வரியைக்`
12. `என்ற` + `ு` → `என்று`

The other **16** line-level crop positions were independently checked against the official witness and require **no inserted fragment**: the booklet line already ends on a complete word/morpheme, or the word continues visibly at the beginning of the next physical line (for example `செய்துகொண்டிருக்` → next-line `கிற`, `கிடைத்திருக்` → next-line `கிறது`, and `இவை` → next-line `களெல்லாம்`).

Page-level correction to earlier bulk CR1:

- bulk CR1 had `ஆகவே நில வரியை குறைத்தோம்`;
- the cropped booklet ends the physical line at `நில வரியை...`;
- TNLA p.92 / proceedings p.490 independently confirms `நில வரியைக் குறைத்தோம்`;
- the missing right-gutter `க்` is therefore restored, without changing any other booklet-visible wording.

Page-boundary evidence:

- incoming boundary: scan 9 closes the Hande agricultural-expenditure response with `... நான் எடுத்துக் காட்ட விரும்புகிறேன்.`; scan 10 begins `ஆளும் காங்கிரஸ் கட்சியைச் சேர்ந்த திரு காசிராமன்...`;
- scan 10 ends `வித்துக் கொள்கிறேன்.`;
- scan 11 begins the heading `தொழில் அபிவிருத்தி`;
- no text was moved across either page boundary.

Exact next page-by-page activity completed below: **booklet scan 11 / printed p.10**.

### Booklet scan 11 / printed p.10

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **11** / printed p. **10**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF pp. **92–93** / proceedings pp. **490–491**;
- the witness confirms the Gopal industrial-development figures and the transition into the James passage;
- visible booklet wording, numerals, punctuation and spacing remain controlling wherever legible.

Marker accounting:

- pre-recovery scan-11 block literal `⟦scan-crop⟧` occurrences: **16**;
- line-level left-gutter source-loss positions: **15**;
- explanatory-note literal-token occurrences: **1**;
- page-level source-loss positions revalidated: **15 / 15**;
- source-loss markers remaining on scan 11: **0**;
- booklet physical line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct missing-fragment recoveries, in physical line order:

1. `ம்பம்` → `கம்பம்` (recovered `க`)
2. `வர்கள்` → `அவர்கள்` (recovered `அ`)
3. `பிவிருத்திக்காக` → `அபிவிருத்திக்காக` (recovered `அ`)
4. `973-74-ல்` → `1973-74-ல்` (recovered `1`)
5. `ன்று` → `என்று` (recovered `எ`)
6. `க்கம் 37-ஐப்` → `பக்கம் 37-ஐப்` (recovered `ப`)
7. `ரிந்து கொள்ளலாம்` → `புரிந்து கொள்ளலாம்` (recovered `பு`)
8. `ன்ற தலைப்பில்` → `என்ற தலைப்பில்` (recovered `எ`)
9. `965-66-ஆம்` → `1965-66-ஆம்` (recovered `1`)
10. `துக்கப்பட்டிருக்கிற` → `ஒதுக்கப்பட்டிருக்கிற` (recovered `ஒ`)
11. `ன்கு கோரிக்கைகளின்` → `நான்கு கோரிக்கைகளின்` (recovered `நா`)

The other **4** line-level crop positions were independently checked against the official witness and require **no inserted fragment**:

- `தொழில்கள் என்ற தலைப்பின் கீழ்...` already begins with a complete source word;
- `விடக்கூடாது...` already begins with a complete source word;
- `தொழிலுக்காக...` already begins with a complete source word;
- `கையை மாத்திரம்...` is the visible continuation of the previous physical-line `கோரிக்`.

Bulk-CR1 page-level result:

- no lexical recovery from bulk CR1 had to be reversed on scan 11;
- the page was restored from the bulk collapsed paragraph to the booklet's physical line sequence;
- the booklet-visible figures `6·56`, `4·48`, `7·50`, `3·35`, `7·5` and `15` were retained without normalization.

Page-boundary evidence:

- incoming boundary: scan 10 ends `வித்துக் கொள்கிறேன்.`; scan 11 begins heading `தொழில் அபிவிருத்தி`;
- scan 11 ends `என்று சொல்லிவிடாமல், என்பால் அன்பு வைத்து, அவர்கள்`;
- scan 12 begins `இந்த நிதி நிலை அறிக்கையில் தன்னுடைய ஆழ்ந்த கருத்துக்களையெல்லாம்...`;
- TNLA proceedings p.491 confirms the same James-passage continuation;
- no text was moved across either page boundary.

Exact next page-by-page activity: **booklet scan 20 / printed p.19**. Do not process scan 21 in the same iteration.

### Booklet scan 20 / printed p.19

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **20** / printed p. **19**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**;
- principal witness span: TNLA PDF pp. **100–101** / proceedings pp. **498–499**;
- the final Karunanidhi continuation on this booklet page is confirmed on TNLA PDF p. **102** / proceedings p. **500**;
- the witness confirms the national-income / money-supply close, the Ananthanayaki and Hande interventions, and the closing production / economic-growth response;
- visible booklet wording remains controlling wherever legible.

Marker accounting:

- pre-recovery scan-20 block literal `⟦scan-crop⟧` occurrences: **41**;
- actual line-level right-gutter source-loss positions: **40**;
- explanatory-note literal-token occurrences: **1**;
- page-level source-loss positions revalidated: **40 / 40**;
- direct missing-fragment/punctuation recoveries: **33**;
- complete-at-edge / visible-next-line positions requiring no inserted fragment: **7**;
- source-loss markers remaining on scan 20: **0**;
- booklet physical line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct recoveries, in physical line order:

1. `தா` → `தான்`
2. `விரும்புகின்றே` → `விரும்புகின்றேனே`
3. first `தலைவரவர்களே` → `தலைவரவர்களே,`
4. `மத்தி` → `மத்திய`
5. `பேசிக்கொ` → `பேசிக்கொண்` before next-line `டிருந்தார்கள்`
6. `நின்றபோ` → `நின்றபோதே`
7. `உணர்ச்ச` → `உணர்ச்சி` before next-line `யோடு`
8. `வி` → `விலை` before next-line `வாசியைக்`
9. `ஆட்சிக்` → `ஆட்சிக்கு`
10. `என்` → `என்று`
11. `பங்` → `பங்கு`
12. `இன்றை` → `இன்றைக்` before next-line `குத்`
13. `மத்திய அ` → `மத்திய அர` before next-line `சிடம்`
14. `என்ன செய்வது` → `என்ன செய்வது?`
15. `பொறு` → `பொறுப்` before next-line `பேற்று`
16. `சொன்னோம்` → `சொன்னோம்.`
17. `எங்களுக்` → `எங்களுக்கு`
18. `சேர்த்துத்தா` → `சேர்த்துத்தான்`
19. `மதி` → `மதிப்` before next-line `புக்குரிய`
20. `நானு` → `நானும்`
21. `உடனே` → `உடனே,`
22. `இன்கிரீஸ்` → `இன்கிரீஸ்ட்`
23. `செய்தால்தா` → `செய்தால்தான்`
24. `அதற்` → `அதற்கு`
25. second `தலைவரவர்களே` → `தலைவரவர்களே,`
26. `சொல்` → `சொல்ல`
27. `அவ` → `அவர்`
28. `அவர்க` → `அவர்கள்`
29. `குறிப்பி` → `குறிப்பிட்` before next-line `டார்கள்`
30. `பெருகினால்தா` → `பெருகினால்தான்`
31. `இப்படி ஏ` → `இப்படி ஏற்` before next-line `படுகிற`
32. `பெருகி` → `பெருகிட`
33. `நா` → `நான்`

The **7** source-loss positions requiring no inserted fragment were independently checked against the official witness: line endings `இந்த`, `சர்வே`, `பாராளு`, `தடுத்து`, `உங்களுக்குச்`, `பேச்சு`, and `கேட்டேன்.` are already complete in the booklet and continue naturally on the next physical line where applicable.

Visible-booklet fidelity correction found during this page-level pass:

- prior canonical text: `வந்தால் வறுமையெல்லாம் குறைப்போம்`
- booklet scan 20 visibly reads: `வந்தால் வரியையெல்லாம் குறைப்போம்`
- TNLA p.101 / proceedings p.499 independently confirms `வரியையெல்லாம்`
- canonical Tamil was corrected to the booklet-visible form; this is not a TNLA normalization.

Page-boundary evidence:

- incoming boundary: scan 19 ends `... அந்தச் சங்கடம் அவர்களுக்கு இருக்கிறது. ஆகவே,`; scan 20 begins `பொறுப்பு மாநில அரசுக்கு அல்ல; மத்திய அரசுக்குத் தான்`;
- scan 20 ends `இங்கே சுட்டிக் காட்டினேன்.`;
- scan 21 begins `அது மாத்திரமல்ல, இன்னும் சில காரணங்கள் இருக்...`;
- no text was moved across either page boundary.

Exact next page-by-page activity: **booklet scan 21 / printed p.20**. Do not process scan 25 in the same iteration.

### Booklet scan 21 / printed p.20

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **21** / printed p. **20**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF pp. **102–103** / proceedings pp. **500–501**;
- the witness confirms the tax-evasion / black-money continuation, Ponnappa Nadar intervention, and rice / food-price-control response;
- visible booklet wording remains controlling wherever legible.

Marker accounting:

- pre-recovery scan-21 block literal `⟦scan-crop⟧` occurrences: **29**;
- actual line-level left-gutter source-loss positions: **28**;
- explanatory-note literal-token occurrences: **1**;
- page-level source-loss positions revalidated: **28 / 28**;
- direct missing-fragment recoveries from the official witness: **1**;
- positions requiring no witness-supplied insertion: **27**;
- source-loss markers remaining on scan 21: **0**;
- booklet physical line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct missing-fragment recovery:

1. previous line ends `இருக்`; cropped next line `ன்றன. ...` → `கின்றன. ...`, giving the cross-line booklet word `இருக்கின்றன`; TNLA p.500 independently confirms the same word.

Two additional **booklet-visible fidelity corrections** were found while the cropped edge was re-read at high resolution:

1. pre-recovery `டிப்பட்டு விடுகிற காரணத்தால்` → `அடிபட்டு விடுகிற காரணத்தால்`; the booklet itself visibly preserves `அடிபட்டு`, and TNLA p.500 independently agrees.
2. pre-recovery single-quote rendering `‘அன் அக்கெளண்டட் மணி’` → booklet-visible double quotation `“அன் அக்கெளண்டட் மணி”`.

All other **27** marked left-edge positions either begin with complete booklet-visible text or are explicit physical-line continuations already preserved in the adjacent line sequence, including `வைத்திருப்பவர் / களே`, `என் / னென்ன`, `முத / லமைச்சரவர்கள்`, `கட்டுப் / படுத்தக்கூடிய`, `படுத்து / கிறோம்`, and `முக் / கியமான`.

Booklet-specific forms retained rather than normalized to the TNLA printing include:

- `கட்டுப் படுத்து / கிறோம்`;
- `கட்டுப் பாட்டிற்குள்`;
- `மிக முக் / கியமான அரிசி விலையை`;
- `பொருட்களுக்கெல்லாம்`;
- `மாநிலங்களே நம்பியிருக்க`;
- `பரவிக்கிடக்கின்ற`.

Illustration text retained from the booklet:

- `வரி ஏய்ப்பு`

Page-boundary evidence:

- incoming boundary: scan 20 ends `இங்கே சுட்டிக் காட்டினேன்.`; scan 21 begins `அது மாத்திரமல்ல, இன்னும் சில காரணங்கள் இருக்`;
- scan 21 ends `காரணத்தால்—இப்பொருள்களின் விலையைக் கட்டுப்படுத்து`;
- scan 22 begins `கின்ற சூழ்நிலை இல்லாத காரணத்தால்—தீர்க்க முடியாத சங்கடத்திற்கு நாம் ஆளாகி இருக்கிறோம்.`;
- the cross-page word is therefore `கட்டுப்படுத்துகின்ற`, with no text moved across the booklet boundary.

Exact next page-by-page activity: **booklet scan 25 / printed p.24**. Do not process scan 26 in the same iteration.

### Booklet scan 25 / printed p.24

Status: **PASS / PAGE-LEVEL RECOVERY VERIFIED**

Evidence:

- controlling booklet: `இருளும் ஒளியும்`, scan **25** / printed p. **24**;
- independent official witness: *Tamil Nadu Legislative Assembly Debates*, **7 March 1973**, TNLA PDF pp. **104–105** / proceedings pp. **502–503**;
- the witness confirms the Kerala / Mysore / Andhra / Tamil Nadu daily electricity-demand comparison, hydroelectric-shortfall explanation, ten-project list, Ananthanayaki English intervention, and opening of Ponnappa Nadar's question;
- visible booklet wording remains controlling wherever legible.

Marker accounting:

- pre-recovery scan-25 block literal `⟦scan-crop⟧` occurrences: **38**;
- actual line-level left-gutter source-loss positions: **37**;
- explanatory-note literal-token occurrences: **1**;
- page-level source-loss positions revalidated: **37 / 37**;
- direct missing-character/punctuation recoveries from the official witness: **4**;
- positions requiring no witness-supplied insertion: **33**;
- source-loss markers remaining on scan 25: **0**;
- booklet physical line breaks: **preserved**;
- contextual/grammar-only guesses: **0**;
- global replacements: **0**.

Direct recoveries, in physical line order:

1. `டுத்துக்கொண்டால்` → `எடுத்துக்கொண்டால்`, restoring the cropped initial `எ`.
2. `1) சேர்வலாறு` → `(1) சேர்வலாறு`, restoring the cropped opening parenthesis.
3. `3) சொலாட்டிப்புழா` → `(3) சொலாட்டிப்புழா`, restoring the cropped opening parenthesis.
4. English `ave been sent ...` → `have been sent ...`, restoring the cropped initial `h`.

The remaining **33** marked positions require no inserted text after booklet/TNLA comparison: they either begin with a complete booklet-visible word or preserve an intentional physical-line continuation, including `கிட்டத் / தட்டப்போய்த்`, `கேட்க / வில்லையா`, `மேல் அமரா / வதித்`, and `திட்ட / மானது`.

Booklet-visible forms retained rather than normalized to the TNLA printing include:

- `இலட்சம்` throughout the electricity-demand figures;
- `நெல்லித்துறைத் திட்டம்`;
- `சொலாட்டிப்புழா திட்டம்`;
- `மேல் அமரா / வதித் திட்டம்` with the booklet physical line break;
- `சண்முகா நதித் திட்டம்`;
- the booklet's English lineation of Ananthanayaki's intervention.

Figures and dates rechecked:

- daily demand: **60 / 130 / 90 / 280 / 225** இலட்சம் யூனிட்;
- Tamil Nadu pump connections: **6 இலட்சம்**;
- project-request years: **71, 72, 73**;
- ten-project total: **1,035 மெகாவாட்**;
- English intervention: **1974–1979** Fifth Plan reference.

No additional non-crop booklet-fidelity correction was required on this page.

Page-boundary evidence:

- incoming boundary: scan 24 closes the preceding electricity-production comparison and its printed map/illustration labels; scan 25 begins `இன்னொன்றையும் மறந்துவிடக்கூடாது. கேரளாவை`;
- scan 25 ends `மானது, நான்காவது திட்டத்தில் உட்படுத்தப்பட்டிருக்`;
- scan 26 begins `கிறதா? அல்லது ஐந்தாவது திட்டத்தில்...`;
- the cross-page word is therefore `உட்படுத்தப்பட்டிருக்கிறதா?`, with no text moved across the booklet boundary.

Exact next page-by-page activity: **booklet scan 26 / printed p.25**. Do not process scan 27 in the same iteration.

