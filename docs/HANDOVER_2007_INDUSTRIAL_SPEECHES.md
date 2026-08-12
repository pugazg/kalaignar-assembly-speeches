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
- Tamil verification commit: `69692a5ed47c937cebea3a19914d2becacc0ab7a`
- English translation + fidelity commit: `9cf3b58fe6530089c8ef08206ceb392261f14d6a`

### Tamil gates complete

Speech 2 was transcribed in three bounded batches: **27–41**, **42–56**, and **57–61**. Gate D passed with exactly **35** unique, monotonic source-page markers, correct locked boundaries and no unresolved placeholder.

Gate E then directly re-read every scan image from **p.27 through p.61** against the canonical Tamil. Nine first-pass discrepancies were corrected and documented. Tamil status is now **verified**, with **no unresolved Tamil readings**.

### English translation and Gate G complete

The English translation was produced only from the final verified Tamil and appended after the complete Tamil transcription. It preserves **35 source-page headings, 27–61**, parliamentary speaker changes/interventions, names, figures, quotations and technical terms.

A separate Gate-G fidelity review was completed page by page against the final verified Tamil. Printed English already present in the source—especially the Government of India letter-of-intent passage on scan p.40 and the `THIRU K.S.G HAJA SHAREEF` intervention on scan p.54—was retained as source English rather than silently rewritten.

Current Speech 2 status:

- Tamil transcription: **verified**
- Unresolved Tamil readings: **none**
- English translation: **complete**
- English fidelity verification: **passed**
- English status: **verified**
- Root README and `data/speeches.json`: **not yet updated**

## Immediate next action — Gate H release/index

Release/index **Speech 2 only**.

Before editing, inspect the current root `README.md` and `data/speeches.json` and follow the established released-speech schema used for Speech 1 and the existing verified 1970 speech. Do not invent fields.

Update only the release/index files actually required by that schema. Record Speech 2 as having verified Tamil and verified English, with links/metadata consistent with existing entries. Validate JSON after editing.

Do **not** alter Speech 2 transcript/source files during Gate H unless a concrete release-blocking inconsistency is discovered. Do not begin Speech 3 in the same release commit.

After Gate H is complete, the next mapped unit is:

- Speech 3
- printed date: `03.05.1989`
- canonical ID: `1989-05-03-industries-debate`
- scan pp. **62–98** / printed pp. **61–97**

Speech 3 must then begin with Tamil first-pass transcription; English remains blocked until its Tamil gates are completed.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- Speech 2 canonical text during the Gate-H index update;
- Speech 3 until Speech 2 Gate H is complete;
- unrelated sources/speeches.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
