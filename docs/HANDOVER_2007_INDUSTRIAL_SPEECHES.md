# Handover — 2007 industrial speeches anthology

## Purpose

Authoritative continuation point for:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Repository: `pugazg/kalaignar-assembly-speeches`

The structural map is complete and locked. The scan image is authoritative for the Tamil source layer; OCR is only a helper and is never canonical. The final Gate-E-verified Tamil is authoritative for English translation/fidelity.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

Locked map: [`../sources/2007-industrial-speeches/mapping.md`](../sources/2007-industrial-speeches/mapping.md)  
Workflow: [`ARCHIVAL_WORKFLOW.md`](ARCHIVAL_WORKFLOW.md)

## Locked speech inventory

| # | Printed date | ISO date | PDF scan pages | Printed pages | Canonical ID |
|---:|---|---|---:|---:|---|
| 1 | 21.03.1963 | 1963-03-21 | 18–26 | 17–25 | `1963-03-21-industries-debate` |
| 2 | 16.04.1981 | 1981-04-16 | 27–61 | 26–60 | `1981-04-16-industries-debate` |
| 3 | 03.05.1989 | 1989-05-03 | 62–98 | 61–97 | `1989-05-03-industries-debate` |
| 4 | 18.04.1990 | 1990-04-18 | 99–135 | 98–134 | `1990-04-18-industries-debate` |
| 5 | 14.08.1996 | 1996-08-14 | 136–171 | 135–170 | `1996-08-14-industries-debate` |
| 6 | 23.04.1997 | 1997-04-23 | 172–198 | 171–197 | `1997-04-23-industries-debate` |
| 7 | 14.05.1998 | 1998-05-14 | 199–240 | 198–239 | `1998-05-14-industries-debate` |
| 8 | 29.04.1999 | 1999-04-29 | 241–277 | 240–276 | `1999-04-29-industries-debate` |
| 9 | 8.05.2000 | 2000-05-08 | 278–303 | 277–302 | `2000-05-08-industries-debate` |
| 10 | 23.08.2006 | 2006-08-23 | 304–326 | 303–325 | `2006-08-23-industries-debate` |

## Completed released work

### Speech 1 — fully released

`1963-03-21-industries-debate`, scan pp.18–26 / printed pp.17–25:

- Tamil: **verified**
- English: **verified**
- release/index commit: `ff2d8d5bb09f07925f8da791b138132041a92f52`

### Speech 2 — fully released

`1981-04-16-industries-debate`, scan pp.27–61 / printed pp.26–60:

- first-pass/completeness commit: `88fb033a2def03f3ef972907b9b6558ad6dbd679`
- Tamil verification commit: `69692a5ed47c937cebea3a19914d2becacc0ab7a`
- English translation + fidelity commit: `9cf3b58fe6530089c8ef08206ceb392261f14d6a`
- root README release commit: `ac49ce2e4696573569816e1dbd747c4dbef74a99`
- `data/speeches.json` release commit: `eb5dda73afbcdf63bfb3735badd04e81b976502c`

Do not alter Speeches 1 or 2 unless separately requested.

## Current active work — Speech 3

- Source label: `உரை : 3`
- Printed date: `03.05.1989`
- Canonical ID: `1989-05-03-industries-debate`
- Locked source range: **scan pp.62–98 / printed pp.61–97**
- Folder: `speeches/1989/1989-05-03-industries-debate/`

### Gate C — complete

Tamil first-pass transcription was completed in three bounded batches:

- Batch 1: **scan pp.62–76 / printed pp.61–75**
- Batch 2: **scan pp.77–91 / printed pp.76–90**
- Batch 3: **scan pp.92–98 / printed pp.91–97**

Final first-pass transcript commit: `d61e938659da1f41bb9188608835146e4f980556`.

### Gate D — passed

The full-speech completeness audit confirmed exactly **37** unique, monotonic source-page markers, **62–98**, no mapped page skipped or duplicated, correct opening/ending boundaries, final parliamentary interventions represented and no unresolved marker.

Gate-D verification-log commit: `32823326403fc8560880ac21257d7c7f3ebac881`.

### Gate E — passed

A strict direct visual/source-fidelity audit was completed against **every controlling scan image p.62 through p.98**.

Four concrete Tamil first-pass discrepancies were corrected:

1. scan p.73: `கருத்தக் கூடாது` → `கருதக் கூடாது`;
2. scan p.94: `சுவரார் அளித்த சலுகைகளும்` → `கவர்னர் அளித்த சலுகைகளும்`;
3. scan p.96: `பரிசீலிப்பு விழாக்களில்` → `பரிசளிப்பு விழாக்களில்`;
4. scan p.97: `கூடங்குளம் போகும்` → `கூடங்குளம் போக்கும்`.

Visibly printed unusual forms were retained rather than silently repaired, including `1986-86-ல்`, `அசோசியேட் செக்டரி`, `வெளிக் கொணரத் தலைப்பட்டது`, the p.92 `547` / `541` estimate inconsistency, and the repeated p.93 wordplay.

Gate-E sequential commits:

- verified transcript: `56716121b7535a3ba22475135e10ae93e4c3c22f`
- verified metadata: `08d81282eef4bc3ffaf694d94727eecd4ecc96c2`
- README/status: `0c231a9622bef8895ed57062f9bb122525ed6529`
- source notes: `281d36a5c07c39c2e9a84838091092815a33d76b`
- verification log / final Gate-E state: `523d7cbf26b1d0e605c5abe65a85974559983cbb`

### Gate F — complete

The complete English translation was produced **only from the final verified Tamil** and appended after the Tamil source layer in `transcript.md`.

Gate-F sequential commits:

- transcript with complete English layer: `cc844648fa3c220b2c721f4177d6e572f58d66a8`
- metadata/status: `d47131215ba08ed318ba3a2406b95a29817cc4e0`
- README/status: `df8c140672d4f36c1affe44639bb92c6f1b54e45`
- source notes: `b320fbd82a326ce86e00822d5c7d0417d81a4704`
- verification log / final Gate-F Speech-3 state: `25469c85158c56cca96e95c8a93b45326f5346ea`

### Gate G — passed

The complete English translation was re-read **page by page against the final Gate-E-verified Tamil for all 37 source pages, 62–98**.

Gate-G checks confirmed:

- exactly **37** English `### Source page N` headings, unique and monotonic from **62 through 98**;
- no omitted or duplicated English source page and no spillover into Speech 4;
- meaning, speaker attribution, parliamentary interventions, quotations, names/initials, dates, numerals, percentages, monetary values/units, industrial terminology and page-transition continuity checked against the corresponding verified Tamil;
- p.66 `1986-86`, p.71 “Associate Sectary,” p.92 `547` / `541` / `721`, p.93 repeated wordplay/laughter and all final interventions remain source-faithful.

Two Gate-G source-preservation/fidelity corrections were made:

1. **p.86:** `aluminium sheets and strips` → `aluminium sheets and pattadaigal (பட்டாடைகள், as printed in the Tamil source)`;
2. **p.94:** `SIPCOT and TIIC` → `SIPCOT and TIC (டிக் in the Tamil source)`.

Gate-G sequential commits:

- verified English transcript: `eb0190d52f12d21411c4638d8d7ae8a911f85805`
- verified English metadata: `0643c283c9b0db432dd1d6800c8dec6f54e94c86`
- README/status: `4196823d4f2140524a4b7ad2f701d1c5c83223b7`
- source notes: `6953ad0e153887d89cd2022204ec0655f85d3596`
- verification log / final Gate-G Speech-3 state: `b7504bb53148a967ba80a8383d25a9a25cd7359b`

Current Speech 3 status:

- Tamil first-pass: **complete**
- Gate D completeness: **passed**
- Gate E Tamil source-fidelity verification: **passed**
- Tamil status: **verified**
- unresolved Tamil readings: **0**
- Gate F English translation: **complete**
- Gate G English fidelity verification: **passed**
- English status: **verified**
- Gate H: **next / eligible**
- root README speech index / `data/speeches.json`: **not yet updated for Speech 3**

## Immediate next action — Gate H release/index

Release Speech 3 through the repository indexes, following the existing released Speech 2 precedent.

For Gate H:

1. Fetch/read current root `README.md`, `data/speeches.json`, Speech 3 `README.md` and `metadata.json` from `main` before editing.
2. Add Speech 3 to the root released-speech table with its verified Tamil/English status and source page range.
3. Add a Speech 3 object to `data/speeches.json` using the existing schema and the source-grounded Speech 3 metadata. Set `languages` to `ta` and `en`, `transcription_status` to `verified`, `verified_against_scan` to `true`, and `translation_status` to `verified`.
4. Do not invent a formal event title unsupported by the source. Use only the neutral/source-grounded archival framing already established in the Speech 3 files and released-entry precedent.
5. Validate that `data/speeches.json` remains valid JSON and that existing released entries remain unchanged.
6. Update this handover and the next-chat prompt with the Gate-H commit SHAs and final Speech 3 release state.
7. Only after Gate H is complete may Speech 4 (`1990-04-18-industries-debate`, scan pp.99–135 / printed pp.98–134) become the next active speech.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- `speeches/1981/1981-04-16-industries-debate/`;
- already released root index/data entries except to append Speech 3 at Gate H;
- unrelated sources/speeches;
- Speech 4 until Speech 3 Gate H is complete.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
