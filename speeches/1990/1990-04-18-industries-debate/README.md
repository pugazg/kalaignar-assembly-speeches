# உரை : 4 — 18.04.1990

## தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்

**மூலத்தில் உள்ள பேச்சாளர் குறிப்பு:** மாண்புமிகு கலைஞர் மு. கருணாநிதி  
**மூல உரை எண்:** உரை : 4  
**மூலத்தில் அச்சிடப்பட்ட தேதி:** 18.04.1990  
**காப்பக ID:** `1990-04-18-industries-debate`

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
| PDF scan pages | 99–135 |
| Printed pages | 98–134 |

இந்த உரையில் scan page = printed page + 1. PDF scan page மற்றும் அச்சுப் பக்க எண் தனித்தனியாகப் பதிவு செய்யப்படுகின்றன.

## Gate C — Tamil first-pass transcription

Gate C is **complete** for the full locked range **scan pp.99–135 / printed pp.98–134**, produced in three bounded batches:

- Batch 1: scan pp.99–113 / printed pp.98–112
- Batch 2: scan pp.114–128 / printed pp.113–127
- Batch 3: scan pp.129–135 / printed pp.128–134

All 37 source pages are represented. Explicit unresolved/`[REVIEW]` readings after Gate C: **0**.

## Gate D — Tamil completeness audit

Gate D **passed**.

- expected mapped pages: **37**;
- represented source-page markers: **37**, exactly **99–135**;
- markers are unique and monotonic;
- no mapped page is skipped or duplicated;
- opening boundary matches scan p.99 (`உரை : 4`, `நாள் : 18.04.1990`);
- ending boundary matches scan p.135, where the final exchange is followed by the decorative ending ornament;
- scan p.136 begins `உரை : 5`, dated `14.08.1996`;
- final printed speaker changes/interventions are represented;
- unresolved-reading markers: **0**.

## Gate E — strict Tamil source-fidelity verification

Gate E **passed** for **all scan pp.99–135**.

The canonical Tamil was re-read page by page directly against the controlling scan, checking words/characters, names and initials, numerals, dates, percentages, monetary values and units, embedded English, speaker labels, punctuation and page transitions. Source-supported first-pass discrepancies were corrected in `transcript.md`; the concrete corrections are recorded in [`verification-log.md`](./verification-log.md).

Visible source anomalies were deliberately retained rather than silently regularised, including printed English forms such as `financed`, `constitute and Inter-Ministerial Committee`, `cilicon`, `stainlees`, `Spensioner Mill` and `ancilary` where those are what the scan prints.

Tamil status is **verified**. Explicit unresolved Tamil readings: **0**.

## Gate F — English translation

Gate F is **complete** for the entire verified range **scan pp.99–135**.

The English was translated only from the final verified Tamil. Every one of the 37 Tamil source-page sections has a matching English `### Source page N` section in [`translation.md`](./translation.md). The translation preserves parliamentary speaker changes and interventions, names, figures, quotations, technical terminology, argument sequence and the source's unusual or internally inconsistent claims. Printed English correspondence embedded in the source has been retained in its source form, including visible anomalies rather than silently corrected.

The English is currently **translated, not yet verified**. Gate G must re-read all 37 English page sections directly against the verified Tamil. The Gate-F companion file is a working translation artifact; after Gate G passes, the verified English should be incorporated after the Tamil layer in the canonical `transcript.md` in line with the established repository format.

## கோப்புகள்

- [`transcript.md`](./transcript.md) — complete **verified** Tamil transcription for scan pp.99–135.
- [`translation.md`](./translation.md) — complete Gate-F English translation for source pages 99–135; **Gate G pending**.
- [`metadata.json`](./metadata.json) — source, locked range, verified Tamil and Gate-F translation state.
- [`source-notes.md`](./source-notes.md) — source authority, boundaries, batch history and audit/translation notes.
- [`verification-log.md`](./verification-log.md) — Gate C–E records plus Gate-F translation record.

## தற்போதைய நிலை

- Gate C Tamil first-pass: **complete**.
- Gate D full-speech completeness audit: **passed**.
- Gate E strict Tamil source-fidelity verification: **passed**.
- Tamil transcription status: **verified**.
- Explicit unresolved Tamil readings: **0**.
- Gate F English translation: **complete — 37/37 source pages**.
- English translation status: **translated / not yet verified**.
- Gate G English fidelity check: **not started**.
- Gate H release/index: **not started**.
- Exact next action: **Gate G — re-read English source pages 99–135 against the final verified Tamil, correct every fidelity issue found, then integrate the verified English after the Tamil in `transcript.md`.**

## காப்பகக் குறிப்பு

Scan image தான் canonical source for the Tamil layer. OCR canonical text அல்ல. Printed wording, period spelling, punctuation, numerals, quotations, speaker labels, interventions and printed English are preserved as far as the scan permits; physical line wrapping alone is normalised. Running headers, printed page numbers and the final decorative ornament are page furniture/boundary evidence rather than speech text. The English layer is subordinate to and derived from the final verified Tamil, and must not be treated as verified until Gate G passes.
