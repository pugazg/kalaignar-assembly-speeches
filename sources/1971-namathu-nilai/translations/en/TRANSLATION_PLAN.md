# நமது நிலை — booklet-only English translation plan

## Status

**GATE F COMPLETE — GATE-G PAGE REVIEW COMPLETE — CONSOLIDATED REFINEMENT PENDING.**

Reader-facing Tamil and English are maintained under:

`speeches/1971/1971-namathu-nilai/`

This source-side directory retains translation planning, progress, glossary and review records only. Do not maintain a second independent copy of the English here.

## Non-negotiable source rule

The only textual authority is the verified Tamil derived from:

`ACL-CPL_01726_நமது_நிலை.pdf`

Working Tamil source files remain under `../../transcription/`.

Tamil Nadu Legislative Assembly and Legislative Council Official Reports are **reference/provenance only**. They may not supply Tamil wording, English wording, missing passages, corrections, terminology or reconstructed House text.

If any Tamil reading appears doubtful, re-check only `ACL-CPL_01726_நமது_நிலை.pdf`.

## Translation object

The reader-facing entry preserves the booklet's two printed speech units in published order:

| Scan pages | Printed pages | Reader-facing scope |
|---:|---:|---|
| 3–37 | 1–35 | Unit 1 — `நமது நிலை`, Governor-address reply compilation |
| 38–60 | 36–58 | Unit 2 — `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்` |

Scan pp.1–2 are source front matter. The booklet is an edited two-House witness; do not reconstruct separate Assembly/Council speeches.

## Translation objective

Produce and verify a faithful reading translation that preserves, as far as English permits:

- argumentative sequence and repetition;
- direct parliamentary address;
- headings and speaker changes;
- humour, irony, idiom and metaphor;
- names, dates, figures, money, percentages and units;
- printed English expressions and source-specific claims;
- booklet page order and source-page boundaries.

Do not modernise, fact-correct, harmonise with Official Reports or fill omissions from another source.

## Completed stages

### Gate F — first-pass population

All F batches are complete. Reader-facing English covers **58/58 speech pages, scan pp.3–60**.

### Gate G — page-by-page fidelity review

All nine Gate-G batches are complete:

- G1 pp.3–10 — complete
- G2 pp.11–18 — complete
- G3 pp.19–26 — complete
- G4 pp.27–34 — complete
- G5 pp.35–37 — complete
- G6 pp.38–44 — complete
- G7 pp.45–51 — complete
- G8 pp.52–58 — complete
- G9 pp.59–60 — complete

Gate-G result:

- speech pages reviewed: **58/58**
- blocking fidelity issues: **0**
- verified Tamil changes: **none**
- Official Report wording used: **none**
- non-blocking refinement candidates: **34**

Detailed findings and all 34 candidates are recorded in `TRANSLATION_REVIEW.md`.

## Consolidated refinement stage

The next stage is a single source-controlled pass over candidates 1–34 in `TRANSLATION_REVIEW.md`.

For every candidate:

1. compare the existing English only with the verified booklet Tamil and immediate booklet context;
2. revise `speeches/1971/1971-namathu-nilai/translation.md` only when the source supports a clearer or closer English rendering;
3. preserve ambiguity rather than resolving it from Assembly/Council Official Reports, outside editions or historical reconstruction;
4. record the final disposition for each candidate in `TRANSLATION_REVIEW.md`;
5. keep source-page markers, headings, figures and source order unchanged unless the verified Tamil itself proves an English fidelity error.

The high-priority candidate is scan p.57 `அறுத்துக்கொள்ள வேண்டும்`, currently rendered `wrest it free`; it must be reconsidered from booklet Tamil/context alone and may remain deliberately ambiguous if no stronger source-controlled resolution exists.

## Final closure check

After all 34 refinement decisions are completed:

- re-check 58/58 source-page markers and continuity;
- re-check headings and intervention labels;
- re-check names, dates, figures, money, percentages and units;
- confirm no content was added from Official Reports;
- update `PROGRESS.md`, `TRANSLATION_REVIEW.md`, reader metadata/README, source README and handover;
- only then may `verified_against_tamil` be set to `true` and English marked verified.

## Tamil lock

The six verified source transcription files remain frozen. Translation difficulty is not evidence for changing Tamil. A Tamil change is allowed only after a direct visual re-check of the controlling booklet scan proves the existing transcription wrong.

## Exact continuation point

Proceed with the **consolidated English refinement pass over candidates 1–34** recorded in `TRANSLATION_REVIEW.md`.
