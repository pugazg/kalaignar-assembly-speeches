# Verification log — உரை : 9 / 8.05.2000

## Source preflight and locked boundaries

Controlling PDF:

- actual pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Speech-9 scan range: **278–303**
- printed range: **277–302**

The attached working copy was independently checked and matches the locked page count and SHA-256.

Boundary re-check before transcription:

- p.277 closes Speech 8 with its closing exchange and ornament;
- p.278 explicitly begins `உரை : 9`, `நாள் : 8.05.2000`;
- p.303 closes Speech 9 with a closing ornament;
- p.304 explicitly begins `உரை : 10`, `நாள் : 23.08.2006`.

Boundary status: **confirmed; unchanged from the locked anthology map**. The p.303/p.304 boundary was re-inspected again while closing Gate C.

## Gate C — Tamil first pass

### Batch 1 — source pp.278–282 / printed pp.277–281

**Complete for this bounded batch.**

- pages transcribed: **5**;
- cumulative coverage after Batch 1: **5/26**;
- unresolved first-pass readings: **0**;
- ending continuation: `இந்த 1999-2000-ல்`.

A post-write visual reread corrected p.282 `முக்கிய களமாக` → `முக்கிய தளமாக`. Correction commit: `dbdcdab67fee3085607bd8929d5cf0b524a8ed85`. This was a Gate-C first-pass correction, **not** Gate-E verification.

### Batch 2 — source pp.283–287 / printed pp.282–286

**Complete for this bounded batch.**

- cumulative coverage: **10/26**;
- cumulative source-page markers: **278–287**, each once and in strict order;
- unresolved first-pass readings: **0**;
- ending continuation: p.287 ends after `தமிழக அரசின்மீது இந்த நீதிமன்றம்`.

Canonical Batch-2 transcript commit: `3fc93b8b3bb7860db225ead53511a747149a0ebd`. Its inspected diff changed only the coverage note and appended pp.283–287.

### Batch 3 — source pp.288–292 / printed pp.287–291

**Complete for this bounded batch.**

- cumulative coverage: **15/26**;
- cumulative source-page markers: **278–292**, each once and in strict order;
- unresolved first-pass readings: **0**;
- ending continuation: `Tanflora Infrastructure Park; 24.85 கோடி ரூபாய் முதலீட்டில் மலரைப் பதப்படுத்தும் தொழில் பூங்கா ஒன்று`.

Canonical Batch-3 transcript commit: `8de59961b972844acffb7f831d1867d2193cbf9d`. Its inspected diff changed only the coverage note and appended pp.288–292.

### Batch 4 — source pp.293–297 / printed pp.292–296

**Complete for this bounded batch.**

- cumulative coverage: **20/26**;
- cumulative source-page markers: **278–297**, each once and in strict order;
- unresolved first-pass readings: **0**;
- ending continuation: `ஆனால், தினமும்`.

Canonical Batch-4 transcript commit: `dcc52ef8fcc7a48517dfa924f5dc297e7a96867d`. Its inspected diff changed only the coverage note and appended pp.293–297. A focused reread supported the unusual p.293 source form `இன்னொன்றியில் சென்னை வர்த்தக மையம்;`; no uncertainty marker remained.

### Batch 5 — source pp.298–302 / printed pp.297–301

**Complete for this bounded batch.**

- pages transcribed in Batch 5: **5**;
- cumulative Speech-9 coverage: **25/26**;
- cumulative source-page markers: **278–302**, each once and in strict order;
- missing/duplicate/reordered markers in completed range: **0**;
- unresolved first-pass readings: **0**;
- ending continuation: p.302 ends mid-sentence after `வெட்டுத் தீர்மானங்களுடைய எண்ணிக்கை 111. நம்பர்`.

Initial Batch-5 transcript commit: `ed2ade25fb1f3808a8cb8f6bfd0918ca1be7f3a5`. Its inspected diff updated the Gate-C coverage note from 20/26 to 25/26 and appended source-page sections 298–302; completed pp.278–297 were not intentionally rewritten.

A focused high-resolution post-write reread found four definite first-pass source-reading corrections:

1. p.298 `பழனிசாமி ஏற்றுக்கொள்கிறாரோ` → `பழனிசாமி ஏற்றுக் கொள்கிறாரோ`;
2. p.298 `டி. மணி ஏற்றுக்கொள்கிறாரோ` → `டி. மணி ஏற்றுக் கொள்கிறாரோ`;
3. p.300 `சிமெண்ட் தயார்செய்வதன்` → `சிமெண்ட் தயார் செய்வதன்`;
4. p.300 `குறைந்த விலையில் தயார்செய்து` → `குறைந்த விலையில் தயார் செய்து`.

Correction commit: `8ed2c3685857e16b368139252386b623875284ab`. The inspected diff contains exactly those four textual corrections and no other transcript changes. These are **Gate-C first-pass corrections, not Gate-E verification corrections**.

Batch-5 source-sensitive material retained without external reconciliation includes:

- p.298 `ரைட்` and the source-varying `ஏற்றுக்கொள்கிறாரோ` / `ஏற்றுக் கொள்கிறாரோ` forms;
- p.299 `'TANCEM'`, `12-12-1994`, the printed `Counter Affidavit` quotation and the source Tamil explanation `மூன்றாவது பிரதிவாதியான டான்செம் நிறைவேற்றவில்லை.` even though its wording is not a literal match for the English quote;
- p.300 the two printed English Government sentences and So. Balakrishnan's `தயார் செய்வதன்` / `தயார் செய்து` wording;
- p.301 the complete 1991-92 through 1999-2000 Ariyalur production figures;
- p.302 `அம்புஜா`, Rs.85 / Rs.145, `50 சதவிகிதத்திலே`, the Chief Secretary committee and `111` cut motions.

Corrected canonical transcript checkpoint after Batch 5: commit `8ed2c3685857e16b368139252386b623875284ab`, blob `67b1cc071ce4c8c04c1ea6748a65e0ffd1d91d3b`.

### Batch 6 — source p.303 / printed p.302

**Complete for this bounded batch. Gate C is now complete.**

- pages transcribed in Batch 6: **1**;
- cumulative Speech-9 first-pass coverage: **26/26, source pp.278–303 / printed pp.277–302**;
- p.303 source-page marker added exactly once;
- first-pass marker sequence now spans **278–303**;
- unresolved first-pass readings: **0**;
- Tamil status: **transcribed; not verified**.

The page was transcribed directly from the rendered controlling scan, beginning with `நன்றாக இல்லை.` immediately after p.302's `111. நம்பர்`. It preserves the remaining Karunanidhi remarks, the Chair's call to `திரு. பி. ஆர். சுந்தரம்`, Sundaram's correction from `2,000 கோடி` to `2,000 இலட்சம்`, explicitly `20 கோடி`, and the Chair's separately printed sequence `200 கோடி, 20 இலட்சம், 2,000 கோடி` without reconciliation. The source form `கேட்டு அமைகிறேன்.` and `ராசிபுரம்.....` are retained as printed.

The printed closing ornament on p.303 confirms the Speech-9 close. Scan p.304 begins `உரை : 10`, `நாள் : 23.08.2006`; no Speech-10 material was included.

Canonical Gate-C-complete transcript commit: `1014c9528404a6334a94ab811d1b0b1142637d72`, blob `9c0a07406b072216a62b07f5cb16d29a45c42d22`. The inspected commit diff changed the Gate-C coverage/status note and appended only the new p.303 section; completed source pp.278–302 were not rewritten.

Gate-C metadata closure commit: `12e3fbefb66dce6325488884ed9aa1917ce18378`.

**Gate C status: complete.** This is still first-pass transcription, not a claim of full character-level source verification.

## Gate D — Tamil completeness/page-marker audit

**Passed.** The complete Speech-9 transcript was audited against the locked structural map.

Audit results:

- expected source range: **278–303**;
- expected printed range: **277–302**;
- expected mapped pages: **26**;
- represented mapped pages: **26/26**;
- source-page markers: **278–303**, exactly once and in strict order;
- missing markers/pages: **0**;
- duplicate markers/pages: **0**;
- reordered markers: **0**;
- start boundary mismatch: **0** — canonical transcript begins at source p.278 with `உரை : 9`, `நாள் : 8.05.2000`;
- end boundary mismatch: **0** — canonical transcript ends on source p.303 after the final Chair intervention and before the printed closing ornament;
- Speech-8 / p.277 spillover: **0**;
- Speech-10 / p.304 spillover: **0**;
- unresolved reading markers: **0**;
- Gate-D canonical Tamil text corrections: **0**.

Speaker/intervention structure was also checked for completeness. The transcript represents the p.278 `திரு. ச. அழகிரி` intervention and return to Karunanidhi; the p.299 printed interruption and subsequent Karunanidhi speaker label; the p.300 `திரு. சோ. பாலகிருஷ்ணன்` intervention and p.301 return to Karunanidhi; and the p.303 Chair / `திரு. பி. ஆர். சுந்தரம்` / Chair sequence. Printed parenthetical interruptions such as `(குறுக்கீடு)` remain represented.

Gate D is a **structural completeness audit only**. It does not establish word/character fidelity against the scan. No canonical Tamil source text was changed during Gate D.

## Gate E — strict Tamil source-fidelity verification

**Not started.** This is now the exact next activity. Gate E must directly re-read all scan/source pp.278–303 against the controlling rendered scan and check words/characters, names/initials, numerals, dates, percentages, monetary values, units, printed English, headings, speaker labels, punctuation where legible, and cross-page continuations. Only definite scan-supported corrections may be applied and documented before Tamil can be marked `verified`.

## English gates

- Gate F: **blocked / not started**;
- Gate G: **not started**.

English may begin only after Gate E is complete and Tamil is verified.

## Exact next activity

Proceed with **Gate E — strict Tamil source-fidelity verification** for Speech 9, covering the locked scan/source range **278–303 / printed 277–302**. Do **not** begin English translation or Speech 10 until Gate E is complete.
