# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1981/1981-04-16-industries-debate/`

Treat those files as controlling instructions. The scan image is authoritative; OCR is not canonical.

## Current state

Speech 1 (`1963-03-21-industries-debate`) is fully released with verified Tamil and English and must remain untouched.

Speech 2:

- Source label: `உரை : 2`
- Printed date: `16.04.1981`
- Canonical ID: `1981-04-16-industries-debate`
- Full scan range: **27–61**
- Printed pages: **26–60**
- Tamil status: **verified**
- Unresolved Tamil readings: **none**
- English status: **verified**
- English translation + fidelity commit: `9cf3b58fe6530089c8ef08206ceb392261f14d6a`

The complete English translation appears after the verified Tamil in `transcript.md`, with source-page headings **27–61**. A separate Gate-G page-by-page fidelity review against the final verified Tamil has passed.

Root README and `data/speeches.json` have **not yet been updated** for Speech 2.

## Next action — Gate H release/index

Proceed directly with **Gate H for Speech 2**.

1. Read the current root `README.md` and `data/speeches.json`.
2. Follow the existing released-speech schema used for Speech 1 and the verified 1970 entry; do not invent fields.
3. Add/release `1981-04-16-industries-debate` with **Tamil verified** and **English verified** statuses and the appropriate canonical links/metadata.
4. Validate `data/speeches.json` after editing.
5. Do not modify Speech 2 canonical transcript/source files unless a concrete release-blocking inconsistency is found.
6. Do not begin Speech 3 in the same release commit.

After Gate H is complete, the next mapped speech is:

- Speech 3
- printed date `03.05.1989`
- canonical ID `1989-05-03-industries-debate`
- scan pp. **62–98** / printed pp. **61–97**

Speech 3 should then begin with bounded Tamil first-pass transcription. English remains blocked until Speech 3 passes its Tamil audit and strict verification gates.

At the end provide an exact handover with files changed, Speech 2 release status, commit SHA, and the exact Speech 3 first-pass starting range.

---
