# உரை : 19 — 06.03.1982

**காப்பக working ID:** `1982-03-06-financial-statement-debate`

## Source unit

- anthology — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`
- source label/date — **உரை : 19 / 06.03.1982**
- canonical date — **1982-03-06**
- global scans — **511–545**
- printed pages — **510–544**
- page count — **35**
- incoming boundary **510→511** — **PASS / locked anthology map**
- outgoing boundary **545→546** — **PASS / locked anthology map**
- scan 510 — **Speech 18 close / excluded**
- scan 546 — **closing portrait/back matter / excluded**

## Existing-work overlap check

- repository `speeches/` currently has **no 1982 directory / no existing Speech-19 working entry**
- `data/speeches.json` currently has **no 1982-03-06 entry**
- therefore this is a **new working entry**, not an overwrite of released material

## Controlling source / working splits

Full controlling source:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`
- physical pages — **546**
- bytes — **393,027,493**
- SHA-256 — `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- textual authority — **rendered scan pixels**
- usable text layer — **none**

Working split 1:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_021_pages_501-525.pdf`
- local pages — **11–25**
- global scans — **511–525**
- printed pages — **510–524**
- Speech-19 coverage — **15 pages**
- split page count — **25**
- split bytes — **18,938,935**
- split SHA-256 — `d32d5b4559b68d81675d80e9bb535e1a0e8eaf6861a6eb037ffb357fad5c92c2`
- boundary witness — local **10 = scan 510 / Speech 18 close / excluded**; local **11 = scan 511 / Speech 19 heading / included**

Working split 2:

- filename — `TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1_part_022_pages_526-546.pdf`
- local pages — **1–20**
- global scans — **526–545**
- printed pages — **525–544**
- Speech-19 coverage — **20 pages**
- split page count — **21**
- split bytes — **15,522,557**
- split SHA-256 — `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`
- boundary witness — local **20 = scan 545 / Speech 19 close / included**; local **21 = scan 546 / closing portrait-back matter / excluded**

The full controlling source hash remains authoritative. During Gate-C Batch 1, the user-supplied part022 file was available and its convenience-file integrity metadata was resolved directly: **15,522,557 bytes / SHA-256 `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`**.

## Source authority

Rendered pixels of the controlling 2007 anthology are the sole textual authority.

No OCR, web copy, Official Report, alternate anthology, released speech or other outside witness may supply, repair or normalize wording.

## Gate state

- source intake — **PASS / COMPLETE**
- Gate C setup — **PASS / COMPLETE**
- Gate C transcription — **PASS / COMPLETE / scans 511–545 / 35 of 35 pages first-pass**
- Gate C.5 — **N/A / CLOSED / 0 historical-glyph corrections**
- Gate D — **PASS / COMPLETE / 35/35 pages / 34/34 internal transitions / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / scans 511–545 / 35 of 35 source-verified / 26 cumulative corrections / 0 unresolved**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate F — **COMPLETE / scans 511–545 / 35 of 35 translated / 0 blockers / 0 Tamil changes**
- English — **TRANSLATED / NOT VERIFIED AGAINST TAMIL / verified_against_tamil=false**
- Gates G–H — **NOT STARTED**
- release — **NOT RELEASED**
- Speech 18 — **RELEASED / CLOSED / locked**
- outside wording imported — **0**

## Gate-C batching

Fixed cadence: **10 source pages per iteration**; only the final remainder may be fewer.

1. Batch 1 — **511–520 / printed pp.510–519 / exactly 10 pages / PASS-COMPLETE**
2. Batch 2 — **521–530 / printed pp.520–529 / exactly 10 pages / PASS-COMPLETE**
3. Batch 3 — **531–540 / printed pp.530–539 / exactly 10 pages / PASS-COMPLETE**
4. Batch 4 FINAL — **541–545 / printed pp.540–544 / exactly 5 pages / PASS-COMPLETE**

Batch 1 lies wholly inside part021. Batch 2 crossed the part021→part022 working-split boundary at **525→526** and that transition is **PASS / preserved**.

## Gate C Batch 1 result

**PASS / COMPLETE — scans 511–520 / printed pp.510–519 / exactly 10 pages; cumulative 10 of 35 first-pass transcribed.**

- source-page markers — **511→520 / 10 / exactly once / ordered**
- source heading **உரை : 19 / 06.03.1982** — **preserved**
- speaker label — **preserved**
- unresolved first-pass readings — **0**
- outside wording imported — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- scan **520** — **ends mid-sentence at `இந்த`; continuation belongs to scan 521 and was not imported**
- scans **521–545** modified — **0**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- part021 Batch-1 source — **local 11–20 / global scans 511–520**
- part022 integrity metadata — **resolved from the user-supplied split: 15,522,557 bytes / SHA-256 `7fc6e4fb4e264c9c4b836150549fc0c8c45458bc9a3869ac313ff6708fb5ceed`**

## Gate C Batch 2 result

**PASS / COMPLETE — scans 521–530 / printed pp.520–529 / exactly 10 pages; cumulative 20 of 35 first-pass transcribed.**

- source-page markers — **511→530 / 20 / exactly once / ordered**
- Batch-2 source coverage — **part021 local 21–25 = scans 521–525; part022 local 1–5 = scans 526–530**
- working-split transition **525→526 / part021→part022** — **PASS / preserved**
- page-spanning continuations **520→521 / 521→522 / 523→524 / 524→525 / 525→526 / 526→527 / 527→528 / 529→530** — **preserved**
- source-printed English on scans **523–525** — **preserved**
- unresolved first-pass readings — **0**
- outside wording imported — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- scan **530** — **closes cleanly; scan 531 wording not imported**
- scans **531–545** modified — **0**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**

## Gate C Batch 3 result

**PASS / COMPLETE — scans 531–540 / printed pp.530–539 / exactly 10 pages; cumulative 30 of 35 first-pass transcribed.**

- source-page markers — **511→540 / 30 / exactly once / ordered**
- Batch-3 source coverage — **part022 local 6–15 = scans 531–540**
- page-spanning continuations **531→532 / 532→533 / 533→534 / 534→535 / 535→536 / 536→537 / 537→538 / 538→539 / 539→540** — **preserved**
- source-printed English on scan **535** — **preserved**
- source-printed English phrase on scan **539** (`foundation, weir pie`) — **preserved as printed**
- unresolved first-pass readings — **0**
- outside wording imported — **0**
- Tamil — **PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- scan **540** — **closes cleanly; scan 541 wording not imported**
- scans **541–545** modified — **0**
- Gate C.5 — **PROVISIONALLY N/A / not closed**
- Gates D–H — **NOT STARTED**

## Gate C Batch 4 FINAL result

**PASS / COMPLETE — scans 541–545 / printed pp.540–544 / exactly 5 pages; cumulative 35 of 35 first-pass transcribed.**

- source-page markers — **511→545 / 35 / exactly once / ordered**
- FINAL source coverage — **part022 local 16–20 = scans 541–545**
- **542→543** continuation — **preserved**
- source-printed English on scan **542** — **preserved as printed**
- speaker changes / interventions on scans **544–545** — **preserved**
- hard outgoing boundary **545→546** — **PASS / scan 546 closing portrait-back matter excluded**
- first-pass unresolved readings — **0**
- outside wording imported — **0**
- Tamil — **TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**
- Gate C — **PASS / COMPLETE / 35 of 35**
- Gate C.5 — **PROVISIONALLY N/A / explicit disposition next**
- Gates D–H — **NOT STARTED**
- release — **NOT RELEASED**

## Gate C.5 disposition

**N/A / CLOSED — modern 2007 typesetting.**

- inspected scope — **scans 511–545 / 35 pages**
- page-specific legacy Tamil typeform anomaly — **none observed**
- historical-glyph corrections — **0**
- unresolved historical-glyph readings — **0**
- Tamil wording changes — **0**
- source-page markers — **unchanged / 511→545 / 35/35**

## Gate D structural completeness audit

**PASS / COMPLETE — 35/35 pages / 34/34 internal transitions / 0 completeness corrections.**

- source-page markers — **511→545 / 35 / exactly once / ordered**
- missing pages — **0**
- duplicate pages — **0**
- empty page sections — **0**
- hard boundaries **510→511 / 545→546** — **PASS**
- working-split transition **525→526** — **PASS**
- all **34/34** internal page transitions — **structurally continuous**
- source heading/date and speaker labels — **represented**
- speaker changes/interventions on scans **544–545** — **represented**
- quotations / figures / repetitions — **structurally represented**
- source-printed English on scans **523–525 / 535 / 542** — **represented**
- scan **539** printed `foundation, weir pie` — **represented as printed**
- scan **546** content — **excluded**
- completeness corrections — **0**
- Tamil wording changes — **0**
- outside wording imported — **0**

Tamil remains **TRANSCRIBED / NOT VERIFIED / verified_against_scan=false**.

## Gate E Batch 1 — scans 511–520

**PASS / COMPLETE — printed pp.510–519 / exactly 10 pages; cumulative 10 of 35 source-verified.**

- source-fidelity corrections — **3 entries / 3 occurrences / 2 affected scans**
- affected scans — **518 / 520**
- unresolved readings — **0**
- outside wording imported — **0**
- source-page markers — **511→545 / unchanged / exactly once / ordered**
- Batch-1 terminal **520→521** continuation — **structurally preserved; scan 521 not source-verified or altered**
- Tamil — **PARTIALLY VERIFIED / verified_against_scan=false**
- scans **521–545** source-verification status — **NOT STARTED**
- Gate F — **blocked until Gate E completes all 35 pages**

### Gate-E Batch-1 correction ledger

1. **scan 518** — `1½ நாள் எடுத்து கொண்டு` → `1½ நாள் எடுத்துக் கொண்டு`.
2. **scan 520** — `எதிர்பார்க்கப்படுகிறது` → `எதிர்பார்க்கப் படுகிறது`.
3. **scan 520** — `கட்டி முடிக்கப்பட்டன` → `கட்டிமுடிக்கப்பட்டன`.

## Gate E Batch 2 — scans 521–530

**PASS / COMPLETE — printed pp.520–529 / exactly 10 pages; cumulative 20 of 35 source-verified.**

- source-fidelity corrections — **4 entries / 4 occurrences / 3 affected scans**
- affected scans — **521 / 529 / 530**
- cumulative Gate-E corrections — **7**
- cumulative affected scans — **5**
- unresolved readings — **0**
- outside wording imported — **0**
- source-page markers — **511→545 / unchanged / exactly once / ordered**
- **520→521** continuation — **PASS / source fidelity verified**
- working-split transition **525→526 / part021→part022** — **PASS / source fidelity preserved**
- source-printed English on scans **523–525** — **preserved as printed**
- scan **531** — **not source-verified or altered**
- Tamil — **PARTIALLY VERIFIED / verified_against_scan=false**
- Gate F — **blocked until all 35 pages complete Gate E**

### Gate-E Batch-2 correction ledger

1. **scan 521** — `இந்த அறிவிப்பை பார்த்தவுடன்` → `இந்த அறிவிப்பைப் பார்த்தவுடன்`.
2. **scan 529** — `பெருந்தலைவர் காமராஜ் அவர்கள் காலத்திலிருந்து` → `பெரும் தலைவர் காமராஜ் அவர்கள் காலத்திலிருந்து`.
3. **scan 529** — `இல்லை நாங்கள் பத்து வயதுக்குப் போடுவோம்` → `இல்லை நாங்கள் பத்து வயதுக்கும் போடுவோம்`.
4. **scan 530** — `முதலமைச்சர் அவர்கள் மேடைவாயிலே எடுத்துக் கூறியிருக்கிறார்கள்` → `முதலமைச்சர் அவர்கள் மேடைவாயில் எடுத்துக் கூறியிருக்கிறார்கள்`.

## Gate E Batch 3 — scans 531–540

**PASS / COMPLETE — printed pp.530–539 / exactly 10 pages; cumulative 30 of 35 source-verified.**

- source-fidelity corrections — **9 entries / 9 occurrences / 5 affected scans**
- affected scans — **532 / 535 / 536 / 537 / 538**
- cumulative Gate-E corrections — **16**
- cumulative affected scans — **10**
- unresolved readings — **0**
- outside wording imported — **0**
- source-page markers — **511→545 / unchanged / exactly once / ordered**
- Government of Tamil Nadu English extract on scan **535** — **preserved as printed**
- source-printed `foundation, weir pie` on scan **539** — **preserved as printed**
- scan **541** — **not source-verified or altered**
- Tamil — **PARTIALLY VERIFIED / verified_against_scan=false**
- Gate F — **blocked until all 35 pages complete Gate E**

### Gate-E Batch-3 correction ledger

1. **scan 532** — `கைத்தறிக்கு வரி போடுவது கிடையாது` → `கைத்தறிக்கு வரி போட்டது கிடையாது`.
2. **scan 535** — `ஏறத்தாழ ஏழு அல்லது எட்டு கோடி ரூபாய் இந்த ஏழு அல்லது எட்டு கோடி ரூபாய்` → `ஏறத்தாழ ஏழு அல்லது எட்டு கோடி ரூபாய். இந்த ஏழு அல்லது எட்டு கோடி ரூபாய்`.
3. **scan 536** — `ஆக 13 கோடி ரூபாய் நாம் இங்கே எடுத்துக் காட்டிய` → `ஆக 13 கோடி ரூபாய் நான் இங்கே எடுத்துக் காட்டிய`.
4. **scan 536** — `ஸ்டீல் ரோலிங் மில்ஸ் அதிபர்களுக்கு வரி விலக்கு செய்துவிட்டு` → `ஸ்டீல் ரீரோலிங் மில்லினுடைய வரியில் நீக்கம் செய்துவிட்டு`.
5. **scan 536** — `இழந்து கொண்டிருக்கின்றோம். இந்த அரசு என்று கூறுவதற்காகவே எடுத்துக் காட்டியிருக்கிறேன்.` → `இழந்து கொண்டிருக்கின்றது, இந்த அரசு என்று குற்றஞ்சாட்டுவது எப்படித் தவறாகும் என்பதுதான் என்னுடைய கேள்வியாகும்.`.
6. **scan 537** — `அவர்களால் திறந்து வைக்கப்பட்டது` → `அவர்களால் திறந்துவைக்கப்பட்டது`.
7. **scan 537** — `எப்படி தூசி படிந்து கிடக்கிறது என்பதை தேவையாக மாண்புமிகு முதலமைச்சர் இந்த மதுரையிலே ஏதோ ஒரு மூலையிலே உள்ள பாதையிலேயே படம் போட்டு காட்டினார்கள்.` → `எப்படி தூசி படிந்து கிடக்கிறது. எவ்வளவு கேவலமாக மோசமான முறையிலே அது மதுரையிலே ஏதோ ஒரு மூலையிலே தள்ளப்பட்டிருக்கிறது என்ற செய்தியைப் பத்திரிகையிலே படம் போட்டுக் காட்டினார்கள்.`.
8. **scan 537** — `எந்தக் கட்சியையும் சாராத ஒரு பெரிய அந்தக் கவலை தரும் சம்பவங்களை எடுத்துக் காட்டியிருக்கிறார்கள்.` → `எந்தக் கட்சியையும் சாராத ஏடுகளிலே அந்த கவலை தரும் சம்பவங்களை எடுத்துக் காட்டியிருக்கிறார்கள்.`.
9. **scan 538** — `2 லட்ச ரூபாய் அளவுக்குத்தான் நடு அதன்மேலே ஆஸ்பெஸ்டாஸ் தகடுகள் போட` → `2 லட்ச ரூபாய் அளவுக்குத் தூண் நட்டு அதன்மேலே ஆஸ்பெஸ்டாஸ் தகடுகள் போட`.

## Gate E Batch 4 FINAL — scans 541–545

**PASS / COMPLETE — printed pp.540–544 / exactly 5 pages; cumulative 35 of 35 source-verified.**

- source-fidelity corrections — **10 entries / 10 occurrences / 4 affected scans**
- affected scans — **541 / 542 / 543 / 544**
- cumulative Gate-E corrections — **26**
- cumulative affected scans — **14**
- unresolved readings — **0**
- outside wording imported — **0**
- source-page markers — **511→545 / unchanged / exactly once / ordered**
- source-printed English on scan **542** — **preserved exactly as printed**
- speaker changes / interventions on scans **544–545** — **verified and preserved**
- terminal boundary **545→546** — **PASS / scan 546 portrait-back matter excluded**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate E — **PASS / COMPLETE / 35 of 35**
- Gate F — **NOT STARTED**

### Gate-E Batch-4 correction ledger

1. **scan 541** — `வெளிநாட்டில் தயாரிக்கப்பட்ட சேஸிஸ்களைக்` → `வெளிநாட்டில் தயாரிக்கப்படும் சேஸிஸ்களைக்`.
2. **scan 542** — `ஃபண்ட்ஸ் ஒதுக்கீடு` → `பண்ட்ஸ் ஒதுக்கீடு`.
3. **scan 542** — `இந்த ஆட்சி என்றைக்கு கொளுவுக்கு வந்ததோ` → `இந்த ஆட்சி என்றைக்கு தொழுவுக்கு வந்ததோ`.
4. **scan 543** — `400 சாட்சியங்கள் விசாரிக்கப்படவேண்டிய சூழ்நிலையில்` → `400 சாட்சியங்கள் விசாரிக்கப்பட வேண்டிய சூழ்நிலையில்`.
5. **scan 543** — `சதி செய்திருக்கிறோம் என்கிற அளவுக்கு வழக்கு` → `சதி செய்கிறோம் என்கிற அளவுக்கு வழக்கு`.
6. **scan 544** — `அவைகளுக்கு எல்லாம் இறுதியில் பதில் கிடைக்கும்` → `அவைகளுக்கு எல்லாம் இறுதியிலே பதில் கிடைக்கும்`.
7. **scan 544** — `எனக்குப் பதில்சொல்வதற்கோ` → `எனக்குப் பதில் சொல்வதற்கோ`.
8. **scan 544** — `எனக்கு பலவீனம் ஏற்பட்டுத்த முடியவில்லை` → `எனக்கு பலவீனம் ஏற்படுத்த முடியவில்லை`.
9. **scan 544** — `வழக்குகள் நடைபெறுகின்றதே தவிர` → `வழக்குகள் நடைபெறுகிறதே தவிர`.
10. **scan 544** — `அதைப்போல நாங்கள் போடவில்லை` → `அதைப்போல நாங்கள் போட்டவில்லை`.

## Gate E closure

**PASS / COMPLETE — scans 511–545 / 35 of 35 source-verified / 26 total corrections / 0 unresolved.**

Tamil is now **VERIFIED / verified_against_scan=true**.

## Gate F Batch 1 — scans 511–540

**PASS / COMPLETE — exactly 30 pages translated; cumulative 30 of 35.**

- translation authority — **final Gate-E-verified Tamil only**
- English source-page sections — **511→540 / 30 / exactly once / ordered**
- blocking translation questions — **0**
- verified-Tamil changes — **0**
- outside English / outside-witness wording imported — **0**
- source-page alignment / paragraph order / continuations — **preserved**
- source-printed English on scans **523–525 / 535** — **preserved verbatim**
- scan **539** `foundation, weir pie` — **preserved exactly as printed**
- Tamil — **VERIFIED / unchanged / verified_against_scan=true**
- English — **IN PROGRESS / NOT VERIFIED AGAINST TAMIL / verified_against_tamil=false**
- scans **541–545** — **NOT TRANSLATED**
- Gate G — **NOT STARTED**

## Gate F Batch 2 FINAL — scans 541–545

**PASS / COMPLETE — exactly 5 pages translated; cumulative 35 of 35.**

- translation authority — **final Gate-E-verified Tamil only**
- cumulative English source-page sections — **511→545 / 35 / exactly once / ordered**
- blocking translation questions — **0**
- verified-Tamil changes — **0**
- outside English / outside-witness wording imported — **0**
- source-printed English on scan **542** — **preserved verbatim**
- speaker changes / interventions on scans **544–545** — **preserved**
- terminal boundary **545→546** — **PASS / scan 546 excluded**
- Tamil — **VERIFIED / unchanged / verified_against_scan=true**
- English — **TRANSLATED / NOT VERIFIED AGAINST TAMIL / verified_against_tamil=false**

## Gate F closure

**COMPLETE — scans 511–545 / 35 of 35 translated / 0 blockers / 0 Tamil changes.**

Gate G is **READY / NOT STARTED**.

## Exact next activity

Perform **Speech 19 Gate G Batch 1 — scans 511–540 / exactly 30 pages** reviewing the Gate-F English against the final verified Tamil.

Do not begin the Gate-G final remainder (scans 541–545) in the same activity.
