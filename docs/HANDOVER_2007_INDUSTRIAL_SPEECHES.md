# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Active unit — Speech 7

- source label: `உரை : 7`
- date: `14.05.1998`
- canonical ID: `1998-05-14-industries-debate`
- scan range: **199–240**
- printed range: **198–239**
- Tamil Gate C: complete
- Tamil Gate D: passed
- Tamil Gate E: passed — **42/42 verified against scan**
- Gate-E corrections: **5**
- Tamil unresolved readings: **0**
- Tamil status: **verified**
- English Gate F: **complete — pp.199–240, 42/42 pages**
- English Gate G: **passed — full 42-page fidelity review complete**
- Gate-G corrections: **0**
- unresolved translation questions: **0**
- English status: **verified against final verified Tamil**

## Gate G English verification

The complete English `translation.md` was re-read against the final verified Tamil `transcript.md` across source pp.199–240. The review checked page correspondence and completeness, cross-page continuations, speaker changes/interventions, names and initials, dates, percentages, money, acreage, employment and megawatt figures, company/project/institution names, technical terminology, printed English, argument order, humour/context markers and the exact p.240 closing boundary.

The full review found:

- checked pages: **42/42**;
- missing/duplicate/reordered English pages: **0**;
- p.241 / Speech-8 spillover: **0**;
- unresolved translation questions: **0**;
- definite Gate-G corrections required: **0**.

Dedicated Gate-G record:

`speeches/1998/1998-05-14-industries-debate/translation-review.md`

Current checkpoints:

- Gate-F canonical completion: `8ce93472ccb01bb2efd41435d4745d3c97f9da1a`
- Gate-G review artifact: `acbfa87f6d806bcae98f51e4df7ad1709fc094ef`
- metadata after Gate G: `9bd37509faab5744c4f3b4bc840ebe394a5b6e3b`
- verification log after Gate G: `69dd7674401c3704bcf566efa76f80940e83c73e`
- README after Gate G: `2276060d962d0fd1811d1f97a86bd8d6fdb13e02`

## Exact next activity — Speech 7 Gate H / release canonicalisation

1. Read `docs/ARCHIVAL_WORKFLOW.md` and inspect the current Speech-7 entry before changing anything.
2. Reconcile the **verified English** into the canonical speech presentation required by the repository workflow. Do not alter the verified Tamil source layer.
3. Inspect `data/speeches.json` and the root README/speech index and add or update Speech 7 as appropriate, following existing repository conventions rather than inventing a new index shape.
4. Reconcile all status/source-path/page-range fields across `metadata.json`, Speech-7 README, `source-notes.md`, `verification-log.md`, `translation-review.md`, canonical transcript/translation presentation and repository indexes.
5. Confirm the source range remains exactly **199–240 / printed 198–239**, with no p.241 / Speech-8 spillover.
6. Leave Speech 7 release-ready and auditable.
7. Do not begin Speech 8 until Speech-7 Gate H is complete.
