# நமது நிலை — booklet-derived 1971 representation design

## Decision

For this source, **do not create reconstructed House transcripts under `speeches/1971/`**.

The reason is archival, not merely technical:

- the only transcription authority is `ACL-CPL_01726_நமது_நிலை.pdf`;
- both booklet editorial units are mixed Assembly/Council compilations;
- the booklet does not preserve either underlying House speech continuously;
- adding wording from the Official Reports is prohibited for this source;
- extracting only selected Assembly-attributed sentences would create a derivative text that the booklet itself does not print as one continuous speech.

Therefore the safest representation is to preserve the booklet transcription as the canonical textual layer and represent the dated Assembly events as **metadata/reference records pointing into that source witness**.

---

## 1. Canonical text remains source-level

Canonical Tamil text for this source remains exclusively in:

- `transcription/scan-001-010.md`
- `transcription/scan-011-020.md`
- `transcription/scan-021-030.md`
- `transcription/scan-031-040.md`
- `transcription/scan-041-050.md`
- `transcription/scan-051-060.md`

These six files collectively represent the verified transcription of the complete 60-page source package.

They are not to be rewritten, resegmented or completed from Assembly/Council reports.

---

## 2. Assembly-facing event representation

Create source-local event reference records rather than new transcript files.

Recommended paths:

```text
sources/1971-namathu-nilai/events/
├── 1971-03-29-assembly-interim-budget-reply.md
└── 1971-04-02-assembly-governors-address-reply.md
```

These records should contain **metadata and provenance only**:

- date;
- House;
- event description;
- which booklet editorial unit contains material from that event;
- booklet scan/printed page ranges involved;
- provenance-ledger classifications;
- explicit warning that the booklet is not a complete verbatim House transcript;
- links to the verified booklet transcription segments;
- links to the provenance ledgers;
- external Official Report identity/page range as reference evidence only.

They must contain **no reconstructed Tamil speech text copied from another PDF**.

---

## 3. Why not `speeches/1971/...` yet

The repository's normal `speeches/YYYY/YYYY-MM-DD-event/` structure implies that a canonical speech transcript exists for that dated event.

For `நமது நிலை`, that implication would be unsafe because:

- Unit 1 combines 2 April Assembly material with 3 April Council material;
- Unit 2 interleaves 29 March Assembly and Council material multiple times;
- the booklet omits some House-record material and rearranges other material;
- the archival instruction forbids importing the missing Official Report text.

A `speeches/1971/.../transcript.md` assembled from only the Assembly-attributed booklet spans would be a new editorial extraction, not the booklet as printed and not the complete Assembly speech.

Therefore no such transcript should be created silently.

---

## 4. Booklet-unit records remain primary for reading

The reader-facing archival sequence should continue to be:

### Unit 1

- scan pp. **3–37**
- printed pp. **1–35**
- Governor-address reply compilation
- mixed provenance: Assembly 2 Apr 1971 + Council 3 Apr 1971

### Unit 2

- scan pp. **38–60**
- printed pp. **36–58**
- `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்`
- mixed provenance: Assembly + Council, both 29 Mar 1971

The source wording and editorial order remain the reading text.

---

## 5. Provenance annotations must stay outside source text

The completed ledgers may identify a span as:

- Assembly-derived;
- Council-derived;
- parallel in both Houses;
- editorially jumped/omitted/reordered.

Those classifications belong in metadata/reference notes.

Do not insert labels such as `[Assembly]`, `[Council]`, reconstructed dates, Official Report page numbers or editorial explanations into the verified Tamil transcription itself unless they are clearly outside the quoted/source-text layer.

---

## 6. External-report references

The following references may be cited in the event records for historical identification only:

- 29 Mar 1971 Assembly Interim-Budget reply — Official Report pp.298–313;
- 29 Mar 1971 Council Budget reply — pp.200–207;
- 2 Apr 1971 Assembly Governor-address reply — pp.314–336;
- 3 Apr 1971 Council Governor-address reply — formal reply pp.434–454, clarifications through p.456.

No textual content from those reports is to be copied into the source transcript or used to complete it.

---

## 7. Indexing rule

Until a future explicit decision authorises a derived `speeches/1971/` representation:

- do **not** add the two dated events to `data/speeches.json` as completed canonical transcripts;
- do **not** add them to the root speech table as if full Assembly transcripts were archived;
- instead, the source package may be listed in an active/source-research section with its verified-transcription status and dated-event reference links.

This prevents the repository index from overstating what the booklet itself contains.

---

## 8. Translation consequence

English translation, when started, should translate the booklet units in their printed editorial order.

It should not be split into reconstructed Assembly/Council speeches using external wording.

Provenance notes may accompany the translation separately.

---

## 9. Representation state

- controlling booklet transcription: **complete / verified**;
- House/date research: **complete for all four underlying reply events**;
- Unit 1 provenance ledger: **complete**;
- Unit 2 provenance ledger: **complete**;
- Official Reports: **reference only**;
- `speeches/1971/` canonical transcripts: **intentionally not created**;
- source-local Assembly event reference records: **ready to create**;
- English: **not started**.

---

## Exact next activity

Create the two source-local Assembly event reference records under:

`sources/1971-namathu-nilai/events/`

They must point only to the verified `நமது நிலை` transcription for textual content and use the other legislative PDFs only for House/date/event provenance.