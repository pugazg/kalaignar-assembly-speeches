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

The same rule controls English: **translate the verified booklet Tamil only**. Do not use Official Report wording as an English source, completion aid or substitute.

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

These conclusions remain metadata only. Do not insert House labels or Official Report text into the verified booklet transcription or translation.

---

## Repository-facing representation

Because the booklet is a mixed two-House editorial witness and external text cannot be imported, **do not create reconstructed `speeches/1971/...` transcripts** for this source.

Locked design:

- preserve the booklet transcription as the canonical textual layer;
- represent dated Assembly context with metadata/provenance records only;
- do not add the dated events to `data/speeches.json` as if complete verbatim Assembly transcripts were archived;
- do not list them in the root canonical speech table as completed speeches.

Relevant files:

- `booklet-derived-representation-design.md`
- `canonical-extraction-policy.md`
- `events/1971-03-29-assembly-interim-budget-reply.md`
- `events/1971-04-02-assembly-governors-address-reply.md`

---

## Reader/source indexing status

Repository discoverability is complete for the source package.

Reader-facing source index:

`sources/1971-namathu-nilai/README.md`

The repository root README exposes the source package and the two dated Assembly reference records while explicitly keeping them outside the canonical speech table and `data/speeches.json`.

---

## English translation status

**Translation planning is complete. Substantive English translation has not started.**

English workspace:

`sources/1971-namathu-nilai/translations/en/`

Created planning/control files:

- `TRANSLATION_PLAN.md`
- `PROGRESS.md`
- `GLOSSARY.md`

### Translation authority

English must translate only the verified Tamil in the six `transcription/scan-*.md` files, which in turn are controlled only by `ACL-CPL_01726_நமது_நிலை.pdf`.

If a Tamil reading becomes doubtful while translating, re-check the controlling booklet scan. **Never resolve it from an Assembly/Council PDF.**

### Planned Gate-F coverage

| Batch | Scan pages | Scope |
|---|---:|---|
| F0 | 1–2 | cover/title + publication introduction/imprint |
| F1 | 3–10 | Unit 1 |
| F2 | 11–18 | Unit 1 |
| F3 | 19–26 | Unit 1 |
| F4 | 27–34 | Unit 1 |
| F5 | 35–37 | Unit 1 close |
| F6 | 38–44 | Unit 2 |
| F7 | 45–51 | Unit 2 |
| F8 | 52–58 | Unit 2 |
| F9 | 59–60 | Unit 2 close / source end |

Current Gate-F coverage: **0 / 60 scan pages**.

Gate G will later re-read the complete English page-by-page against the verified Tamil and will specifically check that no Official Report wording has entered the translation.

### English output design

Gate-F working drafts:

`translations/en/batches/`

After Gate G, consolidate the reviewed English into:

`translations/en/translation.md`

Do not mark English `verified` until the full Gate-G fidelity pass is complete.

---

## Files that must remain untouched

Unless a direct booklet-scan error is proved:

- all six `transcription/scan-*.md` files;
- `correction-application-ledger.md`;
- `transcription-validation.md`;
- all **175** accepted corrections;
- the locked Unit 1 and Unit 2 boundaries;
- both three-way provenance ledgers.

The released 2007 industrial anthology is unrelated and must remain untouched.

---

## Exact continuation point

The booklet-only English translation plan and control scaffolding are complete.

Next substantive activity:

1. Begin **Gate F — F0, scan pp.1–2** only.
2. Translate from the verified Tamil in `transcription/scan-001-010.md`.
3. Lock only the glossary choices required by F0.
4. Save the F0 working translation as `translations/en/batches/f00-scan-001-002.md`.
5. Update `PROGRESS.md` with exact source coverage and commit SHA.
6. Do not start F1 until F0 is durably recorded.

At every future step:

> **Text/translation authority = `ACL-CPL_01726_நமது_நிலை.pdf` via the verified Tamil transcription only. External Assembly/Council PDFs = reference/provenance only.**
