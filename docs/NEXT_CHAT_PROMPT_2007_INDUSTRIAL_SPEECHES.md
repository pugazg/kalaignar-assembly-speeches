# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1989/1989-05-03-industries-debate/`
- root `README.md`
- `data/speeches.json`

Treat those files as controlling instructions. The scan image is authoritative for the Tamil source layer; the final Gate-E-verified Tamil is authoritative for English fidelity. OCR is not canonical.

## Completed released work

Speech 1 (`1963-03-21-industries-debate`) and Speech 2 (`1981-04-16-industries-debate`) are fully released with verified Tamil and verified English and must remain untouched unless separately requested.

## Current active work — Speech 3

- Source label: `உரை : 3`
- Printed date: `03.05.1989`
- Canonical ID: `1989-05-03-industries-debate`
- Full scan range: **62–98**
- Printed pages: **61–97**
- Gate C: **complete**
- Gate D: **passed**
- Gate E: **passed**
- Tamil status: **verified**
- Explicit unresolved Tamil readings: **0**
- Gate F: **complete**
- Gate G: **passed**
- English status: **verified**
- Gate H: **next / eligible**
- Gate-G transcript commit: `eb0190d52f12d21411c4638d8d7ae8a911f85805`
- Gate-G metadata commit: `0643c283c9b0db432dd1d6800c8dec6f54e94c86`
- Gate-G README commit: `4196823d4f2140524a4b7ad2f701d1c5c83223b7`
- Gate-G source-notes commit: `6953ad0e153887d89cd2022204ec0655f85d3596`
- Gate-G verification-log commit: `b7504bb53148a967ba80a8383d25a9a25cd7359b`

Gate G re-read the complete English page by page against the final verified Tamil for exactly **37 source pages, 62 through 98**. Two concrete source-preservation/fidelity corrections were made:

- p.86 `aluminium sheets and strips` → `aluminium sheets and pattadaigal (பட்டாடைகள், as printed in the Tamil source)`;
- p.94 `SIPCOT and TIIC` → `SIPCOT and TIC (டிக் in the Tamil source)`.

The review also confirmed that the English retains source-supported anomalies including p.66 `1986-86`, p.71 “Associate Sectary,” p.92 `547` / `541` / `721`, p.93 repeated wordplay/laughter and the final interventions through p.98.

## Next action — Speech 3 Gate H release/index

Release Speech 3 through the repository indexes, following the existing released Speech 2 precedent.

1. Fetch/read current root `README.md`, `data/speeches.json`, Speech 3 `README.md` and `metadata.json` from `main` before editing.
2. Add Speech 3 to the root released-speech table with its verified Tamil/English status and its source range **scan pp.62–98 / printed pp.61–97**.
3. Add Speech 3 to `data/speeches.json` using the existing schema and source-grounded metadata. Set:
   - `id`: `1989-05-03-industries-debate`
   - `date`: `1989-05-03`
   - `year`: `1989`
   - `speaker_ta`: `மு. கருணாநிதி`
   - `speaker_en`: `M. Karunanidhi`
   - `path`: `speeches/1989/1989-05-03-industries-debate`
   - `languages`: `["ta", "en"]`
   - `transcription_status`: `verified`
   - `verified_against_scan`: `true`
   - `translation_status`: `verified`
4. Use only a source-grounded/neutral title and event description already supported by the Speech 3 files and the released-entry precedent. Do not invent a formal Assembly event or resolution title that is absent from the source.
5. Validate that `data/speeches.json` is valid JSON and that the existing released Speech 1/Speech 2/1970 records remain unchanged except for appending the new Speech 3 record.
6. Update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and this next-chat prompt with the Gate-H commit SHAs and final released state.
7. Only after Gate H is complete may Speech 4 (`1990-04-18-industries-debate`, scan pp.99–135 / printed pp.98–134) become the next active speech.

Do not begin Speech 4 during Gate H itself.

---
