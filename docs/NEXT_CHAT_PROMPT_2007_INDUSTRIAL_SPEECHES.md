# Next-chat prompt — Speech 8 final Gate C merge / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C Batches 1–2 are canonical, and the final Batch 3 has been transcribed and staged. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the current `speeches/1999/1999-04-29-industries-debate/transcript.md` and `gate-c-batch3-pp271-277.md` before writing.
5. Use the controlling scan as the authority for Tamil. OCR/extracted text is only a helper.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C Batch 1: **canonical — scan pp.241–255 / printed pp.240–254**
- Gate C Batch 2: **canonical — scan pp.256–270 / printed pp.255–269**
- canonical Gate C coverage: **30/37 pages, scan pp.241–270 / printed pp.240–269**
- Gate C Batch 3: **transcribed and staged — scan pp.271–277 / printed pp.270–276**
- staging file: `speeches/1999/1999-04-29-industries-debate/gate-c-batch3-pp271-277.md`
- staging commit: `c1caa09e674f62525f25a1a41ccf34be442ed07d`
- Batch-3 unresolved/`[REVIEW]` readings: **0**
- Tamil status: **in-progress, not verified** until the staged batch is merged and checked
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked**

The staged p.277 ending is:

`உப்பளத் தொழில் மாத்திரம் அல்ல, தமிழகத்தில் அப்பளத் தொழிலும் கெடாமல் இந்த அரசு பார்த்துக் கொள்ளும். (மேசையைத் தட்டும் ஒலி).`

The rendered next page was checked: scan p.278 begins `உரை : 9`, `நாள் : 8.05.2000`; it is not part of Speech 8.

## Exact next activity — merge Gate C Batch 3

1. Fetch current canonical `transcript.md` and the staging file using their current SHAs; if anything changed concurrently, refetch and merge safely.
2. Append staged **pp.271–277** immediately after p.270, preserving all existing canonical pp.241–270 exactly.
3. Confirm source-page markers **241–277** are continuous and monotonic: **37 markers, no gaps, duplicates or reordering**.
4. Confirm there is **no `source-page: 278` and no Speech-9 material**.
5. Confirm the complete p.276→277 Opposition Leader / Kalaignar closing sequence and printed ending ornament boundary.
6. Mark Gate C complete at **37/37 pages** and Tamil status `transcribed`, explicitly **not verified**.
7. Remove the staging file only after the canonical merge has been checked.
8. Update metadata, README, source notes, verification log, handover and this prompt.
9. The following activity is **Gate D — full-speech Tamil completeness/page-marker audit**. Do not begin English; Gate E must pass before English starts.
