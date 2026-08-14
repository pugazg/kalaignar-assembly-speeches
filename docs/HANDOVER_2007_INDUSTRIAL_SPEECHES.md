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
- English Gate F: **in progress — pp.199–213 translated, 15/42 pages**
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
- Total translated: **15/42 pages**.
- Exact continuation: **source/scan p.214 / printed p.213**.

Batch 3 preserves the source’s awkward and repeated English/Tamil material without outside correction, including the repeated `Business India` passage, `Economic Intelligency Unit`, `India Uncaged`, `Seeking opportunities in the South`, the printed corruption quotation, public-sector undertaking list, Ranipet SIPCOT chronology, Hosur/Pudukkottai/Gummidipoondi figures, Neyveli `Third mine cut`, and the M.R.L. continuation.

Current Gate-F checkpoints:

- Batch-3 translation commit: `3fac44a6404bcc0304c4a486aaa3e82a5fca1fad`
- metadata after Batch 3: `59bd84a5d1757e708fa39bc496b18b2fa1b38aac`
- README after Batch 3: `1f739786aeac59c3fbc2e00b20d84060011a003e`

## Exact next activity — Speech 7 Gate F Batch 4

1. Continue from the existing `translation.md`; do not restart Gate F.
2. Translate only from final verified Tamil.
3. Translate bounded source/scan **pp.214–218 / printed pp.213–217**.
4. Preserve source-page correspondence, names, initials, dates, figures, percentages, monetary amounts, acreage/units, project/company names, technical terms, parliamentary context and printed English.
5. Do not silently correct source claims or unusual company/name forms.
6. Record unresolved translation questions explicitly rather than guessing.
7. After Batch 4, update `translation.md`, `metadata.json`, README/handover/prompt as needed, and set the exact continuation page.
8. Gate F is a first pass only. Do not mark English verified until separate Gate G passes after all 42 pages are translated.
9. Do not begin Speech 8.

## Minor housekeeping

The verified Tamil body is authoritative. The short archival note at the top of `transcript.md` still carries pre-closure wording; refresh that note only when the file can be safely rewritten without altering verified Tamil source text.

## End-of-handoff state

Speech 7 Tamil is verified. English Gate F is active with **pp.199–213 complete**. Resume exactly at **p.214** for Batch 4, pp.214–218.
