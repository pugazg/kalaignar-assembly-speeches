# நமது நிலை — canonical extraction policy

## Decision status

**LOCKED for this source.**

The two three-way provenance ledgers are complete:

- `unit-1-three-way-alignment-ledger.md`
- `unit-2-three-way-alignment-ledger.md`

They prove that `நமது நிலை` is a **mixed, edited two-House publication witness**, not a verbatim transcript of one continuous Assembly speech in either editorial unit.

This policy defines how the repository may now create dated canonical Assembly entries without damaging either the booklet witness or the recovered legislative records.

---

## 1. Repository scope controls the canonical layer

The repository root defines `kalaignar-assembly-speeches` as an archive of M. Karunanidhi's speeches in the **Tamil Nadu Legislative Assembly**.

Therefore the four directly locked underlying House events do **not** become four canonical speech directories here.

### Canonical in this repository

1. **29 March 1971 — Tamil Nadu Legislative Assembly**  
   Reply to the general discussion on the 1971–72 Interim Budget  
   Official Report printed pp. **298–313**.

2. **2 April 1971 — Tamil Nadu Legislative Assembly**  
   Reply to the debate on the Motion of Thanks for the Governor's Address  
   Official Report printed pp. **314–336**.

### Provenance-only in this repository

3. **29 March 1971 — Tamil Nadu Legislative Council**  
   Budget reply, Official Report pp. **200–207**.

4. **3 April 1971 — Tamil Nadu Legislative Council**  
   Governor-address reply, formal reply pp. **434–454**, immediate clarifications through pp. **455–456**.

The Council records remain essential Class-A evidence for explaining how the booklet was edited, but they must **not** be placed under `speeches/` in this Assembly-only repository.

If a future Legislative Council archive is created, these Council events may be canonicalised there from their own Official Reports. This repository must not pre-empt that separate scope.

---

## 2. Witness hierarchy is event-specific, not global

There are now three distinct witness layers and they must not be collapsed.

### A. Booklet witness — controlling for the publication `நமது நிலை`

Controlling source:

- `ACL-CPL_01726_நமது_நிலை.pdf`
- source-level transcription: `sources/1971-namathu-nilai/transcription/scan-*.md`
- visual audit complete
- **175** scan-supported corrections applied
- unresolved source readings: **0**

For the booklet as a publication, the rendered booklet scan remains the highest textual authority.

Nothing in an Assembly or Council Official Report may be used to silently "correct" the booklet wording, spelling, punctuation, ordering, headings, omissions or editorial selections.

### B. Assembly Official Report — controlling for each dated canonical Assembly speech

For a canonical dated Assembly entry, the relevant **Assembly Official Report scan** becomes the controlling textual witness for that event.

- 29 March event: `713373.pdf`, Official Report pp. **298–313**.
- 2 April event: `927002(1).pdf`, Official Report pp. **314–336**.

The canonical Assembly transcript must be transcribed and verified from those Official Report pages themselves.

The already-verified booklet transcription is a parallel historical publication witness. It is **not** the textual base from which a full Assembly speech may be reconstructed.

### C. Council Official Report — provenance comparator only here

- 29 March Council: `922282.pdf`, pp. **200–207**.
- 3 April Council: `922376.pdf`, pp. **434–456** as mapped.

These records explain the Council-derived material inserted into the booklet. They do not contribute text to the canonical Assembly transcript.

---

## 3. Why the booklet cannot control a dated Assembly transcript

The completed ledgers establish deliberate editing that prevents whole-unit extraction.

### Unit 1

The booklet follows the 2 April Assembly reply as its main backbone through the bus-ceiling / retrospective-effect passage, then switches inside printed p.33 to the 3 April Council prohibition sequence, omits Council p.454, and resumes a later Council clarification from p.455.

Therefore copying Unit 1 wholesale into a `1971-04-02` Assembly entry would falsely attribute Council speech material to the Assembly and would omit the Assembly reply's real continuation and close.

### Unit 2

The booklet begins with the 29 March Assembly reply, switches to Council material inside printed p.51, returns to Assembly material, switches again to the Council State Planning Commission sequence, and finally returns to the Assembly `ரகுமான்கள்` / rights-voice closing.

Therefore copying Unit 2 wholesale into a `1971-03-29` Assembly entry would create a synthetic speech that was never delivered as such in the Assembly.

The correct archival response is **not** to splice the booklet back into a reconstructed House speech. The correct response is to preserve the booklet intact as one witness and separately transcribe the direct House record as the canonical dated event.

---

## 4. Canonical 1971 Assembly entries to create

### Entry A — 29 March 1971

Recommended canonical path:

```text
speeches/1971/1971-03-29-interim-budget-reply/
```

Working event labels:

- Tamil: `1971-72 இடைக்கால நிதிநிலை அறிக்கை மீதான பொது விவாதத்திற்கான பதிலுரை`
- English: `Reply to the general discussion on the Interim Budget for 1971–72`

Controlling event witness:

- Tamil Nadu Legislative Assembly Official Report
- date: **29 March 1971**
- printed pp. **298–313**
- reply begins on p.298 after R. Ponnappa Nadar concludes
- reply ends on p.313
- the Speaker's subsequent statement that the general discussion has concluded is **boundary evidence**, not part of Karunanidhi's speech text

### Entry B — 2 April 1971

Recommended canonical path:

```text
speeches/1971/1971-04-02-governors-address-motion-of-thanks-reply/
```

Working event labels:

- Tamil: `ஆளுநர் உரைக்கு நன்றி தெரிவிக்கும் தீர்மான விவாதத்திற்கான பதிலுரை`
- English: `Reply to the debate on the Motion of Thanks for the Governor's Address`

Controlling event witness:

- Tamil Nadu Legislative Assembly Official Report
- date: **2 April 1971**
- printed pp. **314–336**
- reply begins on p.314 after R. Ponnappa Nadar concludes
- Karunanidhi's reply closes on p.336
- the Motion of Thanks being put and carried on p.337 is **boundary/completion evidence**, not part of the speech text

The exact Tamil/English event labels may be refined only from the recovered Official Report or other direct legislative metadata. They must not be promoted as quoted printed titles unless the source itself prints them that way.

---

## 5. Transcript construction rule

For both 1971 canonical Assembly entries:

1. transcribe the complete mapped Assembly Official Report span in order;
2. preserve the Official Report's wording, spelling, numerals, printed English, speaker labels and interventions;
3. use explicit Official Report page markers;
4. do not insert booklet headings merely because they are useful editorial headings;
5. do not remove Official Report passages omitted by the booklet;
6. do not insert Council passages preserved by the booklet;
7. do not use booklet wording to silently repair a difficult Official Report reading;
8. if the Official Report scan is genuinely unreadable, mark the uncertainty and use the booklet only as a separately documented comparison clue, never as an unmarked substitution.

Recommended page-marker convention for these entries:

```html
<!-- official-report-page: 298 -->
```

If the repository prefers to retain the existing generic `<!-- source-page: N -->` convention, `source-notes.md` must explicitly state that these numbers are **printed Official Report pages**, not physical PDF pages. Do not mix booklet scan-page numbers into the canonical Assembly transcript.

---

## 6. Parallel-witness comparison rule

`நமது நிலை` should be cited in each canonical entry's `source-notes.md` as a **parallel edited publication witness**.

The notes should state:

- the booklet publication identity and date;
- which booklet unit contains material from the event;
- the relevant provenance ledger;
- that the booklet mixes Assembly and Council material;
- that wording/order differences between the booklet and Official Report are witness differences, not automatic errors;
- that the booklet's 175 source-supported corrections belong to the booklet witness only.

A useful comparison table may record major overlaps and omissions, but it must not turn into a conflated transcript.

### Conflict rule

If the booklet and Official Report differ:

- preserve the Official Report reading in the canonical Assembly transcript if that reading is visually verified in the Official Report scan;
- preserve the booklet reading in the booklet transcription if that reading is visually verified in the booklet scan;
- document the variance only when archivally useful;
- never choose one witness and overwrite the other merely to make them agree.

This repository is preserving **witnesses**, not manufacturing a harmonised critical edition.

---

## 7. Gate and verification semantics for the new canonical entries

The booklet's completed visual audit does **not** transfer `verified` status to the dated Assembly entries.

Each new Assembly entry must independently pass the repository workflow against its own controlling Official Report scan.

### Gate C — Tamil first pass

Create a complete Tamil transcription from the relevant Official Report pages.

Initial metadata must use a non-verified state such as `in-progress` or `transcribed` as appropriate.

### Gate D — completeness

Confirm every mapped Official Report page is represented exactly once and all interventions within the speech sequence are present.

### Gate E — source-fidelity verification

Perform a direct page-by-page visual audit of the Official Report scan. Only after this may the dated Assembly entry use:

```json
"status": "verified",
"verified_against_scan": true
```

For these 1971 entries, `verified_against_scan=true` means **verified against the Assembly Official Report scan**, not verified against `நமது நிலை`.

### Gates F–G — English

English must translate the **verified canonical Assembly transcript** from the Official Report.

Do not translate the mixed booklet unit and relabel it as an Assembly speech.

### Gate H — release

Only after Tamil and English are independently verified may the entry be added as released material to:

- `data/speeches.json`;
- the root README speech index;
- any release/status summaries.

---

## 8. Booklet source status after canonical extraction begins

Canonical Assembly work must not disturb the completed source layer.

The following remain locked unless a direct scan-supported error is later discovered:

- all six corrected `transcription/scan-*.md` files;
- `correction-application-ledger.md`;
- `transcription-validation.md`;
- the **175** accepted corrections;
- Unit 1 and Unit 2 booklet boundaries;
- the two three-way provenance ledgers.

Creating the canonical Assembly entries is a **new witness-layer activity**, not a continuation of booklet transcription correction.

---

## 9. Council treatment

Because this repository is Assembly-scoped:

- do not create `speeches/1971/...` entries for the 29 March or 3 April Council replies;
- do not list them in `data/speeches.json`;
- do not list them in the root Assembly speech index;
- retain their report identities, page spans and direct anchors under `sources/1971-namathu-nilai/` as provenance research;
- use them whenever necessary to prevent Council material from being misattributed to an Assembly event.

The Council evidence is therefore **archivally essential but non-canonical in this repository**.

---

## 10. Locked canonical matrix

| Canonical target | Repository treatment | Controlling textual witness | Parallel witness | Current status |
|---|---|---|---|---|
| 29 Mar 1971 Assembly Interim-Budget reply, pp.298–313 | **Create canonical Assembly entry** | Assembly Official Report `713373.pdf` | `நமது நிலை` Unit 2 + Council provenance ledger | **ready for Gate C** |
| 2 Apr 1971 Assembly Governor-address reply, pp.314–336 | **Create canonical Assembly entry** | Assembly Official Report `927002(1).pdf` | `நமது நிலை` Unit 1 + Council provenance ledger | **ready for Gate C** |
| 29 Mar 1971 Council Budget reply, pp.200–207 | provenance only | Council Official Report `922282.pdf` | `நமது நிலை` Unit 2 | no canonical entry here |
| 3 Apr 1971 Council Governor-address reply, pp.434–454 + clarifications | provenance only | Council Official Report `922376.pdf` | `நமது நிலை` Unit 1 | no canonical entry here |

---

## 11. Exact next activity

Begin **Gate C for the 29 March 1971 Assembly Interim-Budget reply** first because:

- its complete Official Report span is already locked at pp.298–313;
- its opening and closing boundaries are direct;
- it is the earlier of the two in-scope Assembly events;
- the Unit 2 provenance ledger is complete.

Next pass should:

1. create `speeches/1971/1971-03-29-interim-budget-reply/` using the established speech-entry structure;
2. make `713373.pdf` / Official Report pp.298–313 the controlling canonical source;
3. transcribe the complete Tamil reply from those pages in order;
4. preserve all Official Report interventions and material even when omitted by `நமது நிலை`;
5. record `நமது நிலை` only as a parallel edited witness in `source-notes.md`;
6. keep `verified_against_scan=false` until a separate full Official Report visual audit is complete;
7. do not begin English yet.

After 29 March reaches Gate E, repeat the same process for the **2 April 1971 Assembly reply, pp.314–336**.
