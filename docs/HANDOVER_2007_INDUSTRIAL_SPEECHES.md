# Handover — 2007 industrial speeches anthology

## Source authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

Locked source: **329 PDF pages**, **217,124,211 bytes**, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Released speeches

**Speeches 1–9 are fully released through Gate H with verified Tamil and verified English. Do not restart, retranscribe or modify those released source/translation layers unless a concrete correction is explicitly requested and source-supported.**

## Active archival unit — Speech 10

- source label: `உரை : 10`
- printed date: `23.08.2006`
- ISO date: `2006-08-23`
- canonical ID: `2006-08-23-industries-debate`
- scan/source pages: **304–326**
- printed pages: **303–325**
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10
- scan p.326 closes Speech 10
- scan pp.327–328 are `குறிப்புகள்`; p.329 is portrait/back matter

## Current Speech-10 state

- Gate C: **complete — 23/23 pages**;
- Gate D: **passed**;
- Gate E: **passed — 23/23 pages, 6 definite Tamil corrections, 0 unresolved readings**;
- Tamil: **verified against scan**;
- Gate F: **complete — 23/23 English pages translated from final verified Tamil**;
- Gate G: **passed — 23/23 pages reviewed, 9 cumulative English corrections, 0 unresolved questions**;
- `verified_against_tamil`: **true**;
- Kalaignar voice-retention policy: **full-speech reviewed**;
- Gate H: **in progress**;
- Gate-H preparation: **complete**;
- canonical Tamil+English merge: **not yet complete**;
- indexed: **false**;
- release-ready: **false**.

The verified English remains in five working segments:

1. `translation.md` — source pp.304–308;
2. `translation-gate-f-batch-2.md` — pp.309–313;
3. `translation-gate-f-batch-3.md` — pp.314–318;
4. `translation-gate-f-batch-4.md` — pp.319–323;
5. `translation-gate-f-batch-5.md` — pp.324–326.

`translation-review.md` records all nine Gate-G corrections and the release invariant.

## Exact next activity — Speech 10 Gate H canonical merge

1. Leave the verified Tamil in `transcript.md` untouched.
2. Append the complete Gate-G-verified English after the Tamil layer, using the five working segments as authoritative inputs.
3. Do not rewrite or newly polish the English during consolidation.
4. Preserve exact English page correspondence for source pp.304–326.
5. Recheck especially the corrected p.308→309, p.313→314 and p.323→324 boundaries; the restored latter p.318 passage; p.323 Perambalur desk-thumping position; and p.326 six-lane-road desk-thumping position.
6. Confirm all 23 English page sections are present with no gap or overlap and all Kalaignar voice-sensitive passages remain intact.
7. Only after the canonical merge passes, update `data/speeches.json`, root README, Speech-10 README, verification log and this handover; retire working translation segments according to the established released-speech pattern; then mark Gate H passed and Speech 10 released.

Do not call Speech 10 released before that merge and release audit are complete.
