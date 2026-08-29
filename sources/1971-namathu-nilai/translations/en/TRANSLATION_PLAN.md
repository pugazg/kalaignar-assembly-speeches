# நமது நிலை — booklet-only English translation plan

## Status

**ACTIVE — speech-folder population has started.**

Reader-facing Tamil and English are now maintained under:

`speeches/1971/1971-namathu-nilai/`

This source-side directory retains translation planning, progress and glossary records only. Do not maintain a second independent copy of the English here.

## Non-negotiable source rule

The only textual authority is the verified Tamil derived from:

`ACL-CPL_01726_நமது_நிலை.pdf`

Working Tamil source files remain:

- `../../transcription/scan-001-010.md`
- `../../transcription/scan-011-020.md`
- `../../transcription/scan-021-030.md`
- `../../transcription/scan-031-040.md`
- `../../transcription/scan-041-050.md`
- `../../transcription/scan-051-060.md`

Tamil Nadu Legislative Assembly and Legislative Council Official Reports are **reference/provenance only**. They may not supply Tamil wording, English wording, missing passages, corrections, terminology or reconstructed House text.

If any Tamil reading appears doubtful, re-check only `ACL-CPL_01726_நமது_நிலை.pdf`.

## Translation object

The reader-facing speech entry preserves the booklet's two printed speech units in their published order:

| Scan pages | Printed pages | Reader-facing scope |
|---:|---:|---|
| 3–37 | 1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| 38–60 | 36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

Scan pp.1–2 are source front matter and remain documented in the source package; the `speeches/` entry begins with the speech text on scan p.3.

The booklet is an edited two-House witness. Do not reconstruct separate Assembly/Council speeches.

## Translation objective

Produce a faithful reading translation, preserving as far as English permits:

- argumentative sequence and repetition;
- direct parliamentary address;
- headings and speaker changes;
- humour, irony, idiom and metaphor;
- names, dates, figures, money, percentages and units;
- printed English expressions and source-specific claims;
- booklet page order and source-page boundaries.

Do not modernise, fact-correct, harmonise with Official Reports or fill omissions from another source.

## Page fidelity

Use the same markers as the verified Tamil:

```html
<!-- source-page: 3 -->
```

These markers refer only to physical pages of `ACL-CPL_01726_நமது_நிலை.pdf`.

## Reader-facing files

Actual working text lives in:

- `../../../../speeches/1971/1971-namathu-nilai/transcript.md`
- `../../../../speeches/1971/1971-namathu-nilai/translation.md`

Supporting metadata lives beside them in that speech folder.

The source-side `PROGRESS.md` and `GLOSSARY.md` remain the workflow-control records.

## Gate-F population batches

Proceed in bounded source order:

- **F1a:** scan pp.3–5 — complete
- **F1b:** scan pp.6–10
- **F2:** scan pp.11–18
- **F3:** scan pp.19–26
- **F4:** scan pp.27–34
- **F5:** scan pp.35–37 — complete Unit 1
- **F6:** scan pp.38–44
- **F7:** scan pp.45–51
- **F8:** scan pp.52–58
- **F9:** scan pp.59–60 — complete Unit 2

Total reader-facing speech coverage: **58 scan pages, pp.3–60**.

Each batch must update both `transcript.md` and `translation.md` in the speech folder and then update `PROGRESS.md`.

## Gate-G English fidelity review

After Gate F covers scan pp.3–60, perform a separate page-by-page review against the verified booklet Tamil. Check:

- 58/58 speech-page coverage;
- no omitted or duplicated Tamil content;
- no unsupported English additions;
- page/batch continuations;
- headings, interventions and speaker labels;
- names, initials, dates, figures and units;
- rhetorical force and idioms;
- no imported Official Report wording.

Record that review in `TRANSLATION_REVIEW.md` before marking English verified.

## Tamil lock

The six verified source transcription files remain frozen. Translation difficulty is not evidence for changing Tamil. A Tamil change is allowed only after a direct visual re-check of the controlling booklet scan proves the existing transcription wrong.

## Exact continuation point

Continue the speech-folder entry from **scan p.6**:

1. append verified Tamil scan pp.6–10 to `speeches/1971/1971-namathu-nilai/transcript.md`;
2. translate those same pages into `translation.md` using only that Tamil;
3. record any recurring English decisions in `GLOSSARY.md`;
4. update `PROGRESS.md`;
5. do not use external legislative wording.
