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

- Gate F canonical working translation: **Batches 1–6 merged**
- canonical translated source/scan pages: **241–270**
- canonical corresponding printed pages: **240–269**
- canonical completed English pages: **30/37**
- canonical Batch-6 merge checkpoint: `8ebc4ee41b88888c70b10647cad46fa4fca8af86`
- Gate F Batch 7: **translation complete in staging — source pp.271–275 / printed pp.270–274 — 5 pages**
- Batch-7 staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch7-pp271-275.md`
- Batch-7 staging commit: `fc53f15e568f5b60a4de9d2b79653dd48c67b2ca`
- Batch-7 unresolved translation questions: **0**
- English status: **in progress, not verified**
- Gate G: **not started**

Gate F uses only the final verified Tamil and preserves source-page correspondence, interventions, names, figures, embedded printed English, humour/context and source historical/factual claims without silent correction.

Batch 7 covers pp.271–275: `தமிழ்நெட் 1999`, the Unicode Consortium and `Tamil Virtual University`; the 1,200-school / approximately 48,000-student computer-training scheme and the court's remarks; the transition to the granite-lease case; Rule 39 and Government Order No. 97 dated 8-3-1993; the source's 125 leases / 9 districts / 196.80 hectares / Rs.95 crore figures; and the High Court passages through p.275. Printed English judicial quotations are retained as printed, including the quotation split across pp.274–275.

## Exact next activity — merge Batch 7, then final Gate F Batch 8

1. Fetch current canonical `translation.md` and staged `gate-f-batch7-pp271-275.md` immediately before editing.
2. Merge source-page sections **271–275** after canonical source p.270.
3. Update only the Gate-F working note from 30/37 through p.270 to **35/37 through p.275**.
4. Inspect the resulting commit/diff for accidental changes to Batches 1–6.
5. If clean, reconcile metadata and README to canonical Gate F **35/37**, completed source pp.241–275 / printed pp.240–274, next source page **276**, unresolved translation questions **0**, and remove the pending-batch record.
6. Delete `gate-f-batch7-pp271-275.md` after successful canonical merge.
7. Then proceed to **final Gate F Batch 8 — source/scan pp.276–277 / printed pp.275–276**.
8. Preserve the remaining printed High Court quotation, the granite/TAMIN closing, the Speaker/Thiru So. Balakrishnan intervention, all figures and the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay faithfully.
9. After pp.276–277 are translated, Gate F may be complete at **37/37**, but English must still remain **not verified** until separate Gate G is performed.
