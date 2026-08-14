# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English must be translated from and later verified against the **final verified Tamil**. Follow `docs/ARCHIVAL_WORKFLOW.md`.

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
- English Gate F canonical: **pp.199–228, 30/42 pages**
- English Gate G: **not started**

## Gate F English progress

Canonical `translation.md` currently contains Batches 1–6, source pp.199–228, **30/42 pages**.

- Batch 1: pp.199–203 — complete and canonical
- Batch 2: pp.204–208 — complete and canonical
- Batch 3: pp.209–213 — complete and canonical
- Batch 4: pp.214–218 — complete and canonical
- Batch 5: pp.219–223 — complete and canonical
- Batch 6: pp.224–228 — complete and canonical
- Batch 7: pp.229–233 — **translation complete and staged** in `speeches/1998/1998-05-14-industries-debate/gate-f-batch7-pp229-233.md`

Batch 7 was translated only from the final verified Tamil. It preserves source-page correspondence and the p.228→229 continuation. It covers PVC foamed sheets/artificial-wood products, Sriram Auto Components (Madras) Limited, Ramana Sekar Steels Limited, S.K.M. egg processing, the 33-factory progress summary, the M.S. Swaminathan/Siruseri biotechnology park announcement, motor-component and software venture-capital schemes, the `Global Village` passage, and the ITIT→TANITEC announcement through the p.233→234 continuation.

Batch-7 staged translation commit: `9f4757935c99acfb71d9195b4711c2060c086b55`.

No unresolved translation question was introduced. English remains in progress and unverified.

## Exact next activity

1. Safely merge `gate-f-batch7-pp229-233.md` into current canonical `translation.md` immediately after source p.228 without altering pp.199–228.
2. Confirm canonical page sequence is exactly pp.199–233 and that both p.228→229 and p.233→234 continuation boundaries are represented correctly.
3. Update `metadata.json`, Speech-7 README, this handover and `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md` to **35/42 canonical English pages**.
4. Remove the temporary Batch-7 staged file only after the canonical merge is confirmed.
5. Then set the next translation activity to **Gate F Batch 8: source/scan pp.234–238 / printed pp.233–237**.
6. English remains **in progress, not verified** until complete Gate F and separate Gate G.
7. Do not begin Speech 8.
