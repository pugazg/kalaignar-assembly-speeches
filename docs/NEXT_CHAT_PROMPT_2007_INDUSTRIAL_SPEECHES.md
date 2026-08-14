# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released anthology state

Speeches **1–5** are fully released with verified Tamil and verified English:

- Speech 1 — `1963-03-21-industries-debate`, scan pp.18–26;
- Speech 2 — `1981-04-16-industries-debate`, scan pp.27–61;
- Speech 3 — `1989-05-03-industries-debate`, scan pp.62–98;
- Speech 4 — `1990-04-18-industries-debate`, scan pp.99–135;
- Speech 5 — `1996-08-14-industries-debate`, scan pp.136–171.

Do not modify those released speeches absent a separately justified correction.

Speech 5 completed Gates C–H. Its final state is:

- Tamil: **verified**, 36/36 pages, scan pp.136–171 / printed pp.135–170;
- Gate-E corrections: **23**;
- unresolved Tamil readings: **0**;
- English: **verified**, 36/36 page sections;
- Gate-G corrections: **7**;
- Gate H: **passed**;
- root `README.md` and `data/speeches.json`: Speech 5 released/indexed.

## Active unit — Speech 6

- source label: `உரை : 6`;
- printed date: `23.04.1997`;
- canonical ID: `1997-04-23-industries-debate`;
- locked range: **scan pp.172–198 / printed pp.171–197**;
- total mapped scan pages: **27**;
- scan/printed relationship: **scan page = printed page + 1**;
- Gate A source preflight: **complete at anthology level**;
- Gate B structural mapping: **complete and locked**;
- Gate C Tamil first-pass transcription: **not started**;
- Gate D: **not started**;
- Gate E: **not started**;
- Gate F: **blocked until Tamil verification**;
- Gate G: **not started**;
- Gate H: **not started**.

## Exact next action — Speech 6 Gate C

Begin **Tamil first-pass transcription** from the controlling scan at **scan p.172 / printed p.171**.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, and `sources/2007-industrial-speeches/mapping.md` before writing.
2. Inspect the actual scan images; the scan image is authoritative. OCR/extracted text may only be a helper.
3. Confirm p.172 begins `உரை : 6`, `நாள் : 23.04.1997` before creating or populating the Speech-6 canonical files.
4. Use canonical folder `speeches/1997/1997-04-23-industries-debate/` and the standard five-file structure: `README.md`, `metadata.json`, `source-notes.md`, `transcript.md`, `verification-log.md`.
5. Preserve wording, spelling, punctuation, numerals, names, headings, speaker labels, interventions and printed English exactly as supported by the scan. Do not silently modernise or correct.
6. Use explicit `<!-- source-page: N -->` markers.
7. Work in a bounded first batch, preferably **scan pp.172–186 / printed pp.171–185**, unless the source has a natural internal stopping point earlier.
8. At the end of the batch record exact completed pages, continuation text, unresolved readings and commits in the Speech-6 tracking files and in the handover/next prompt.
9. Do not begin English translation until Gates D–E have passed for the complete Speech 6.

## Speech-5 Gate-H release commits

- machine-readable release index — `a3e6f1d61813c4c869ba5b59e8d09f4b1a20faa0`;
- root README speech index/repository state — `ae23f1d7f134928085e0e225780edb5c46b5064d`;
- Speech-5 README marked fully released — `8e20ca73d2209bca8b2f58c03497cb03a23b1857`;
- Speech-5 source notes Gate-H record — `88ba98f0c2537a2e5ac6eeea29b03cfae97b80d6`;
- Speech-5 verification log Gate-H closure — `f01689426bc22a892bc339595a94e3a7540f56a6`.

The Speech-5 `metadata.json` already consistently recorded Tamil and English as `verified`, so Gate H required no metadata schema change.
