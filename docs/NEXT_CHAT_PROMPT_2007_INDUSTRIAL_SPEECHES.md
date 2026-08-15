# Next-chat prompt — Speech 8 Gate E Batch 5 canonical merge / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C is complete at 37/37 pages, Gate D has passed, Gate E Batches 1–4 are canonically complete, and Batch 5 visual review is complete but has one staged correction awaiting canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read `speeches/1999/1999-04-29-industries-debate/gate-e-batch5-pp261-265.md`.
5. Fetch the current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
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
- Gate E Batches 1–4: **canonically complete — scan pp.241–260 / printed pp.240–259**
- canonical Gate-E verified pages: **20/37**
- canonical Gate-E applied corrections: **25**
- Batch 5 visual review: **complete — scan pp.261–265 / printed pp.260–264 — 5/5 pages**
- Batch 5 unresolved readings: **0**
- Batch 5 pending canonical corrections: **1**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

## Batch-5 staged correction

Scan p.261:

`ஆட்டோமொபைல்` → `ஆட்டோ மொபைல்`

The controlling scan visibly prints the two words separately in the Sriram Auto Components entry. Scan pp.262–265 required no other definite correction.

The p.260→261 and p.265→266 continuations have already been visually checked and are intact.

Staging file:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch5-pp261-265.md`

Staging commit: `a1f1a9f7e2221cfd525b052ae440c3511c224237`.

## Exact next activity — close Batch 5 safely

1. Merge exactly the p.261 `ஆட்டோமொபைல்` → `ஆட்டோ மொபைல்` correction into canonical `transcript.md`.
2. In the same canonical update, change only the archival status note from Gate E verified through scan pp.241–260 / printed pp.240–259 to **scan pp.241–265 / printed pp.240–264**.
3. Inspect the canonical commit diff. It must contain no unrelated Tamil changes.
4. After the diff is clean, update metadata, README, source notes and verification log to:
   - verified scan range **241–265**;
   - verified printed range **240–264**;
   - verified pages **25/37**;
   - cumulative Gate-E corrections **26**;
   - next verification scan page **266**;
   - unresolved readings **0**.
5. Remove `gate-e-batch5-pp261-265.md` after successful canonical merge and status closure.
6. Update handover and this prompt.
7. The next bounded visual activity after Batch-5 closure is **Gate E Batch 6 — scan pp.266–270 / printed pp.265–269**.
8. Do not begin English until Gate E has passed all **37/37** Tamil pages.
