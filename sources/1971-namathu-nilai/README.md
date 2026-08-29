# நமது நிலை — 1971 source package

This directory preserves the archival source package for the 1971 Government of Tamil Nadu booklet **`நமது நிலை`**.

## Controlling textual source

`ACL-CPL_01726_நமது_நிலை.pdf`

This PDF is the **only textual authority** for the Tamil transcription and the English translation derived from it.

Other Assembly and Legislative Council PDFs are **reference/provenance only**. Their wording was not copied into, merged with, or used to repair the booklet transcription or translation.

## Reader-facing speech entry

The complete booklet speech text and verified English translation are maintained under:

[`../../speeches/1971/1971-namathu-nilai/`](../../speeches/1971/1971-namathu-nilai/)

Final state:

- Tamil reader-facing range: **scan pp.3–60 — complete, 58/58 speech pages**
- English Gate F: **58/58 complete**
- English Gate G: **58/58 reviewed, 0 blocking issues**
- consolidated refinement: **34/34 decisions complete**
- final closure: **PASS**
- English: **VERIFIED against the verified booklet Tamil**
- external legislative wording imported: **none**

The entry preserves the booklet as an edited two-House compilation and does not reconstruct separate Assembly/Council transcripts. Scan pp.1–2 remain publication front matter/source metadata and are not inserted into the speech transcript as spoken text.

## Source identity

- publication title: `நமது நிலை`
- imprint: `சென்னை 22-5-1971.`
- issuing body: `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- physical scan pages: **60**
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

## Locked source structure

| Scan pages | Printed pages | Content |
|---:|---:|---|
| 1–2 | — | cover / publication front matter |
| 3–37 | 1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| 38–60 | 36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

## Verified Tamil transcription

Status: **complete and visually verified against the controlling booklet scan**.

- [`transcription/scan-001-010.md`](./transcription/scan-001-010.md)
- [`transcription/scan-011-020.md`](./transcription/scan-011-020.md)
- [`transcription/scan-021-030.md`](./transcription/scan-021-030.md)
- [`transcription/scan-031-040.md`](./transcription/scan-031-040.md)
- [`transcription/scan-041-050.md`](./transcription/scan-041-050.md)
- [`transcription/scan-051-060.md`](./transcription/scan-051-060.md)

Audit result:

- scan traversal: **1–60 / 60**
- confirmed visual-fidelity corrections: **175**
- unresolved word/character readings: **0**
- external legislative text imported: **none**

Supporting records:

- [`correction-application-ledger.md`](./correction-application-ledger.md)
- [`transcription-validation.md`](./transcription-validation.md)
- [`source-archival-release-status.md`](./source-archival-release-status.md)

## Provenance research

Completed maps:

- [`unit-1-three-way-alignment-ledger.md`](./unit-1-three-way-alignment-ledger.md)
- [`unit-2-three-way-alignment-ledger.md`](./unit-2-three-way-alignment-ledger.md)

They explain House/date provenance without changing source text. Dated Assembly reference records remain metadata/provenance only and are intentionally not promoted into complete canonical dated transcripts.

## Translation records

- [`translations/en/TRANSLATION_PLAN.md`](./translations/en/TRANSLATION_PLAN.md)
- [`translations/en/PROGRESS.md`](./translations/en/PROGRESS.md)
- [`translations/en/GLOSSARY.md`](./translations/en/GLOSSARY.md)
- [`translations/en/TRANSLATION_REVIEW.md`](./translations/en/TRANSLATION_REVIEW.md)

Actual reader-facing English is maintained only in the `speeches/` entry.

The final translation review records **58/58 pages reviewed, 0 blocking fidelity issues, 34/34 refinement decisions completed, final closure PASS, and English verified against the verified booklet Tamil**.

## Indexing rule

The booklet's publication date is not treated as a single speech date. The booklet-level entry therefore remains outside the canonical dated speech table and `data/speeches.json`; the dated event records remain provenance references.

## Handover

[`../../docs/HANDOVER_1971_NAMATHU_NILAI.md`](../../docs/HANDOVER_1971_NAMATHU_NILAI.md)

## Workflow state

**Closed.** Future textual changes must remain controlled by the booklet scan / verified booklet Tamil, never by external Official Report wording.
