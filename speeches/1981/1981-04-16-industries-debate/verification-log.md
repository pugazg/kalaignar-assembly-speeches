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
**Speech state:** partial

The first-pass transcription was read from the scan images, not taken from OCR as canonical text. Printed English embedded in the Tamil speech was retained, including:

- `High proportion of people in Tamil Nadu are below the poverty line.` on scan p.28;
- `Comptroller and Auditor-General of India` and `Tamilnadu Sugarcane Farm Corporation` on scan p.31;
- the Government of India letter-of-intent passage on scan p.40.

## 3. Batch page-marker audit

**Status:** passed for the completed batch only

`transcript.md` contains exactly these source-page markers:

`27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41`

Checks:

- [x] 15 markers are present;
- [x] markers are monotonic;
- [x] no duplicate marker appears;
- [x] no page in the completed 27–41 batch is skipped;
- [x] scan p.27 start contains the expected `உரை : 2 / நாள் : 16.04.1981` boundary;
- [x] scan p.41 is retained as an intentionally partial sentence ending;
- [x] Speech 2 is not presented as complete.

This is a batch-integrity check, **not** the full-speech Tamil completeness audit.

## 4. Batch transition notes

The following page continuations were preserved rather than silently rewriting sentence boundaries:

- p.28 → p.29: `அதிகாரிகளால்` → `சுட்டிக்காட்டப்பட்டு கூட...`
- p.29 → p.30: `வேலை` → `வாய்ப்பைப் பெற்றிருக்கிறார்கள்...`
- p.30 → p.31: `புள்ளி` → `விவரங்கள் "Comptroller and Auditor-General of India"...`
- p.31 → p.32: `பெரம்பலூர்` → `சுகர் மில்ஸ் லிமிடெட்...`
- p.32 → p.33: `பலரால்` → `எடுத்துக் காட்டப்பட்டது.`
- p.33 → p.34: `தமிழகத்திற்கு வேண்டும்` → `என்று எப்படி கேட்பது?`
- p.34 → p.35: `எழுச்சி நாள்` → `கொண்டாடினோம்.`
- p.35 → p.36: `ஆக்கிவிட்டோமோ` → `என்று ஐயத்தக்க அளவிற்கு...`
- p.36 → p.37: `மிகப்` → `பெரிய, முதல் முதல் ஒரு பெரிய...`
- p.38 → p.39: `அறிவித்து விட்டு,` → `ஆனால் அது 1983-84ம் ஆண்டிலேதான்...`
- p.39 → p.40: `மாநில திட்டக் குழுவின்` → `6வது திட்ட அறிக்கையிலே...`
- p.40 → p.41: `இதற்கு` → `மேலான விவரங்கள்...`

## 5. Exact continuation point

Current canonical first-pass text stops at the end of scan p.41:

`... கூட்டுத்துறையில் ஒரு நிறுவனத்தை ஆரம்பிக்க வேண்டுமென்று ஒரு மனு`

Scan p.42 begins:

`கொடுத்தார்கள். அண்ணா அவர்கள் 6.12.1968-ல்...`

**Next transcription action:** begin at scan p.42 and continue with the next bounded batch, recommended pp.42–56.

## 6. Current status

- Completed scan pages: **27–41**.
- Pending scan pages in Speech 2: **42–61**.
- Tamil first-pass status: **in-progress**.
- Full-speech completeness audit: **not yet eligible**.
- Separate strict page-by-page visual/source-fidelity verification: **not completed**.
- Explicit unresolved-reading placeholders: **none currently flagged**.
- English translation: **blocked / not started**.
- Root release index update: **not eligible while partial**.

No status in this file should be read as a claim that pp.27–41 have already passed the repository's later `verified` gate.
