# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English must be translated from and verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

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
- locked scan range: **199–240**
- locked printed range: **198–239**
- mapped pages: **42**
- Gate C: **complete — 42/42**
- Gate D: **passed**
- Gate E: **passed — 42/42 pages verified against scan**
- cumulative Gate-E corrections: **5**
- unresolved/`[REVIEW]`: **0**
- Tamil status: **verified against scan**
- English Gate F: **unblocked, not started**
- English Gate G: **not started**

## Gate E history

### Batch 1 — passed

Audited **scan pp.199–213 / printed pp.198–212**. Three canonical corrections were applied in commit `4c42c979f087a78cdaeef3e96a12506bcdd7693e`:

1. p.202 `விற்கப்படுகின்ற` → `விற்கப்படுகிற`;
2. p.205 `தெரிவித்து உண்மை` → `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கின்றேன்` → `சுட்டிக் காட்டியிருக்கிறேன்`.

### Batch 2 — passed

Audited **scan pp.214–228 / printed pp.213–227**. Two canonical corrections were applied in transcript commit `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693`:

1. p.214 Hyundai allotment `552 ஏக்கர்` → `532 ஏக்கர்`;
2. p.227 `புயூஜிகுரா லிமிடெட்` → `ப்யூஜிகுரா லிமிடெட்`.

### Batch 3 — passed

Audited **scan pp.229–240 / printed pp.228–239** directly against rendered scan images. No additional definite canonical correction was required. The p.240 closing sequence and full printed `THIRU B. VENKATASAMY` intervention were directly checked; scan p.241 / Speech 8 was excluded.

## Full Gate-E closure — passed

The separate closure check confirmed:

- the three bounded batches collectively cover exactly **scan pp.199–240 / printed pp.198–239**, 42/42 pages;
- all five logged corrections are present in canonical `transcript.md`;
- unresolved/`REVIEW` readings are **0**;
- source-page structure remains the exact locked **199–240** sequence;
- no p.241 marker or Speech-8 heading/date spillover exists;
- p.199 opening heading/date/speaker label is intact;
- p.240 Speaker → `THIRU B. VENKATASAMY` → Tamil follow-up → Kalaignar final-reply sequence is intact;
- audited printed-English passages remain represented.

Tamil therefore satisfies the repository definition of **verified**.

Gate-E closure checkpoints:

- metadata verified/unblock Gate F: `0e09cc6344f1b3295dba1402340fd716beb6cedc`
- README closure: `b861a17e8ca9901694508927e65586571abad033`
- source notes closure: `c9585b731daa4a55b5fec9d2d1b369dcba5e946d`
- verification log closure: `0fdbeb155f73b059dd5d98c9eb4547f9c7ee21f1`

## Exact next activity — Speech 7 Gate F English translation

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover and the current `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md`.
2. Inspect Speech 6 only as the released translation-structure reference (`translation.md`, canonical English placement, metadata and verification trail); do not modify Speech 6.
3. Use **only the final verified Speech-7 Tamil** as the translation source. Do not translate OCR or an earlier draft.
4. Preserve source-page correspondence **199–240** in the English working file.
5. Preserve argumentative sequence, parliamentary context, speaker/intervention changes, quoted/printed English, names, figures, dates, percentages, money, units and technical terminology.
6. Do not silently correct historical/factual claims made in the source. Translator clarification, if ever necessary, must be visibly distinguished.
7. For a long translation, use bounded Gate-F batches and record exact completed source pages and continuation point after each batch.
8. Gate G remains required after the complete English first pass; do not mark English verified during Gate F.
9. Do not begin Speech 8.

### Minor transcript-note housekeeping

The Tamil source layer itself is verified and the authoritative status files now record Gate E as passed. The short archival note at the top of `transcript.md` still contains its earlier first-pass status wording because the canonical source body was not rewritten during the closure-only status pass. Refresh that note to the verified wording when the canonical transcript is next safely rewritten/merged; do not alter any verified Tamil source text while doing so.

## New-window source requirement

The controlling PDF is not required merely to translate the already verified Tamil. If a Tamil source-fidelity question arises during translation, return to the controlling scan; do not resolve it from outside knowledge.

## End-of-handoff state

Speeches 1–6 remain fully released and untouched. Speech 7 Tamil is **verified against scan pp.199–240** with **5 Gate-E corrections and 0 unresolved readings**. **English Gate F is now the exact next activity.** Do not begin Speech 8.
