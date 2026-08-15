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

- Gate F canonical working translation: **Batches 1–7 merged**
- canonical translated source/scan pages: **241–275**
- canonical corresponding printed pages: **240–274**
- canonical completed English pages: **35/37**
- canonical Batch-7 merge checkpoint: `673265033d6618c173ca3e03927cc714f1747ee7`
- Gate F final Batch 8: **translation complete in staging — source pp.276–277 / printed pp.275–276 — 2 pages**
- Batch-8 staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch8-pp276-277.md`
- Batch-8 staging commit: `435add96dd85cd8a618636bbc4b90e4030deb9de`
- Batch-8 unresolved translation questions: **0**
- Speech-8 boundary: **ends at source p.277; source p.278 begins Speech 9; no spillover**
- English status: **in progress, not verified**
- Gate G: **not started**

Gate F uses only the final verified Tamil and preserves source-page correspondence, interventions, names, figures, embedded printed English, humour/context and source historical/factual claims without silent correction.

Final Batch 8 preserves the remaining printed High Court quotation; `8-ஏ`; the `டாமின்` / TAMIN public-auction passage; Kalaignar's closing; the Speaker → `திரு. சோ. பாலகிருஷ்ணன்` intervention; the source figures 5,000 acres / Rs.29 / Rs.429 / Rs.1½ crore / roughly Rs.400; and the final `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay, represented as salt-pan (*uppalam*) / *appalam* so the sound-play is not lost.

## Exact next activity — close Gate F, then begin Gate G

1. Fetch current canonical `translation.md` and staged `gate-f-batch8-pp276-277.md` immediately before editing.
2. Merge source-page sections **276–277** after canonical source p.275.
3. Update only the Gate-F working note as needed to say Gate F covers **source pp.241–277 / printed pp.240–276, 37/37 pages** and is complete.
4. Inspect the canonical commit/diff carefully to ensure Batches 1–7 were not accidentally changed.
5. If clean, reconcile metadata and README to Gate F **complete — 37/37**, completed source pp.241–277 / printed pp.240–276, next source page null, unresolved translation questions **0**; remove the pending-batch record.
6. Delete `gate-f-batch8-pp276-277.md` after successful canonical merge.
7. Gate F completion does **not** make English verified. Set Gate F complete while keeping translation unverified and Gate G not-started until the separate fidelity review begins.
8. Then begin **Gate G — full-speech English fidelity review against the final verified Tamil**, preferably in bounded batches with corrections documented and canonical diffs inspected.
9. Do not start Speech 9 until Speech 8 has completed Gate G and Gate H unless the user explicitly changes priority.
