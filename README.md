# kalaignar-assembly-speeches

தமிழகச் சட்டமன்றத்தில் கலைஞர் மு. கருணாநிதி ஆற்றிய உரைகளை, கிடைக்கக்கூடிய அச்சு/scan மூலங்களின் அடிப்படையில், தேதிவாரியாகவும் நிகழ்வுவாரியாகவும் பாதுகாக்கும் digital archive.

This repository is a source-faithful digital archive of M. Karunanidhi's speeches in the Tamil Nadu Legislative Assembly. Each speech is organised primarily by **date and legislative event**, while historical publication titles are preserved as source metadata.

## Archival principles

- **Source first:** Tamil transcription follows the scanned publication; wording and spelling are not silently modernised.
- **Traceability:** source-page transitions are retained in the transcript.
- **Parliamentary context:** printed headings, speaker labels, interjections, figures and exchanges are retained where present in the source.
- **Uncertainty is explicit:** unclear readings should be marked for review rather than guessed.
- **Verification states:** `transcribed` → `reviewed` → `verified`.
- **Translation:** the complete Tamil source transcription comes first; an English translation is included **after** it.
- **Canonical organisation:** folder names use `YYYY-MM-DD-event` so the collection can scale independently of later booklet/publication titles.

Detailed working method: [`docs/ARCHIVAL_WORKFLOW.md`](./docs/ARCHIVAL_WORKFLOW.md)

## Active source handovers

- [`நமது நிலை` — 1971 source package](./sources/1971-namathu-nilai/README.md) — 60-page Government of Tamil Nadu booklet. **Tamil transcription is complete and visually verified against `ACL-CPL_01726_நமது_நிலை.pdf`; 175 scan-supported corrections applied; unresolved readings 0.** Other Assembly/Council PDFs are reference/provenance only and are not transcription sources.
  - Assembly event reference: [`29 March 1971 — Interim-Budget reply`](./sources/1971-namathu-nilai/events/1971-03-29-assembly-interim-budget-reply.md)
  - Assembly event reference: [`2 April 1971 — Governor-address reply`](./sources/1971-namathu-nilai/events/1971-04-02-assembly-governors-address-reply.md)
  - Handover: [`docs/HANDOVER_1971_NAMATHU_NILAI.md`](./docs/HANDOVER_1971_NAMATHU_NILAI.md)
- [`2007 industrial speeches anthology`](./docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md) — 329-page source mapped into 10 dated speeches. **All 10 speeches in the 2007 industrial-speeches anthology are fully released with verified Tamil and verified English.**
- Copy/paste continuation prompt: [`docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`](./docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md)

### `நமது நிலை` indexing note

The two 1971 dated files linked above are **metadata/provenance event references**, not reconstructed verbatim Assembly transcripts. The source booklet is an edited two-House witness. For this archival package, Tamil wording comes only from `ACL-CPL_01726_நமது_நிலை.pdf`; external legislative records are used only to establish House/date/event/provenance context. Accordingly, these reference records are intentionally **not** added to the canonical speech table below or to `data/speeches.json`.

## Speech index

| Date | Publication / speech | Assembly event | Tamil | English | Verification |
|---|---|---|---|---|---|
| 21-03-1963 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 1](./speeches/1963/1963-03-21-industries-debate/) | தொழில்துறை மானியத்தின்மீது உரை | Verified | Verified | Verified against scan pp. 18–26 |
| 09-09-1970 | [உதயக் கதிர்](./speeches/1970/1970-09-09-no-confidence-motion/) | நம்பிக்கையில்லாத் தீர்மான விவாதத்திற்கான பதிலுரை | Verified | Verified | Verified against scan pp. 5–46 |
| 16-04-1981 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 2](./speeches/1981/1981-04-16-industries-debate/) | தொழில் கொள்கைகள், திட்டங்கள் மற்றும் மானியக் கோரிக்கை குறித்த உரை | Verified | Verified | Verified against scan pp. 27–61 |
| 03-05-1989 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 3](./speeches/1989/1989-05-03-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 62–98 |
| 18-04-1990 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 4](./speeches/1990/1990-04-18-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 99–135 |
| 14-08-1996 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 5](./speeches/1996/1996-08-14-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 136–171 |
| 23-04-1997 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 6](./speeches/1997/1997-04-23-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 172–198 |
| 14-05-1998 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 7](./speeches/1998/1998-05-14-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 199–240 |
| 29-04-1999 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 8](./speeches/1999/1999-04-29-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 241–277 |
| 08-05-2000 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 9](./speeches/2000/2000-05-08-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 278–303 |
| 23-08-2006 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 10](./speeches/2006/2006-08-23-industries-debate/) | தொழில்துறை மற்றும் தகவல் தொழில்நுட்பத் துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 304–326 |

Machine-readable index: [`data/speeches.json`](./data/speeches.json)

## Repository structure

```text
kalaignar-assembly-speeches/
├── README.md
├── data/
│   └── speeches.json
├── docs/
│   ├── ARCHIVAL_WORKFLOW.md
│   ├── HANDOVER_1971_NAMATHU_NILAI.md
│   ├── HANDOVER_2007_INDUSTRIAL_SPEECHES.md
│   └── NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md
├── sources/
│   ├── 1971-namathu-nilai/
│   │   ├── README.md
│   │   ├── events/
│   │   ├── transcription/
│   │   └── provenance / audit records
│   └── 2007-industrial-speeches/
│       └── mapping.md
└── speeches/
    ├── 1963/
    │   └── 1963-03-21-industries-debate/
    ├── 1970/
    │   └── 1970-09-09-no-confidence-motion/
    ├── 1981/
    │   └── 1981-04-16-industries-debate/
    ├── 1989/
    │   └── 1989-05-03-industries-debate/
    ├── 1990/
    │   └── 1990-04-18-industries-debate/
    ├── 1996/
    │   └── 1996-08-14-industries-debate/
    ├── 1997/
    │   └── 1997-04-23-industries-debate/
    ├── 1998/
    │   └── 1998-05-14-industries-debate/
    └── 1999/
        └── 1999-04-29-industries-debate/
            ├── README.md
            ├── metadata.json
            ├── source-notes.md
            ├── transcript.md
            ├── translation.md
            ├── translation-review.md
            └── verification-log.md
```

## Current verification convention

A file marked **transcribed** has a complete first-pass transcription from the scan. It is not labelled **verified** until a separate, stricter page-by-page/character-level comparison has been completed. This distinction is intentional: archival completeness and archival certainty are tracked separately.
