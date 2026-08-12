# Handover — 2007 industrial speeches anthology

## Purpose

This handover is the authoritative starting point for the **transcription phase** of the source:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Repository: `pugazg/kalaignar-assembly-speeches`

The structural mapping phase is complete. The next chat/session should **not remap the book from scratch** unless it finds contradictory primary-source evidence. It should begin Tamil transcription using the locked map below.

## Controlling source

- Publication title: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- Publisher: தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004
- Sales rights: பூம்புகார் பதிப்பகம்
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

The PDF is image/scanned source material. The scan image is authoritative. OCR must not be treated as canonical text.

## Important corrected history

An early file-reading interface exposed only 150 rendered pages, which temporarily led to the incorrect conclusion that Speech 5 was incomplete. Direct inspection of the original PDF established that the file has **329 pages** and Speech 5 continues normally. That temporary conclusion is fully superseded.

## Structural mapping status

The entire PDF was visually mapped in bounded batches through p.329. A second focused visual boundary review was then performed at:

`18, 26–27, 61–62, 98–99, 135–136, 171–172, 198–199, 240–241, 277–278, 303–304, 326–327`

All mapped boundaries were confirmed unchanged.

Locked source map: [`../sources/2007-industrial-speeches/mapping.md`](../sources/2007-industrial-speeches/mapping.md)

Repository workflow: [`ARCHIVAL_WORKFLOW.md`](ARCHIVAL_WORKFLOW.md)

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

Non-speech material:

- scan pp.1–17 — front matter;
- scan pp.327–328 — `குறிப்புகள்`;
- scan p.329 — closing portrait/back matter.

The `industries-debate` slug is intentionally neutral. It is an archival subject label based on the anthology's subject, not a claim that the printed Assembly event had that formal title.

## Current transcription state

**No Tamil transcription from this anthology has been started in the canonical speech folders yet.**

The next unit of work is:

- Speech: `உரை : 1`
- Printed date: `21.03.1963`
- Canonical ID: `1963-03-21-industries-debate`
- Source range: **PDF scan pp.18–26 / printed pp.17–25**
- Target folder: `speeches/1963/1963-03-21-industries-debate/`

Because Speech 1 is only nine scan pages, transcribe the **entire speech as one bounded first-pass unit**, then run its completeness audit. Do not start Speech 2 in the same batch merely to increase batch size.

## What the next session should create for Speech 1

Follow the existing 1970 entry as structural precedent and create:

```text
speeches/1963/1963-03-21-industries-debate/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
└── verification-log.md
```

During first-pass transcription:

- `metadata.json` transcription status must not be `verified`;
- translation status must remain blocked/not started;
- page boundaries must use `<!-- source-page: N -->`;
- preserve exact source wording, spelling, punctuation, numerals and speaker/intervention labels as far as the scan permits;
- normalise physical line wrapping only;
- mark unreadable material explicitly rather than guessing.

## Required order of work for each speech

`Tamil first-pass transcription → Tamil completeness audit → stricter visual/source-fidelity review → Tamil verified → English translation → English fidelity review → release/index update`

**English translation must not begin before the Tamil audit gates are complete.**

## Verification language

Use status terms literally:

- `transcribed` = complete first pass;
- `reviewed` = separate review completed, but final strict scan audit not necessarily complete;
- `verified` = direct page-by-page visual source-fidelity comparison completed and corrections applied.

Do not claim `verified` after OCR, spot checks or fluent-looking text.

## Source-specific cautions

1. Track **PDF scan page** separately from **printed page**. From the speech section onward, the common relationship is scan page = printed page + 1, but use the locked map rather than blindly deriving ranges.
2. Preserve the source's exact date formatting in source metadata (`8.05.2000` is printed without a leading zero) while using ISO dates for canonical IDs.
3. Member interventions are part of the speech sequence and must remain in the transcript.
4. English phrases/quotations printed inside the Tamil source must be transcribed as printed; they are not the later English translation layer.
5. Decorative ending marks are boundary evidence, not text to invent into the speech body.
6. Do not infer historical office/role when the page only supplies a speaker label. Enrich roles only from source-supported or separately verified evidence.

## Existing repository content that must remain untouched

The verified 1970 speech `speeches/1970/1970-09-09-no-confidence-motion/` is already complete, including verified Tamil and English. Processing this anthology must not alter that speech unless a separate task explicitly requests it.

## Indexing policy during this phase

Do not add a speech to the root release index merely because its folder has been opened. Add/update index data when the speech has reached the repository's defined release point and statuses accurately represent the work actually completed.

## End-of-session handover requirement

At the end of every future transcription session, record:

- canonical speech ID;
- exact PDF scan pages completed;
- exact continuation point;
- whether the speech is partial/complete;
- current Tamil status;
- unresolved readings;
- translation status;
- files changed;
- latest relevant commit SHA.

This avoids re-reading completed source pages or accidentally promoting incomplete work.

## Immediate next action

Begin **Speech 1 / 21.03.1963**, scan pp.18–26, as a complete Tamil first-pass transcription. After that, perform the Tamil completeness audit but keep English translation blocked until the later strict source-fidelity gate is completed.
