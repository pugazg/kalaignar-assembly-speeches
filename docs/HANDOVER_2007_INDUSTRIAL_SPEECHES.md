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

### Tamil first pass — complete

Speech 2 has now been transcribed in three bounded batches:

- Batch 1: scan pp.27–41
- Batch 2: scan pp.42–56
- Batch 3: scan pp.57–61

Cumulative range: **scan pp.27–61 / printed pp.26–60**.

The full-speech Gate-D completeness audit has passed:

- all **35** mapped source pages are represented;
- source-page markers **27–61** are complete, unique and monotonic;
- no mapped page is duplicated or skipped;
- the opening aligns with `உரை : 2 / நாள் : 16.04.1981`;
- printed speaker changes/interventions are represented;
- no explicit unreadable/`[REVIEW]` placeholder remains;
- scan p.61 contains Kalaignar's final intervention followed by the decorative ending ornament;
- scan p.62 begins `உரை : 3 / நாள் : 03.05.1989`, confirming the locked end boundary.

A direct visual reading of p.57 corrected the earlier continuation note: the source reads `பட்டிருக்கிறார்கள். இது ஒன்றும் புதிதும் அல்ல.` rather than `புதியது அல்ல`.

### Current Speech 2 status

- Tamil first-pass: **complete**
- Tamil completeness audit: **passed**
- Tamil status: **transcribed**
- Strict Tamil page-by-page/source-fidelity verification: **not yet completed**
- Explicit unresolved-reading placeholders: **0**, but this is not a verification claim
- English translation: **blocked / not started**
- Root release index and `data/speeches.json`: **not yet updated**

`transcribed` must not be treated as `verified`. English must remain blocked until the separate strict visual verification is genuinely complete.

## Immediate next action

Perform **Gate E — strict Tamil visual/source-fidelity verification across scan pp.27–61**, page by page.

Check words/characters, names and initials, figures/dates/percentages/units, printed English, headings, speaker labels, punctuation where legible, and omissions/repetitions across page transitions. Apply every correction found and document it in `verification-log.md`.

Only after that audit may Tamil be marked `verified` and English translation begin.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- root release index and `data/speeches.json` until Speech 2 reaches its release gate;
- unrelated sources/speeches.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, translation status, files changed, commit SHA, and exact next action.
