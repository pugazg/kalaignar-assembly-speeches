# Next-chat prompt — Speech 8 Gate E Batch 7 canonical merge / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C is complete at 37/37 pages, Gate D has passed, Gate E Batches 1–6 are canonically complete, and Batch 7 visual review is complete with one staged correction awaiting canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read `speeches/1999/1999-04-29-industries-debate/gate-e-batch7-pp271-275.md`.
5. Fetch current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
6. Use the controlling rendered scan as the authority for Tamil. OCR/extracted text is only a helper.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E Batches 1–6: **canonically complete — scan pp.241–270 / printed pp.240–269**
- canonical Gate-E verified pages: **30/37**
- canonical Gate-E applied corrections: **27**
- Batch 7 visual review: **complete — scan pp.271–275 / printed pp.270–274 — 5/5 pages**
- Batch 7 unresolved readings: **0**
- Batch 7 pending canonical corrections: **1**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

## Batch-7 staged correction

Scan p.274:

`ஏராளமான தொகைகளை லஞ்சம் செய்து கொண்டு` → `ஏராளமான தொகைகளை வசூல் செய்து கொண்டு`

The controlling scan clearly prints `வசூல் செய்து கொண்டு` in the Tamil court-summary sentence immediately before the first printed High Court English quotation. Scan pp.271–273 and p.275 required no other definite correction.

The p.270→271 and p.275→276 continuations have already been visually checked and are intact.

Staging file:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch7-pp271-275.md`

Staging commit: `f84f49652ac589c0310be4406e541f970e21a992`.

## Exact next activity — close Batch 7 safely

1. Merge exactly the p.274 correction into canonical `transcript.md`.
2. In the same canonical update, change only the archival status note from Gate E verified through scan pp.241–270 / printed pp.240–269 to **scan pp.241–275 / printed pp.240–274**.
3. Inspect the canonical commit diff. It must contain no unrelated Tamil changes.
4. After the diff is clean, update metadata, README, source notes and verification log to:
   - verified scan range **241–275**;
   - verified printed range **240–274**;
   - verified pages **35/37**;
   - cumulative Gate-E corrections **28**;
   - next verification scan page **276**;
   - unresolved readings **0**.
5. Remove `gate-e-batch7-pp271-275.md` after successful canonical merge and status closure.
6. Update handover and this prompt.
7. The next bounded visual activity is the final **Gate E Batch 8 — scan pp.276–277 / printed pp.275–276**.
8. Do not begin English until Gate E has passed all **37/37** Tamil pages.
