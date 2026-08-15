# Next-chat prompt — Speech 8 Gate D / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C is now complete at 37/37 pages. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Fetch the current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` before auditing.
5. Use the controlling scan as the authority. OCR/extracted text is only a helper.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C Batch 1: **complete — scan pp.241–255 / printed pp.240–254**
- Gate C Batch 2: **complete — scan pp.256–270 / printed pp.255–269**
- Gate C Batch 3: **complete and merged — scan pp.271–277 / printed pp.270–276**
- Gate C: **complete — 37/37 pages**
- canonical transcript merge commit: `d0fd3ea71f29838299eb5d7008e4149b7399498c`
- Tamil status: **transcribed, not verified**
- unresolved/`[REVIEW]` readings: **0**
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked**

The temporary Batch-3 staging file has been removed after successful canonical merge. The canonical transcript ends on p.277 with the Opposition Leader salt-pan intervention and Kalaignar's reply ending:

`உப்பளத் தொழில் மாத்திரம் அல்ல, தமிழகத்தில் அப்பளத் தொழிலும் கெடாமல் இந்த அரசு பார்த்துக் கொள்ளும். (மேசையைத் தட்டும் ஒலி).`

There is no `source-page: 278` and no Speech-9 spillover.

## Exact next activity — Gate D full-speech Tamil completeness/page-marker audit

1. Audit canonical `transcript.md` across **scan pp.241–277 / printed pp.240–276**.
2. Confirm all **37** page markers are present exactly once and in strict monotonic sequence **241 through 277**, with no gaps, duplicates or reordering.
3. Confirm the opening has `உரை : 8`, `நாள் : 29.04.1999`, and the source speaker label.
4. Confirm the p.277 ending is the complete Speaker → `திரு. சோ. பாலகிருஷ்ணன்` → Kalaignar salt-pan closing sequence.
5. Confirm there is no `source-page: 278`, `உரை : 9`, or `8.05.2000` in the Speech-8 transcript.
6. Check that printed speaker changes/interventions are structurally represented and count any unresolved markers.
7. If Gate D passes, update metadata, README, source notes, verification log, handover and this prompt. Keep Tamil **not verified**; Gate E remains required.
8. Do not begin English. Gate F remains blocked until Gate E passes.
