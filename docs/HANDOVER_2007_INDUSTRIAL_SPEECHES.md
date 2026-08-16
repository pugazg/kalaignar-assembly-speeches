# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English is translated and fidelity-reviewed against the **final verified Tamil**, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 8

Speeches 1–8 are fully released through Gate H. Do not restart or modify their verified Tamil/English content while processing Speech 9.

## Active unit — Speech 9

- source label: `உரை : 9`
- printed date: `8.05.2000`
- ISO date: `2000-05-08`
- canonical ID: `2000-05-08-industries-debate`
- PDF scan pages: **278–303**
- printed pages: **277–302**
- scan p.277 closes Speech 8
- scan p.278 begins Speech 9
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`)

The working PDF matches the locked **329 pages**, **217,124,211 bytes**, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Speech 9 Tamil gates

- Gate C: **complete — 26/26**
- Gate D: **passed**
- Gate E: **passed — 26/26 directly verified against scan**
- Gate-E corrections: **3**
- unresolved Tamil readings: **0**
- Tamil status: **verified**

Gate-E corrections:

1. p.279 `பிள்ளைகளை யெல்லாம்` → `பிள்ளைகளையெல்லாம்`.
2. p.293 `இன்னொன்றியில்` → `இஃதன்னியில்`.
3. p.303 `வெட்டுத் தீர்மானங்களையும்` → `வெட்டுத்தீர்மானங்களையும்`.

Verified Tamil blob: `ac00a79863c0b0bdbaac6d9fb7b03f7e4c1bb577`.

## Speech 9 English gates

### Gate F

**Complete — 26/26 pages**, source pp.278–303 / printed pp.277–302.

The English was translated only from the final verified Tamil. Working segments are:

- `translation.md` — pp.278–285
- `translation-gate-f-batch-2.md` — pp.286–290
- `translation-gate-f-batch-3.md` — pp.291–295
- `translation-gate-f-batch-4.md` — pp.296–300
- `translation-gate-f-batch-5.md` — pp.301–303

`translation-consolidated.md` records the consolidation manifest for release work.

### Gate G

**Passed — 26/26 pages reviewed against final verified Tamil.**

Voice rule: retain Kalaignar's parliamentary language and voice — long argumentative movement, repetition, direct address, rhetorical questions, humour, irony, wordplay, metaphors, political phrasing, register shifts and stage markers — rather than polishing into generic modern English. Printed English and source-supported oddities must not be silently corrected.

Gate-G corrections: **2**.

1. p.284: restored the actual scientific-advance → need to join/compete → Tamil Nadu first-place/praise argumentative sequence, replacing an unsupported generic Gate-F transition.
2. p.286: `இந்தக் கேமிரா கழுவும்போது` is retained as the source-odd `When this camera is washed`, not interpretively normalised to `When this camera develops`.

Final source p.303 required **no English correction**. The `111` joke, request to withdraw all cut motions, `I take my seat`, P. R. Sundaram's `2,000 crore` → `2,000 lakh, that is, 20 crore` correction, interrupted `Rasipuram.....`, and the Speaker's final `200 crore, 20 lakh, 2,000 crore` sequence all passed fidelity review.

Unresolved translation questions: **0**. `verified_against_tamil=true`.

## Current Speech-9 truth

- Gate C: **complete**
- Gate D: **passed**
- Gate E: **passed**
- Gate F: **complete**
- Gate G: **passed**
- Tamil verified: **yes**
- English verified: **yes**
- Gate-G cumulative corrections: **2**
- unresolved Tamil readings: **0**
- unresolved translation questions: **0**
- Gate H: **not started**
- Speech 10: **not started**

Recent checkpoints:

- final Gate-G p.303 working-segment checkpoint: `a507189599a7a95b40c12972462f133c46e120b6`
- metadata Gate-G closure: `744106710a584ce1a2ec503003790c9987b92366`
- verification-log Gate-G closure: `ebdcf7124f57e308d2e64a18684a4262d43151cf`
- README Gate-G closure: `9ddb0a3e844b1d9366557942c5f568c1db218535`

## Exact next activity — Speech 9 Gate H

1. Re-read `docs/ARCHIVAL_WORKFLOW.md` and inspect the established Speech-1–8 Gate-H/release pattern before writing.
2. Perform **Gate H release preparation and canonical merge** for Speech 9 only.
3. Merge the final verified English after the final verified Tamil in the repository's canonical release form, preserving page correspondence and the verified English wording.
4. Run the required release/completeness checks and ensure no working placeholder or duplicate page remains.
5. Update metadata, README, verification/release artefacts and repository-level mapping/index files exactly as prescribed by the workflow/reference releases.
6. Mark Speech 9 released only after those checks pass.
7. Do **not** begin Speech 10 in the same bounded activity unless explicitly requested.
