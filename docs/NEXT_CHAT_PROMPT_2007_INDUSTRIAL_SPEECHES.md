# Next-chat prompt — Speech 8 final Gate E Batch 8 / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Gate C is complete at 37/37 pages, Gate D has passed, and Gate E Batches 1–7 are canonically complete. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Fetch current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
5. Use the controlling rendered scan as the authority for Tamil. OCR/extracted text is only a helper.

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
- Gate-E verified pages: **35/37**
- Gate-E cumulative corrections: **28**
- unresolved readings in verified range: **0**
- next verification scan page: **276**
- Tamil status: **reviewed, not fully verified**
- English: **blocked**

## Batch-7 closure

Scan pp.271–275 / printed pp.270–274 were visually verified 5/5. One definite source-supported correction was merged into canonical `transcript.md`:

- p.274 `ஏராளமான தொகைகளை லஞ்சம் செய்து கொண்டு` → `ஏராளமான தொகைகளை வசூல் செய்து கொண்டு`.

Scan pp.271–273 and p.275 required no additional correction. The p.270→271 and p.275→276 continuations are intact. The canonical commit diff was inspected and contains only the archival status-note update plus this one correction. No unrelated Tamil change was introduced.

Batch-7 canonical transcript checkpoint: `d3106a9d88ed7d5c801398b14e1705eff446a18c`.

## Exact next activity — final Gate E Batch 8

1. Visually verify **scan pp.276–277 / printed pp.275–276** directly against the controlling scan.
2. On p.276, check the opening printed High Court English quotation exactly, the following Tamil paragraph, the source form `8-ஏ`, the `டாமின்` passage, the speech-closing `வணக்கம்`, applause marker, and the Speaker transition.
3. On p.277, check the full `திரு. சோ. பாலகிருஷ்ணன்` intervention, including `5,000`, `29`, `429`, `ஒன்றரை கோடி`, and Kalaignar's reply including `400`, `29`, and the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay.
4. Verify all words/characters, names, numerals, punctuation, speaker labels, printed English and cross-page continuity.
5. Confirm the exact Speech-8 close on p.277 and **no p.278 / Speech-9 spillover**.
6. Preserve source spelling and period forms exactly; do not modernise, improve or reconcile against outside knowledge.
7. Apply only definite scan-supported corrections and log each before→after reading with page number.
8. Record any unresolved reading explicitly instead of guessing.
9. If both pages pass, close Gate E at **37/37 pages**, set Tamil status to **verified**, set `verified_against_scan: true`, mark Gate E `passed`, set next verification page to null, and reconcile metadata/README/source notes/verification log/handover/prompt.
10. English Gate F may be unblocked only after the Tamil Gate-E closure is fully reconciled; do not begin translation in the same activity unless the archival workflow explicitly requires it.
