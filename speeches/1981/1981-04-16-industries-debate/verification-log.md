# Verification log — உரை : 2 / 16.04.1981

This log tracks Speech 2 as a multi-batch transcription. `in-progress` is used literally: only part of the locked speech range has been transcribed, so neither `transcribed` nor `verified` is appropriate yet.

## 1. Locked speech range

- PDF scan pages: **27–61**
- Printed pages: **26–60**
- Total scan pages in speech: **35**
- Canonical ID: `1981-04-16-industries-debate`

## 2. Tamil first-pass batch 1

**Completed:** PDF scan pp. **27–41** / printed pp. **26–40**  
**Batch size:** 15 scan pages  
**Speech state after batch:** partial

The first-pass transcription was read from the scan images, not taken from OCR as canonical text. Printed English embedded in the Tamil speech was retained, including the poverty-line sentence, Comptroller and Auditor-General material and the Government of India letter-of-intent passage.

## 3. Tamil first-pass batch 2

**Completed:** PDF scan pp. **42–56** / printed pp. **41–55**  
**Batch size:** 15 scan pages  
**Cumulative completed range:** scan pp. **27–56** / printed pp. **26–55**  
**Speech state after batch:** partial

This batch preserves the printed parliamentary exchanges involving the chair, `கலைஞர் மு. கருணாநிதி`, `மாண்புமிகு திரு. எஸ். திருநாவுக்கரசு`, `திரு. க. அன்பழகன்`, `திரு. கே. எஸ். ஜி. ஹாஜாஷெரீப்`, `திரு. துரைமுருகன்`, and `திரு. என். எஸ். வி. சித்தன்`, as printed.

Printed English source text is retained rather than translated or normalised, including:

- `Bagasse`;
- `Not Feasible`;
- `Interest free sales tax loan`;
- `IDBI refinancing`;
- the full scan-p.54 passage headed `THIRU K.S.G HAJA SHAREEF`.

## 4. Cumulative page-marker audit

**Status:** passed for the completed first-pass range only

`transcript.md` contains exactly **30** source-page markers, covering:

`27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56`

Checks:

- [x] 30 markers are present;
- [x] markers are monotonic;
- [x] no duplicate marker appears;
- [x] no page in the completed 27–56 range is skipped;
- [x] Speech 2 is still presented as partial / `in-progress`;
- [x] scan p.56 is retained as an intentionally partial sentence ending.

This is a batch-integrity check, **not** the full-speech Tamil completeness audit and **not** strict visual verification.

## 5. Batch-2 transition notes

The following source-page continuations are preserved explicitly:

- p.41 → p.42: `ஒரு மனு` → `கொடுத்தார்கள். அண்ணா அவர்கள் 6.12.1968-ல்...`
- p.42 → p.43: `தீதா கிருஷ்ணன் என்கிற` → `முன்னாள் தொழில்துறை செயலாளருக்கு மேல்;`
- p.43 → p.44: `புறப்` → `ஆகியிருக்கிறது.`
- p.44 → p.45: `இதைத்` → `தொடங்குவதற்குமுன்பு...`
- p.45 → p.46: `வட பகுதியில் அவர்கள்` → `தொழிலைத் துவங்க விரும்புகிறார்கள்;`
- p.46 → p.47: `தமிழக` → `அரசோடு அவர்கள் தொடர்பு கொண்டு...`
- p.47 → p.48: `தர நீங்கள்` → `ஒப்புக்கொள்ளவில்லை.`
- p.48 → p.49: `அவர்கள்` → `போயிருக்கிறார்கள்.`
- p.49 → p.50: `இந்த அரசு` → `தரவில்லை என்பதுதான் காரணம்.`
- p.50 → p.51: `இத்தனை ஏக்கர் இடம் வேண்டுமென்று` → `சொல்கிறார்கள்.`
- p.51 → p.52: `எந்த, எந்த` → `நேரத்திலே...`
- p.52 → p.53: `மாண்புமிகு ஜனாதிபதி` → `அவர்களும், ரயில்வே அமைச்சரும்...`
- p.54 → p.55: `என்று தெரிந்த` → `உடனே அல்லது இங்கே இருந்து...`
- p.55 → p.56: `என்று` → `சொல்கிறார்கள்.`

## 6. Exact continuation point

Current canonical first-pass text stops at the end of scan p.56:

`... தமிழ்நாட்டிலும் சில நிறுவனங்களில் தனியார் சிலர் தலைவர்களாக நியமிக்கப்`

Scan p.57 begins:

`பட்டிருக்கிறார்கள். இது ஒன்றும் புதியது அல்ல. திரு. டாண்டன்...`

**Next transcription action:** begin at scan p.57 and complete the final first-pass batch through scan p.61.

## 7. Current status

- Completed scan pages: **27–56**.
- Pending scan pages in Speech 2: **57–61**.
- Tamil first-pass status: **in-progress**.
- Full-speech completeness audit: **not yet eligible**.
- Separate strict page-by-page visual/source-fidelity verification: **not completed**.
- Explicit unresolved-reading placeholders: **none currently flagged**.
- English translation: **blocked / not started**.
- Root release index update: **not eligible while partial**.

No status in this file should be read as a claim that pp.27–56 have already passed the repository's later `verified` gate.
