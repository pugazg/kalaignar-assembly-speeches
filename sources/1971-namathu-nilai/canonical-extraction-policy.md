# நமது நிலை — archival transcription authority and canonical-use policy

## Decision status

**LOCKED and implemented for this source.**

The controlling textual source for every Tamil textual layer is only:

`ACL-CPL_01726_நமது_நிலை.pdf`

- physical scan pages: **60**
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

The six corrected source-transcription files under `sources/1971-namathu-nilai/transcription/` remain the canonical Tamil textual witness.

Additional Assembly and Legislative Council PDFs are **reference/provenance evidence only**. They are not transcription or translation authorities for this archival work.

## 1. Controlling textual authority

For `நமது நிலை`, Tamil wording, spelling, punctuation, headings, figures, printed English, speaker labels, interventions, page boundaries, repetitions, omissions and editorial ordering come only from the booklet scan.

Completed Tamil audit:

- scan pages reviewed: **1–60 / 60**
- accepted scan-supported corrections: **175**
- unresolved source readings: **0**

Those corrections remain locked unless a future direct recheck of the same booklet scan proves a specific error.

## 2. Permitted use of external legislative records

Assembly/Council records may establish only metadata/provenance such as:

- sitting date and House;
- event/debate context;
- likely source relationship of a booklet span;
- booklet source switches, omissions, rearrangements or selections;
- bibliographic/session information.

Completed provenance ledgers:

- `unit-1-three-way-alignment-ledger.md`
- `unit-2-three-way-alignment-ledger.md`

These are reference maps, not textual authorities.

## 3. Prohibited use of external legislative wording

Do not use Assembly/Council PDFs to:

- fill material omitted by the booklet;
- replace a booklet word, spelling, punctuation or label;
- insert absent interventions or paragraphs;
- rebuild a continuous House speech;
- harmonise witness differences;
- supply English translation wording or resolve a difficult Tamil phrase.

A disagreement between records is a **witness difference**, not permission to change the booklet witness.

## 4. Historical provenance established

The research identified four underlying reply events:

| Editorial unit | House | Date | Reference finding |
|---|---|---|---|
| Unit 1 | Legislative Assembly | 2 Apr 1971 | Governor-address Motion of Thanks reply |
| Unit 1 | Legislative Council | 3 Apr 1971 | Governor-address reply |
| Unit 2 | Legislative Assembly | 29 Mar 1971 | Interim-Budget reply |
| Unit 2 | Legislative Council | 29 Mar 1971 | Interim-Budget reply |

These establish context/provenance only.

## 5. Publication structure remains canonical

The booklet is an edited two-House witness:

- Unit 1: scan pp. **3–37** / printed pp. **1–35**
- Unit 2: scan pp. **38–60** / printed pp. **36–58**

The archival representation preserves these units in their printed order and does not reconstruct separate House transcripts.

## 6. Implemented `speeches/1971/` representation

A booklet-level reader-facing entry has been explicitly implemented at:

`speeches/1971/1971-namathu-nilai/`

This entry is **not** a dated Official Report transcript. It is classified as a `booklet-edited-two-house-compilation` and preserves only booklet-derived Tamil wording.

Because the booklet has no single speech date:

- `date` remains `null`;
- the publication date is recorded separately as source metadata;
- the entry is not added to the canonical dated speech table or `data/speeches.json` as one Assembly event.

Dated source-local event records remain provenance references only.

## 7. Verification semantics

For Tamil, `verified_against_scan` means verified against `ACL-CPL_01726_நமது_நிலை.pdf`.

For English, `verified_against_tamil` means verified against the final verified booklet Tamil only.

Neither status means harmonisation with Assembly/Council Official Reports.

## 8. English translation rule and final state

English must translate only the verified booklet Tamil and preserve the booklet order. It may not import Official Report wording.

Final status:

- Gate F first pass: **58/58 speech pages complete**
- Gate G page review: **58/58 complete, 0 blocking issues**
- consolidated refinement: **34/34 decisions complete**
- final closure: **PASS**
- English: **verified against the verified booklet Tamil**
- external legislative wording imported: **none**

## 9. Locked assets

The following remain authoritative/locked:

- the six source transcription files;
- `correction-application-ledger.md`;
- the **175** accepted visual-fidelity corrections;
- Unit 1 and Unit 2 source boundaries;
- the two completed provenance ledgers;
- the booklet-only authority rule.

The provenance ledgers may evolve if better metadata evidence appears; the booklet text changes only on direct booklet-scan evidence.

## 10. Workflow state

The booklet-derived Tamil/English workflow is **closed**.

Any future Tamil correction requires direct scan evidence. Any future English correction must be derived only from the verified booklet Tamil and immediate booklet context. External legislative PDFs remain provenance/reference only.
