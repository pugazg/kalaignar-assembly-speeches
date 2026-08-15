# Next-chat prompt — Speech 8 Gate F Batch 6 merge / Batch 7 / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Tamil Gates C–E are complete and Tamil is verified against the controlling scan. Gate F Batches 1–5 are canonically merged. Gate F Batch 6 has been fully translated in a staging file and awaits canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current `speeches/1999/1999-04-29-industries-debate/metadata.json`, `README.md`, `translation.md`, `gate-f-batch6-pp266-270.md`, and canonical `transcript.md`.
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
- Gate F canonical: **Batches 1–5 merged, source pp.241–265 / printed pp.240–264, 25/37 pages**
- Gate F Batch 6: **translation complete in staging, source pp.266–270 / printed pp.265–269, 5 pages**
- staging file: `speeches/1999/1999-04-29-industries-debate/gate-f-batch6-pp266-270.md`
- staging commit: `a7c2cb03b9964720a34b5ad9c313d3aaba9b2bb7`
- Batch-6 unresolved translation questions: **0**
- Gate G: **not-started**

## Exact next activity

First close Batch 6 canonically, then proceed to Batch 7.

1. Fetch current canonical `translation.md` and staged `gate-f-batch6-pp266-270.md` immediately before editing.
2. Append source-page sections **266–270** from the staging file after canonical source p.265.
3. Change the Gate-F working note only as needed to say Batches 1–6 cover **source pp.241–270 / printed pp.240–269, 30/37 pages**.
4. Inspect the canonical commit/diff to ensure Batches 1–5 were not accidentally changed.
5. Reconcile metadata and README to canonical completed source pp.241–270, printed pp.240–269, 30/37 pages, next source page **271**, unresolved translation questions **0**; remove the pending-batch record.
6. Delete `gate-f-batch6-pp266-270.md` after successful merge.
7. Continue **Gate F Batch 7 — source/scan pp.271–275 / printed pp.270–274** from the final verified Tamil.
8. Preserve source-page correspondence, parliamentary sequence, names, figures, dates, monetary values, company/technical names and printed English. Do not silently correct source claims.
9. English remains **in-progress, not verified** until all 37 pages complete Gate F and subsequently pass separate Gate G.

Batch 6 ends on source p.270 with the Worldtel passage promising one-lakh-fifty-thousand jobs and an internet-enabled Tamil Nadu. Source p.271 begins with the `தமிழ்நெட் 1999` / Unicode Consortium discussion.
