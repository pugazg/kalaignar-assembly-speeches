# Source notes — உரை : 4 / 18.04.1990

## Source used

Scanned publication: `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

Controlling source facts:

- title: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- first edition: `மே, 2007`
- publisher: தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004
- sales rights: பூம்புகார் பதிப்பகம்
- actual PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

The PDF is image-based. The scan image is authoritative for the Tamil source layer; OCR or reconstructed text is not canonical.

## Locked boundary for Speech 4

| Field | Value |
|---|---|
| Source label | `உரை : 4` |
| Printed date | `18.04.1990` |
| Canonical ID | `1990-04-18-industries-debate` |
| PDF scan pages | **99–135** |
| Printed pages | **98–134** |

For this speech: `PDF scan page = printed page + 1`.

The opening boundary is visually explicit: scan p.99 / printed p.98 begins `உரை : 4`, `நாள் : 18.04.1990`, followed by `மாண்புமிகு கலைஞர் மு. கருணாநிதி :`.

The ending boundary was rechecked during Gates C, D and E: scan p.135 / printed p.134 contains the final interventions and ends with Kalaignar's reply to `திரு. கே. ரமணி`, followed by the decorative floral ending ornament. Scan p.136 / printed p.135 begins `உரை : 5`, `நாள் : 14.08.1996`.

## Gate C — Tamil first-pass transcription

The full speech was transcribed directly from the controlling scan in three bounded batches:

- Batch 1: **scan pp.99–113 / printed pp.98–112**
- Batch 2: **scan pp.114–128 / printed pp.113–127**
- Batch 3: **scan pp.129–135 / printed pp.128–134**

Gate C represented all **37** mapped pages with explicit `<!-- source-page: N -->` markers. Explicit unreadable/`[REVIEW]` markers: **0**.

Important page transitions preserved include p.113→114 (`யாரோ “என்.ஆர்.ஐ.” பெர்சன்களையெல்லாம்` → `துரத்துகிறோம் என்று...`) and the p.128→129 split word (`30 வட்டங்` → `களைத் தனியாக...`).

## Gate D — full-speech completeness audit

Gate D **passed** for locked scan range **99–135 / printed pp.98–134**.

- expected source-page markers: **37**;
- represented markers: **37**, exactly **99–135**;
- markers unique and monotonic;
- no mapped page skipped or duplicated;
- correct p.99 opening boundary;
- correct p.135 ending boundary and ornament;
- p.136 begins Speech 5, confirming no spillover;
- printed speaker changes/interventions represented through the final exchange;
- unresolved-reading markers: **0**.

## Gate E — strict page-by-page visual/source-fidelity verification

Gate E **passed** after the complete canonical Tamil was compared directly against every controlling scan image from **p.99 through p.135**.

The audit checked individual words/characters, names and initials, numerals, dates, percentages, monetary values and units, embedded English passages, speaker labels, punctuation and page-transition continuity. Corrections supported directly by the scan were applied to `transcript.md`; the full correction ledger is in `verification-log.md`.

Representative source-fidelity corrections include:

- p.111 printed English `ancilary` retained instead of first-pass `ancillary`;
- p.112 interruption punctuation corrected to `(குறுக்கீடு) சிரிப்பு.`;
- p.114 wording corrected to `அரசுத் தலையிட தயங்காது`, `குறிப்பிட விரும்புகிறேன்`, and `விவாதிக்கப்பட இருப்பதால்`;
- p.119 company wording corrected to `ஹம்போல் ஹெவி ஆலை`;
- p.120 source forms restored for `அழகர்சாமி ... குறிப்பிட்டார்கள்`, `ராஜேந்திரன் ... எழுப்பினார்கள்`, `அளவிற்குத்`, and `கேஸ்டிக் சோடா`;
- p.122 `உமா ஓயர் பிராடக்ட்` restored;
- p.123 date corrected from `1-11-1990` to the printed `1-1-1990`;
- pp.125–127 several first-pass wording errors corrected in the Neyveli/TIIC/sales-tax discussion, including `பேச்சு நடைபெற்று`, `அனுமதிப்பதையும்`, `வட்டி இல்லாத`, `ஏற்பட வாய்ப்பு`, and `சட்டத்திருத்தமும்`;
- p.128 list fidelity corrected for punctuation, `கும்மிடிப்பூண்டி` and `தாராபுரம் 7`;
- p.129 split printed form normalised only across physical line wrapping to `சதவிகிதத்திற்குக்`;
- p.133 source quotation marks around `“தொழில்கள்”` and the printed asterisk before `திரு. சா. பீட்டர் ஆல்போன்ஸ்` preserved;
- p.135 `இருக்கக் கூடிய` restored.

The audit also deliberately retained source anomalies rather than silently modernising them. Examples include printed English `Government of India for financed`, `constitute and Inter-Ministerial Committee`, `cilicon`, `stainlees`, `Spensioner Mill`, and `ancilary`, as well as unusual Tamil/list forms that are visibly present in the scan such as p.128 `ஆலங்குடி 3, 1, அறந்தாங்கி 4`.

Tamil status after Gate E: **verified**. Explicit unresolved Tamil readings: **0**.

## Transcription policy applied

1. Preserve printed wording, period spelling, punctuation, numerals, quotations and headings as far as legible.
2. Preserve printed English and transliterated technical terms in the Tamil source layer; normalise only physical line wrapping.
3. Preserve speaker/member interventions and interruption markers where printed.
4. Mark every PDF source page with `<!-- source-page: N -->`.
5. Do not silently repair printer errors, grammar, political/historical claims or unusual source forms.
6. Mark genuinely unreadable material for review rather than guessing.
7. Treat running headers, printed page numbers and decorative ending marks as page furniture/boundary evidence rather than speech text.

## Current gate status

- Gate C Tamil first-pass: **complete**.
- Gate D full-speech completeness audit: **passed**.
- Gate E strict Tamil source-fidelity verification: **passed**.
- Tamil status: **verified**.
- Explicit unresolved Tamil readings: **0**.
- Gate F English translation: **ready / not started**.
- Gate G English fidelity verification: **not started**.
- Gate H release/index: **not started**.

## Exact next action

Run Gate F: translate the **final verified Tamil** for scan pp.99–135 into English, preserving source-page correspondence, parliamentary interventions, figures, names, technical terms and source claims/anomalies. Do not begin Speech 5. After the complete English translation exists, run Gate G before any Gate-H release/index update.
