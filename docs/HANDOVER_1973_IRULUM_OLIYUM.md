# Handover — 1973 `இருளும் ஒளியும்`

## Repository

`pugazg/kalaignar-assembly-speeches`, branch `main`.

**LIVE MAIN IS AUTHORITATIVE.** Fetch live `main` first and preserve newer durable work.

Checkpoint before this handover rewrite:

`5f9b46226414d165ac872d5a779d61cd9aa462cd` — `Advance README after crop integrity audit`

## Active work

Current priority is **Unit 1 post-release crop recovery, one booklet page per iteration**.

Unit 1 had previously passed Gate H and was released. It is legitimately reopened because the newly supplied official TNLA Assembly Debates volume provides primary-source text for wording physically lost at the gutter of the `இருளும் ஒளியும்` scan.

**Unit 2 Gate D is paused.**

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

## Exact next activity — Gate-E Tamil fidelity recheck for recovered spans/pages

Re-run **Gate E only for the affected recovered pages/spans**:

**4–5, 10–11, 20–21, 25–27, 34–35**

This is not a whole-speech retranscription. Recheck the canonical Tamil against the controlling booklet pixels, using TNLA only where the booklet gutter physically removed text.

Verify at minimum:

1. every direct crop recovery recorded in `crop-recovery-audit.md`;
2. booklet-visible wording adjacent to every recovered fragment;
3. names / initials / speaker labels;
4. numerals, dates, percentages, money and units;
5. embedded English — especially `THIRUMATHI T. N. ANANDANAYAKI...` and `Ratification`;
6. headings and intervention boundaries;
7. punctuation where booklet pixels are legible;
8. physical line breaks and all nine recovery-touched page boundaries;
9. retained booklet-specific forms against TNLA differences;
10. scan-35 integrity correction `தெரிவிக்கப்பட் / டும்`.

If Gate-E recheck passes, next activity becomes **English repair / retranslation for the recovered spans**.

Do **not** repair English, run Gate G, re-close Gate H, restore RELEASED, or resume Unit 2 in the same iteration.

## Required files

Read before Gate-E Tamil fidelity recheck:

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

1. **Gate-E Tamil fidelity recheck for affected recovered pages/spans**;
2. English repair/retranslation for recovered spans;
3. Gate-G English fidelity recheck;
4. Gate-H canonical bilingual revalidation;
5. restore RELEASED only after all checks pass;
6. resume Unit 2 Gate D D1.

## Current Unit 1 release state

- `transcription.status = crop-recovery-in-progress`
- `transcription.verified_against_scan = false`
- page-by-page verified scans: **4–5, 10–11, 20–21, 25–27, 34–35 — COMPLETE**
- whole-Tamil crop-recovery integrity audit — **PASS / COMPLETE**
- next activity: **Gate-E Tamil fidelity recheck for recovered spans/pages**
- Gate E — recheck required
- English `verified_against_tamil = false`
- Gate G — recheck required
- Gate H — reopened
- release — recovery in progress

## Unit 2 paused state

`சட்டமன்ற மேலவையில்` / 8-3-1973:

- Gate A — PASS
- Gate B — PASS / LOCKED
- Gate C — COMPLETE — 22/22
- Gate C.5 — PASS / COMPLETE — 22/22
- historical-glyph corrections — 2
- unresolved glyph clusters — 0
- Gate D — NOT STARTED / PAUSED
- English — BLOCKED

Do not resume Unit 2 until Unit-1 crop recovery/revalidation is complete.
