# நமது நிலை — corrected source-level transcription

## Status

This directory contains the **audit-consolidated source-level Tamil transcription** of `ACL-CPL_01726_நமது_நிலை.pdf`.

The user-supplied word-to-word text was used as the first-pass baseline. The rendered 60-page scan is the controlling textual authority. The first full visual-fidelity pass produced **175 confirmed discrepancy entries**, all mapped in `../correction-application-ledger.md` and applied to this transcription set.

This is **not yet a canonical dated/House-specific speech transcript** and must not be marked `verified_against_scan=true` at the speech level. The source says the published material combines responses delivered in both the Legislative Assembly and Legislative Council, but the edition does not provide a secure House/date split for the underlying speeches.

## Files and physical coverage

| File | Scan pages | Printed pages / matter | Editorial unit |
|---|---:|---|---|
| `scan-001-010.md` | 1–10 | cover, front matter, printed 1–8 | front matter + Unit 1 |
| `scan-011-020.md` | 11–20 | printed 9–18 | Unit 1 |
| `scan-021-030.md` | 21–30 | printed 19–28 | Unit 1 |
| `scan-031-040.md` | 31–40 | printed 29–38 | Unit 1 through scan 37; Unit 2 from scan 38 |
| `scan-041-050.md` | 41–50 | printed 39–48 | Unit 2 |
| `scan-051-060.md` | 51–60 | printed 49–58 | Unit 2 + physical ending |

## Locked editorial-unit boundaries

### Unit 1

- scan pages: **3–37**
- printed pages: **1–35**
- editorial description: response to the debate on the motion of thanks for the Governor's address
- scan 37 provides the physical closing boundary

### Unit 2

- scan pages: **38–60**
- printed pages: **36–58**
- printed heading: `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்`
- scan 60 is the physical ending of the publication

Scan pages 1–2 are cover/front matter and are retained as source matter rather than silently discarded.

## Page-marker invariant

The transcription set uses:

```html
<!-- source-page: N -->
```

for the physical scan pages represented in this source-level layer.

The six bounded files partition scan pages **1–60** into non-overlapping ten-page ranges. The intended invariant is therefore one marker for each physical scan page, in monotonic order from 1 through 60. Canonical speech extraction later must retain the relevant speech-text page markers without confusing cover/front matter with speech pages.

## Material deliberately excluded from speech/publication text

The following are not silently promoted into the source transcription:

- Connemara Public Library stamps and accession markings;
- handwriting/later annotations;
- scan artefacts and bleed-through;
- illustration-only wording that the first pass accidentally merged into the speech, including the identified illustration captions/signboards;
- OCR contamination absent from the rendered publication page.

Illustrations remain part of the physical source, but illustration text is not treated as spoken parliamentary text unless the printed layout supports that classification.

## Source fidelity rules applied

The consolidation preserves scan-supported:

- historical spelling and source anomalies;
- word/compound spacing where the visual audit established it;
- punctuation where legible and specifically audited;
- names and initials;
- figures, percentages, money values and year/date forms;
- speaker labels and interventions;
- printed English/transliterated terminology;
- repetitions even when grammatically unusual.

Physical line wrapping may be represented as ordinary Markdown paragraphs, but the text is not modernised or grammatically improved.

## Audit provenance

Detailed before/after evidence is retained in:

- `../visual-fidelity-audit.md` — scan 1–20 / entries 1–30;
- `../visual-fidelity-audit-batch-03.md` — scan 21–30 / entries 31–63;
- `../visual-fidelity-audit-batch-04.md` — scan 31–40 / entries 64–90;
- `../visual-fidelity-audit-batch-05.md` — scan 41–50 / entries 91–141;
- `../visual-fidelity-audit-batch-06.md` — scan 51–60 / entries 142–175;
- `../correction-application-ledger.md` — page-by-page application index for entries 1–175.

## Important status distinction

The original first-pass text is no longer the best source-level working text. These corrected files incorporate the findings of the first full visual audit.

However:

- **source-level first visual pass:** complete;
- **correction application:** complete;
- **canonical dated speech split:** unresolved;
- **canonical Gate D/E:** not yet claimable;
- **English translation:** blocked;
- **Gate H/release:** not applicable yet for this source.

## Next work

Perform the consolidation/transition QA recorded in `../transcription-validation.md`, then address the unresolved House/date split as a separate structural/metadata problem without changing the source-faithful text merely to match outside records.