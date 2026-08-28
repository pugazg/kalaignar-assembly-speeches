# Source mapping — நமது நிலை

## Gate A — source preflight

Status: **complete for the supplied scan**.

### Controlling source identity

- **Scan filename:** `ACL-CPL_01726_நமது_நிலை.pdf`
- **Actual PDF pages:** **60**
- **File size:** **21,613,923 bytes**
- **SHA-256:** `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`
- **Controlling authority:** rendered scan pages. OCR/extracted text is navigation assistance only.

### Publication evidence visible in the scan

- **Printed title:** `நமது நிலை`
- **Cover attribution:** `தமிழக முதல்வர் கலைஞர் மு.கருணாநிதி`
- **Imprint/date statement in front matter:** `சென்னை 22-5-1971.`
- **Issuing body printed in front matter:** `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- No separate edition-number statement or printer statement has been located in this 60-page scan.

The Connemara Public Library stamps and handwritten/library marks visible on some pages are later library matter and are **not** part of the speech text or publication imprint.

### Physical structure and pagination

| PDF scan pages | Printed pages | Classification |
|---:|---:|---|
| 1 | — | Cover/title page with later library stamp |
| 2 | — | Publication/editorial introduction; imprint dated 22-5-1971 |
| 3–37 | 1–35 | First editorial speech unit |
| 38–60 | 36–58 | Second editorial speech unit |

From scan p.3 onward the source follows a continuous printed-page sequence corresponding to `scan page = printed page + 2`. The second unit's opening page does not visibly carry a folio at the top, but it lies between printed p.35 (scan p.37) and printed p.37 (scan p.39) in the continuous source sequence and is therefore mapped as printed p.36.

No missing, duplicated or blank physical PDF pages were detected in the supplied 60-page file. Scan quality is generally readable but uneven: the source has old-print softness, speckling/bleed, illustrations, and later library stamps/handwriting on some pages. These must be distinguished from printed speech content during transcription.

The physical PDF ends on scan p.60 / printed p.58 with the end of the second unit, a closing ornament and a later library stamp. No additional speech or back-matter page follows in this PDF.

### Repository duplicate check

Before creating this source map, live `main` was inspected. No existing source folder, canonical speech entry or data-index entry matching:

- `ACL-CPL_01726_நமது_நிலை.pdf`,
- `நமது நிலை`,
- the printed Governor-address date `24-3-1971`, or
- the interim-budget-response wording

was found. There is no existing `speeches/1971/` directory in live `main`. Existing released speeches from other sources are unchanged.

## Gate B — structural mapping

### Important source-specific complication

This booklet is **not safely separable into ordinary dated single-speech entries from the scan alone**.

The front matter says the Governor-address thanks debate and the 1971–72 interim-budget debate occurred in both the Legislative Assembly and Legislative Council. The first unit says Kalaignar `இரு அவைகளிலும் விடையளித்தார்கள்`; the second unit explicitly describes itself as `உரைகளின் தொகுப்பு` from the Assembly and Council.

The edition does **not** print an individual reply date at either unit opening, and it does not print an explicit Assembly-to-Council transition that would allow the two-house speeches to be split into independently dated canonical speech records without external primary evidence. Therefore this map locks the **edition's two editorial units**, not hypothetical underlying House-speech boundaries.

The printed `24-3-1971` on scan p.3 is explicitly the date of Governor Sardar Ujjal Singh's address, **not stated as the date of Kalaignar's reply**. It must not be silently reused as the speech date.

### Locked source-unit inventory

| Unit | Printed source label / opening | Printed speech date | ISO speech date | PDF scan pages | Printed pages | Boundary evidence | Canonical repository ID |
|---|---|---|---|---:|---:|---|---|
| 1 | `நமது நிலை` — introduction to the reply on the motion of thanks for the Governor's address | **Not printed for Kalaignar's reply.** Source mentions `24-3-1971` only as the Governor-address date. | **unresolved** | 3–37 | 1–35 | Opens on scan p.3 after front matter. Scan p.37 ends after a `முதல்வர்:` reply and is followed by a printed closing ornament. Scan p.38 starts a new bold section heading. | **pending** — do not invent a dated canonical ID |
| 2 | `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` | **Not printed** | **unresolved** | 38–60 | 36–58 | Scan p.38 opens with a new section heading and states that the following text is a compilation of the Chief Minister's speeches replying to the interim-budget debate in the Assembly and Council. Scan p.60 ends the text and carries the final closing ornament; no further page follows. | **pending** — do not invent a dated canonical ID |

### Focused second boundary check

A second direct visual check was completed at the critical transition and physical ending:

- **scan p.37 / printed p.35:** first unit closes after the final `முதல்வர்:` intervention/reply and a distinct editorial ornament;
- **scan p.38 / printed p.36:** new heading `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` begins the second unit;
- **scan p.60 / printed p.58:** second unit reaches its physical/textual ending and closing ornament; there is no scan p.61.

The source-unit boundaries are therefore **locked at scan pp.3–37 and 38–60**.

## Source-level transcription and visual-fidelity status

Because the user supplied a full word-to-word transcription with source intake, that text was retained as the **first-pass baseline** while the House/date split remained unresolved. It was not treated as authoritative.

The complete source was then checked word by word against the rendered scan:

- scan pages visually traversed: **1–60 / 60**;
- printed pages visually traversed: front matter + **1–58**;
- confirmed first-pass discrepancy entries: **175**;
- unresolved word/character readings after that first full pass: **0**.

The 175 discrepancies are documented in the visual-fidelity audit series and consolidated in:

- `correction-application-ledger.md`

All scan-supported corrections have now been applied to a **source-level corrected transcription** under:

- `transcription/scan-001-010.md`
- `transcription/scan-011-020.md`
- `transcription/scan-021-030.md`
- `transcription/scan-031-040.md`
- `transcription/scan-041-050.md`
- `transcription/scan-051-060.md`

Consolidation/transition QA is recorded in:

- `transcription-validation.md`

During that QA, one error introduced by the consolidation itself on scan p.57 was caught by reopening the scan and corrected; it was not counted as a new first-pass discrepancy.

## Focused House/date evidence pass

Status: **complete**.

The complete source-internal evidence inventory is recorded in:

- `house-date-evidence.md`

The focused reread confirmed:

- `22-5-1971` is the publication/imprint date, not a printed reply date;
- `24-3-1971` is explicitly the Governor's joint-address date, not a printed Kalaignar reply date;
- Unit 1 explicitly says Kalaignar replied in both Houses;
- Unit 2 explicitly describes the text as an `உரைகளின் தொகுப்பு` from the Assembly and Council;
- Unit 1 contains an explicit `சட்டசபையில்` reference on scan p.32 / printed p.30 and Council-specific references around scan pp.34–35 / printed pp.32–33;
- Unit 2 contains an explicit `மேலவையில்` reference on scan p.54 / printed p.52;
- none of these references is accompanied by a new House heading, reply date, `உரை` label, separator, or restart formula that securely identifies a splice point.

**Negative finding:** this edition does not securely expose the underlying Assembly/Council transcript boundaries or Kalaignar's exact reply dates. Candidate transition loci around the first Council-specific references must remain research leads only. Because Unit 2 calls itself a `தொகுப்பு`, it is unsafe to assume a simple contiguous Assembly-block / Council-block structure.

## Gate status / canonical transcription block

- **Gate A:** complete.
- **Gate B:** source-unit boundaries complete and second-checked.
- **Source-level first-pass visual audit:** complete.
- **Source-level correction application:** complete.
- **Focused source-internal House/date evidence pass:** complete; result is negative for a secure House/date split.
- **Canonical dated speech inventory:** **blocked** pending separately verified primary legislative records.
- **Canonical Gate C/D/E:** **not yet claimable**. The corrected source-level files are a holding/source-witness layer and must not be mislabeled as a verified dated Assembly speech.
- **English / Gates F–G:** blocked.
- **Gate H / release:** not applicable yet for this source.

Do not create a canonical `speeches/YYYY/YYYY-MM-DD-.../` record, set `verified_against_scan=true`, or begin English until the date/House-boundary problem is resolved with source-supported evidence. Do not use the Governor's `24-3-1971` address date as Kalaignar's reply date by assumption.

## Exact continuation point

Next activity: move to a **separately sourced primary-record research layer** without altering the corrected source transcription.

1. Locate official Tamil Nadu Legislative Assembly proceedings for the 1971 Governor-address motion-of-thanks debate and interim-budget debate.
2. Locate Legislative Council proceedings for the corresponding debates.
3. Establish exact sitting/reply dates from primary records.
4. Compare distinctive opening/closing phrases against this edition to test whether defensible House boundaries can be aligned.
5. Record external provenance separately from source facts.
6. Create dated canonical speech entries only if the primary records support a secure House/date/text alignment.