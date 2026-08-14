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

The attached PDF used for Speech-7 work independently matched all three locked byte-level facts above.

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

Speech 6 (`23.04.1997`) completed Gates C–H. Gate-H release commit: `188a79e1b9de76b6bf2bbe037185aef2b6ffe7b1`.

## Active unit — Speech 7

- source label: `உரை : 7`
- printed date: `14.05.1998`
- ISO date: `1998-05-14`
- canonical ID: `1998-05-14-industries-debate`
- locked scan range: **199–240**
- locked printed range: **198–239**
- mapped pages: **42**
- relationship: **scan page = printed page + 1**
- canonical folder: `speeches/1998/1998-05-14-industries-debate/`
- Gate A: complete at anthology level
- Gate B: complete / boundary locked
- Gate C: **in progress — Batches 1 and 2 complete, 30/42 pages**
- Gates D–H: **not started**
- English: **blocked until the complete Tamil passes Gates D and E**

### Boundaries

The controlling scan was directly checked at both Speech-7 boundaries:

- scan p.198 / printed p.197 closes Speech 6 with `நன்றி, வணக்கம். (மேசையைத் தட்டும் ஒலி).` and the decorative ending ornament;
- scan p.199 / printed p.198 begins `உரை : 7`, `நாள் : 14.05.1998`, followed by `மாண்புமிகு கலைஞர் மு. கருணாநிதி :`;
- scan p.240 / printed p.239 closes Speech 7 with the final exchange and decorative ending ornament;
- scan p.241 / printed p.240 begins `உரை : 8`, `நாள் : 29.04.1999`.

No boundary changed.

## Speech 7 — Gate C completed work

### Batch 1

- scan pages: **199–213**
- printed pages: **198–212**
- count: **15 pages**
- post-write Gate-C corrections: 2
- unresolved readings: 0

Batch 1 ended:

`மேலும், எண்ணெய்க் கசடு`

### Batch 2

- scan pages: **214–228**
- printed pages: **213–227**
- count: **15 pages**
- cumulative first-pass pages: **30/42**
- unresolved/`[REVIEW]` readings: **0**
- Tamil status: **in-progress**
- English status: **blocked**

The p.213→214 continuation was preserved, with scan p.214 beginning:

`வருகிறதே, அதிலேயிருந்து மின்சாரம் தயாரிக்கலாம், 250`

Batch 2 covers SIPCOT expansion/progress, investment/export ranking discussion, foreign direct investment, power projects, Hyundai Motor India and a long TIDCO/SIPCOT industrial-project sequence. Printed English/company forms were retained rather than externally corrected.

### Exact continuation point

Scan p.228 / printed p.227 ends:

`இதற்கான ஒப்பந்தம் 7-1-1998 அன்று கையெழுத்தானது.`

Direct inspection of scan p.229 / printed p.228 confirms the next section begins:

`PVC foamed sheets -செயற்கை மரப்பொருள் திட்டம்.`

Therefore the exact next page is **scan p.229 / printed p.228**.

### Speech-7 Batch-2 repository checkpoints

- canonical transcript through p.228: `938679d94990e460d23ba0a72c7488c94f65e839`
- metadata status update: `a74e71a4aa9fd440563e034ed76ad0c69c453c99`
- README Batch-2 update: `b99d6b266aea3e8b4e117207e5e8a6f6b2c420db`
- source-notes Batch-2 update: `eb7135364874cc66c2d41689fa66df8781ffd82c`
- verification-log Batch-2 update: `0926fc9939401eb5eb078604fa6ec8230a6de2f4`

## Exact next activity — Speech 7 Gate C Batch 3

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`, and `sources/2007-industrial-speeches/mapping.md` before writing.
2. Inspect the existing Speech-7 canonical files and continue them; do not create duplicates or rewrite pp.199–228 merely for style.
3. Re-open scan pp.228→229 and confirm the continuation above before appending.
4. Continue Gate C from **scan p.229 / printed p.228**.
5. Transcribe the remaining bounded range **scan pp.229–240 / printed pp.228–239**. Stop at the verified Speech-7 boundary; do not enter scan p.241 / Speech 8.
6. Preserve source-supported wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions and printed English exactly as supported by the scan. Only physical line wrapping may be normalised.
7. Append explicit page markers and record any uncertain readings rather than guessing.
8. When all 42 Speech-7 pages are represented, mark Gate C `transcribed` only after asserting exact page coverage **199–240**, then perform Gate D as a separate completeness/page-marker audit.
9. Do not begin Gate E until Gate D passes.
10. Do not start English until the complete Tamil passes Gates D and E.
11. Do not begin Speech 8.

At the end of Batch 3, refresh this handover and the next-chat prompt with Gate-C completion/Gate-D status and relevant commit SHA(s).

## New-window source requirement

The controlling PDF is not stored in the GitHub repository. In a new chat window, if the PDF is not already available there, the user must attach `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf` before scan-level transcription can continue.

## End-of-handoff state

Speeches 1–6 remain fully released and untouched. Speech 7 is the sole active anthology unit. Gate C Batches 1–2 are complete through **scan p.228 / printed p.227**, covering **30/42 pages**. Resume exactly at **scan p.229 / printed p.228** with `PVC foamed sheets -செயற்கை மரப்பொருள் திட்டம்.`
