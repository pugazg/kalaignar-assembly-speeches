# Handover — 1973 `இருளும் ஒளியும்`

## Repository

`pugazg/kalaignar-assembly-speeches`, branch `main`.

**LIVE MAIN IS AUTHORITATIVE.** Fetch live `main` first and preserve newer durable work.

Checkpoint before this handover rewrite:

`33f90a04aec35334b938205f92b1f3fbd5db84a5` — `Advance root status to Unit 2 Gate E E3`

## Active work

**Unit 1 is CLOSED / RELEASED again.** Post-release crop recovery and all downstream revalidation are complete:

- page-level crop recovery — COMPLETE;
- whole-Tamil integrity audit — PASS;
- focused post-recovery Gate E — PASS;
- English recovered-span repair — COMPLETE;
- focused post-recovery Gate G — PASS;
- Gate H canonical bilingual release revalidation — **PASS / REVALIDATED AFTER CROP RECOVERY**.

**Current priority: Unit 2 / `சட்டமன்ற மேலவையில்` / 8-3-1973 — Gate F English translation F1, scans 41–50 / printed pp.40–49. Tamil Gate E is PASS / COMPLETE and verified against scan.**

Do not reopen Unit 1 unless genuinely new controlling-source evidence appears.

## Source hierarchy

### Primary controlling publication

`TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

- 64 scans
- 101,602,456 bytes
- SHA-256: `0330e70d6d7a62e2c84d712966a8436b91956d722134bc71ca0b2329283f8694`
- Unit 1: scans **4–40** / printed pp. **3–39**
- Unit 2: scans **41–62** / printed pp. **40–61**
- visible booklet pixels remain controlling

### Official crop-recovery witness

`927193.pdf`

- Tamil Nadu Legislative Assembly Debates
- sitting date: **7 March 1973**
- 119 PDF pages
- 184,860,788 bytes
- SHA-256: `b56b0e2d70fb64ec026312ca62d925cb2ef7df32feb8a9578848df97461c54b4`
- Karunanidhi reply begins around TNLA PDF p.86 / proceedings p.484

### Recovery rules

1. Booklet pixels win wherever legible.
2. TNLA may supply only text physically missing because of gutter crop.
3. Do not normalize visible booklet wording to TNLA.
4. Do not recover from OCR alone.
5. Never reconstruct from grammar/context.
6. Preserve exact booklet physical line breaks and page boundaries.
7. Record page-specific provenance in `crop-recovery-audit.md`.
8. A bulk-recovered page is not closed until it passes its own page-level revalidation turn.

## Legacy crop-marker inventory

The existing legacy inventory counts literal `⟦scan-crop⟧` occurrences in the affected page blocks:

| Scan | Legacy count |
|---:|---:|
| 4 | 38 |
| 5 | 16 |
| 10 | 29 |
| 11 | 16 |
| 20 | 41 |
| 21 | 29 |
| 25 | 38 |
| 26 | 37 |
| 27 | 38 |
| 34 | 6 |
| 35 | 37 |

Legacy total: **325**.

Bulk CR1 populated scans **4, 5, 10 and 11**, removing **99** literal occurrences. Remaining legacy occurrences: **226** on scans **20–21, 25–27, 34–35**.

Important count clarification established during scan-5 page-level revalidation: the legacy page count can include the literal token written inside the explanatory scan-condition note. For scan 5, the legacy count **16** equals **15 actual line-level source-loss positions + 1 explanatory literal token**. Future page-level work must report both when they differ rather than treating the legacy count as the number of missing text fragments.

## Page 4 — PASS / CLOSED

Booklet scan **4** / printed p.**3** is individually revalidated.

Durable checkpoints:

- `fc5735436e30009bb2f6d82e7908610f8209cf82` — revalidated page-4 transcript
- `380462a399c0ed1d543856a6fd7e9c91df754f49` — page-4 recovery audit
- `eed0f0b487b963755e8eda0e2d23735d61860964` — page-by-page metadata state
- `bb415982708f2eb123629c7fb18cfd593490fe4b` — README advanced to page 5

Result:

- old literal crop-marker occurrences reviewed: **38**
- direct missing-fragment recoveries: **10**
- source-loss markers remaining: **0**
- source line breaks preserved
- figures **81 / 175 / 38 / 58 / 43** checked
- `திரு தங்கமணி வழக்கு` checked
- boundary confirmed: scan 4 ends `சுதந்திரக்`; scan 5 starts `கட்சியின் சார்பில்...`
- contextual guesses: **0**
- global replacements: **0**

## Page 5 — PASS / CLOSED

Booklet scan **5** / printed p.**4** is now individually revalidated.

Durable checkpoints:

- `a3df57ef76ddf8169629ed9309f1af4b427152ed` — page-5 transcript revalidation
- `96da715ea00d07cd7adaf16d9b7266c206830ae4` — page-5 recovery audit
- `47bb9852a18c3f5bd155f8005ec46fdb3048084f` — metadata advanced through page 5
- `31d17e4b003c7e3c768b8d24998724019c11ff82` — README advanced to scan 10
- `c7d39c5a6d8354aeaa73ff3c4f8e17f12c65aa2d` — next-chat prompt advanced to scan 10

Evidence:

- TNLA PDF p. **87** / proceedings p. **485**
- Hande / Ananthanayaki / Ponnappa Nadar continuation confirmed
- Congress-governance comparison confirmed
- `20 ஆண்டுக் காலம்` confirmed with booklet line break preserved
- `62 நாட்கள்` confirmed
- illustration text retained from booklet
- incoming boundary: scan 4 `சுதந்திரக்` → scan 5 `கட்சியின் சார்பில்...`
- outgoing boundary: scan 5 `பாளையங்` → scan 6 `கோட்டைச் சிறைச்சாலையில்...`

Result:

- legacy literal `⟦scan-crop⟧` occurrences: **16**
- actual line-level source-loss positions: **15**
- direct missing-fragment recoveries: **15**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- one earlier bulk-CR1 overreach corrected:
  - unsupported collapsed form: `... கட்சியின் தலைவரான பொன்னப்ப நாடார் ...`
  - page-level verified physical sequence:
    - `நம்முடைய நிறுவன காங்கிரஸ் கட்சியின் தலைவர்`
    - `திரு. பொன்னப்ப நாடார் அவர்கள் என்னை 62 நாட்கள் பாளையங்`
  - the booklet visibly supports the first line ending `தலைவர்`; TNLA independently confirms `தலைவர் திரு. பொன்னப்ப நாடார்`.

## Page 10 — PASS / CLOSED

Booklet scan **10** / printed p.**9** is now individually revalidated.

Evidence:

- TNLA PDF pp. **91–92** / proceedings pp. **489–490**
- Kasiraman land-tax comparison confirmed
- transition into `விவசாய வருமான வரி` confirmed
- all booklet-visible numerals, spelling, punctuation and spacing preserved
- incoming boundary: scan 9 closes `... நான் எடுத்துக் காட்ட விரும்புகிறேன்.`; scan 10 begins `ஆளும் காங்கிரஸ் கட்சியைச் சேர்ந்த திரு காசிராமன்...`
- outgoing boundary: scan 10 ends `வித்துக் கொள்கிறேன்.`; scan 11 begins `தொழில் அபிவிருத்தி`

Result:

- legacy literal crop-marker occurrences: **29**
- actual line-level source-loss positions: **28**
- direct missing-fragment recoveries: **12**
- complete-at-edge / visible-next-line positions requiring no inserted fragment: **16**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- one earlier bulk-CR1 omission corrected:
  - `ஆகவே நில வரியை குறைத்தோம்`
  - → physical line end `ஆகவே நில வரியைக்`
  - next line `குறைத்தோம் என்று சொல்லுவது ஒரு மாயை; ‘Myth’ என்று`
  - TNLA independently confirms the missing `க்`.

## Page 11 — PASS / CLOSED

Booklet scan **11** / printed p.**10** has been individually revalidated.

Result:

- legacy literal crop-marker count: **16**
- actual line-level source-loss positions: **15**
- direct missing-fragment recoveries: **11**
- complete-at-edge / visible-continuation positions requiring no inserted fragment: **4**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- TNLA evidence: PDF pp. **92–93** / proceedings pp. **490–491**
- Gopal figures and James transition rechecked without normalization
- incoming boundary: scan 10 ends `வித்துக் கொள்கிறேன்.`; scan 11 begins `தொழில் அபிவிருத்தி`
- outgoing boundary: scan 11 ends `... என்பால் அன்பு வைத்து, அவர்கள்`; scan 12 begins `இந்த நிதி நிலை அறிக்கையில்...`

## Page 20 — PASS / CLOSED

Booklet scan **20** / printed p.**19** is now individually recovered and revalidated.

Evidence:

- principal TNLA witness: PDF pp. **100–101** / proceedings pp. **498–499**
- closing Karunanidhi continuation: TNLA PDF p. **102** / proceedings p. **500**
- national-income / money-supply close confirmed
- Ananthanayaki and Hande interventions confirmed
- production / economic-growth close confirmed
- incoming boundary: scan 19 ends `... அந்தச் சங்கடம் அவர்களுக்கு இருக்கிறது. ஆகவே,`; scan 20 begins `பொறுப்பு மாநில அரசுக்கு அல்ல; மத்திய அரசுக்குத் தான்`
- outgoing boundary: scan 20 ends `இங்கே சுட்டிக் காட்டினேன்.`; scan 21 begins `அது மாத்திரமல்ல, இன்னும் சில காரணங்கள் இருக்...`

Result:

- legacy literal crop-marker occurrences: **41**
- actual line-level source-loss positions: **40**
- direct missing-fragment/punctuation recoveries: **33**
- complete-at-edge / visible-next-line positions requiring no inserted fragment: **7**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- visible-booklet fidelity correction: `வறுமையெல்லாம்` → `வரியையெல்லாம்`, independently confirmed by TNLA.

## Page 21 — PASS / CLOSED

Booklet scan **21** / printed p.**20** is now individually recovered and revalidated.

Evidence:

- TNLA witness: PDF pp. **102–103** / proceedings pp. **500–501**
- tax-evasion / black-money continuation confirmed
- Ponnappa Nadar intervention confirmed
- rice / food-price-control response confirmed
- `வரி ஏய்ப்பு` illustration label retained
- incoming boundary: scan 20 ends `இங்கே சுட்டிக் காட்டினேன்.`; scan 21 begins `அது மாத்திரமல்ல, இன்னும் சில காரணங்கள் இருக்`
- outgoing boundary: scan 21 `... விலையைக் கட்டுப்படுத்து` → scan 22 `கின்ற சூழ்நிலை...`, preserving cross-page `கட்டுப்படுத்துகின்ற`

Result:

- legacy literal crop-marker occurrences: **29**
- actual line-level source-loss positions: **28**
- direct official-witness missing-fragment recoveries: **1**
- positions requiring no inserted fragment: **27**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- visible-booklet corrections:
  - `டிப்பட்டு` → `அடிபட்டு`;
  - `‘அன் அக்கெளண்டட் மணி’` → `“அன் அக்கெளண்டட் மணி”`.

## Page 25 — PASS / CLOSED

Booklet scan **25** / printed p.**24** is now individually recovered and revalidated.

Evidence:

- TNLA witness: PDF pp. **104–105** / proceedings pp. **502–503**
- Kerala / Mysore / Andhra / Tamil Nadu electricity-demand comparison confirmed
- hydroelectric-shortfall paragraph confirmed
- ten-project list confirmed
- Ananthanayaki English intervention confirmed
- Ponnappa Nadar question opening confirmed
- incoming boundary: scan 25 begins `இன்னொன்றையும் மறந்துவிடக்கூடாது. கேரளாவை` after scan 24's electricity-production comparison/map
- outgoing boundary: scan 25 `... உட்படுத்தப்பட்டிருக்` → scan 26 `கிறதா? ...`, preserving cross-page `உட்படுத்தப்பட்டிருக்கிறதா?`

Result:

- legacy literal crop-marker occurrences: **38**
- actual line-level source-loss positions: **37**
- direct official-witness missing-character/punctuation recoveries: **4**
- positions requiring no inserted fragment: **33**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- direct recoveries:
  - `டுத்துக்கொண்டால்` → `எடுத்துக்கொண்டால்`
  - `1)` → `(1)`
  - `3)` → `(3)`
  - `ave been` → `have been`
- no additional non-crop booklet-fidelity correction was required.

## Page 26 — PASS / CLOSED

Booklet scan **26** / printed p.**25** is now individually recovered and revalidated.

Evidence:

- TNLA witness: PDF pp. **105–106** / proceedings pp. **503–504**
- Ponnappa Nadar question completion confirmed
- Karunanidhi answer confirmed
- Kalpakkam / Neyveli / Tuticorin central-project paragraph confirmed
- Kumarasami fourth-plan passage confirmed
- opening project-approval procedure confirmed
- incoming boundary: scan 25 `... உட்படுத்தப்பட்டிருக்` → scan 26 `கிறதா? ...`
- outgoing boundary: scan 26 ends `பின், திட்டக் குழுவிற்கு அதை அனுப்பும்.`; scan 27 begins `திட்டக் குழுவில் தொழில் நுட்ப ஆலோசனைக் குழு மறு...`

Result:

- legacy literal crop-marker occurrences: **37**
- actual line-level source-loss positions: **36**
- direct official-witness missing-character/punctuation recoveries: **6**
- positions requiring no inserted fragment: **30**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- direct recoveries:
  - `திட்டங்கள` → `திட்டங்கள்`
  - `வருகிறோம்` → `வருகிறோம்.`
  - `பொதுமக்களிட` → `பொதுமக்களிடத்தில்`
  - `உடனடியா` → `உடனடியாக`
  - `ஆராய்ந்து` → `ஆராய்ந்து,`
  - `பெற்` → `பெற்ற`
- one source-visible line-split correction:
  - `உட்படுத்தப்பட்ட` → `உட்படுத்தப்பட்` / next-line `டிருக்கிறதா ?`.

## Page 27 — PASS / CLOSED

Booklet scan **27** / printed p.**26** is now individually recovered and revalidated.

Evidence:

- TNLA witness: PDF pp. **106–107** / proceedings pp. **504–505**
- technical-advisory / Planning Commission approval sequence confirmed
- Nellikuthurai / Servalaru / Paraliyar examples confirmed
- no-approval / machinery-import argument confirmed
- corruption / inquiry passage confirmed
- opening `மத்தியில் இருந்து.........` section confirmed
- incoming boundary: scan 26 ends `பின், திட்டக் குழுவிற்கு அதை அனுப்பும்.`; scan 27 begins `திட்டக் குழுவில் தொழில் நுட்ப ஆலோசனைக் குழு மறு`
- outgoing boundary: scan 27 `... தேர்ந்` → scan 28 `தெடுக்கப்படுகிற ...`, preserving cross-page `தேர்ந்தெடுக்கப்படுகிற`

Result:

- legacy literal crop-marker occurrences: **38**
- actual line-level source-loss positions: **37**
- direct official-witness missing-character recoveries: **10**
- positions requiring no inserted fragment: **27**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- direct recoveries include `மறு / படியும்`, `அளிக் / கிறது`, `ஒரு`, `ஆண்டுகள்`, `சேர்வலாறு`, `அனுப்பப்பட்டன`, `கடற் / கரையில்`, `அப்படி`, `செயல் / பட`, and `நடந்தி / ருக்கிறது`
- booklet-visible fidelity corrections:
  - `கட்` → `கடற்`
  - `திட்டங்களே` → `திட்டங்களை`
  - `நடந்து / கிறது` → `நடந்தி / ருக்கிறது`.

## Page 34 — PASS / CLOSED

Booklet scan **34** / printed p.**33** is now individually recovered and revalidated.

Evidence:

- principal TNLA witness: PDF p. **112** / proceedings p. **510**
- TNLA p.113 / proceedings p.511 checked for continuation context
- Ananthanayaki / Hande exchange confirmed
- cropped Karunanidhi generator/licence response confirmed
- incoming context: scan 33 closes the electricity-relief/private-generator-tax paragraph; scan 34 begins the street-light restriction paragraph
- outgoing boundary: scan 34 `... எப்படியாவது, நாங்கள்` → scan 35 `செலவு செய்துவிட்ட காரணத்தினாலே...`

Result:

- legacy literal crop-marker occurrences: **6**
- actual line-level source-loss positions: **5**
- direct official-witness recoveries: **2**
- positions requiring no inserted fragment: **3**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- recovered:
  - `லைசென்ஸ் வழங்கப்படவில்லை` → `லைசென்ஸ் வழங்கப்படவில்லை.`
  - `முதல் அமைச்ச` → `முதல் அமைச்சர்`
- booklet-visible `லைசென்ஸ்` retained rather than TNLA `லைசென்சே`
- booklet-visible `வந்து` retained where TNLA differs.

## Page 35 — PASS / CLOSED — FINAL LEGACY CROP PAGE

Booklet scan **35** / printed p.**34** is now individually recovered and revalidated.

Evidence:

- TNLA PDF p. **112** / proceedings p. **510** confirms the opening generator/licence continuation;
- TNLA PDF p. **113** / proceedings p. **511** confirms the `குடியிருப்பு மனைப்பட்டா` passage;
- scan 36 / printed p.35 was visually checked for the outgoing boundary;
- incoming boundary: scan 34 `... எப்படியாவது, நாங்கள்` → scan 35 `செலவு செய்துவிட்ட காரணத்தினாலே...`;
- outgoing boundary: scan 35 ends `விவரத்தை நான் இங்கே தெரிவித்துக்கொள்கிறேன்.`; scan 36 begins heading `ஒன்பது அறிவிப்புகள்`.

Result:

- legacy literal crop-marker occurrences: **37**
- actual line-level source-loss positions: **36**
- direct official-witness recoveries: **2**
- positions requiring no inserted fragment: **34**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- contextual guesses: **0**
- global replacements: **0**
- recovered:
  - `,41,000 பேர்` → `1,41,000 பேர்`
  - `ஒரு இலட்சத்து 57 ஆயிரம் பட்டாக்களுக்கான அந்த` → `ஆக, ஒரு இலட்சத்து 57 ஆயிரம் பட்டாக்களுக்கான அந்த`
- dates/figures rechecked: **27-2-1972, 6,764, 15-6-1972, 26,150, 14-9-1972, 28-2-1973, 1,15,227, பிப்ரவரி 1973, 1,48,000, 1,41,000, 8,700**, plus the word-form totals and remaining acknowledgements;
- booklet-visible forms such as `மென்று கேட்டார்கள்`, `பட்ட மாட்டாது`, `ஆட்சேபணை`, and `அக்குலெட்ஜ்மெண்ட்` were retained rather than normalized to TNLA.

All legacy gutter-crop pages in Unit 1 are now individually **PASS / CLOSED**:

**4–5, 10–11, 20–21, 25–27, 34–35**

## Whole-Tamil crop-recovery integrity audit — PASS / COMPLETE

Scope: canonical Tamil scans **4–40 / printed pp.3–39**.

Result:

- Tamil source-page markers **4–40**: **37 / 37**, exactly once and strictly monotonic;
- recovered pages checked: **11 / 11** — scans **4–5, 10–11, 20–21, 25–27, 34–35**;
- legacy gutter placeholders on recovered pages: **0**;
- legacy gutter placeholders anywhere in canonical Tamil: **0**;
- documented recovery boundaries: **9 / 9 PASS**;
- scan-13 smaller cartoon-label hold: **unchanged / separate**;
- booklet-specific wording retained against TNLA differences: **PASS**;
- contextual guesses introduced by recovery: **0**.

Boundary joins confirmed:

- 4→5 `சுதந்திரக் / கட்சியின்`
- 5→6 `பாளையங் / கோட்டைச்`
- 20→21 sentence close → `அது மாத்திரமல்ல...`
- 21→22 `கட்டுப்படுத்து / கின்ற`
- 25→26 `உட்படுத்தப்பட்டிருக் / கிறதா?`
- 26→27 sentence close → `திட்டக் குழுவில்...`
- 27→28 `தேர்ந் / தெடுக்கப்படுகிற`
- 34→35 `நாங்கள் / செலவு செய்துவிட்ட...`
- 35→36 sentence close → `ஒன்பது அறிவிப்புகள்`

Integrity-audit correction:

- scan 35 residual canonical lineation `ஆட்சேபணை தெரிவிக்கப்பட்ட / டும்`
- corrected to booklet-visible `ஆட்சேபணை தெரிவிக்கப்பட் / டும்`
- continuous word remains `தெரிவிக்கப்பட்டும்`
- this is a booklet-pixel lineation correction, not TNLA normalization;
- page-35 recovery counts remain **2 direct witness recoveries / 34 no-insert positions**.

## Post-recovery Gate E — PASS / COMPLETE

Focused source-fidelity recheck scope:

**scans 4–5, 10–11, 20–21, 25–27, 34–35**  
printed pp. **3–4, 9–10, 19–20, 24–26, 33–34**

Result:

- affected booklet scans visually re-read: **11 / 11**;
- every direct crop recovery rechecked against the page-level recovery audit;
- booklet-visible text adjacent to recoveries: **PASS**;
- names / initials / speaker labels: **PASS**;
- numerals, dates, money, units and project figures: **PASS**;
- embedded English: **PASS**, including scan 25 `THIRUMATHI T. N. ANANDANAYAKI...` and scan 27 `Ratification`;
- headings / intervention boundaries / legible punctuation: **PASS**;
- physical line breaks on recovered pages: **PASS**;
- recovery-touched page boundaries: **9 / 9 PASS**;
- booklet-specific forms retained against TNLA differences: **PASS**;
- scan-13 small cartoon-label hold: **unchanged / separate**;
- focused Gate-E new corrections: **0**;
- unresolved Tamil fidelity questions: **0**;
- `transcription.verified_against_scan=true` restored.

The preceding whole-Tamil integrity audit's one correction remains confirmed:

- scan 35 `ஆட்சேபணை தெரிவிக்கப்பட்ட / டும்`
- → booklet-visible `ஆட்சேபணை தெரிவிக்கப்பட் / டும்`
- continuous word: `தெரிவிக்கப்பட்டும்`.

Tamil crop recovery + integrity + focused Gate-E fidelity recheck are now **CLOSED / PASS**.

## Post-recovery English repair — COMPLETE

Scope:

**source pages 4–5, 10–11, 20–21, 25–27, 34–35**

Result:

- repaired English source-page sections: **11 / 11**;
- translation source: final post-recovery **Gate-E-verified Tamil**;
- TNLA was not translated independently into English;
- source-printed English remains verbatim;
- inherited English crop markers before repair: **249**;
- inherited English crop markers after repair: **0**;
- English source-page sections **4–40** remain exactly once and strictly monotonic.

Marker inventory resolved:

- p4 **24**
- p5 **12**
- p10 **21**
- p11 **11**
- p20 **32**
- p21 **20**
- p25 **30**
- p26 **28**
- p27 **33**
- p34 **6**
- p35 **32**

Notable repairs:

- scan 4: inclusive **81-member** count restored;
- scan 4→5: Swatantra Party continuation restored;
- scan 10: complete tax-head list restored;
- scan 11: **Kambam**, **1973-74**, **1965-66**, **four demands** restored;
- scan 20: stale pre-recovery **“reduce poverty”** corrected to **“reduce all taxes”** for final Tamil `வரியையெல்லாம்`;
- scan 21: recovered quotation force around **“unaccounted money”** retained;
- scan 25: list **(1)** / **(3)** and source-printed **have been sent** restored;
- scan 27: recovered `கடற்கரையில்` rendered **“at the seashore”**; `Ratification` retained;
- scan 34→35: generator/licence exchange repaired across the source-page boundary;
- scan 35: **1,41,000** and concluding `ஆக,` transition restored.

The prior full Gate-G PASS is historical only because it reviewed the pre-recovery English.

## Focused post-recovery Gate G — PASS / COMPLETE

Scope:

**English source pages 4–5, 10–11, 20–21, 25–27, 34–35**

Result:

- repaired English pages reviewed: **11 / 11**;
- review source: final post-recovery Gate-E-verified Tamil;
- omissions / additions: **PASS**;
- recovered-fragment fidelity: **PASS**;
- names / speaker labels / intervention order: **PASS**;
- dates / numerals / money / units / project names / Plan chronology: **PASS**;
- source-printed English: **PASS / verbatim**;
- English source-page sequence **4–40**: **PASS / exactly once / monotonic**;
- legacy English crop markers: **0**;
- unresolved English fidelity questions: **0**;
- `verified_against_tamil=true`.

Definite focused corrections: **2**

1. scan 35:
   - before: `Even if Ministers themselves go and open them, licences will not be issued to them...`
   - after: `Even if Ministers themselves go and inaugurate it, licences will not be issued for it...`
   - reason: final Tamil has `திறந்து வைத்தாலும் அதற்கு லைசென்சுகள்...`; the earlier English incorrectly redirected `அதற்கு` to people.

2. scan 35:
   - before: `Thus, Thus, I place before the House...`
   - after: `Thus, I place before the House...`
   - reason: duplicate repair artifact; Tamil has one `ஆக,`.

Historical pre-recovery Gate G remains recorded with **15** corrections. Focused post-recovery Gate G adds **2**, for **17 cumulative definite English fidelity corrections across both review eras**.

## Post-recovery Gate H — PASS / RELEASED

Gate-H canonical bilingual integrity / release revalidation is **COMPLETE**.

Checks passed:

- Tamil source-page markers **4–40** — **37/37**, exactly once, strictly monotonic;
- English source-page sections **4–40** — **37/37**, exactly once, strictly monotonic;
- Tamil legacy crop markers — **0**;
- English legacy crop markers — **0**;
- canonical Tamil remains the final post-recovery Gate-E-verified payload;
- canonical English remains the focused post-recovery Gate-G-verified payload;
- Tamil→English merge transition — **PASS**;
- recovery-touched bilingual boundaries **9/9 PASS**:
  - 4→5
  - 5→6
  - 20→21
  - 21→22
  - 25→26
  - 26→27
  - 27→28
  - 34→35
  - 35→36;
- historical Gate-G boundary repairs **37→38** and **39→40** remain intact;
- scan-13 small cartoon-label hold remains explicit / unchanged;
- `translation.md` remains a retired pointer;
- work metadata / README, `data/speeches.json`, and root README/index synchronized;
- Gate-H language corrections — **0**.

Release result:

- Gate H — **PASS / REVALIDATED AFTER CROP RECOVERY**
- Tamil `verified_against_scan=true`
- English `verified_against_tamil=true`
- Unit 1 — **RELEASED**
- unresolved Tamil fidelity questions — **0**
- unresolved English fidelity questions — **0**

## Unit 2 Gate D D1 — PASS

Scope:

- scans **41–50**
- printed pp. **40–49**
- pages reviewed: **10 / 10**

Result:

- source-page markers **41→50** — exactly once / monotonic / no skip / no duplicate;
- page-boundary continuity — **9 / 9 PASS**;
- headings / paragraph order / speaker interventions — **PASS**;
- figures / dates / source-printed English placement — **PASS**;
- newly identified crop holds — **0**;
- unresolved completeness questions — **0**;
- Gate-D completeness corrections — **2**.

D1 corrections:

1. scan **43** / printed p.**42** — added a conservative printed-illustration note for the audience/crowd scene at the source position between paragraphs.
2. scan **44** / printed p.**43** — added a conservative printed-illustration note for the staged Yamadharman/buffalo scene at its source position.

These are source-context completeness additions only. No speech wording was invented or normalized.

Key checked continuations include:

- 41→42 `தெரிந்து / கொண்டிருந்தும்`;
- 44→45 `அல்லது / தோழமைக் கட்சிகளின் சார்பிலோ`;
- 45→46 `முன் / கூட்டியே`;
- 47→48 `உயர்ந்திருக்கிறதே / அல்லாமல் அதிகமல்ல`;
- 48→49 `தெரிந்து / கொள்கிற அளவுக்கு`;
- 49→50 `பரிபூரண / மாக முடிந்துவிட்டது`.

Scan 50 retains both printed Punjab Electricity Board English quotations in the correct structural location.

## Unit 2 Gate D D2 — PASS

Scope:

- scans **51–60**
- printed pp. **50–59**
- pages reviewed: **10 / 10**

Result:

- source-page markers **51→60** — exactly once / monotonic / no skip / no duplicate;
- page-boundary continuity — **9 / 9 PASS**;
- headings / paragraph order / speaker interventions — **PASS**;
- figures / dates / list structure — **PASS**;
- source-printed English on scans **52–55** — **PASS / structurally retained in place**;
- newly identified crop holds — **0**;
- D2 completeness corrections — **0**;
- D2 unresolved completeness questions — **0**;
- cumulative Gate-D coverage — **20 / 22**;
- cumulative Gate-D completeness corrections — **2**.

Key checked continuations include:

- 51→52 `எதை / எதை விலக்கிவிடலாமென்று`;
- 52→53 `13-வது பிரிவில் / Prosecution for false complaint...`;
- 55→56 `அவர்கள் என்ன செய்ய / வேண்டும்?`;
- 56→57 `துணிச்சலோடும், / நேர்மையோடும்,`;
- 57→58 `5 ஆயிரம் ரூபாய் தான் / விவசாயம் அல்லாத வருமானம்...`;
- 58→59 `வீட்டு வசதி / வாரியம்`.

Scan 60 correctly ends mid-sentence at the visible `30`; D3 must resume from scan 61 without reconstructing forward.

## Unit 2 Gate D — PASS / COMPLETE

Gate D final scope:

- scans **41–62**
- printed pp. **40–61**
- pages audited: **22 / 22**

Batch results:

- D1 scans 41–50 — **PASS / 2 completeness corrections / 0 unresolved**
- D2 scans 51–60 — **PASS / 0 corrections / 0 unresolved**
- D3 scans 61–62 — **PASS / 0 corrections / 0 unresolved**

D3 closing checks:

- incoming 60→61 continuation: scan 60 visible final `30` → scan 61 `மனுக்கள் தான் வந்திருக்கின்றன.` — **PASS**;
- scan 61 heading `மாற்றம்!` — **PASS**;
- scan 61→62 paragraph continuity — **PASS**;
- final State-autonomy argument — **PASS**;
- final acknowledgements — **PASS**;
- closing `வணக்கம்` — **PASS**;
- closing ornament — **represented**;
- scan 63 — printer/imprint matter;
- scan 64 — back cover;
- no third speech follows.

Gate-D final result:

- source-page sequence **41→62** — exactly once / no skip / no duplicate;
- cumulative completeness corrections — **2**;
- unresolved completeness questions — **0**;
- physical crop holds — **0**;
- speech-end classification — **LOCKED / PASS**;
- `completeness_audit_passed=true`;
- Gate E — **UNBLOCKED / NEXT**.

## Unit 2 Gate E E1 — PASS

Scope:

- scans **41–50**
- printed pp. **40–49**
- pages visually re-read: **10 / 10**

Result:

- strict visual word/character fidelity audit — **PASS**;
- names / initials / speaker labels — **PASS**;
- numerals / dates / money / units — **PASS**;
- embedded source English — **PASS / verbatim**;
- headings / interventions / punctuation where legible — **PASS**;
- page-boundary continuity — **PASS**;
- D1 illustration-context notes on scans 43–44 — **structurally confirmed**;
- E1 corrections — **1**;
- unresolved source-fidelity questions — **0**.

Definite E1 correction:

- scan **44** / printed p.**43**
  - before: `சில பேர் ரசிப்பார்கள் என்ற நிலைமை எண்ணி,`
  - source: `சில பேர் ரசிப்பார்கள் என்று நிலைமையை எண்ணி,`
  - after: `சில பேர் ரசிப்பார்கள் என்று நிலைமையை எண்ணி,`

This is an ordinary source-fidelity correction. Gate-C.5 historical `மாறாக` on the same page remains unchanged and source-supported.

Scan 50's source-printed Punjab Electricity Board English quotations were rechecked and retained verbatim, including the source's unusual wording `The offer of Rs. 45 lakhs was had on behalf of the Board...`.

Cumulative Gate-E coverage: **10 / 22 pages**.  
Cumulative Gate-E corrections: **1**.  
Unresolved Gate-E questions: **0**.

## Unit 2 Gate E E2 — PASS

Scope:

- scans **51–60**
- printed pp. **50–59**
- pages visually re-read: **10 / 10**

Result:

- strict visual word/character fidelity audit — **PASS**;
- names / initials / speaker labels — **PASS after two scan-59 punctuation repairs**;
- numerals / dates / money / units / legal references — **PASS**;
- embedded source English on scans 52–55 — **PASS / verbatim**;
- headings / interventions / punctuation where legible — **PASS**;
- page-boundary continuity 51→52 through 59→60 — **9 / 9 PASS**;
- Gate-C.5 scan-58 `வேலைதான்` — **revalidated / preserved**;
- E2 corrections — **11**;
- unresolved source-fidelity questions — **0**.

Definite E2 corrections:

- scan **51** / printed p.**50** — `வருந்தத்தக்கதென்று` → `வருந்தத் தக்கதென்று`;
- scan **52** / printed p.**51** — `சொல்லப்படுகிறது—எக்ஸ்ட்ரா` → `சொல்லப் படுகிறது—எக்ஸ்ட்ரா`;
- scan **54** / printed p.**53** — `எழுதியிருக்கிறார்` → `எழுதியார்கள்`;
- scan **54** / printed p.**53** — `அது மாத்திரமுமல்லது` → `அது மாத்திரமும் அல்லது`;
- scan **56** / printed p.**55** — `எடுத்துக் காட்டினர்` → `எடுத்துக் காட்டினார்கள்`;
- scan **57** / printed p.**56** — restored printed ellipsis: `இங்கே எடுத்துக் காட்டி... விரும்புகிறேன்.`;
- scan **59** / printed p.**58** — `அதை விட்டு விட்டு கையகப்படுத்திக் கொள்ளுங்கள்` → `அதை விட்டு விட்டுக் கையகப்படுத்திக் கொள்ளுங்கள்`;
- scan **59** / printed p.**58** — restored `:—` in the `திரு கே. ராஜாராம்` speaker label;
- scan **59** / printed p.**58** — restored `:—` in the `மாண்புமிகு டாக்டர் மு. கருணாநிதி` speaker label;
- scan **60** / printed p.**59** — `பரிசீலிக்கப்பட்டிருக்கின்றன` → `பரிசீலிக்கப்படுகின்றன`;
- scan **60** / printed p.**59** — `நீட்டிக்கப்பட்ட பட்டு` → `நீட்டிக்கப் பட்டு`.

Cumulative Gate-E coverage: **20 / 22 pages**.  
Cumulative Gate-E corrections: **12**.  
Unresolved Gate-E questions: **0**.

## Exact next activity — Unit 2 Gate E E3 / FINAL

Perform **Gate E Tamil source-fidelity verification E3 / FINAL — scans 61–62 / printed pp.60–61**.

For scans 61–62:

1. visually compare every Tamil word / character to the controlling booklet;
2. verify names / initials / speaker labels, numerals and punctuation;
3. verify the `மாற்றம்!` heading and all paragraph boundaries;
4. verify incoming continuity from scan 60's terminal `30` into scan 61;
5. verify scan 61→62 continuity;
6. verify the final State-autonomy argument, acknowledgements, `வணக்கம்` and closing ornament;
7. preserve source spelling, compounds and historical forms;
8. record every definite correction with scan / printed-page provenance;
9. if E3 passes, mark Gate E **PASS / COMPLETE — 22/22**, set Tamil `verified_against_scan=true`, and only then unblock English.

Do **not** begin English translation in the same iteration.

## Required files

Read before Unit-2 Gate-E E3 / FINAL work:

1. this handover
2. `docs/NEXT_CHAT_PROMPT_1973_IRULUM_OLIYUM.md`
3. `speeches/1973/1973-03-07-financial-statement-reply/crop-recovery-audit.md`
4. `speeches/1973/1973-03-07-financial-statement-reply/transcript.md`
5. `speeches/1973/1973-03-07-financial-statement-reply/metadata.json`
6. `speeches/1973/1973-03-07-financial-statement-reply/README.md`
7. `speeches/1973/1973-03-07-financial-statement-reply/verification-log.md`
8. `speeches/1973/1973-03-07-financial-statement-reply/source-notes.md`

If either PDF is missing in a new chat, retrieve it from conversation/Library before asking the user to upload again.

## Recovery sequence

All affected pages are individually revalidated. Page-level crop recovery is **COMPLETE**.

Next:

1. **Unit 2 Gate F English translation F1 — scans 41–50 / printed pp.40–49**, using only the final Gate-E-verified Tamil.

## Current Unit 1 release state

- `transcription.status = verified-after-crop-recovery`
- `transcription.verified_against_scan = true`
- page-by-page verified scans: **4–5, 10–11, 20–21, 25–27, 34–35 — COMPLETE**
- whole-Tamil crop-recovery integrity audit — **PASS / COMPLETE**
- focused post-recovery Gate E — **PASS / COMPLETE**
- Tamil verified_against_scan — **true**
- English recovered-span repair — **COMPLETE / 249 → 0 markers**
- focused post-recovery Gate G — **PASS / COMPLETE — 2 corrections / 0 unresolved**
- English `verified_against_tamil = true`
- Gate G — **PASS / REVALIDATED AFTER CROP RECOVERY**
- Gate H — **PASS / REVALIDATED AFTER CROP RECOVERY**
- release — **RELEASED**
- next activity — **Unit 2 Gate F F1 — scans 41–50 / printed pp.40–49**

## Unit 2 active-next state

`சட்டமன்ற மேலவையில்` / 8-3-1973:

- Gate A — PASS
- Gate B — PASS / LOCKED
- Gate C — COMPLETE — 22/22
- Gate C.5 — PASS / COMPLETE — 22/22
- historical-glyph corrections — 2
- unresolved glyph clusters — 0
- Gate D — **PASS / COMPLETE — 22 of 22 / 2 cumulative corrections / 0 unresolved**
- English — **UNBLOCKED / NOT STARTED**
- Gate E — **PASS / COMPLETE — 22 of 22 / 15 cumulative corrections / 0 unresolved**
- Tamil `verified_against_scan` — **true**
- exact next activity — **Gate F F1 scans 41–50 / printed pp.40–49**

Unit 1 remains locked/released. Unit 2 Tamil is verified. Continue only Unit-2 Gate-F F1 in the next iteration; do not begin Gate G.

## Unit 2 Gate E E3 / FINAL — PASS / COMPLETE

Scans **61–62 / printed pp.60–61** were re-read against the controlling booklet pixels.

- E3 pages reviewed — **2 / 2**
- E3 corrections — **3**
- cumulative Gate-E corrections — **15**
- unresolved source-fidelity questions — **0**
- Gate-E cumulative coverage — **22 / 22**
- incoming scan 60→61 continuation — **PASS**
- scan 61→62 continuity — **PASS**
- `மாற்றம்!` — **PASS**
- final State-autonomy argument — **PASS**
- final acknowledgements / `வணக்கம்` / closing ornament — **PASS**

Corrections:

1. scan **61** / printed p.**60** — `தேதியே வைக்கவில்லை.` → `தேதியே வைக்க வில்லை.`
2. scan **62** / printed p.**61** — `பொறுப்புகளை` → `பொறுப்புக்களை` in `சில பொறுப்புக்களை நாம் ஏற்றுக் கொண்டிருக்கிறோம்.`
3. scan **62** / printed p.**61** — `பொறுப்புகள்` → `பொறுப்புக்கள்` in the `ஊறுதேடாத வகையில்...` passage.

Gate E is now **PASS / COMPLETE** and Unit-2 Tamil is **VERIFIED AGAINST SCAN**.

English is now **UNBLOCKED**, but was not started in this iteration.

## Exact next activity — Unit 2 Gate F F1

Translate **scans 41–50 / printed pp.40–49** from the **final Gate-E-verified Tamil**.

- preserve argument order, repetitions, direct address, humour, irony and parliamentary interventions;
- preserve names, figures, technical terms and source-printed English;
- do not correct historical claims or polish Kalaignar's voice into generic English;
- preserve source-page correspondence;
- process the 10-scan-page F1 batch only;
- update metadata / README / verification log / handover / next prompt;
- do **not** begin Gate G in the same iteration.

