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

The full-speech completeness audit has passed:

- exactly **37** source-page markers, **62–98**;
- markers unique and monotonic;
- no mapped page skipped or duplicated;
- p.62 opening matches the locked Speech 3 start;
- p.98 ends with Kalaignar's reply to `திரு. வி. கே. சின்னசாமி` followed by the decorative floral ending ornament;
- p.99 directly checked and begins `உரை : 4 / நாள் : 18.04.1990`;
- parliamentary interventions through pp.94–98 are represented;
- explicit unreadable/`[REVIEW]` markers: **0**.

Gate-D/status commits:

- metadata: `5200d5f14c016374626eb7ee28fa47979a795432`
- README: `7b30fce84a2427ae29328c072fe5a24aabe1f109`
- source notes: `d927c4cc93ab301cb43057c463a50d60c63e4302`
- verification log / Gate D: `32823326403fc8560880ac21257d7c7f3ebac881`

Current Speech 3 status:

- Tamil first-pass: **complete**
- Gate D completeness: **passed**
- Tamil status: **transcribed**
- unresolved Tamil readings: **0 explicitly flagged**
- Gate E strict visual/source-fidelity verification: **not started**
- English translation: **blocked / not started**
- root README speech index / `data/speeches.json`: **not updated for Speech 3**

## Immediate next action — Gate E

Perform a strict direct page-by-page visual/source-fidelity audit of the complete canonical Tamil against the controlling scan for **scan pp.62–98 / printed pp.61–97**.

For Gate E:

1. Read current `transcript.md`, `metadata.json`, `source-notes.md` and `verification-log.md` before editing.
2. Re-read every scan image p.62 through p.98 directly; scan images control all readings.
3. Compare the canonical Tamil page by page, checking words/characters, names/initials, dates, numerals, percentages, monetary values/units, printed English/transliterations, headings, speaker labels/interventions, punctuation where legible, and page-transition continuity.
4. Correct every concrete discrepancy in `transcript.md` and document the corrections in `verification-log.md`.
5. Do not silently modernise or repair source wording that is visibly printed, even when unusual.
6. If a reading remains genuinely uncertain, leave an explicit review marker rather than guessing.
7. Only after all pp.62–98 are directly checked may Tamil status become `verified`.
8. English remains blocked until Gate E passes.
9. Do not begin Speech 4.

After Gate E passes, the next workflow stage will be Gate F English translation from the final verified Tamil.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- `speeches/1981/1981-04-16-industries-debate/`;
- root released-speech index entries for already released speeches;
- unrelated sources/speeches;
- Speech 4 until Speech 3 has completed its own workflow and release.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
