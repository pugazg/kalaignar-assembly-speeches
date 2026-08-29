# Handover — 1971 `நமது நிலை`

## Repository

`pugazg/kalaignar-assembly-speeches`

Branch: `main`

Active source package:

`sources/1971-namathu-nilai/`

## Non-negotiable textual-authority rule

The **only transcription authority** for this archival source is:

`ACL-CPL_01726_நமது_நிலை.pdf`

Do not transcribe from, complete from, repair from, normalize toward, or merge wording from any Tamil Nadu Legislative Assembly or Legislative Council PDF.

Those additional legislative PDFs are **reference/provenance sources only**. They may establish House, date, event context, sitting chronology and provenance alignment, but their words must not enter the Tamil archival transcription.

The same rule applies to future English work: translate the verified booklet Tamil, not Official Report wording.

---

## Source identity

- printed title: `நமது நிலை`
- cover attribution: `தமிழக முதல்வர் கலைஞர் மு.கருணாநிதி`
- imprint: `சென்னை 22-5-1971.`
- issuing body: `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- physical PDF pages: **60**
- file size: **21,613,923 bytes**
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

## Locked physical/source structure

| Scan pages | Printed pages | Classification |
|---:|---:|---|
| 1–2 | — | cover / publication front matter |
| 3–37 | 1–35 | Editorial Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| 38–60 | 36–58 | Editorial Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

No missing, duplicated or blank source pages were found in the controlling scan.

---

## Tamil transcription status

**COMPLETE AND VISUALLY VERIFIED AGAINST THE CONTROLLING BOOKLET SCAN.**

Canonical source transcription files:

- `sources/1971-namathu-nilai/transcription/scan-001-010.md`
- `sources/1971-namathu-nilai/transcription/scan-011-020.md`
- `sources/1971-namathu-nilai/transcription/scan-021-030.md`
- `sources/1971-namathu-nilai/transcription/scan-031-040.md`
- `sources/1971-namathu-nilai/transcription/scan-041-050.md`
- `sources/1971-namathu-nilai/transcription/scan-051-060.md`

Locked audit outcome:

- scan pages visually traversed: **1–60 / 60**
- confirmed first-pass discrepancies corrected: **175**
- unresolved source word/character readings: **0**
- external legislative wording imported: **none**

Supporting files:

- `correction-application-ledger.md`
- `transcription-validation.md`
- `source-archival-release-status.md`

Do not alter these verified files unless a new correction is supported directly by the controlling `ACL-CPL_01726_நமது_நிலை.pdf` scan.

---

## Historical/provenance research status

Direct legislative reference research established all four underlying reply events:

| Editorial unit | House | Date | Reference span/context |
|---|---|---|---|
| Unit 1 | Tamil Nadu Legislative Assembly | **2 Apr 1971** | Governor-address Motion of Thanks reply, Official Report pp.314–336 |
| Unit 1 | Tamil Nadu Legislative Council | **3 Apr 1971** | Governor-address reply, pp.434–454; clarifications through p.456 |
| Unit 2 | Tamil Nadu Legislative Assembly | **29 Mar 1971** | Interim-Budget reply, pp.298–313 |
| Unit 2 | Tamil Nadu Legislative Council | **29 Mar 1971** | Budget reply, pp.200–207 |

These page ranges are **reference metadata only** in this archival workflow.

Completed provenance ledgers:

- `unit-1-three-way-alignment-ledger.md`
- `unit-2-three-way-alignment-ledger.md`

### Unit 1 provenance conclusion

The booklet principally follows the 2 April Assembly reply and then changes to selected 3 April Council prohibition material late in the unit. The booklet also performs omission/selection inside the Council-derived ending.

### Unit 2 provenance conclusion

The booklet interleaves material associated with the 29 March Assembly and Council replies multiple times. There is no single defensible Assembly→Council splice.

These conclusions must remain metadata. Do not insert House labels or Official Report text into the verified booklet transcription.

---

## Repository-facing representation

Because the booklet is a mixed two-House editorial witness and external text cannot be imported, **do not create reconstructed `speeches/1971/...` transcripts** for this source.

Design decision:

- preserve the booklet transcription as the canonical textual layer;
- represent dated Assembly context with metadata/provenance records only;
- do not add the dated events to `data/speeches.json` as if complete verbatim Assembly transcripts were archived;
- do not list them in the root speech table as completed canonical speeches.

Relevant policy files:

- `booklet-derived-representation-design.md`
- `canonical-extraction-policy.md`

Source-local Assembly event reference records already created:

- `events/1971-03-29-assembly-interim-budget-reply.md`
- `events/1971-04-02-assembly-governors-address-reply.md`

Both records point back to the booklet transcription and contain no replacement Tamil text from Official Reports.

---

## Reader/source index

Repository discoverability is now **complete** for this stage.

The source package has a reader-facing index:

`sources/1971-namathu-nilai/README.md`

It links the verified transcription, correction/audit records, event references, provenance ledgers, representation policy and this handover.

The repository root `README.md` now exposes `நமது நிலை` under the active source handovers section, links both dated Assembly reference records and explicitly states that they are metadata/provenance records rather than complete canonical Assembly transcripts.

The two event references remain intentionally absent from the canonical speech table and `data/speeches.json`.

---

## English status

**Not started.**

Tamil source verification is complete, so English is now technically eligible under the normal workflow, but the following source-specific rule controls:

- translate only the verified booklet Tamil;
- preserve the booklet's printed editorial order and headings;
- do not split or reconstruct English into separate Assembly/Council speeches;
- do not import wording from any Official Report;
- keep provenance notes separate from translated source text.

---

## Files that must remain untouched

Unless a direct booklet-scan error is proved:

- all six `transcription/scan-*.md` files;
- `correction-application-ledger.md`;
- `transcription-validation.md`;
- all **175** accepted corrections;
- the locked Unit 1 and Unit 2 boundaries;
- both three-way provenance ledgers.

The released 2007 industrial anthology is unrelated and must remain untouched as well.

---

## Exact continuation point

The indexing/handover activity is complete.

Next substantive source activity:

1. Prepare a **booklet-only English translation plan** for `நமது நிலை` before translating any text.
2. The translation plan must use only the verified Tamil in the six `transcription/scan-*.md` files as source text.
3. Preserve the booklet's two editorial units and printed order; do not reconstruct separate Assembly/Council speeches.
4. External Assembly/Council PDFs may remain available only for provenance notes and must not supply English wording.
5. Do not change the verified Tamil while planning or translating unless a direct error is independently proved against `ACL-CPL_01726_நமது_நிலை.pdf`.

At every future step, remember: **Tamil transcription authority = `ACL-CPL_01726_நமது_நிலை.pdf` only.**
