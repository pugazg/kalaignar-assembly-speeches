# Next-chat prompt — Speech 8 Gate F final merge / Gate G start / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Tamil Gates C–E are complete and Tamil is verified against the controlling scan. Gate F Batches 1–7 are canonically merged. Final Gate F Batch 8 has been fully translated in a staging file and awaits canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current `speeches/1999/1999-04-29-industries-debate/metadata.json`, `README.md`, `translation.md`, `gate-f-batch8-pp276-277.md`, and canonical `transcript.md`.
5. Use the **final verified Tamil** in canonical `transcript.md` as the sole textual authority for English fidelity work.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan/source pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E: **passed — 37/37 pages**
- Gate-E cumulative corrections: **29**
- unresolved Tamil readings: **0**
- Tamil status: **verified against scan**
- Gate F canonical: **Batches 1–7 merged, source pp.241–275 / printed pp.240–274, 35/37 pages**
- canonical Batch-7 merge checkpoint: `673265033d6618c173ca3e03927cc714f1747ee7`
- final Gate F Batch 8: **translation complete in staging, source pp.276–277 / printed pp.275–276, 2 pages**
- staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch8-pp276-277.md`
- staging commit: `435add96dd85cd8a618636bbc4b90e4030deb9de`
- Batch-8 unresolved translation questions: **0**
- Speech-8 ending confirmed at source p.277; p.278 begins Speech 9; **no Speech-9 spillover**
- Gate G: **not-started**

## Exact next activity

First close Gate F canonically, then begin Gate G.

1. Fetch current canonical `translation.md` and staged `gate-f-batch8-pp276-277.md` immediately before editing.
2. Append source-page sections **276–277** from the staging file after canonical source p.275.
3. Change the Gate-F working note only as needed to state that Gate F covers **source pp.241–277 / printed pp.240–276, 37/37 pages**, and that Gate F is complete while English remains unverified.
4. Inspect the canonical commit/diff to ensure Batches 1–7 were not accidentally changed.
5. Reconcile metadata and README to Gate F `complete`, completed source pp.241–277 / printed pp.240–276, 37/37 pages, next source page null, unresolved translation questions **0**; remove the pending-batch record.
6. Delete `gate-f-batch8-pp276-277.md` after a clean merge.
7. Do **not** mark translation `verified`; Gate G is a separate full-speech fidelity review.
8. Begin Gate G against the final verified Tamil. Use bounded review batches, compare Tamil and English page-by-page, record definite corrections, and inspect canonical diffs before advancing verified coverage.
9. Preserve printed English passages exactly where they were intentionally retained in Gate F. Do not silently modernise or fact-correct source claims during Gate G.
10. Do not start Speech 9 until Speech 8 completes Gate G and Gate H unless the user explicitly changes priority.

Final Batch 8 begins on source p.276 with the printed High Court quotation `.... the money due to the Government has been siphoned off by them...` and ends on p.277 with the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay after the So. Balakrishnan intervention.
