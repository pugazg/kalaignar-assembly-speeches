# நமது நிலை — booklet-derived 1971 representation design

## Final decision and implementation

The original design correctly rejected reconstructed House-specific transcripts. A later explicit project decision implemented a **booklet-level reader-facing entry** instead:

`speeches/1971/1971-namathu-nilai/`

This implementation does **not** reconstruct an Assembly or Council Official Report speech. It preserves the verified `நமது நிலை` booklet witness in its own printed order, with the two editorial units intact and mixed-House provenance documented separately.

## Controlling principles

- only `ACL-CPL_01726_நமது_நிலை.pdf` may supply Tamil textual wording;
- English is translated only from the verified booklet Tamil;
- Assembly/Council Official Reports remain reference/provenance only;
- no missing Official Report wording may be inserted;
- no Council-derived span is silently relabelled as Assembly text;
- the booklet publication date is not treated as a single speech date.

## Canonical source text

The six verified source-transcription files under `transcription/` remain the canonical Tamil witness for the complete 60-page source package.

The reader-facing entry copies only the speech-text range:

- Unit 1: scan pp.3–37 / printed pp.1–35
- Unit 2: scan pp.38–60 / printed pp.36–58

Scan pp.1–2 remain publication front matter/source metadata.

## Reader-facing representation

The implemented folder contains:

- `README.md`
- `metadata.json`
- `source-notes.md`
- `transcript.md`
- `translation.md`

Its classification is:

**booklet-edited-two-house-compilation**

It is deliberately not represented as one dated Assembly transcript. `metadata.json` therefore retains:

`"date": null`

while recording the booklet publication date separately.

## Dated event records

The source-local event records remain provenance/reference objects:

- `events/1971-03-29-assembly-interim-budget-reply.md`
- `events/1971-04-02-assembly-governors-address-reply.md`

The Council and Assembly references documented in the provenance ledgers establish historical source relationships but do not supply textual content to the reader-facing transcript or translation.

## Indexing rule

The booklet-level entry is intentionally **not** added to the root canonical dated speech table or `data/speeches.json` as though it were one complete Assembly speech.

The root README instead links the source package and explains the special indexing rule.

## Translation consequence — completed

The English translation follows the booklet's printed editorial order rather than being split into reconstructed House speeches.

Final translation state:

- Gate F: **58/58 pages complete**
- Gate G: **58/58 pages reviewed, 0 blocking issues**
- consolidated refinement: **34/34 decisions complete**
- final closure: **PASS**
- English: **verified against the verified booklet Tamil**
- Official Report wording imported: **none**

## Final representation state

- controlling booklet transcription: **complete / verified**
- House/date research: **complete for all four underlying reply events**
- Unit 1 provenance ledger: **complete**
- Unit 2 provenance ledger: **complete**
- Official Reports: **reference only**
- reconstructed dated House transcripts: **intentionally not created**
- booklet-level `speeches/1971/1971-namathu-nilai/` entry: **created / complete / verified**
- English: **complete / verified**

This file now records the implemented representation rather than the superseded pre-implementation state.
