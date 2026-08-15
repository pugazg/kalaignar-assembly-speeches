# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated from the final verified Tamil, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter it while processing Speech 8.

## Active unit — Speech 8

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Tamil gates

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E: **passed — 37/37 pages directly verified against scan**
- cumulative Gate-E corrections: **29**
- unresolved Tamil readings: **0**
- Tamil status: **verified**
- canonical Gate-E completion checkpoint: `7ddf8745a4c3417750c0c7130ae20edb8b4cca62`

## English status

- Gate F canonical working translation: **Batches 1–5 merged**
- canonical translated source/scan pages: **241–265**
- canonical corresponding printed pages: **240–264**
- canonical completed English pages: **25/37**
- canonical Batch-5 merge checkpoint: `336291291d27d3144c8c2fd89b70a3363b2d3371`
- Gate F Batch 6: **translation complete in staging — source pp.266–270 / printed pp.265–269 — 5 pages**
- Batch-6 staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch6-pp266-270.md`
- Batch-6 staging commit: `a7c2cb03b9964720a34b5ad9c313d3aaba9b2bb7`
- Batch-6 unresolved translation questions: **0**
- English status: **in progress, not verified**
- Gate G: **not started**

Gate F uses only the final verified Tamil and preserves source-page correspondence, interventions, names, figures, embedded printed English, humour/context and source historical/factual claims without silent correction.

Batch 6 covers pp.266–270: the printed `Economic Times` quotations on 100-per-cent export-oriented units, including the source form `As against 3,503, cent per cent EOUS...`; the `Times of India` CDR quotations and Tamil explanation; Jones Long Wootten / `International Real Estates` / Chennai passage; the 13-9-1998 `Vikatan` editorial; information-technology development; 23,000 engineering graduates / more than 13,000 IT-related graduates / more than 22,000 `Software Professionals`; the separate department from 5-10-1998; `I.T. Task Force`, `(I.T.Policy)`, Siruseri 1,000-acre hardware/software park, `(I.T. Super Highway)`, TCS/Wipro/Infosys/Polaris and Worldtel / one-lakh-fifty-thousand employment. Printed English is retained rather than silently corrected.

## Exact next activity — merge Batch 6, then begin Batch 7

1. Fetch current canonical `translation.md` and staged `gate-f-batch6-pp266-270.md` immediately before editing.
2. Merge source-page sections **266–270** after canonical source p.265.
3. Update only the Gate-F working note from 25/37 through p.265 to **30/37 through p.270**.
4. Inspect the resulting commit/diff for accidental changes to Batches 1–5.
5. If clean, reconcile metadata and README to canonical Gate F **30/37**, completed source pp.241–270 / printed pp.240–269, next source page **271**, unresolved translation questions **0**, and remove the pending-batch record.
6. Delete `gate-f-batch6-pp266-270.md` after successful canonical merge.
7. Then proceed to **Gate F Batch 7 — source/scan pp.271–275 / printed pp.270–274**.
8. Do not mark English verified; Gate G remains separate after Gate F completes all 37 pages.
