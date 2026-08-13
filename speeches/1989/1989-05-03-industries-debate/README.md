# உரை : 3 — 03.05.1989

## தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்

**மூலத்தில் உள்ள பேச்சாளர் குறிப்பு:** மாண்புமிகு கலைஞர் மு. கருணாநிதி  
**மூல உரை எண்:** உரை : 3  
**மூலத்தில் அச்சிடப்பட்ட தேதி:** 03.05.1989  
**காப்பக ID:** `1989-05-03-industries-debate`

`industries-debate` என்பது தொகுப்பின் தொழில்துறைச் சார்பை அடிப்படையாகக் கொண்ட நடுநிலையான காப்பக slug மட்டுமே. இதை மூலத்தில் அச்சிடப்பட்ட அதிகாரப்பூர்வ சட்டமன்ற நிகழ்வு/தீர்மானத் தலைப்பாகக் கருதவில்லை.

பேச்சாளரின் அக்காலப் பதவியை வெளிப்புற வரலாற்றுத் தகவலை கொண்டு சேர்க்காமல், மூலத்தில் அச்சிடப்பட்ட speaker label மட்டுமே source metadata-ஆகப் பதிவு செய்யப்பட்டுள்ளது.

## மூல வெளியீடு

- **நூல்:** `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- **முதற்பதிப்பு:** மே, 2007
- **வெளியீட்டாளர்:** தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004
- **விற்பனை உரிமை:** பூம்புகார் பதிப்பகம்
- **PDF scan pages:** 329
- **SHA-256:** `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

## இந்த உரையின் முழுப் பக்க வரம்பு

| வகை | வரம்பு |
|---|---:|
| PDF scan pages | 62–98 |
| Printed pages | 61–97 |

இந்த உரையில் scan page = printed page + 1. PDF scan page மற்றும் அச்சுப் பக்க எண் தனித்தனியாகப் பதிவு செய்யப்படுகின்றன.

## Tamil transcription and verification status

The complete Tamil transcription covers **scan pp.62–98 / printed pp.61–97** in three first-pass batches:

- Batch 1: **62–76**
- Batch 2: **77–91**
- Batch 3: **92–98**

Gate D full-speech completeness audit passed with exactly **37** unique, monotonic source-page markers, **62 through 98**, no skipped or duplicated mapped page, correct opening/ending boundaries and all printed interventions represented.

Gate E then re-read **every scan page 62–98 directly against the canonical Tamil**. Four concrete first-pass discrepancies were corrected:

1. scan p.73: `கருத்தக் கூடாது` → `கருதக் கூடாது`;
2. scan p.94: `சுவரார் அளித்த சலுகைகளும்` → `கவர்னர் அளித்த சலுகைகளும்`;
3. scan p.96: `பரிசீலிப்பு விழாக்களில்` → `பரிசளிப்பு விழாக்களில்`;
4. scan p.97: `கூடங்குளம் போகும்` → `கூடங்குளம் போக்கும்`.

No unresolved Tamil reading remains. Tamil status is **verified**.

## Gate F — English translation

The complete English translation was produced **only from the final verified Tamil** and appended after the Tamil source layer in `transcript.md`.

Gate F covers the full source sequence **62–98** and preserves source-page correspondence for all **37** pages, the parliamentary speaker sequence and interventions, names/initials, dates, numerals, percentages, monetary values/units, quotations, laughter and desk-thumping markers, technical terminology and source-supported anomalies.

## Gate G — English fidelity verification

Gate G has **passed**. Each of the **37 English source-page sections, 62–98**, was re-read directly against the corresponding final verified Tamil section.

The p.86 source-preservation correction remains:

- **source p.86** — provisional English `aluminium sheets and strips` was changed to `aluminium sheets and pattadaigal (பட்டாடைகள், as printed in the Tamil source)`.

### Post-release institutional correction — source p.94

The Tamil source layer visibly prints `சிப்காட், டிக் நிறுவனங்களிடமிருந்து...` and remains unchanged because the scan controls the transcription. During Gate G the English had been changed from `TIIC` to `TIC` solely to mirror the printed Tamil form `டிக்`.

The project owner subsequently clarified that the institution referred to is **TIIC**, not `TIC`; there is no intended Tamil Nadu industrial institution called `TIC` in this context. The final English translation has therefore been corrected to **`SIPCOT and TIIC`**. This is recorded as an editorial/institutional identification in the English layer, while the source-faithful Tamil continues to preserve the printed `டிக்`.

The review also confirmed that source anomalies deliberately retained in the Tamil remain visible in English, including the p.66 `1986-86` date, the p.71 source term `Associate Sectary`, the p.92 `547` / `541` / `721` estimate sequence and the repeated p.93 wordplay.

English status remains **verified** after the documented post-release correction.

## Gate H — release/index

Gate H has **passed**.

- Speech 3 is present in the root repository speech index with Tamil and English both marked `Verified` and source coverage `scan pp. 62–98`.
- `data/speeches.json` contains the `1989-05-03-industries-debate` record using the existing released-entry schema.
- The machine-readable entry records `languages: ["ta", "en"]`, `transcription_status: "verified"`, `verified_against_scan: true`, and `translation_status: "verified"`.
- The existing released Speech 1, 1970, and Speech 2 records were left unchanged; Speech 3 was appended as the fourth machine-readable record.
- The resulting `data/speeches.json` was parsed successfully as valid JSON.

Release/index commits:

- root README: `3e3dfe207435dd8d78ef263d472798e2acc248e5`
- `data/speeches.json`: `a83d671fb6d313e30c3846658f38546eff049796`

## கோப்புகள்

- [`transcript.md`](./transcript.md) — complete verified Tamil plus verified English translation, with source-page correspondence and the documented p.94 TIIC institutional correction.
- [`metadata.json`](./metadata.json) — source, full range, Tamil verification and English verification status metadata.
- [`source-notes.md`](./source-notes.md) — source authority, locked boundaries and verification/release/editorial-correction notes.
- [`verification-log.md`](./verification-log.md) — Gate-C through Gate-H workflow records plus the post-release TIIC correction.

## தற்போதைய நிலை

- Tamil first-pass transcription: **complete**.
- Gate D Tamil completeness: **passed**.
- Gate E Tamil source-fidelity verification: **passed for scan pp.62–98**.
- Tamil status: **verified**.
- Explicit unresolved Tamil readings: **0**.
- Gate F English translation: **complete**.
- Gate G English fidelity verification: **passed for all 37 source pages, 62–98**.
- English status: **verified**.
- Gate H release/index: **passed**.
- Release status: **fully released**.
- Post-release p.94 institutional correction: **English uses TIIC; Tamil source remains `டிக்`**.
- Next anthology unit: Speech 4, `1990-04-18-industries-debate`, scan pp.99–135 / printed pp.98–134.

## காப்பகக் குறிப்பு

Scan image தான் canonical source for the Tamil layer. The final Gate-E-verified Tamil is authoritative for English fidelity, while explicitly documented editorial identification may be recorded separately in the English layer when requested. OCR canonical text அல்ல. Printed wording, period spelling, punctuation, numerals, quotations, speaker labels, interventions and printed English are preserved as far as the scan permits; physical line wrapping alone is normalised. Running headers, printed page numbers and the closing decorative ornament are treated as page furniture/boundary evidence rather than speech text. Source forms that are visibly unusual remain preserved rather than silently modernised.
