# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter its verified Tamil or English while processing Speech 8.

## Active unit — Speech 8

Locked source mapping:

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- relationship: scan page = printed page + 1
- previous boundary: scan p.240 closes Speech 7
- next boundary: scan p.278 begins Speech 9 (`8.05.2000`)

The opening and closing boundaries were re-confirmed directly from the controlling scan before transcription: p.241 begins `உரை : 8 / நாள் : 29.04.1999`; p.277 closes Speech 8; p.278 begins Speech 9.

## Gate C — complete

Speech 8 now has a complete canonical first-pass Tamil transcription.

- Batch 1: scan pp.**241–255** / printed pp.**240–254** — 15 pages
- Batch 2: scan pp.**256–270** / printed pp.**255–269** — 15 pages
- Batch 3: scan pp.**271–277** / printed pp.**270–276** — 7 pages
- cumulative canonical coverage: **241–277 / 240–276 — 37/37 pages**
- unresolved/`[REVIEW]` readings: **0**
- Tamil status: **transcribed, not verified**
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked**

Gate-C final merge checkpoint:

- canonical `transcript.md`: `d0fd3ea71f29838299eb5d7008e4149b7399498c`
- metadata Gate-C closure: `d97cbcbc4a914f6264238c06228eee4931f351a6`
- README Gate-C closure: `53593a05ccb272eb74c3c9082278737c7d094f40`
- source notes Gate-C closure: `4f1209a986a29adca77ad81cd59856a3825ac655`
- verification log Gate-C closure: `94c7b09e716a48913f89809e4d66bfe06d9a9540`
- removed merged Batch-3 staging file: `87766fbdfee5a546f8ac20d8ae585ecbfe162270`

## Gate-C closure checks

The final staged pp.271–277 were appended after p.270 without altering the earlier canonical text. The canonical transcript now runs from `source-page: 241` through `source-page: 277`, with the p.270→271 transition intact. The p.276→277 closing sequence retains the Speaker label, Opposition Leader `திரு. சோ. பாலகிருஷ்ணன்`, and Kalaignar's final reply ending with the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay and `(மேசையைத் தட்டும் ஒலி).`

`source-page: 278` is absent and no Speech-9 text was entered.

## Exact next activity — Speech 8 Gate D

1. Fetch the current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` before auditing.
2. Perform the full-speech Tamil completeness/page-marker audit across **scan pp.241–277 / printed pp.240–276**.
3. Confirm all **37** source-page markers are present exactly once, monotonic and gap-free: 241, 242, ... 277.
4. Confirm the opening matches `உரை : 8 / நாள் : 29.04.1999` and the closing is the p.277 salt-pan intervention/final Kalaignar reply.
5. Confirm there is no `source-page: 278`, no Speech-9 heading/date and no duplicated or reordered page section.
6. Check that printed speaker changes/interventions are structurally represented and that any unresolved markers are counted.
7. If Gate D passes, update metadata/README/source notes/verification log/handover/prompt to `gate_d_status: passed` and Tamil status `reviewed` or the repository's established post-Gate-D equivalent, but **do not mark Tamil verified**.
8. Gate E is the following activity. Do not begin English until Gate E passes.
