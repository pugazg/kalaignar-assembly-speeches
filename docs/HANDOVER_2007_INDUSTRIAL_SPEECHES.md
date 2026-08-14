# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English must be translated from and verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Locked map: `sources/2007-industrial-speeches/mapping.md`

## Locked speech inventory

| # | Date | Scan pages | Printed pages | Canonical ID |
|---:|---|---:|---:|---|
| 1 | 21.03.1963 | 18–26 | 17–25 | `1963-03-21-industries-debate` |
| 2 | 16.04.1981 | 27–61 | 26–60 | `1981-04-16-industries-debate` |
| 3 | 03.05.1989 | 62–98 | 61–97 | `1989-05-03-industries-debate` |
| 4 | 18.04.1990 | 99–135 | 98–134 | `1990-04-18-industries-debate` |
| 5 | 14.08.1996 | 136–171 | 135–170 | `1996-08-14-industries-debate` |
| 6 | 23.04.1997 | 172–198 | 171–197 | `1997-04-23-industries-debate` |
| 7 | 14.05.1998 | 199–240 | 198–239 | `1998-05-14-industries-debate` |
| 8 | 29.04.1999 | 241–277 | 240–276 | `1999-04-29-industries-debate` |
| 9 | 8.05.2000 | 278–303 | 277–302 | `2000-05-08-industries-debate` |
| 10 | 23.08.2006 | 304–326 | 303–325 | `2006-08-23-industries-debate` |

## Released anthology state

Speeches **1–6** are fully released with verified Tamil and verified English. Leave them untouched absent a separately justified correction.

Speech 6 (`23.04.1997`) completed Gates C–H:

- Tamil: **verified against scan pp.172–198**, 27/27 pages;
- Gate-E corrections: **6**;
- unresolved Tamil readings: **0**;
- English: **verified against the final verified Tamil**, 27/27 source-page sections;
- Gate-G corrections: **12**;
- unresolved English fidelity issues: **0**;
- canonical `transcript.md`: verified Tamil followed by verified English;
- Gate H: **passed**;
- root `README.md` and `data/speeches.json`: Speech 6 released as Verified / Verified.

Relevant checkpoints:

- Gate-G verified English + canonical merge: `921c196ba069ef90cc29b09e71b9700bfeccf2d6`
- Gate-H canonical release/index update: `188a79e1b9de76b6bf2bbe037185aef2b6ffe7b1`

## Next active unit — Speech 7

- source label: `உரை : 7`
- printed date: `14.05.1998`
- ISO date: `1998-05-14`
- canonical ID: `1998-05-14-industries-debate`
- locked scan range: **199–240**
- locked printed range: **198–239**
- mapped pages: **42**
- relationship: **scan page = printed page + 1**
- previous boundary: scan p.198 closes Speech 6; scan p.199 begins `உரை : 7`, `நாள் : 14.05.1998`
- next boundary: the locked structural map ends Speech 7 at scan p.240; scan p.241 begins Speech 8 dated `29.04.1999`
- canonical folder: `speeches/1998/1998-05-14-industries-debate/`
- folder state at handoff: **not yet created**
- Gate A: complete at anthology level
- Gate B: complete / boundary locked
- Gate C: **not started**
- Gates D–H: **not started**
- English: **blocked until the complete Tamil passes Gates D and E**

## Exact new-chat startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read this handover and `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the controlling scan directly at the Speech-7 boundaries: p.198→199 and p.240→241. The scan, not OCR, is authoritative.
5. Inspect the repository and confirm the Speech-7 folder has not already been started. If work exists, continue it instead of creating duplicates.
6. Create the five standard canonical files under `speeches/1998/1998-05-14-industries-debate/`:
   - `README.md`
   - `metadata.json`
   - `source-notes.md`
   - `transcript.md`
   - `verification-log.md`
7. Begin **Gate C Batch 1** with scan pp.**199–213** / printed pp.**198–212** unless the source structure gives a strong reason to stop earlier.
8. Preserve source-supported wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions and printed English. Only physical line wrapping may be normalised.
9. At the end of the batch, record pages completed, exact continuation words, unresolved readings, next scan page and commit SHA(s).
10. Keep Tamil status `in-progress`. Do not mark `transcribed` or `verified` after a partial batch.
11. Do not start English before Speech 7 passes Gates D and E.
12. Do not begin Speech 8 while Speech 7 is active.

## New-window source requirement

The controlling PDF is not stored in the GitHub repository. In a new chat window, if the PDF is not already available there, the user must attach `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf` before scan-level transcription can begin.

## End-of-handoff state

Speech 6 is fully released. Speech 7 is the sole next active anthology unit and should be started in a **new chat window**.
