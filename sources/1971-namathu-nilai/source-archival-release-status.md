# நமது நிலை — source archival release status

## Current source status

Controlling source:

`ACL-CPL_01726_நமது_நிலை.pdf`

This PDF is the **only textual authority** for the archival transcription in this source package.

### Source identity

- physical scan pages: **60**
- publication title: `நமது நிலை`
- imprint statement: `சென்னை 22-5-1971.`
- issuing body: `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`
- SHA-256: `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`

### Locked source structure

| Source range | Printed range | Unit |
|---|---:|---|
| scan pp. 1–2 | — | cover / publication front matter |
| scan pp. 3–37 | printed pp. 1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| scan pp. 38–60 | printed pp. 36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

---

## Tamil transcription status

**COMPLETE AND VISUALLY VERIFIED AGAINST THE CONTROLLING BOOKLET SCAN.**

The verified segmented transcription is stored in:

- `transcription/scan-001-010.md`
- `transcription/scan-011-020.md`
- `transcription/scan-021-030.md`
- `transcription/scan-031-040.md`
- `transcription/scan-041-050.md`
- `transcription/scan-051-060.md`

Audit result:

- physical scan traversal: **1–60 / 60**
- printed speech pages traversed: **1–58**
- confirmed first-pass discrepancies corrected: **175**
- unresolved word/character readings: **0**

Supporting records:

- `correction-application-ledger.md`
- `transcription-validation.md`

No further Tamil transcription from any Assembly or Legislative Council PDF is required or permitted for this source archival layer.

---

## External legislative records — reference status only

Additional Assembly and Legislative Council PDFs were used to identify the historical setting of the booklet and to understand its editorial construction.

They establish the following reference events:

| Unit | House | Date | Reference finding |
|---|---|---|---|
| Unit 1 | Tamil Nadu Legislative Assembly | **2 Apr 1971** | Governor-address Motion of Thanks reply |
| Unit 1 | Tamil Nadu Legislative Council | **3 Apr 1971** | Governor-address reply |
| Unit 2 | Tamil Nadu Legislative Assembly | **29 Mar 1971** | Interim-Budget reply |
| Unit 2 | Tamil Nadu Legislative Council | **29 Mar 1971** | Interim-Budget reply |

The Assembly/Council PDFs are **not transcription witnesses for this archive**. Their wording must not be copied into, merged with, or used to repair the booklet transcription.

---

## Provenance mapping status

Both three-way provenance ledgers are complete:

- `unit-1-three-way-alignment-ledger.md`
- `unit-2-three-way-alignment-ledger.md`

Their purpose is to answer questions such as:

- which House/date a booklet passage most likely derives from;
- where the booklet changes source;
- which material was selected, omitted or reordered by the booklet editors;
- whether a `மேலவை` or `சட்டசபை` reference is an internal reference rather than an editorial splice marker.

They do **not** alter the verified booklet transcription.

---

## Editorial construction now established

### Unit 1

The booklet principally follows material associated with the **2 April 1971 Assembly reply**, then later selects material associated with the **3 April 1971 Council reply**, including the prohibition discussion and final clarification.

This is provenance metadata only. The source text remains exactly what `நமது நிலை` prints.

### Unit 2

The booklet interleaves material associated with the **29 March 1971 Assembly and Council replies** more than once rather than using one simple House-transition point.

Again, this is provenance metadata only. The source text remains exactly what `நமது நிலை` prints.

---

## Archival release rule

For this source package, the verified Tamil archival witness is the complete booklet transcription represented by the six segmented files above.

The archival layer must preserve:

- booklet wording;
- booklet spelling;
- booklet punctuation;
- booklet headings;
- booklet page boundaries;
- booklet ordering;
- booklet omissions and editorial selections.

No external legislative text may be added for completeness.

---

## `speeches/1971/` representation status

**Not yet created.**

Reason: the booklet is an edited two-House witness. A dated Assembly-facing index entry must not silently turn the booklet into a reconstructed Official Report speech.

Any future `speeches/1971/...` representation must satisfy all of the following:

1. Tamil wording comes only from `ACL-CPL_01726_நமது_நிலை.pdf` as preserved in the verified source transcription;
2. external Assembly/Council reports contribute only date/House/event/provenance metadata;
3. Council-derived booklet material is not falsely labelled as Assembly text;
4. omitted Official Report material is not inserted;
5. the entry clearly states that the textual witness is the 1971 booklet and that the booklet itself is editorially compiled.

Until that representation is designed and checked, the source-level transcription is the canonical textual record for this source.

---

## English status

**Not started / blocked.**

When English work begins, it must translate the verified booklet Tamil only. External Assembly/Council wording must not be imported into the translation.

---

## Exact next activity

Prepare the **booklet-derived 1971 representation design** before creating anything under `speeches/1971/`.

The design should determine whether the safest repository-facing representation is:

- one archival entry per booklet editorial unit with explicit mixed-House provenance; or
- Assembly-facing excerpt/index records that point back to the complete source transcription without pretending to be complete verbatim Assembly transcripts.

Whichever representation is chosen, the Tamil textual content must remain sourced only from `ACL-CPL_01726_நமது_நிலை.pdf`.