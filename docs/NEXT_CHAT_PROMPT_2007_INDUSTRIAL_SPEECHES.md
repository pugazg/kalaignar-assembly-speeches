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

### Tamil work completed

The Tamil first-pass transcription is complete for all scan pp.27–61. Gate D completeness passed with 35 unique monotonic page markers and no mapped page omitted or duplicated.

Gate E has also been completed: every scan page 27–61 was directly compared against the canonical Tamil. Nine additional first-pass discrepancies were corrected and documented in `verification-log.md`.

Current Tamil status is **`verified`**. Unresolved Tamil readings: **none**.

English translation has **not started**, but the verified-Tamil prerequisite is now satisfied. Root README and `data/speeches.json` must remain untouched until English is translated and separately verified.

## Next action — English translation

Proceed directly with the **complete English translation of Speech 2 from the verified Tamil only**.

Append the English layer after the complete Tamil transcription in `transcript.md`, following the established repository precedent:

```text
---
# English translation
> Translation note ...

### Source page 27
...

### Source page 28
...

...

### Source page 61
...
```

Translation rules:

- translate the verified Tamil, not OCR and not an earlier draft;
- preserve the source-page sequence 27–61;
- preserve parliamentary speaker changes/interventions and quoted material;
- preserve all names, numerals, dates, percentages, monetary amounts and technical terms consistently;
- do not silently correct factual or historical claims made in the source;
- do not infer a historical office not established by the source;
- where the Tamil layer already contains printed English passages, keep their source character clear rather than treating them as newly authored translator prose.

After the complete translation, perform a **separate English fidelity verification against the final verified Tamil, page by page**. Do not mark English `verified` before that check.

Only after English is verified should the root README and `data/speeches.json` be updated for release.

At the end provide an exact handover: pages translated, English fidelity status, Tamil status, unresolved issues, files changed, commit SHA, and exact next action.

---
