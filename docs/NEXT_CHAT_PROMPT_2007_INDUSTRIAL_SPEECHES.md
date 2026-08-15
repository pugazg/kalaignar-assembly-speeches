# Next-chat prompt — Speech 8 Gate E canonical closure / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C is complete at 37/37 pages, Gate D has passed, Gate E Batches 1–7 are canonically complete, and the final Batch 8 visual review is complete with one staged correction awaiting canonical merge. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read `speeches/1999/1999-04-29-industries-debate/gate-e-batch8-pp276-277.md`.
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
- Gate E Batches 1–7: **canonically complete — scan pp.241–275 / printed pp.240–274**
- canonical Gate-E verified pages: **35/37**
- canonical Gate-E applied corrections: **28**
- final Batch 8 visual review: **complete — scan pp.276–277 / printed pp.275–276 — 2/2 pages**
- Batch 8 unresolved readings: **0**
- Batch 8 pending canonical corrections: **1**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

## Final Batch-8 staged correction

Scan p.276, Speaker line:

`மாண்புமிகு எதிர்க்கட்சித் தலைவர்.` → `மாண்புமிகு எதிர்க் கட்சித் தலைவர்.`

The controlling scan clearly prints the spaced source form `எதிர்க் கட்சித் தலைவர்`. Scan p.277 required no definite correction.

The final visual audit also confirmed:

- p.275→276 judgment continuation is intact;
- p.276 printed High Court quotation, `8-ஏ`, `டாமின்`, speech close, applause marker, and Speaker transition are source-faithful apart from the staged Speaker-line spacing correction;
- p.276→277 Opposition Leader continuation is intact;
- p.277 figures `5,000`, `29`, `429`, `ஒன்றரை கோடி`, `400` and the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay are intact;
- p.277 ends Speech 8 after the final `(மேசையைத் தட்டும் ஒலி).`;
- p.278 was separately rendered and begins `உரை : 9`, `நாள் : 8.05.2000`.

Staging file:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch8-pp276-277.md`

Staging commit: `a0e45fd44f9da244c7e27f1a3c53736d6e996ab2`.

## Exact next activity — close Gate E safely

1. Merge exactly the p.276 Speaker-line correction into canonical `transcript.md`.
2. In the same canonical update, change only the archival note from Gate E verified through scan pp.241–275 / printed pp.240–274 to full **scan pp.241–277 / printed pp.240–276 — 37/37 pages**, and mark Tamil there as verified.
3. Inspect the canonical commit diff. It must contain no unrelated Tamil changes.
4. After the diff is clean, reconcile metadata, README, source notes and verification log to:
   - transcription/Tamil status **verified**;
   - Gate E **passed**;
   - verified scan range **241–277**;
   - verified printed range **240–276**;
   - verified pages **37/37**;
   - cumulative Gate-E corrections **29**;
   - next verification scan page **null**;
   - unresolved readings **0**;
   - `verified_against_scan: true`;
   - strict full-speech visual verification true.
5. Set the translation Tamil prerequisite as satisfied and unblock Gate F, but leave English translation **not-started** in this closure activity.
6. Remove `gate-e-batch8-pp276-277.md` after successful canonical merge and status closure.
7. Update handover and this prompt to the first bounded **Gate F English translation** activity from the final verified Tamil.
8. Do not begin English until all Gate-E closure records agree.
