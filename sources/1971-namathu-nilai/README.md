# நமது நிலை — 1971 source package

This directory preserves the archival source package for the 1971 Government of Tamil Nadu booklet **`நமது நிலை`**.

## Controlling textual source

`ACL-CPL_01726_நமது_நிலை.pdf`

This PDF is the **only textual authority** for the Tamil transcription in this package.

Other Assembly and Legislative Council PDFs are used **only for reference and provenance** — for example, to establish House, date, event context and editorial-source relationships. Their wording must not be copied into, merged with, or used to repair the booklet transcription.

## Source identity

- publication title: `நமது நிலை`
- imprint statement: `சென்னை 22-5-1971.`
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

Status: **complete and visually verified against `ACL-CPL_01726_நமது_நிலை.pdf`**.

The complete source transcription is segmented only for repository manageability:

- [`transcription/scan-001-010.md`](./transcription/scan-001-010.md)
- [`transcription/scan-011-020.md`](./transcription/scan-011-020.md)
- [`transcription/scan-021-030.md`](./transcription/scan-021-030.md)
- [`transcription/scan-031-040.md`](./transcription/scan-031-040.md)
- [`transcription/scan-041-050.md`](./transcription/scan-041-050.md)
- [`transcription/scan-051-060.md`](./transcription/scan-051-060.md)

Audit result:

- scan traversal: **1–60 / 60**
- confirmed visual-fidelity corrections applied: **175**
- unresolved word/character readings: **0**
- external legislative text imported into transcription: **none**

See:

- [`correction-application-ledger.md`](./correction-application-ledger.md)
- [`transcription-validation.md`](./transcription-validation.md)
- [`source-archival-release-status.md`](./source-archival-release-status.md)

## Dated Assembly event reference records

The booklet is an edited two-House publication witness rather than a continuous verbatim transcript of either House. To make the Assembly context discoverable without manufacturing a reconstructed speech, this package uses metadata/provenance event records:

- [`29 March 1971 — Assembly Interim-Budget reply`](./events/1971-03-29-assembly-interim-budget-reply.md)
- [`2 April 1971 — Assembly Governor-address reply`](./events/1971-04-02-assembly-governors-address-reply.md)

These files contain **no substitute transcription from the Official Reports**. They point back to the verified booklet transcription for Tamil wording.

## Provenance research

External legislative records were used to establish four underlying historical events:

| Unit | House | Date | Reference context |
|---|---|---|---|
| Unit 1 | Legislative Assembly | **2 Apr 1971** | Governor-address Motion of Thanks reply |
| Unit 1 | Legislative Council | **3 Apr 1971** | Governor-address reply |
| Unit 2 | Legislative Assembly | **29 Mar 1971** | Interim-Budget reply |
| Unit 2 | Legislative Council | **29 Mar 1971** | Interim-Budget reply |

The completed span-level provenance maps are:

- [`unit-1-three-way-alignment-ledger.md`](./unit-1-three-way-alignment-ledger.md)
- [`unit-2-three-way-alignment-ledger.md`](./unit-2-three-way-alignment-ledger.md)

They describe provenance only. They do not authorize changes to the source text.

## Representation policy

Do **not** create reconstructed `speeches/1971/.../transcript.md` files from the other legislative PDFs for this source.

The repository-facing design is documented in:

- [`booklet-derived-representation-design.md`](./booklet-derived-representation-design.md)
- [`canonical-extraction-policy.md`](./canonical-extraction-policy.md)

The canonical textual record for this source remains the booklet transcription exactly as verified from `ACL-CPL_01726_நமது_நிலை.pdf`.

## English status

**Not started.**

Any future English translation must translate the verified booklet Tamil in the booklet's printed editorial order. External Assembly/Council wording must not be imported.

## Handover

Project continuation state is recorded in:

[`../../docs/HANDOVER_1971_NAMATHU_NILAI.md`](../../docs/HANDOVER_1971_NAMATHU_NILAI.md)
