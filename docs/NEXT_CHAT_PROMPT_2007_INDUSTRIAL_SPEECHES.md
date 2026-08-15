# Next-chat prompt — Speech 8 Gate F Batch 5 merge / Batch 6 / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Tamil Gates C–E are complete and Tamil is verified against the controlling scan. Gate F Batches 1–4 are canonically merged. Gate F Batch 5 has been fully translated in a staging file and awaits canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current `speeches/1999/1999-04-29-industries-debate/metadata.json`, `README.md`, `translation.md`, `gate-f-batch5-pp261-265.md`, and canonical `transcript.md`.
5. Use the **final verified Tamil** in canonical `transcript.md` as the sole textual source for English translation. Do not translate from OCR or an earlier draft.

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
- Gate F canonical: **Batches 1–4 merged, source pp.241–260 / printed pp.240–259, 20/37 pages**
- Gate F Batch 5: **translation complete in staging, source pp.261–265 / printed pp.260–264, 5 pages**
- staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch5-pp261-265.md`
- staging commit: `966a186de3014496649fc23b29b704504d163366`
- Batch-5 unresolved translation questions: **0**
- Gate G: **not-started**

## Exact next activity

First close Batch 5 canonically, then proceed to Batch 6.

1. Fetch current canonical `translation.md` and staged `gate-f-batch5-pp261-265.md` immediately before editing.
2. Append source-page sections **261–265** from the staging file after canonical source p.260.
3. Change the Gate-F working note only as needed to say Batches 1–5 cover **source pp.241–265 / printed pp.240–264, 25/37 pages**.
4. Inspect the canonical commit/diff to ensure Batches 1–4 were not accidentally changed.
5. Reconcile metadata and README to canonical completed source pp.241–265, printed pp.240–264, 25/37 pages, next source page **266**, unresolved translation questions **0**; remove the pending-batch record.
6. Delete `gate-f-batch5-pp261-265.md` after successful merge.
7. Continue **Gate F Batch 6 — source/scan pp.266–270 / printed pp.265–269** from the final verified Tamil.
8. Preserve source-page correspondence, parliamentary sequence, names, figures, dates, monetary values, company/technical names and printed English. Do not silently correct source claims.
9. English remains **in-progress, not verified** until all 37 pages complete Gate F and subsequently pass separate Gate G.

Batch 5 ends on source p.265 with the `Economic Times` lead-in dated 28-4-1999. Source p.266 begins with the printed English quotation: `Tamil Nadu followed closely by Gujarat has taken the lead...`.
