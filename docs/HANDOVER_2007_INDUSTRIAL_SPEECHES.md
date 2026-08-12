# Handover — 2007 industrial speeches anthology

## Purpose

This handover is the authoritative continuation point for transcription of:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Repository: `pugazg/kalaignar-assembly-speeches`

The structural mapping phase is complete and locked. Do **not** remap the anthology from scratch unless direct contradictory evidence is found in the primary scan.

## Controlling source

- Publication title: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- Publisher: தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004
- Sales rights: பூம்புகார் பதிப்பகம்
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

The PDF is image/scanned source material. The scan image is authoritative. OCR is only a helper and is never canonical.

An earlier interface exposed only 150 rendered pages; that was a rendering limitation, not the source length. Direct inspection established the full **329-page** PDF.

## Structural mapping status

The entire PDF was visually mapped through p.329. A focused second boundary review was completed at:

`18, 26–27, 61–62, 98–99, 135–136, 171–172, 198–199, 240–241, 277–278, 303–304, 326–327`

All ten mapped speech boundaries were confirmed unchanged.

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

Non-speech material:

- scan pp.1–17 — front matter;
- scan pp.327–328 — `குறிப்புகள்`;
- scan p.329 — closing portrait/back matter.

The `industries-debate` slug is intentionally neutral. It is an archival subject label based on the anthology's subject, not a claim that the printed Assembly event had that formal title.

## Completed canonical work

### Speech 1 — fully released

- Source label: `உரை : 1`
- Printed date: `21.03.1963`
- Canonical ID: `1963-03-21-industries-debate`
- PDF scan pages: **18–26**
- Printed pages: **17–25**
- Folder: `speeches/1963/1963-03-21-industries-debate/`
- Tamil first pass: **complete**
- Tamil completeness audit: **passed**
- Strict Tamil page-by-page visual/source-fidelity verification: **passed**
- Tamil status: **verified**
- Unresolved Tamil readings: **none**
- English translation: **complete from verified Tamil**
- English fidelity verification: **passed**
- English status: **verified**
- Translation/verification commit: `df3a909622b90dcb5b476cd65ee36a50897dac8a`
- Root release index and `data/speeches.json`: **updated after verification**

Speech 1 must not be altered while processing Speech 2 unless a separate task explicitly requests a correction.

## Immediate next speech

### Speech 2

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Full source range: **PDF scan pp.27–61 / printed pp.26–60**
- Target folder: `speeches/1981/1981-04-16-industries-debate/`

Speech 2 is 35 scan pages, so use bounded Tamil first-pass batches rather than attempting to mix it with another speech. Recommended first batch: **scan pp.27–41**. Continue later with **42–56**, then **57–61**, unless scan evidence suggests a safer natural stopping point.

For Speech 2 create/maintain:

```text
speeches/1981/1981-04-16-industries-debate/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
└── verification-log.md
```

During partial transcription, status must remain `in-progress`. Do not call the speech `transcribed` until every mapped page 27–61 is represented and the completeness audit has passed.

## Mandatory workflow

For every speech:

`Tamil first-pass transcription → Tamil completeness audit → strict page-by-page visual/source-fidelity verification → Tamil verified → English translation → English fidelity verification → release/index update`

English translation must remain blocked until the complete Tamil speech has passed the required Tamil verification gate.

Status terms are literal:

- `in-progress` — only part of the mapped speech has been transcribed;
- `transcribed` — complete Tamil first pass exists for all mapped source pages;
- `reviewed` — separate review completed, but strict final scan audit is not necessarily complete;
- `verified` — complete direct page-by-page visual comparison against the controlling scan has been completed and corrections applied.

Never mark `verified` merely because OCR completed, text looks fluent, the full range was typed, or spot checks passed.

## Source-fidelity requirements

- Preserve exact printed wording, period spelling, punctuation where legible, numerals, headings, speaker labels, member interventions and printed English passages.
- Normalise only physical line wrapping.
- Mark every PDF source page explicitly with `<!-- source-page: N -->`.
- Track PDF scan page and printed page separately.
- Do not silently correct printer errors, grammar, political/historical claims or period terminology.
- If a reading cannot be established from the scan, mark it for review rather than guessing.
- Do not infer the speaker's historical office/role from general knowledge when the source does not establish it.
- Decorative ending marks are boundary evidence, not speech text.

## Existing content that must remain untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/` — fully verified/released;
- `speeches/1970/1970-09-09-no-confidence-motion/` — fully verified/released;
- unrelated sources and speeches.

## End-of-session handover requirement

At the end of every transcription session, record:

- canonical speech ID;
- exact PDF scan pages completed;
- exact continuation point;
- whether the speech is partial or complete;
- current Tamil status;
- unresolved readings;
- translation status;
- files changed;
- latest relevant commit SHA;
- exact next action.

## Immediate next action

Begin **Speech 2 / 16.04.1981** from current `main`, with Tamil first-pass transcription of **PDF scan pp.27–41** as the first bounded batch. Do not start English translation and do not modify Speech 1 or the verified 1970 speech.
