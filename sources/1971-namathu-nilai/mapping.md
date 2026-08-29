# Source mapping — நமது நிலை

## Gate A — source preflight

Status: **complete for the supplied scan**.

### Controlling source identity

- **Scan filename:** `ACL-CPL_01726_நமது_நிலை.pdf`
- **Actual PDF pages:** **60**
- **File size:** **21,613,923 bytes**
- **SHA-256:** `5cfbf0e5d01a9cedb252a12168e9e6a14a9a2061c7d78848dde692d5fa241acb`
- **Controlling authority for the booklet witness:** rendered booklet scan pages. OCR/extracted text is navigation assistance only.

### Publication evidence

- **Printed title:** `நமது நிலை`
- **Cover attribution:** `தமிழக முதல்வர் கலைஞர் மு.கருணாநிதி`
- **Imprint/date statement:** `சென்னை 22-5-1971.`
- **Issuing body:** `செய்தி-விளம்பரத் துறை, தமிழ்நாடு அரசு.`

Connemara Public Library stamps and later handwritten/library marks are not part of the publication text.

### Physical structure

| PDF scan pages | Printed pages | Classification |
|---:|---:|---|
| 1 | — | Cover/title page |
| 2 | — | Publication/editorial introduction and imprint |
| 3–37 | 1–35 | Editorial Unit 1 — Governor-address replies |
| 38–60 | 36–58 | Editorial Unit 2 — Interim-Budget replies |

From scan p.3 onward: `printed page = scan page - 2`.

No missing, duplicated or blank physical PDF pages were detected.

---

## Gate B — structural mapping

Status: **complete and locked**.

The booklet is **not a simple set of verbatim single-House transcripts**. Its front matter says the relevant debates/replies occurred in both the Legislative Assembly and Legislative Council. Unit 2 explicitly describes itself as an `உரைகளின் தொகுப்பு` from both Houses.

External Class-A Official Reports were required to establish the underlying House/date events and the booklet's editorial construction.

### Locked source-unit inventory

| Unit | Printed source label | PDF scan pages | Printed pages | Underlying primary events | Provenance status |
|---|---|---:|---:|---|---|
| 1 | `நமது நிலை` — Governor-address reply material | 3–37 | 1–35 | Assembly **2 Apr 1971**, reply pp.314–336; Council **3 Apr 1971**, formal reply pp.434–454 + clarifications | **three-way span ledger complete** |
| 2 | `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` | 38–60 | 36–58 | Assembly **29 Mar 1971**, reply pp.298–313; Council **29 Mar 1971**, reply pp.200–207 | **three-way span ledger complete** |

### Source-unit boundaries

- scan p.37 / printed p.35 closes Unit 1 after the final `முதல்வர்:` exchange and editorial ornament;
- scan p.38 / printed p.36 begins Unit 2;
- scan p.60 / printed p.58 ends Unit 2 and the physical PDF.

---

## Source-level transcription / visual-fidelity status

Completed:

- scan pages visually traversed: **1–60 / 60**;
- printed pages visually traversed: front matter + **1–58**;
- confirmed first-pass discrepancy entries: **175**;
- unresolved word/character readings: **0**.

The 175 accepted corrections are consolidated in `correction-application-ledger.md` and applied to:

- `transcription/scan-001-010.md`
- `transcription/scan-011-020.md`
- `transcription/scan-021-030.md`
- `transcription/scan-031-040.md`
- `transcription/scan-041-050.md`
- `transcription/scan-051-060.md`

QA is recorded in `transcription-validation.md`.

The legislative Official Reports do **not** supersede this booklet transcription. The booklet remains its own source witness.

---

## Source-internal House/date evidence

`house-date-evidence.md` remains the source-internal evidence record.

Key findings:

- `22-5-1971` is the booklet publication date, not a reply date;
- `24-3-1971` is the Governor's joint-address date, not Karunanidhi's reply date;
- Unit 1 says he replied in both Houses;
- Unit 2 is explicitly a two-House compilation;
- isolated `சட்டசபையில்` / `மேலவையில்` references are not safe splice markers.

The recovered 2 April Assembly report proves the last point directly because a reference to the Council Opposition Leader occurs **inside the Assembly speech itself**.

---

# Primary-record mapping — locked

Detailed research:

- `primary-record-retrieval-pass-09.md`
- `primary-record-retrieval-pass-10.md`
- `primary-record-retrieval-pass-11.md`
- `primary-record-retrieval-pass-12.md`
- `primary-record-research.md`

## Four-event lock matrix

| Unit | House | Date | Reply span | Completion/status |
|---|---|---|---|---|
| Unit 1 | Legislative Assembly | **2 Apr 1971** | **pp.314–336** | Motion carried p.337 |
| Unit 1 | Legislative Council | **3 Apr 1971** | **pp.434–454** | Clarifications pp.455–456; motion carried p.456 |
| Unit 2 | Legislative Assembly | **29 Mar 1971** | **pp.298–313** | General discussion concludes p.313 |
| Unit 2 | Legislative Council | **29 Mar 1971** | **pp.200–207** | Reply concludes p.207 |

All four events are direct Class-A locks.

---

## Unit 1 three-way provenance — COMPLETE

See `unit-1-three-way-alignment-ledger.md`.

Locked editorial model:

1. booklet opening through the bus-ceiling / retrospective-effect sentence on scan p.35 / printed p.33 follows the **2 April Assembly reply** as its main backbone;
2. the booklet then switches to the **3 April Council** prohibition sequence;
3. it omits Council p.454;
4. it resumes the later Council p.455 prohibition clarification.

Therefore Unit 1 is a **mixed, edited two-House witness** and cannot be copied wholesale into a dated Assembly speech.

---

## Unit 2 three-way provenance — COMPLETE

See `unit-2-three-way-alignment-ledger.md`.

Locked editorial model:

1. Unit 2 begins on the **29 March Assembly** reply;
2. **Assembly → Council** inside scan p.53 / printed p.51 at the `இடைக்கால உரிமைக்குரல்` sequence;
3. **Council → Assembly** inside scan p.57 / printed p.55 after the `காவடி` / Delhi-echo material;
4. **Assembly → Council** inside scan p.59 / printed p.57 at the State Planning Commission heading;
5. **Council → Assembly** inside scan p.60 / printed p.58 for the final State-autonomy / `ரகுமான்கள்` / rights-voice close.

Both primary records also contain material deliberately omitted from the booklet.

Therefore Unit 2 is a **mixed, interleaved two-House editorial compilation**, not a continuous House transcript.

---

# Canonical extraction policy — LOCKED

See `canonical-extraction-policy.md`.

The repository root defines this project as an archive of **Tamil Nadu Legislative Assembly speeches**. Therefore the four underlying events do not become four canonical entries here.

### Canonical Assembly targets

1. `speeches/1971/1971-03-29-interim-budget-reply/`
   - controlling witness: Assembly Official Report `713373.pdf`, printed pp. **298–313**;
   - booklet Unit 2 = parallel edited witness only.

2. `speeches/1971/1971-04-02-governors-address-motion-of-thanks-reply/`
   - controlling witness: Assembly Official Report `927002(1).pdf`, printed pp. **314–336**;
   - booklet Unit 1 = parallel edited witness only.

### Council treatment

The 29 March and 3 April Council replies remain provenance evidence under this source directory. No Council canonical speech directories, root-index entries or `data/speeches.json` entries are created in this Assembly-only repository.

### Witness rule

- booklet scan controls the booklet transcription;
- Assembly Official Report controls each canonical Assembly transcript;
- Council Official Reports are provenance comparators here;
- no witness silently corrects another;
- the booklet's **175 corrections remain booklet-witness corrections only**.

### Verification rule

The new 1971 Assembly entries must independently pass Gate E against their **Assembly Official Report scans**. The booklet's completed visual audit does not transfer `verified_against_scan=true` to the dated Assembly entries.

English remains blocked until each Official Report-based canonical Tamil transcript is verified.

---

## Current gate status

- **Gate A / booklet:** complete.
- **Gate B / booklet:** complete.
- **Booklet Tamil transcription:** complete.
- **Booklet visual audit:** complete.
- **Correction application:** complete — **175** corrections.
- **House/date research:** complete.
- **Unit 1 three-way provenance:** complete.
- **Unit 2 three-way provenance:** complete.
- **Canonical extraction policy:** complete and locked.
- **29 Mar 1971 Assembly Gate C:** **ready to begin**.
- **2 Apr 1971 Assembly Gate C:** ready after the chronological first entry.
- **English / Gates F–G:** blocked.
- **Gate H / 1971 release:** not yet reached.

Do not alter the six corrected booklet transcription files while creating the new Official Report-based canonical entries.

## Exact continuation point

Begin **Gate C for 29 March 1971**:

1. create `speeches/1971/1971-03-29-interim-budget-reply/`;
2. use `713373.pdf` Official Report pp. **298–313** as the controlling textual witness;
3. transcribe the complete Assembly reply in order, including Official Report material omitted by the booklet;
4. preserve speaker labels/interventions within the reply sequence;
5. record `நமது நிலை` Unit 2 and `unit-2-three-way-alignment-ledger.md` as parallel/provenance witnesses only;
6. keep `verified_against_scan=false` until a separate page-by-page Official Report visual audit is complete;
7. do not begin English.
