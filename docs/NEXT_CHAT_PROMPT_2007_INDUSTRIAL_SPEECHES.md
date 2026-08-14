# Next-chat prompt — Speech 7 full Gate E closure / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart transcription or repeat the three Gate-E page-audit batches. Gate C is complete, Gate D passed, and all 42 Speech-7 pages have now completed bounded Gate-E visual audit.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect `speeches/1998/1998-05-14-industries-debate/` and continue the existing canonical files.
5. Use the actual controlling PDF scan for any targeted recheck needed to resolve a closure inconsistency. The rendered scan controls; OCR/extracted text and outside knowledge are helpers only.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- do not silently modernise, normalise, reconstruct or improve printed Tamil

If the controlling PDF is unavailable and a visual recheck becomes necessary, attach:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

## Speech 7 locked identity

- source label: `உரை : 7`
- date: `14.05.1998`
- canonical ID: `1998-05-14-industries-debate`
- scan pages: **199–240**
- printed pages: **198–239**
- total mapped pages: **42**
- scan page = printed page + 1
- p.241 begins Speech 8 and must not be included

## Completed state

- Gate C: **complete — 42/42 pages**;
- Gate D: **passed**;
- Gate E Batch 1: **passed — scan pp.199–213**;
- Gate E Batch 2: **passed — scan pp.214–228**;
- Gate E Batch 3: **passed — scan pp.229–240**;
- Gate E individually audited: **42/42 pages**;
- cumulative Gate-E corrections: **5**;
- unresolved/`[REVIEW]`: **0**;
- Gate E formal status: **pending full-speech closure**;
- Tamil status: **transcribed, not yet formally verified**;
- English: **blocked**.

The five canonical Gate-E corrections are:

1. p.202 `விற்கப்படுகின்ற` → `விற்கப்படுகிற`;
2. p.205 `தெரிவித்து உண்மை` → `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கின்றேன்` → `சுட்டிக் காட்டியிருக்கிறேன்`;
4. p.214 Hyundai allotment `552 ஏக்கர்` → `532 ஏக்கர்`;
5. p.227 `புயூஜிகுரா லிமிடெட்` → `ப்யூஜிகுரா லிமிடெட்`.

Batch 3 found no additional definite canonical correction on pp.229–240 and preserved the p.240 closing sequence and full printed `THIRU B. VENKATASAMY` intervention.

Relevant checkpoints:

- Batch-2 transcript correction commit: `2ae1963b7d9c5dde4a96eb5ff8b8affbaf3a6693`
- Batch-3 metadata: `ca4a6ae3be253931b06d0289203fdf623a1ce914`
- Batch-3 verification log: `10727ca745a8545ca1459d930c6e5cb13f4cc47c`
- Batch-3 README: `1deaf218879cd87b5b2bfe7547e886bf0025d61e`
- Batch-3 source notes: `75ae00483e7f60515dc3b96e6e9a2beb62eda5c0`
- refreshed handover: `422bd1de5a1188f74ab5849cc6cb020364de61fa`

## Exact next activity — full Gate-E closure check

1. Confirm the three bounded Gate-E batches collectively cover exactly **42/42 pages**, scan pp.199–240 / printed pp.198–239.
2. Confirm the five corrections above are present canonically in `transcript.md` and no correction has been lost or duplicated.
3. Confirm unresolved/`[REVIEW]` readings are **0**.
4. Re-run structural checks: exactly 42 `source-page` markers, monotonic sequence 199–240, no gaps, duplicates or reordering, no p.241 marker and no Speech-8 heading/date spillover.
5. Confirm p.199 opening heading/date/speaker label remains intact.
6. Confirm p.240 closing sequence remains intact, including Speaker, `THIRU B. VENKATASAMY`, Tamil follow-up and Kalaignar's final reply; confirm audited printed-English passages remain represented.
7. Reconcile status across `transcript.md`, `metadata.json`, `README.md`, `source-notes.md` and `verification-log.md`.
8. If all checks pass, mark Gate E **passed**, set Tamil to **verified against scan**, set all 42 pages as verified, update the archival note in `transcript.md`, and unblock English Gate F.
9. Do not begin Speech 8.

After closure, the next activity should be the repository-defined English Gate F workflow for Speech 7, following `docs/ARCHIVAL_WORKFLOW.md` and the released speeches' established translation structure.
