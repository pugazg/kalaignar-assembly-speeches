# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the **final verified Tamil**, not OCR or earlier drafts. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 8

Speeches 1–8 are fully released through Gate H. Do not restart or modify their verified Tamil/English content while processing Speech 9.

## Active unit — Speech 9

- source label: `உரை : 9`
- printed date: `8.05.2000`
- ISO date: `2000-05-08`
- canonical ID: `2000-05-08-industries-debate`
- PDF scan pages: **278–303**
- printed pages: **277–302**
- page relationship: scan page = printed page + 1
- scan p.277 closes Speech 8
- scan p.278 begins Speech 9
- scan p.303 closes Speech 9 with the printed ornament
- scan p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`)

The working PDF matches the locked **329 pages**, **217,124,211 bytes**, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Speech 9 Tamil gates

### Gate C

**Complete — 26/26 pages**, source pp.278–303 / printed pp.277–302.

### Gate D

**Passed.** Source-page markers 278–303 occur exactly once and in strict order; no missing/duplicate/reordered markers and no Speech-8/Speech-10 spillover.

### Gate E

**Passed — all 26/26 pages directly verified against the controlling rendered scan.**

Gate-E corrections:

1. p.279 `பிள்ளைகளை யெல்லாம்` → `பிள்ளைகளையெல்லாம்`.
2. p.293 `இன்னொன்றியில்` → `இஃதன்னியில்`.
3. p.303 `வெட்டுத் தீர்மானங்களையும்` → `வெட்டுத்தீர்மானங்களையும்`.

The final p.303 reread re-confirmed `கேட்டு அமைகிறேன்.`, Chair call `திரு. பி. ஆர். சுந்தரம்.`, Sundaram's `2,000 கோடி` → `2,000 இலட்சம்` / `20 கோடி`, `ராசிபுரம்.....`, the Chair's separately printed `200 கோடி, 20 இலட்சம், 2,000 கோடி`, and the final Chair intervention before the closing ornament. Scan p.304 begins Speech 10 and is excluded.

A final pre-close canonical re-fetch also confirmed that the earlier Gate-C p.298 corrections `பழனிசாமி ஏற்றுக் கொள்கிறாரோ` and `டி. மணி ஏற்றுக் கொள்கிறாரோ` were already present. The interim Batch-5 note describing them as a current regression was a comparison-state error; no p.298 restoration was needed.

## Current Speech-9 truth

- Gate C: **complete**
- Gate D: **passed**
- Gate E: **passed**
- verified source range: **278–303**
- verified printed range: **277–302**
- verified pages: **26/26**
- cumulative definite Gate-E corrections: **3**
- unresolved readings: **0**
- Tamil status: **verified against scan**
- `verified_against_scan`: **true**
- English Gate F: **not started; unblocked**
- English Gate G: **not started**
- Speech 10: **not started**

Current checkpoints after Gate E closure:

- transcript: `8ab00921d9e8e3d7c0742ee9c4f3943ae1b7b109`
- transcript blob: `ac00a79863c0b0bdbaac6d9fb7b03f7e4c1bb577`
- metadata: `827976ee91e064be0b0723d2e76b5d49d8ca079a`
- README: `ec9ef168df26a11cdbc89eda39544de94fad6d84`
- verification log: `256cd0c3f086a67ad21012e74bb1d649405df148`

## Exact next activity — Speech 9 Gate F

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover, the current Speech-9 `metadata.json`, `README.md`, `source-notes.md`, `transcript.md`, and `verification-log.md` before writing.
2. Begin **Gate F English translation from the final verified Tamil only**.
3. Follow the established Speech-1–8 translation pattern and preserve source-page correspondence (`<!-- source-page: N -->` or the repository's established English-page markers as prescribed by the workflow/reference implementation).
4. Translate faithfully rather than smoothing away parliamentary repetition, source-supported oddities, embedded English, figures, dates, speaker labels or interruptions.
5. Where the verified Tamil intentionally preserves source inconsistency, translate the verified Tamil rather than silently reconciling against external knowledge or OCR.
6. Keep unresolved translation questions explicit rather than guessing.
7. Do not begin Gate G until Gate F is complete.
8. Do not begin Speech 10.
