# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches`.

We are now moving from **structural mapping to Tamil transcription** for the attached source:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any transcription, fetch and read the current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- the existing verified speech structure under `speeches/1970/1970-09-09-no-confidence-motion/` as a format precedent

Treat those repository files as the controlling project instructions.

## Source facts already established

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: May 2007
- Actual PDF pages: **329**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- The source is a compilation of **10 separately dated Assembly speeches**.
- The complete source map and a second visual boundary re-check are already finished and locked in `mapping.md`.
- Do **not** repeat the 329-page structural mapping unless you find direct contradictory evidence in the scan.
- An earlier interface showed only the first 150 rendered pages; that was only a rendering/interface limit, not the PDF length.
- This attached PDF is the controlling source for this transcription work. The scan image is authoritative; OCR is not canonical.

## Start with Speech 1 only

- Source label: `உரை : 1`
- Printed date: `21.03.1963`
- Canonical ID: `1963-03-21-industries-debate`
- PDF scan pages: **18–26**
- Printed pages: **17–25**
- Target path: `speeches/1963/1963-03-21-industries-debate/`

Speech 1 is only nine scan pages, so complete the full Tamil first-pass transcription for pp.18–26 as one bounded unit. Do **not** continue into Speech 2 in the same unit.

## Required files

Create the canonical speech entry following the repository's existing structure:

```text
speeches/1963/1963-03-21-industries-debate/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
└── verification-log.md
```

## Transcription rules

- Preserve source wording, spelling, punctuation, numerals, headings, speaker labels, member interventions and printed English passages as far as the scan permits.
- Normalise only physical line wrapping into readable paragraphs.
- Use explicit source-page markers such as `<!-- source-page: 18 -->`.
- Do not silently correct apparent printer errors, historical claims, grammar or period spelling.
- If something is genuinely unreadable, mark it for review rather than guessing.
- Keep PDF scan page and printed page distinct in metadata/source notes.
- Do not infer the speaker's office/role from general knowledge when the source does not establish it.

## Audit gates

The sequence is mandatory:

`Tamil first-pass transcription → Tamil completeness audit → strict page-by-page visual/source-fidelity verification → Tamil verified → English translation → English fidelity verification`

For this next session, begin with the complete Tamil first pass for Speech 1 and then its completeness audit. If you proceed to the stricter Tamil visual verification, document it accurately in `verification-log.md` and change status only when that audit is genuinely complete.

**English translation must remain blocked until the Tamil audit/verification gates required by the repository workflow are complete.** Do not translate early.

## Git discipline

- Work from the current `main` branch.
- Do not modify the already verified 1970 speech or unrelated sources.
- Push bounded, descriptive commits.
- Update only index/release files when the workflow says the speech is ready for that status.
- At the end, give me an exact handover: files changed, source pages completed, Tamil status, unresolved readings, translation status, commit SHA, and the exact next action.

Please start by confirming the repository/source state from the files above, then proceed directly with Speech 1 pp.18–26.

---
