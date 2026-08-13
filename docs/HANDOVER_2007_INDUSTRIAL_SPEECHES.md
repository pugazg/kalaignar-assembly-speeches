# Handover — 2007 industrial speeches anthology

## Purpose

Continuation point for `pugazg/kalaignar-assembly-speeches` using:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

The scan image is authoritative for Tamil transcription. OCR is only a helper. English is translated from and checked against the verified Tamil. Any later contextual identification added to English must be documented without rewriting the source-faithful Tamil.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Workflow: `docs/ARCHIVAL_WORKFLOW.md`
- Locked map: `sources/2007-industrial-speeches/mapping.md`

## Locked speech inventory

| # | Date | Scan pages | Printed pages | Canonical ID |
|---:|---|---:|---:|---|
| 1 | 21.03.1963 | 18–26 | 17–25 | `1963-03-21-industries-debate` |
| 2 | 16.04.1981 | 27–61 | 26–60 | `1981-04-16-industries-debate` |
| 3 | 03.05.1989 | 62–98 | 61–97 | `1989-05-03-industries-debate` |
| 4 | 18.04.1990 | 99–135 | 98–134 | `1990-04-18-industries-debate` |
| 5 | 14.08.1996 | 136–171 | 135–170 | `1996-08-14-industries-debate` |
| 6 | 23.04.1997 | 172–198 | 171–197 | `1997-04-23-industries-debate` |
| 7 | 14.05.1998 | 199–240 | 198–239 | `1998-05-14-industries-debate` |
| 8 | 29.04.1999 | 241–277 | 240–276 | `1999-04-29-industries-debate` |
| 9 | 08.05.2000 | 278–303 | 277–302 | `2000-05-08-industries-debate` |
| 10 | 23.08.2006 | 304–326 | 303–325 | `2006-08-23-industries-debate` |

## Released anthology speeches

Speeches 1, 2 and 3 are fully released with verified Tamil and verified English.

### Speech 3 final state

Canonical ID: `1989-05-03-industries-debate`  
Range: scan pp.62–98 / printed pp.61–97

- Gate C: complete
- Gate D: passed
- Gate E: passed
- Tamil: **verified**
- unresolved Tamil readings: **0**
- Gate F: complete
- Gate G: passed
- English: **verified**
- Gate H: passed
- release status: **fully released**

Gate-H release commits:

- root README: `3e3dfe207435dd8d78ef263d472798e2acc248e5`
- `data/speeches.json`: `a83d671fb6d313e30c3846658f38546eff049796`

### Important post-release correction — source p.94 / TIIC

The verified Tamil source on p.94 visibly reads:

`சிப்காட், டிக் நிறுவனங்களிடமிருந்து லோன் வாங்கியிருக்கிறார்கள்.`

That Tamil wording remains unchanged because the scan controls the archival transcription.

Final project state:

- Tamil source layer: retains **`டிக்`** exactly as printed.
- English translation: uses **`SIPCOT and TIIC`**.
- The TIIC form is explicitly treated as a contextual/editorial institutional identification in English, not as a claim that the scan literally prints `TIIC`.
- Tamil verification, English verification and Gate H release status remain valid.

Post-release TIIC correction commits:

- `transcript.md`: `822bb9ca97d43655f80ec222b2a4572a898c3e58`
- Speech 3 `README.md`: `0adad93cd31e71a88900cad5a35180b619974f5e`
- `source-notes.md`: `0eadb079ed213a14517f437e49f0483ce9c9c750`
- `verification-log.md`: `5b2016282588dcec121e2354c567711eda4e47da`

Do not revert the English back to `TIC` in later work.

## Current active work — Speech 4

- Source label: `உரை : 4`
- Printed date: `18.04.1990`
- Canonical ID: `1990-04-18-industries-debate`
- Locked range: **scan pp.99–135 / printed pp.98–134**
- Total mapped pages: **37**
- Gate C: **in progress**
- Gate C completed pages: **scan pp.99–128 / printed pp.98–127**
- Represented source-page markers: **30 of 37**, exactly **99–128**, unique and monotonic
- Tamil status: **in-progress**
- Explicit unresolved Tamil readings: **0**
- Next scan page: **129 / printed p.128**
- Gate D: **not started**
- Gate E: **not started**
- English: **blocked / not started until Tamil Gates C–E are complete**
- Speech 4 folder: `speeches/1990/1990-04-18-industries-debate/`

Boundary remains locked: scan p.98 ends Speech 3; scan p.99 begins `உரை : 4`, dated `18.04.1990`; Speech 4 ends at scan p.135 and scan p.136 begins Speech 5.

### Gate C Batch 1 completed

Batch 1 directly transcribed **scan pp.99–113 / printed pp.98–112** from the controlling scan images.

Batch 1 commit: `4f876e0e40057f423741239fcd74b1d000eb0099`

Batch-1 continuation was:

- scan p.113 ends: `யாரோ “என்.ஆர்.ஐ.” பெர்சன்களையெல்லாம்`
- scan p.114 begins: `துரத்துகிறோம் என்று - அந்த பெரியசாமி அவர்கள் நடத்துகின்ற...`

### Gate C Batch 2 completed

Batch 2 directly transcribed **scan pp.114–128 / printed pp.113–127** from the controlling scan images and appended it to the canonical `transcript.md`.

The Speech-4 progress files were updated:

- `speeches/1990/1990-04-18-industries-debate/transcript.md`
- `speeches/1990/1990-04-18-industries-debate/metadata.json`
- `speeches/1990/1990-04-18-industries-debate/README.md`
- `speeches/1990/1990-04-18-industries-debate/source-notes.md`
- `speeches/1990/1990-04-18-industries-debate/verification-log.md`

Batch-2/progress commits:

- transcript: `07067b8dbaed5c5baf66b86fe49b9c5773b9a2c0`
- metadata: `13403ab4ebd71074e734bad81d769a5b43d0edeb`
- README: `5a18086ceb841d94dfd7c4273d437713e27381cf`
- source notes: `a5f226328776de308f66867bf1a0b98d9fae6d77`
- verification log: `3490b23cd66e1473abf1a54cfd0432fcfb8394f6`

Exact Batch-2 continuation boundary:

- scan p.128 ends: `30 வட்டங்`
- scan p.129 begins: `களைத் தனியாக அறிவித்து அவர்களுக்கு மேலும் சில சலுகைகளைச் செய்யலாம் என்ற முயற்சியை இப்போது அரசு மேற்கொண்டிருக்கிறது...`

Scan p.129 was inspected only to establish the continuation; it has **not** yet been transcribed.

## Immediate next action — Speech 4 Gate C final batch

Complete the remaining Tamil first-pass transcription for **scan pp.129–135 / printed pp.128–134**.

1. Re-read current `docs/ARCHIVAL_WORKFLOW.md`, this handover, `sources/2007-industrial-speeches/mapping.md`, and the existing Speech 4 files before editing.
2. Reconfirm scan p.129 directly from the rendered page and continue from `களைத் தனியாக அறிவித்து அவர்களுக்கு மேலும் சில சலுகைகளைச் செய்யலாம்...`.
3. Append scan pp.129–135 to `speeches/1990/1990-04-18-industries-debate/transcript.md`.
4. Add exactly one `<!-- source-page: N -->` marker for every remaining scan page.
5. Preserve wording, period spelling, punctuation, numerals, headings, speaker labels, interventions, technical transliterations and printed English as visible.
6. Mark genuinely unreadable text explicitly instead of guessing.
7. Reconfirm scan p.135 is the locked Speech-4 ending and scan p.136 begins Speech 5; do not transcribe Speech 5.
8. Once pp.129–135 are represented, run Gate D full-speech completeness audit for exactly **37 markers, 99–135**, unique and monotonic, with no skipped/duplicated page and correct start/end boundaries.
9. After Gate D, keep Tamil status `transcribed`; do **not** mark `verified` until a separate Gate E strict page-by-page visual audit has been completed.
10. Do not begin English translation before Gate E passes.

## Content to leave untouched

Unless explicitly requested, do not modify released Speeches 1–3, the released index records, unrelated sources, or Speech 5+ while Speech 4 is active. The Speech 3 TIIC correction described above is the final intended state.

## End-of-session requirement

Record canonical ID, exact pages completed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
