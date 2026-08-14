# Next-chat prompt — Speech 7 Gate E Batch 2 / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart transcription or Gate E. Gate C is complete, Gate D passed, and Gate E Batch 1 has passed through scan p.213.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect `speeches/1998/1998-05-14-industries-debate/` and continue the existing canonical files.
5. Inspect the actual controlling PDF scan before making any correction. The rendered scan controls; OCR/extracted text and the existing transcript are helpers only.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil
- do not silently modernise, normalise, reconstruct or improve printed Tamil

If the controlling PDF is unavailable in a new chat, attach:

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
- Gate E Batch 1: **passed — scan pp.199–213 / printed pp.198–212**;
- Gate E audited: **15/42 pages**;
- Gate-E corrections: **3**;
- unresolved/`[REVIEW]`: **0**;
- Tamil status: **transcribed, not verified**;
- English: **blocked**.

Gate-E Batch-1 corrections applied in canonical transcript commit `4c42c979f087a78cdaeef3e96a12506bcdd7693e`:

1. p.202 `விற்கப்படுகின்ற` → `விற்கப்படுகிற`;
2. p.205 `தெரிவித்து உண்மை` → `தெரிவித்தது உண்மை`;
3. p.209 `சுட்டிக் காட்டியிருக்கின்றேன்` → `சுட்டிக் காட்டியிருக்கிறேன்`.

The corrected Batch-1 audit record is in `gate-e-batch1-corrections.md`.

Relevant checkpoints:

- canonical transcript corrections: `4c42c979f087a78cdaeef3e96a12506bcdd7693e`
- corrected Batch-1 audit record: `b268d0d6b62ce8366258260303915e7052bd41c7`
- metadata: `cfa53dec9a3febc14269a1127a3cc7928d86381b`
- verification log: `7e8164170d29c53ce837a21625c4bda73387e845`
- README: `4d7fc9162bbc777d39d6dcf829c28e41d784c424`
- handover: `57ebdcd5327fe1469e8f6e6d8382787ae7919736`

## Exact next activity — Speech 7 Gate E Batch 2

1. Re-open the controlling scan at **scan p.214 / printed p.213**.
2. Strictly verify **scan pp.214–228 / printed pp.213–227** against canonical `transcript.md`.
3. Check Tamil words/characters, names/initials, dates, percentages, monetary values, acreage/units, headings, speaker labels, interventions/context markers, embedded/printed English, punctuation where legible and cross-page continuity.
4. The scan wins over OCR, extracted text, outside knowledge and plausible reconstruction.
5. Preserve unusual/historical/source forms.
6. Apply each source-supported correction to canonical `transcript.md` and itemise it in `verification-log.md` with scan/printed page references.
7. Record unresolved readings explicitly rather than guessing.
8. Update the Speech-7 status/audit files with Batch-2 progress.
9. After Batch 2, Gate E will still have scan pp.229–240 remaining.
10. Do not begin English until Gate E passes all 42 pages.
11. Do not begin Speech 8.

At the end of the session, refresh the handover and this prompt with the exact next Gate-E page and relevant commit SHA(s).
