# நமது நிலை — source archival release status

## Final source status

Controlling source:

`ACL-CPL_01726_நமது_நிலை.pdf`

This PDF is the **only textual authority** for the archival Tamil transcription and the English translation derived from it.

- physical scan pages: **60**
- publication title: `நமது நிலை`
- imprint: `சென்னை 22-5-1971.`
- issuing body: `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

## Locked source structure

| Source range | Printed range | Unit |
|---|---:|---|
| scan pp.1–2 | — | cover / publication front matter |
| scan pp.3–37 | printed pp.1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| scan pp.38–60 | printed pp.36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

## Tamil transcription

**COMPLETE AND VISUALLY VERIFIED.**

The canonical source witness remains the six segmented files under `transcription/`.

- physical scan traversal: **1–60 / 60**
- printed speech pages traversed: **1–58**
- confirmed scan-supported discrepancies corrected: **175**
- unresolved word/character readings: **0**
- external legislative wording imported: **none**

The six transcription files are frozen unless a direct re-check of the controlling booklet scan proves a specific error.

## Provenance research

The additional Assembly/Council records established four underlying reply events:

| Unit | House | Date | Reference finding |
|---|---|---|---|
| Unit 1 | Legislative Assembly | 2 Apr 1971 | Governor-address Motion of Thanks reply |
| Unit 1 | Legislative Council | 3 Apr 1971 | Governor-address reply |
| Unit 2 | Legislative Assembly | 29 Mar 1971 | Interim-Budget reply |
| Unit 2 | Legislative Council | 29 Mar 1971 | Interim-Budget reply |

Both three-way provenance ledgers are complete:

- `unit-1-three-way-alignment-ledger.md`
- `unit-2-three-way-alignment-ledger.md`

These records are **metadata/reference only**. Their wording did not enter the booklet Tamil or English.

## Reader-facing booklet representation

Implemented at:

`../../speeches/1971/1971-namathu-nilai/`

This is a **booklet-level edited two-House compilation**, not a reconstructed dated Assembly transcript.

- Tamil: **scan pp.3–60, 58/58 speech pages complete**
- English: **scan pp.3–60 complete and verified**
- Unit 1 and Unit 2 preserved in printed order
- source-page markers retained
- publication date retained as source metadata only
- `date: null` retained because the booklet has no single speech date

The entry is intentionally not added to the canonical dated speech table or `data/speeches.json` as one Assembly event.

## English verification

**COMPLETE AND VERIFIED AGAINST THE VERIFIED BOOKLET TAMIL.**

- Gate F: **58/58 pages complete**
- Gate G: **58/58 pages reviewed**
- blocking fidelity issues: **0**
- consolidated refinement: **34/34 decisions complete**
- final closure check: **PASS**
- Official Report wording used: **none**

The final review and closure record is:

`translations/en/TRANSLATION_REVIEW.md`

## Release rule

The released archival object preserves:

- booklet wording and spelling in Tamil;
- booklet punctuation, headings and page boundaries;
- booklet ordering, omissions and editorial selections;
- the two printed editorial units;
- a source-controlled English reading translation verified only against the verified booklet Tamil;
- House/date provenance separately, without reconstruction.

No external legislative text may be added for completeness.

## Final state

**SOURCE PACKAGE AND BOOKLET-DERIVED TAMIL/ENGLISH READER ENTRY RELEASED / CLOSED.**

Future textual changes require direct evidence from the controlling booklet scan for Tamil, or a correction derived only from the verified booklet Tamil for English.
