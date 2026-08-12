# Handover — 2007 industrial speeches anthology

## Purpose

Authoritative continuation point for:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Repository: `pugazg/kalaignar-assembly-speeches`

The structural map is complete and locked. The scan image is authoritative; OCR is only a helper and is never canonical.

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

Four concrete first-pass discrepancies were corrected:

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

The complete English translation has been produced **only from the final verified Tamil** and appended after the Tamil source layer in `transcript.md`.

Gate-F state:

- English source-page correspondence: **37 pages, 62–98**;
- full argumentative/source sequence retained;
- speaker changes and parliamentary interventions translated;
- dates, figures, percentages, monetary values, units, quotations and technical terminology carried through;
- laughter and desk-thumping markers retained in English;
- unusual source-supported terminology and internal inconsistencies were not silently corrected from outside knowledge;
- English status: **complete-unverified**;
- Gate G fidelity review: **not started**.

Gate-F sequential commits:

- transcript with complete English layer: `cc844648fa3c220b2c721f4177d6e572f58d66a8`
- metadata/status: `d47131215ba08ed318ba3a2406b95a29817cc4e0`
- README/status: `df8c140672d4f36c1affe44639bb92c6f1b54e45`
- source notes: `b320fbd82a326ce86e00822d5c7d0417d81a4704`
- verification log / final Gate-F Speech-3 state: `25469c85158c56cca96e95c8a93b45326f5346ea`

Current Speech 3 status:

- Tamil first-pass: **complete**
- Gate D completeness: **passed**
- Gate E strict source-fidelity verification: **passed**
- Tamil status: **verified**
- unresolved Tamil readings: **0**
- Gate F English translation: **complete**
- English status: **complete-unverified**
- Gate G: **next**
- Gate H: **blocked**
- root README speech index / `data/speeches.json`: **not updated for Speech 3**

## Immediate next action — Gate G English fidelity verification

Perform a strict page-by-page review of the **complete English translation against the final verified Tamil** for source pages **62–98**.

For Gate G:

1. Read the current Speech 3 `transcript.md`, `metadata.json`, `source-notes.md`, `verification-log.md` and `README.md` from `main` before editing.
2. Compare each English `### Source page N` section directly against the corresponding verified Tamil `<!-- source-page: N -->` section.
3. Check completeness and fidelity of meaning, speaker attribution, parliamentary interventions, quotations, dates, numerals, percentages, monetary values/units, industrial terminology, source-supported names/initials and page-transition continuity.
4. Pay particular attention to source anomalies deliberately retained in Tamil, including `1986-86-ல்`, `அசோசியேட் செக்டரி`, the p.92 `547` / `541` inconsistency, and the repeated p.93 wordplay. The English must not silently erase or historically repair these.
5. Correct every concrete English fidelity discrepancy in `transcript.md` and document all corrections in `verification-log.md`.
6. Only after all **37 pages 62–98** have been directly checked may English status become `verified`.
7. After Gate G passes, Gate H release/index becomes eligible: update root README and `data/speeches.json` following the Speech 2 precedent.
8. Do not begin Speech 4 before Speech 3 Gate H is complete.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- `speeches/1981/1981-04-16-industries-debate/`;
- root released-speech index entries for already released speeches;
- unrelated sources/speeches;
- Speech 4 until Speech 3 Gate H is complete.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
