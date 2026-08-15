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

- Gate F canonical working translation: **Batches 1–3 merged**
- canonical translated source/scan pages: **241–255**
- canonical corresponding printed pages: **240–254**
- canonical completed English pages: **15/37**
- Gate F Batch 4: **translation complete in staging — source pp.256–260 / printed pp.255–259 — 5 pages**
- Batch-4 staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch4-pp256-260.md`
- Batch-4 staging commit: `57279f22d23da9f285890db6b64ce8325eafea23`
- Batch-4 unresolved translation questions: **0**
- English status: **in progress, not verified**
- Gate G: **not started**

Gate F uses only the final verified Tamil and preserves source-page correspondence, interventions, names, figures, embedded printed English, humour/context and source historical/factual claims without silent correction.

Batch 4 covers pp.256–260: Alangulam cement factory; Ranipet and Hosur SIPCOT industrial complexes; 1989–90 industries; the 1991–96 and 1996–99 investment/employment comparison; Hyundai, Mitsubishi Lancer, Ford and the Irungattukottai component-factory list; S.K.M. Egg Products / Mayilsamy Gounder–Mayilanandam passage; Thapar DuPont; and Asian Lighting. The translation deliberately preserves source-supported anomalies rather than correcting them, including p.257 `Rs. 1.125 crore` followed by p.258 `Rs. 1,125 crore`.

## Exact next activity — merge Batch 4, then begin Batch 5

1. Fetch current canonical `translation.md` immediately before editing.
2. Merge the completed staged Batch 4 sections for source pp.256–260 after source p.255.
3. Update only the Gate-F working note from 15/37 through p.255 to **20/37 through p.260**.
4. Inspect the resulting commit/diff for accidental changes to Batches 1–3.
5. If clean, reconcile metadata and README to canonical Gate F **20/37**, completed source pp.241–260 / printed pp.240–259, next source page **261**, unresolved translation questions **0**, and remove `pending_gate_f_batch`.
6. Delete `gate-f-batch4-pp256-260.md` after successful canonical merge.
7. Then proceed to **Gate F Batch 5 — source/scan pp.261–265 / printed pp.260–264**.
8. Do not mark English verified; Gate G remains separate after Gate F completes all 37 pages.
