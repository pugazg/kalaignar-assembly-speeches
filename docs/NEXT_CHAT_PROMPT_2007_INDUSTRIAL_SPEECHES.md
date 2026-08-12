# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches`.

Continue the attached source:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any transcription, fetch and read the current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- the completed Speech 1 entry under `speeches/1963/1963-03-21-industries-debate/`
- the verified 1970 entry under `speeches/1970/1970-09-09-no-confidence-motion/` as a structural precedent

Treat those repository files as the controlling project instructions.

## Source facts already established

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: May 2007
- Actual PDF pages: **329**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- The source contains **10 separately dated Assembly speeches**.
- The complete map and a second visual boundary re-check are finished and locked in `mapping.md`.
- Do **not** repeat the 329-page structural mapping unless direct contradictory evidence appears in the scan.
- The scan image is authoritative; OCR is not canonical.

## Completed work

Speech 1 — `1963-03-21-industries-debate`, scan pp.18–26 — is fully released:

- Tamil: **verified**
- unresolved Tamil readings: **none**
- English: **verified**
- indexed in the root README and `data/speeches.json`

Do not modify Speech 1 while processing Speech 2 unless explicitly requested.

## Proceed with Speech 2

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Full PDF scan range: **27–61**
- Printed pages: **26–60**
- Target path: `speeches/1981/1981-04-16-industries-debate/`

Speech 2 is 35 scan pages. Start with a bounded Tamil first-pass batch of **PDF scan pp.27–41**. Do not continue beyond p.41 merely to complete a paragraph if the page itself provides a safe continuation point; record the exact continuation text in the handover.

Create/maintain:

```text
speeches/1981/1981-04-16-industries-debate/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
└── verification-log.md
```

## Transcription rules

- Preserve source wording, spelling, punctuation, numerals, headings, speaker labels, member interventions and printed English passages as far as the scan permits.
- Normalise only physical line wrapping into readable paragraphs.
- Use explicit source-page markers such as `<!-- source-page: 27 -->`.
- Do not silently correct printer errors, historical claims, grammar or period spelling.
- If something is genuinely unreadable, mark it for review rather than guessing.
- Keep PDF scan page and printed page distinct in metadata/source notes.
- Do not infer the speaker's office/role from general knowledge when the source does not establish it.

## Status and audit gates

The mandatory sequence is:

`Tamil first-pass transcription → Tamil completeness audit → strict page-by-page visual/source-fidelity verification → Tamil verified → English translation → English fidelity verification → release/index update`

Because this is only the first batch of Speech 2, Tamil status must remain **in-progress** after pp.27–41. Do not label Speech 2 `transcribed`, `reviewed` or `verified` prematurely.

English translation must remain blocked until the **entire** Speech 2 Tamil transcription, completeness audit and strict visual verification have been completed.

## Git discipline

- Work from current `main`.
- Do not modify Speech 1, the verified 1970 speech, or unrelated sources.
- Push bounded descriptive commits.
- At the end give an exact handover: files changed, scan pages completed, exact continuation point, partial/complete state, Tamil status, unresolved readings, translation status, commit SHA, and exact next action.

Proceed directly with Speech 2, Tamil first-pass transcription, scan pp.27–41.

---
