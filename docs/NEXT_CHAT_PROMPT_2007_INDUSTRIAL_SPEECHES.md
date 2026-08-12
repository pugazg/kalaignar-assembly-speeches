# Next-chat prompt — 2007 industrial speeches transcription

Copy the text below into a new ChatGPT chat and attach the same source PDF.

---

I am continuing my GitHub project `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Before doing any work, read current `main` versions of:

- `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `sources/2007-industrial-speeches/mapping.md`
- `speeches/1989/1989-05-03-industries-debate/`

Treat those files as controlling instructions. The scan image is authoritative for the Tamil source layer; the final Gate-E-verified Tamil is authoritative for English fidelity. OCR is not canonical.

## Completed released work

Speech 1 (`1963-03-21-industries-debate`) and Speech 2 (`1981-04-16-industries-debate`) are fully released with verified Tamil and verified English and must remain untouched unless separately requested.

## Current active work — Speech 3

- Source label: `உரை : 3`
- Printed date: `03.05.1989`
- Canonical ID: `1989-05-03-industries-debate`
- Full scan range: **62–98**
- Printed pages: **61–97**
- Gate C: **complete**
- Gate D: **passed**
- Gate E: **passed**
- Tamil status: **verified**
- Explicit unresolved Tamil readings: **0**
- Gate F: **complete**
- English status: **complete-unverified**
- Gate G: **next / not started**
- Gate-F transcript commit: `cc844648fa3c220b2c721f4177d6e572f58d66a8`
- Gate-F final verification-log commit: `25469c85158c56cca96e95c8a93b45326f5346ea`

Gate F translated the complete final verified Tamil and appended the English layer after it in `transcript.md`. The English has explicit `### Source page N` correspondence for exactly **37 pages, 62 through 98**, and retains the parliamentary sequence, speaker changes/interventions, quotations, figures and technical terminology. It is not yet verified.

Source forms and inconsistencies that must remain visible in the fidelity review include:

- `1986-86-ல்` in the Gujarat investment comparison;
- `அசோசியேட் செக்டரி`, reflected in the provisional English as the source term “Associate Sectary”;
- the p.92 sequence printing `547 கோடி` and later `541 கோடி` before the `721 கோடி` revised estimate;
- the repeated `வலியுறுத்தி` / `கேட்டுக்கொண்டதன் பேரில்` wordplay on p.93;
- printed laughter and desk-thumping markers and all final interventions.

## Next action — Speech 3 Gate G English fidelity verification

Perform a strict page-by-page fidelity review of the complete English translation against the **final verified Tamil** for source pages **62–98**.

1. Fetch/read current Speech 3 `transcript.md`, `metadata.json`, `source-notes.md`, `verification-log.md` and `README.md` from `main` before editing.
2. Compare each English `### Source page N` section directly against the corresponding verified Tamil `<!-- source-page: N -->` section.
3. Check every page for completeness and fidelity of meaning, speaker attribution, parliamentary interventions, quotations, names and initials, dates, numerals, percentages, monetary values and units, industrial terminology and page-transition continuity.
4. Verify that source anomalies and period terminology are preserved rather than silently corrected from external knowledge, especially `1986-86-ல்`, `அசோசியேட் செக்டரி`, the p.92 `547` / `541` inconsistency and the p.93 repeated wordplay.
5. Correct every concrete English fidelity discrepancy in `transcript.md` and document every correction in `verification-log.md`.
6. Confirm exactly **37** English source-page headings, unique and monotonic from **62 through 98**, with no omission, duplication or spillover into Speech 4.
7. Only after all 37 pages have been directly checked may English status become `verified`; update metadata/README/source notes accordingly.
8. After Gate G passes, proceed to Gate H release/index by updating the root README and `data/speeches.json` following the Speech 2 precedent.
9. Do not begin Speech 4 before Speech 3 Gate H is complete.

At the end, update `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` with the Gate-G corrections, English status, files changed, commit SHA and exact Gate-H action.

---
