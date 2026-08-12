# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before transcription, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1981/1981-04-16-industries-debate/`

Treat them as controlling instructions. The scan image is authoritative; OCR is not canonical.

## Current state

Speech 1 (`1963-03-21-industries-debate`) is fully released with verified Tamil and English and must remain untouched.

Speech 2:

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Full PDF scan range: **27–61**
- Printed pages: **26–60**
- Folder: `speeches/1981/1981-04-16-industries-debate/`

### Already completed

Tamil first-pass transcription is complete for **scan pp.27–56 / printed pp.26–55**, in two 15-page batches.

- Source-page markers: **27–56 inclusive, 30 unique monotonic markers**
- Tamil status: **in-progress**
- Speech is still partial
- Pending first-pass pages: **57–61**
- Full-speech completeness audit has not begun
- Strict full-speech visual verification has not been completed
- Explicit unresolved-reading placeholders: none currently flagged; this is not a verification claim
- English translation is blocked / not started
- Do not update root release indexes while the speech is partial

Exact current ending on scan p.56:

`... தமிழ்நாட்டிலும் சில நிறுவனங்களில் தனியார் சிலர் தலைவர்களாக நியமிக்கப்`

Scan p.57 continues:

`பட்டிருக்கிறார்கள். இது ஒன்றும் புதியது அல்ல. திரு. டாண்டன்...`

## Next bounded batch

Proceed directly with the **final Tamil first-pass transcription of scan pp.57–61 / printed pp.56–60**.

Append to the existing `transcript.md`; do not redo pp.27–56 unless a concrete first-pass correction is identified from the scan.

Maintain/update:

```text
speeches/1981/1981-04-16-industries-debate/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
└── verification-log.md
```

## Rules

- Preserve printed wording, period spelling, punctuation, numerals, headings, speaker labels, interventions and printed English passages as far as legible.
- Normalise only physical line wrapping.
- Add `<!-- source-page: N -->` for every new PDF page.
- Do not silently correct source errors, grammar, historical claims or terminology.
- Mark genuinely unreadable text for review rather than guessing.
- Keep scan-page and printed-page numbering separate.
- Do not infer the speaker's historical office from general knowledge.

Mandatory sequence:

`Tamil first-pass → full-speech completeness audit → strict visual/source-fidelity verification → Tamil verified → English translation → English fidelity verification → release/index update`

After pp.57–61 are transcribed, the Tamil first pass will be complete, but do **not** immediately mark the speech `verified` and do **not** begin English translation. First run the full-speech completeness audit across pp.27–61; then perform the separate strict page-by-page visual/source-fidelity verification required by the repository workflow.

At the end give an exact handover with files changed, pages completed, continuation/end point, Tamil status, unresolved readings, translation status, commit SHA and exact next action.

---
