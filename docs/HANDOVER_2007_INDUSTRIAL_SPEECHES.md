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
- English Gate G: **not started**

## Gate F English progress

Canonical `translation.md` currently contains Batches 1–5, source pp.199–223, **25/42 pages**.

- Batch 1: pp.199–203 — complete
- Batch 2: pp.204–208 — complete
- Batch 3: pp.209–213 — complete
- Batch 4: pp.214–218 — complete and canonical
- Batch 5: pp.219–223 — complete and canonical
- Batch 6: pp.224–228 — **translation complete and staged** in `speeches/1998/1998-05-14-industries-debate/gate-f-batch6-pp224-228.md`

Batch 6 was translated only from final verified Tamil and preserves source-page correspondence and the source’s printed/unusual company and project forms. It includes Saint-Gobain, P.V.C. Rexine, Bis-Phenol-A, Tamil Nadu Toll Road Management Company Ltd., the Biaxially Oriented Polypropylene project, Iljin Automotive, Makushta Aircondition India, Dynamatic, Marqube India, Mando Brake System, Pos Hyundai Steel Manufacturing India, the Maraimalai Nagar Optical Fibre Cable project with the verified `ப்யூஜிகுரா லிமிடெட்` reading represented as Fujikura Limited, MCC Scrab Agro Limited, Metal Halide Lamp, Tauraus Novelties Limited, Pioneer Breeding Farms and Frozen French Fries through p.228.

Batch-6 staged translation commit: `a9aaed05e8eff99d0566ee6a787df3cdbe71a30c`.

## Exact next activity

1. Safely merge `gate-f-batch6-pp224-228.md` into the current canonical `translation.md` after source page 223 without altering pp.199–223.
2. Confirm canonical page sequence is exactly pp.199–228 and that the p.223→224 boundary is intact.
3. Update `metadata.json`, Speech-7 README, this handover and `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md` to **30/42 canonical English pages**.
4. Remove the temporary staged Batch-6 file only after the canonical merge is confirmed.
5. Then set the next translation activity to Gate F Batch 7, source/scan pp.229–233 / printed pp.228–232.
6. English remains **in progress, not verified** until complete Gate F and separate Gate G.
7. Do not begin Speech 8.
