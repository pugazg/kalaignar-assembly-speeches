# kalaignar-assembly-speeches

தமிழகச் சட்டமன்றத்தில் கலைஞர் மு. கருணாநிதி ஆற்றிய உரைகளை, கிடைக்கக்கூடிய அச்சு/scan மூலங்களின் அடிப்படையில், தேதிவாரியாகவும் நிகழ்வுவாரியாகவும் பாதுகாக்கும் digital archive.

This repository is a source-faithful digital archive of M. Karunanidhi's speeches in the Tamil Nadu Legislative Assembly. Each ordinary canonical speech is organised primarily by **date and legislative event**, while historical publication titles and special mixed-source publications are preserved with explicit source metadata.

## Archival principles

- **Source first:** Tamil transcription follows the scanned publication; wording and spelling are not silently modernised.
- **Traceability:** source-page transitions are retained in the transcript.
- **Parliamentary context:** printed headings, speaker labels, interjections, figures and exchanges are retained where present in the source.
- **Uncertainty is explicit:** unclear readings should be marked for review rather than guessed.
- **Verification states:** `transcribed` → `reviewed` → `verified`.
- **Translation:** the complete verified Tamil source controls the English translation.
- **Canonical organisation:** dated canonical speech folders normally use `YYYY-MM-DD-event`; exceptional edited compilations are identified explicitly rather than assigned a false single speech date.

Detailed working method: [`docs/ARCHIVAL_WORKFLOW.md`](./docs/ARCHIVAL_WORKFLOW.md)

## Source handovers / special packages

- [`நமது நிலை` — 1971 source package](./sources/1971-namathu-nilai/README.md) — 60-page Government of Tamil Nadu booklet. **Tamil transcription is complete and visually verified against `ACL-CPL_01726_நமது_நிலை.pdf`; 175 scan-supported corrections; unresolved readings 0. The booklet-level reader entry now has complete Tamil and English, with English verified after 58/58-page Gate-G review, 34/34 refinement decisions and final closure PASS.** Other Assembly/Council PDFs remain reference/provenance only.
  - Reader-facing booklet entry: [`speeches/1971/1971-namathu-nilai/`](./speeches/1971/1971-namathu-nilai/)
  - Assembly event reference: [`29 March 1971 — Interim-Budget reply`](./sources/1971-namathu-nilai/events/1971-03-29-assembly-interim-budget-reply.md)
  - Assembly event reference: [`2 April 1971 — Governor-address reply`](./sources/1971-namathu-nilai/events/1971-04-02-assembly-governors-address-reply.md)
  - Handover: [`docs/HANDOVER_1971_NAMATHU_NILAI.md`](./docs/HANDOVER_1971_NAMATHU_NILAI.md)
- [`நமது விளக்கம்` — 1971 source package](./sources/1971-namathu-vilakkam/README.md) — 61-scan Government of Tamil Nadu booklet. **COMPLETE / CLOSED: Gate A–H PASS / COMPLETE. Tamil is VERIFIED 57/57; English is VERIFIED AGAINST TAMIL 57/57 after 42 cumulative Gate-G refinements and 0 blocking issues. Gate H confirmed scan 60 as the speech terminus, scan 61 as non-speech, preserved the edited two-House indexing policy, and RELEASED / CLOSED the booklet entry.**
  - Reader-facing booklet entry: [`speeches/1971/1971-namathu-vilakkam/`](./speeches/1971/1971-namathu-vilakkam/)
  - Event reference: [`29 June 1971 — Assembly budget reply`](./sources/1971-namathu-vilakkam/events/1971-06-29-assembly-budget-reply.md)
  - Event reference: [`30 June 1971 — Council budget reply`](./sources/1971-namathu-vilakkam/events/1971-06-30-council-budget-reply.md)
  - Handover: [`docs/HANDOVER_1971_NAMATHU_VILAKKAM.md`](./docs/HANDOVER_1971_NAMATHU_VILAKKAM.md)
- [`இருளும் ஒளியும்` — 1973 source package](./sources/1973-irulum-oliyum/mapping.md) — 64-scan Government of Tamil Nadu publication containing the 7-3-1973 Assembly reply and 8-3-1973 Legislative Council reply. **COMPLETE / CLOSED: both units have verified Tamil, verified English, canonical bilingual transcripts, synchronized indexes and Gate-H RELEASED status. Unit 1 remains RELEASED / REVALIDATED AFTER CROP RECOVERY; Unit 2 is RELEASED after Gate H.**
  - Released Unit 1: [`7-3-1973 — சட்டப் பேரவையில்`](./speeches/1973/1973-03-07-financial-statement-reply/)
  - Released Unit 2: [`8-3-1973 — சட்டமன்ற மேலவையில்`](./speeches/1973/1973-03-08-financial-statement-reply/)
  - Handover: [`docs/HANDOVER_1973_IRULUM_OLIYUM.md`](./docs/HANDOVER_1973_IRULUM_OLIYUM.md)
- [`2007 industrial speeches anthology`](./docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md) — 329-page source mapped into 10 dated speeches. **All 10 speeches are fully released with verified Tamil and verified English.**
- [`நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)` — 2007 source package](./sources/2007-financial-statement-speeches-part-1/README.md) — **546-scan anthology; Gate A + Gate B COMPLETE / LOCKED; 19 speech units mapped. Speeches 1–17 are RELEASED / CLOSED through Gate H with verified Tamil and verified English.** Speech 12 / 07.03.1973 is a separately released independent parallel witness at [`1973-03-07-financial-statement-debate`](./speeches/1973/1973-03-07-financial-statement-debate/): **Gate H PASS / COMPLETE; canonical bilingual transcript COMPLETE; 0 Tamil / 0 English Gate-H wording changes**. The separately released `1973-03-07-financial-statement-reply` remains unchanged. To avoid a second canonical same-date record, the dated speech table and `data/speeches.json` intentionally retain only the existing reply entry; the anthology witness remains discoverable through the source package and repository status sections. Speech 13 / 14.03.1974 and Speech 14 / 10.03.1975 are RELEASED / CLOSED through Gate H. Speech 15 / 03.08.1977 is RELEASED / CLOSED through Gate H: Tamil VERIFIED 36/36, English VERIFIED AGAINST TAMIL 36/36 after 6 Gate-G refinements, canonical bilingual transcript complete, Gate-H wording changes 0 Tamil / 0 English, and indexes synchronized. Speech 16 / 1.3.1978 is RELEASED / CLOSED through Gate H: Tamil VERIFIED 33/33, English VERIFIED AGAINST TAMIL 33/33 after 9 Gate-G refinements, canonical bilingual transcript complete, Gate-H wording changes 0 Tamil / 0 English, and indexes synchronized. Speech 17 / 22 & 23.3.1979 is RELEASED / CLOSED through Gate H as one source-preserved multi-date unit: boundaries 388→389 and 481→482 PASS; no explicit internal date divider is printed, so no single canonical date or page-level date split is assigned. Tamil is VERIFIED 93/93 after 37 Gate-E corrections with 0 unresolved; English is VERIFIED AGAINST TAMIL 93/93 after 43 Gate-G refinements with 0 blockers; Gate-H wording changes are 0 Tamil / 0 English; the canonical bilingual transcript is complete and `translation.md` is the released pointer. Because there is no single canonical date, the root dated speech table and `data/speeches.json` remain unchanged intentionally. Speech 18 / 09.07.1980 Gate C is IN PROGRESS: Batches 1–2 scans 482–501 / 20 pages are COMPLETE, cumulative 20/29 first-pass; Tamil is PARTIALLY TRANSCRIBED / NOT VERIFIED / verified_against_scan=false. Exact next: Speech 18 Gate C Batch 3 FINAL — scans 502–510 / exactly 9 pages.
  - Handover: [`docs/HANDOVER_2007_FINANCIAL_STATEMENT_SPEECHES_PART_1.md`](./docs/HANDOVER_2007_FINANCIAL_STATEMENT_SPEECHES_PART_1.md)
  - Continuation prompt: [`docs/NEXT_CHAT_PROMPT_2007_FINANCIAL_STATEMENT_SPEECHES_PART_1.md`](./docs/NEXT_CHAT_PROMPT_2007_FINANCIAL_STATEMENT_SPEECHES_PART_1.md)
- Copy/paste continuation prompt: [`docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`](./docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md)

### 1971 edited-booklet indexing note

Both `நமது நிலை` and `நமது விளக்கம்` are **edited two-House booklet witnesses** and do not have one safe canonical speech date. Their reader-facing folders preserve each booklet itself with `date: null`; dated event files remain metadata/provenance references.

Accordingly, neither booklet-level entry is added to the canonical dated speech table below or to `data/speeches.json` as though it were one complete Assembly transcript. Each booklet's Tamil wording remains controlled only by its own scan; external legislative records may establish House/date/event provenance but must not silently replace booklet text.

### 1973 same-date parallel-witness indexing note

The released 2007-anthology Speech 12 at `speeches/1973/1973-03-07-financial-statement-debate/` is an independent source witness to the separately released `1973-03-07-financial-statement-reply/`.

Both records remain preserved and released, but the canonical dated speech table and `data/speeches.json` retain only the existing reply record for **07-03-1973**. This avoids creating a second canonical same-date index entry while keeping the anthology witness discoverable through the source-package and repository-status links above.

## Speech index

| Date | Publication / speech | Assembly event | Tamil | English | Verification |
|---|---|---|---|---|---|
| 05-03-1958 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 1](./speeches/1958/1958-03-05-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 18–24 |
| 04-03-1959 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 2](./speeches/1959/1959-03-04-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 25–33 |
| 16-03-1960 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 3](./speeches/1960/1960-03-16-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 34–42 |
| 06-03-1961 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 4](./speeches/1961/1961-03-06-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 43–48 |
| 02-07-1962 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 5](./speeches/1962/1962-07-02-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 49–59 |
| 07-03-1963 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 6](./speeches/1963/1963-03-07-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 60–75 |
| 07-03-1964 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 7](./speeches/1964/1964-03-07-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 76–89 |
| 04-03-1966 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 8](./speeches/1966/1966-03-04-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 90–112 |
| 29-03-1971 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 9](./speeches/1971/1971-03-29-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 113–116; independent parallel witness |
| 29-06-1971 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 10](./speeches/1971/1971-06-29-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 117–151; independent parallel witness |
| 10-03-1972 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 11](./speeches/1972/1972-03-10-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 152–190 |
| 21-03-1963 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 1](./speeches/1963/1963-03-21-industries-debate/) | தொழில்துறை மானியத்தின்மீது உரை | Verified | Verified | Verified against scan pp. 18–26 |
| 09-09-1970 | [உதயக் கதிர்](./speeches/1970/1970-09-09-no-confidence-motion/) | நம்பிக்கையில்லாத் தீர்மான விவாதத்திற்கான பதிலுரை | Verified | Verified | Verified against scan pp. 5–46 |
| 07-03-1973 | [இருளும் ஒளியும் — சட்டப் பேரவையில்](./speeches/1973/1973-03-07-financial-statement-reply/) | நிதிநிலை அறிக்கை விவாதத்திற்கான பதிலுரை | Verified | Verified | Gate H revalidated after TNLA-assisted gutter recovery; RELEASED |
| 08-03-1973 | [இருளும் ஒளியும் — சட்டமன்ற மேலவையில்](./speeches/1973/1973-03-08-financial-statement-reply/) | நிதிநிலை அறிக்கை விவாதத்திற்கான பதிலுரை | Verified | Verified | Gate H PASS; RELEASED |
| 14-03-1974 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 13](./speeches/1974/1974-03-14-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 231–262 |
| 10-03-1975 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 14](./speeches/1975/1975-03-10-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 263–319 |
| 03-08-1977 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 15](./speeches/1977/1977-08-03-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 320–355 |
| 01-03-1978 | [நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — உரை : 16](./speeches/1978/1978-03-01-financial-statement-debate/) | நிதிநிலை அறிக்கை மீது உரை | Verified | Verified | Gate H PASS; RELEASED — source scans 356–388 |
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
│   ├── HANDOVER_1971_NAMATHU_VILAKKAM.md
│   ├── HANDOVER_2007_INDUSTRIAL_SPEECHES.md
│   └── NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md
├── sources/
│   ├── 1971-namathu-nilai/
│   │   ├── README.md
│   │   ├── events/
│   │   ├── transcription/
│   │   ├── translations/en/
│   │   └── provenance / audit records
│   ├── 1971-namathu-vilakkam/
│   │   ├── README.md
│   │   ├── mapping.md
│   │   └── events/
│   ├── 1973-irulum-oliyum/
│   │   └── mapping.md
│   └── 2007-industrial-speeches/
│       └── mapping.md
└── speeches/
    ├── 1958/
    ├── 1959/
    ├── 1960/
    ├── 1961/
    ├── 1962/
    ├── 1963/
    ├── 1970/
    ├── 1971/
    │   ├── 1971-namathu-nilai/
    │   └── 1971-namathu-vilakkam/
    ├── 1973/
    │   ├── 1973-03-07-financial-statement-debate/   # released 2007 anthology parallel witness; intentionally not duplicated in dated index
    │   ├── 1973-03-07-financial-statement-reply/
    │   └── 1973-03-08-financial-statement-reply/
    ├── 1977/
    │   └── 1977-08-03-financial-statement-debate/
    ├── 1980/
    │   └── 1980-07-09-financial-statement-debate/   # Speech 18 active; Gate C Batches 1–2 complete / 20 of 29
    ├── 1981/
    ├── 1989/
    ├── 1990/
    ├── 1996/
    ├── 1997/
    ├── 1998/
    ├── 1999/
    ├── 2000/
    └── 2006/
```

## Current verification convention

A file marked **transcribed** has a complete first-pass transcription from the scan. It is not labelled **verified** until a separate stricter comparison has been completed. For source-derived English, `verified` means reviewed against the verified Tamil controlled by the same source, unless a source-specific note states otherwise.
