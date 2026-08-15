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

- Gate F canonical working translation: **Batches 1–4 merged**
- canonical translated source/scan pages: **241–260**
- canonical corresponding printed pages: **240–259**
- canonical completed English pages: **20/37**
- Gate F Batch 5: **translation complete in staging — source pp.261–265 / printed pp.260–264 — 5 pages**
- Batch-5 staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch5-pp261-265.md`
- Batch-5 staging commit: `966a186de3014496649fc23b29b704504d163366`
- Batch-5 unresolved translation questions: **0**
- English status: **in progress, not verified**
- Gate G: **not started**

Gate F uses only the final verified Tamil and preserves source-page correspondence, interventions, names, figures, embedded printed English, humour/context and source historical/factual claims without silent correction.

Batch 5 covers pp.261–265: Karur Yarn Links, Taurus Novelties, Sriram Auto Components, Ramanasekar Steels, the Salem SISCOL and Basin Bridge G.M.R. Vasavi projects; Saint-Gobain and the Irungattukottai project list; biotechnology/TIDEL/Pennar/SISCOL/Taramani projects; Ennore L.N.G. and Jayankondam power projects; total investment/employment figures; and the C.M.I.E. industrial-investment ranking through the `Economic Times` lead-in on p.265. Source-internal figures and forms are preserved rather than silently reconciled.

## Exact next activity — merge Batch 5, then begin Batch 6

1. Fetch current canonical `translation.md` and staged `gate-f-batch5-pp261-265.md` immediately before editing.
2. Merge source-page sections **261–265** after canonical source p.260.
3. Update only the Gate-F working note from 20/37 through p.260 to **25/37 through p.265**.
4. Inspect the resulting commit/diff for accidental changes to Batches 1–4.
5. If clean, reconcile metadata and README to canonical Gate F **25/37**, completed source pp.241–265 / printed pp.240–264, next source page **266**, unresolved translation questions **0**, and remove the pending-batch record.
6. Delete `gate-f-batch5-pp261-265.md` after successful canonical merge.
7. Then proceed to **Gate F Batch 6 — source/scan pp.266–270 / printed pp.265–269**.
8. Do not mark English verified; Gate G remains separate after Gate F completes all 37 pages.
