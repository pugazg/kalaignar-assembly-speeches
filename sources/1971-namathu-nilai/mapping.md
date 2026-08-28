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

| Unit | Printed source label / opening | Printed speech date | Primary-record status | PDF scan pages | Printed pages | Boundary evidence | Canonical repository ID |
|---|---|---|---|---:|---:|---|---|
| 1 | `நமது நிலை` — introduction to the reply on the motion of thanks for the Governor's address | **Not printed for Kalaignar's reply.** Source mentions `24-3-1971` only as the Governor-address date. | Assembly: **LOCKED to 2 April 1971**, reply pp. 314–336, motion completed p.337. Council: official programme strongly establishes **3 April 1971** as Chief Minister reply day, but direct 3 April text is still missing. Booklet is a mixed two-House editorial witness. | 3–37 | 1–35 | Opens on scan p.3 after front matter. Scan p.37 ends after a `முதல்வர்:` reply and is followed by a printed closing ornament. Scan p.38 starts a new bold section heading. | **pending span-level provenance alignment** — do not copy the whole editorial unit into a dated Assembly record |
| 2 | `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` | **Not printed** | Underlying Assembly and Council replies both **LOCKED to 29 March 1971**; booklet itself is a mixed two-House editorial compilation requiring span-level alignment. | 38–60 | 36–58 | Scan p.38 opens with a new section heading and states that the following text is a compilation of the Chief Minister's speeches replying to the interim-budget debate in the Assembly and Council. Scan p.60 ends the text and carries the final closing ornament; no further page follows. | **pending span-level provenance alignment** — do not split at an assumed House boundary |

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

## Focused source-internal House/date evidence pass

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

**Source-internal negative finding remains valid:** the edition itself does not securely expose the underlying Assembly/Council transcript boundaries or Kalaignar's exact reply dates. The later primary-record work does not change the booklet scan; it provides external provenance evidence.

The direct 2 April Assembly record now adds an important caution: some `மேலவை` references in Unit 1 are themselves present inside the Assembly reply, so such references cannot be treated mechanically as House-transition markers.

---

## Primary-record status update — 29 August 2026

Detailed evidence is recorded in:

- `primary-record-retrieval-pass-09.md`
- `primary-record-retrieval-pass-10.md`
- `primary-record-retrieval-pass-11.md`
- `primary-record-research.md`

### Unit 1 — Assembly reply directly locked

The supplied `927002(1).pdf` directly establishes:

- date: **2 April 1971**;
- House: **Tamil Nadu Legislative Assembly**;
- subject: Governor-address Motion of Thanks;
- Karunanidhi reply starts on printed p. **314** after Thiru R. Ponnappa Nadar;
- the opening directly matches the booklet's distinctive **67 members / 183–33 / 52–34** sequence;
- the reply remains directly aligned through late State-autonomy, Mujibur Rahman, `50 சென்ட்`, bus-ceiling and retrospective-effect material;
- the reply continues through printed p. **336**;
- the Motion of Thanks is put and carried unanimously on p. **337**.

Therefore the Unit 1 Assembly event is **LOCKED to 2 April 1971**.

### Unit 1 — mixed-witness conclusion and Council target

The booklet then moves from directly Assembly-aligned bus-ceiling material into the `வேடுவர்கள் சூழ்ந்த மான்` prohibition sequence, whereas the recovered Assembly report follows a different closing route.

Unit 1 is therefore also a **mixed two-House editorial witness**.

The Council evidence now gives an exceptionally strong official chronology for the remaining component:

- the 26 March Business Advisory programme explicitly schedules **3 April 1971** for `Reply to the debate on the Governor's Address by the Hon. Chief Minister`;
- Volume LXXXVIII places the 3 April Governor-address continuation at pp. **411–456**;
- `922362(1).pdf` shows **2 April** still in continuing member debate;
- `922416(1).pdf` shows that by **5 April** the Governor had received the completed Resolution of Thanks.

The actual 3 April Council daily report is still required before the booklet's final prohibition sequence can be text-locked to that House/date.

### Unit 2 — both underlying House replies directly locked

#### Legislative Assembly

Direct Assembly Official Report evidence establishes:

- date: **29 March 1971**;
- Fifth Assembly, Session I;
- Volume I (Nos. 1–5);
- Karunanidhi's Interim Budget general-discussion reply: **printed pp. 298–313**.

The reply opening and multiple internal/closing anchors directly match Unit 2, including the late `மாநிலத்திற்கு மாநிலம் ரகுமான்களைத் தோற்றுவிக்க...` sentence.

#### Legislative Council

Direct Council Official Report evidence establishes:

- date: **29 March 1971**;
- Thirty-Eighth Session;
- Volume **LXXXVIII**;
- Karunanidhi's Budget general-discussion reply: **printed pp. 200–207**.

The Council reply explicitly says that Karunanidhi had already given the corresponding reply in the **Legislative Assembly that morning**.

The Council sequence directly matches important booklet material including the `உரிமைக் குரல்` / opposition-cooperation discussion, parliamentary-method argument, the `காவடி` passage and the State Planning Commission / ten-year planning discussion.

### Unit 2 structural conclusion

The two primary reports prove that Unit 2 is an editorial compilation drawing from **both 29 March 1971 House replies**.

A simple one-time Assembly→Council splice is **not defensible**: late booklet material matches the Council, while the booklet's final `ரகுமான்களைத் தோற்றுவிக்க...` sentence matches the Assembly closing sequence.

The correct next step is therefore a **three-way span-level alignment**, not a guessed page split.

## Gate status / canonical transcription block

- **Gate A:** complete.
- **Gate B:** source-unit boundaries complete and second-checked.
- **Source-level first-pass visual audit:** complete.
- **Source-level correction application:** complete.
- **Focused source-internal House/date evidence pass:** complete; source alone remains insufficient for a House splice.
- **Unit 1 underlying Assembly event:** **locked — 2 April 1971, reply pp. 314–336; motion completed p.337**.
- **Unit 1 underlying Council event:** **date strongly established as 3 April by official chronology; direct text still missing**.
- **Unit 1 booklet-to-House provenance mapping:** **blocked pending direct 3 April Council text and three-way alignment**.
- **Unit 2 underlying Assembly event:** **locked — 29 March 1971, pp. 298–313**.
- **Unit 2 underlying Council event:** **locked — 29 March 1971, pp. 200–207**.
- **Unit 2 booklet-to-House provenance mapping:** **in progress / blocked pending three-way span alignment**.
- **Canonical Gate C/D/E:** not yet claimable for booklet-derived dated entries because the mixed editorial witnesses still require defensible span provenance.
- **English / Gates F–G:** blocked.
- **Gate H / release:** not applicable yet for this source.

Do not create a canonical `speeches/YYYY/YYYY-MM-DD-.../` record from either booklet unit merely by splitting it at an inferred transition, set `verified_against_scan=true`, or begin English until the House/date/text provenance is safely mapped.

## Exact continuation point

1. Recover the **3 April 1971 Legislative Council Official Report**, especially Governor-address pp. **411–456**.
2. Phrase-align its Chief Minister reply against Unit 1's final prohibition sequence:
   - `வேடுவர்கள் சூழ்ந்த மான்`;
   - surrounding-State / Pondicherry prohibition comparison;
   - D. K. Shanmugam's song;
   - R. Krishnaswami Naidu's appeal;
   - Karunanidhi's final clarification.
3. Build a **three-way Unit-1 alignment ledger**:
   - booklet Unit 1, scan pp. 3–37 / printed pp. 1–35;
   - Assembly 2 April 1971 reply, Official Report pp. 314–336;
   - Council 3 April 1971 reply, once recovered.
4. Build/continue the **three-way Unit-2 alignment ledger**:
   - booklet Unit 2, scan pp. 38–60 / printed pp. 36–58;
   - Assembly 29 March 1971 reply, Official Report pp. 298–313;
   - Council 29 March 1971 reply, Official Report pp. 200–207.
5. Classify each booklet span as Assembly / Council / both / editorially combined or reordered / unmatched without altering source wording.
6. Create dated canonical speech entries only after the relevant source spans can be defensibly assigned to the underlying House records.
