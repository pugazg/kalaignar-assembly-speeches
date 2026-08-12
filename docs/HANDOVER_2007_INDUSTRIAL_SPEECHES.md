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

## Completed canonical work

### Speech 1 — fully released

`1963-03-21-industries-debate`, scan pp.18–26 / printed pp.17–25:

- Tamil: **verified**
- English: **verified**
- released/indexed in root README and `data/speeches.json`
- release/index commit: `ff2d8d5bb09f07925f8da791b138132041a92f52`

Do not alter Speech 1 unless separately requested.

## Current active work — Speech 2

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Source range: **scan pp.27–61 / printed pp.26–60**
- Folder: `speeches/1981/1981-04-16-industries-debate/`
- First-pass/completeness commit: `88fb033a2def03f3ef972907b9b6558ad6dbd679`

### Tamil first pass and Gate D — complete

Speech 2 was transcribed in three bounded batches: **27–41**, **42–56**, and **57–61**.

The Gate-D completeness audit passed with exactly **35** unique, monotonic source-page markers, no skipped/duplicated mapped page, correct opening and ending boundaries, and no unresolved placeholder.

### Gate E — strict Tamil source-fidelity verification complete

Every scan image from **p.27 through p.61** was directly re-read against the canonical transcript after Gate D. The audit checked words/characters, names/initials, figures/dates/percentages/units, printed English, headings, speaker labels/interventions, legible punctuation and page-transition continuity.

Nine additional first-pass discrepancies were corrected:

- p.29 `இன்னைக்கும்` → `இன்றைக்கும்`;
- p.29 `சனவரி திங்களில்` → `சனவரித் திங்களில்`;
- p.32 `நமக்கு கொடுப்பதற்கு` → `நமக்குக் கொடுப்பதற்கு` in the `8 சதவீதம்` sentence;
- p.38 `திட்டத்தட்ட` → `கிட்டத்தட்ட`;
- p.38 `விடப்படைக்கூடிய` → `விடப்படையக்கூடிய`;
- p.44 `ஃபீசிபிள் அல்ல` → `பீசிபிள் அல்ல` at that specific source occurrence;
- p.45 `நாட் ஃபீசிபிள்` → `நாட் பீசிபிள்`;
- p.51 `இப்பொழுதுதான்` → `இப்பொழுது தான்`;
- p.60 `நிலையையும்` → `நிலைமையும்`.

Unusual but visibly printed forms were deliberately retained rather than normalised, including `வாங்கலை`, `Not Feasible என்று என்று`, the separate p.45 `ஃபீசிபிள் என்று ப்ரூப் செய்யப்படாத`, `::பர்ஸ்ட் ஸ்டேஜ்`, `::பெர்டிலைசர்ஸ்`, `109 கோடி`, and the unusual p.61 `சட்டத்திலேயும் ... கடுமையாக விமர்சிக்கப்பட்டு` passage.

### Current Speech 2 status

- Tamil first-pass: **complete**
- Tamil completeness audit: **passed**
- Strict Tamil page-by-page/source-fidelity verification: **passed for pp.27–61**
- Tamil status: **verified**
- Unresolved Tamil readings: **none**
- English translation: **not started**
- Verified-Tamil prerequisite for translation: **satisfied**
- Root release index and `data/speeches.json`: **not yet updated**

The root release/index files must remain untouched until the English translation is complete and has passed its own fidelity verification.

## Immediate next action

Begin **English translation of Speech 2 from the verified Tamil only**.

Requirements for the English stage:

- place English only after the complete verified Tamil in `transcript.md`;
- preserve the source-page sequence with `### Source page 27` through `### Source page 61`;
- preserve argumentative sequence, parliamentary context, quotations, names, figures and technical terms;
- translate the verified Tamil, not OCR or an earlier draft;
- do not silently correct source claims, period terminology or unusual printed statements;
- keep embedded English source passages faithful to what is already printed rather than rewriting them as if they were translator prose.

After the complete English translation, perform a **separate full English fidelity verification against the final verified Tamil**. Only after that may English be marked `verified` and the Gate-H release/index update begin.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- root README and `data/speeches.json` until Speech 2 reaches the release gate;
- Speech 3 and unrelated sources/speeches.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, translation status, files changed, commit SHA, and exact next action.
