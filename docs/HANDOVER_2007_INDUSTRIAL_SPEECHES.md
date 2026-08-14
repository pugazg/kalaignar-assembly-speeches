# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English must be translated from and later verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Locked map: `sources/2007-industrial-speeches/mapping.md`

## Released anthology state

Speeches **1–6** are fully released with verified Tamil and verified English. Leave them untouched absent a separately justified correction.

## Active unit — Speech 7

- source label: `உரை : 7`
- date: `14.05.1998`
- canonical ID: `1998-05-14-industries-debate`
- scan range: **199–240**
- printed range: **198–239**
- mapped pages: **42**
- Tamil Gate C: **complete**
- Tamil Gate D: **passed**
- Tamil Gate E: **passed — 42/42 verified against scan**
- Gate-E corrections: **5**
- Tamil unresolved/`[REVIEW]`: **0**
- Tamil status: **verified**
- English Gate F: **in progress — pp.199–218 translated, 20/42 pages**
- English Gate G: **not started**
- unresolved translation questions: **0**

## Gate E closure

The full Gate-E closure passed. The five canonical corrections present in verified Tamil are:

1. p.202 `விற்கப்படுகிற`;
2. p.205 `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கிறேன்`;
4. p.214 Hyundai allotment `532 ஏக்கர்`;
5. p.227 `ப்யூஜிகுரா லிமிடெட்`.

Closure checkpoints:

- metadata: `0e09cc6344f1b3295dba1402340fd716beb6cedc`
- README: `b861a17e8ca9901694508927e65586571abad033`
- source notes: `c9585b731daa4a55b5fec9d2d1b369dcba5e946d`
- verification log: `0fdbeb155f73b059dd5d98c9eb4547f9c7ee21f1`

## Gate F English progress

English working file: `speeches/1998/1998-05-14-industries-debate/translation.md`.

- Batch 1: source pp.199–203 — complete.
- Batch 2: source pp.204–208 — complete.
- Batch 3: source pp.209–213 — complete.
- Batch 4: source pp.214–218 — complete and merged into canonical `translation.md`.
- Total translated: **20/42 pages**.
- Exact continuation: **source/scan p.219 / printed p.218**.

Batch 4 preserves the p.213→214 M.R.L. oil-refinery continuation, 250 MW oil-residue proposal, SIPCOT complex figures, verified Hyundai `532 acres`, investment/export data, Business Today `Objective / Perception / Rank` wording, and FDI figures/argument. A concurrent SHA change initially prevented the merge, so pp.214–218 were staged in `gate-f-batch4-pp214-218.md`; the batch was subsequently merged safely into current canonical `translation.md` without overwriting pp.199–213.

Current Gate-F checkpoints:

- Batch-4 staged translation: `3ebb821cb1ba435efc2cb0adf2662143feca71a1`
- canonical Batch-4 merge: `ce433f91838e31220e5a04e14c2fb6a82a77cb20`
- metadata after Batch 4: `e67e9eafe32aac2a1314b944bf25d65c01de9a6d`
- README after Batch 4: `a191610a09f2f14769a96dbd6f6d08a96a64c4a0`

## Exact next activity — Speech 7 Gate F Batch 5

1. Continue from current canonical `translation.md`; do not restart Gate F.
2. Translate only from final verified Tamil.
3. Translate bounded source/scan **pp.219–223 / printed pp.218–222**.
4. Preserve source-page correspondence, names, initials, dates, figures, percentages, monetary amounts, acreage/units, project/company names, technical terms, parliamentary context and printed English.
5. Preserve the p.218→219 continuation and any later cross-page continuations exactly enough to remain source-faithful.
6. Do not silently correct source claims or unusual company/name forms.
7. Record unresolved translation questions explicitly rather than guessing.
8. After Batch 5, update `translation.md`, `metadata.json`, README/handover/prompt and set the next exact source page.
9. Gate F is a first pass only. Do not mark English verified until separate Gate G passes after all 42 pages are translated.
10. Do not begin Speech 8.

## Minor housekeeping

The verified Tamil body is authoritative. The short archival note at the top of `transcript.md` still carries pre-closure wording; refresh that note only when the file can be safely rewritten without altering verified Tamil source text.

## End-of-handoff state

Speech 7 Tamil is verified. English Gate F is active with **pp.199–218 complete**. Resume exactly at **p.219** for Batch 5, pp.219–223.
