# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continuation point for `pugazg/kalaignar-assembly-speeches` using `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription. OCR is only a helper. English is translated from and checked against the verified Tamil. External context must never rewrite the source-faithful Tamil.

## Mandatory recurring checkpoint

After every speech is fully completed and released through Gate H, update this handover and `docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md` before beginning the next speech. Record final Gates C–H status, exact ranges, unresolved readings, important corrections/anomalies, canonical files, release commits, next speech, exact next batch and current continuation point.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Workflow: `docs/ARCHIVAL_WORKFLOW.md`
- Locked map: `sources/2007-industrial-speeches/mapping.md`

The earlier p.150 source-availability warning was a chat-preview limitation only. Direct inspection established that the uploaded raw PDF is the complete controlling 329-page file; later Speech-5 pages were rendered directly from that source.

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

Speeches **1–4** are fully released with verified Tamil and verified English:

- Speech 1 — `1963-03-21-industries-debate`, scan pp.18–26
- Speech 2 — `1981-04-16-industries-debate`, scan pp.27–61
- Speech 3 — `1989-05-03-industries-debate`, scan pp.62–98
- Speech 4 — `1990-04-18-industries-debate`, scan pp.99–135

Do not modify those released speeches while processing Speech 5 unless a separately justified consistency correction is required.

Important retained released-speech note: Speech-3 verified Tamil on p.94 remains `சிப்காட், டிக் நிறுவனங்களிடமிருந்து...`; final English uses `SIPCOT and TIIC` as the documented institutional identification. Do not revert it to `TIC`.

## Current active work — Speech 5

- Source label: `உரை : 5`
- Printed date: `14.08.1996`
- Canonical ID: `1996-08-14-industries-debate`
- Locked range: **scan pp.136–171 / printed pp.135–170**
- Total mapped scan pages: **36**
- Gate C: **complete — 36/36 pages represented**
- Gate D: **passed**
- Tamil status: **transcribed**, not reviewed or verified
- explicit unresolved/`[REVIEW]` readings after Gate D: **0**
- Gate E: **not started; exact next activity**
- English / Gate F: **blocked until Gate E passes and Tamil is verified**
- Gates G/H: **not started**

The standard five-file folder is `speeches/1996/1996-08-14-industries-debate/`.

## Gate C completed batches

- Batch 1: **scan pp.136–150 / printed pp.135–149**
- Batch 2: **scan pp.151–165 / printed pp.150–164**
- Batch 3: **scan pp.166–171 / printed pp.165–170**

Batch 3 continued the p.165 sentence at p.166 with `என்பதையும் நான் இங்கே சொல்லிக்கொள்ள வேண்டியவனாக இருக்கின்றேன்.` and carried the transcript through the final parliamentary exchanges on p.171.

The p.171 ending is visually confirmed: `திரு. ஆர். சொக்கர்` asks about the `சிங்கப்பூர் காரிடார்`; Kalaignar replies that, not necessarily under that name, the government will try to bring a corridor-like major industry from Singapore to Tamil Nadu. The decorative ending ornament follows. Scan p.172 begins `உரை : 6`, dated `23.04.1997`, confirming the locked boundary.

### Gate-C / Gate-D commits from the latest activity

- complete `transcript.md` pp.136–171 — `a4840561021c7455e0e778552883cf67290cd174`
- `metadata.json` advanced to `transcribed`, Gate D passed — `171f0e75b3563e75bd622b66b56783010f487dc5`
- speech `README.md` advanced to Gate E — `533bf367a2fe118ba83e4a7096d6fed2f9058abd`
- `source-notes.md` Batch 3 + Gate D — `a8565a140cf5cd66c28f8aa688d042af44c4fca2`
- `verification-log.md` Gate D pass — `a9258f06263723b81bcba8817a581e7dc95b51cb`
- next-chat prompt advanced to Gate E — `76d0f65826450fbd5ff1c683d355eb062488fbda`

Earlier Batch-2 checkpoint commits remain documented in repository history; do not revert them.

## Gate D result

The full-speech completeness/page-marker audit passed for scan pp.136–171:

- expected pages: **36**;
- represented pages: **36**, exactly **136–171**;
- no mapped page skipped or duplicated;
- opening p.136 matches `உரை : 5 / நாள் : 14.08.1996`;
- ending p.171 and p.172 next-speech boundary match the locked map;
- final speaker/intervention sequence is represented;
- explicit unresolved-reading markers: **0**.

Gate D proves completeness only. It does not prove source fidelity. Tamil therefore remains `transcribed`, not `verified`.

## First-pass forms requiring deliberate Gate-E checking

Do not automatically modernise or correct unusual forms. Visually verify them against the scan. Recorded examples include:

- p.142 `இஃதன்னியில்`
- p.145 `ஆலங்குளம் ஆஸ்பெஸ்டாஸ் பயிற்சித் தொழிற்சாலை`
- p.146 `ஓட்டலுக்கு மறுப்பு எழுதினாரோ அந்தச் செயலாளர்`
- p.154 `Our closed historical and cultural ties`
- p.155 `Sigapore`
- p.156 `Tom, Tick & Harry`
- p.157 `business-men`
- pp.158–159 `Liquified Natural Gas` / `LNG Terminal (Liquified)`
- p.162 `அருணா ஷூகாஸ்`
- p.163 `தேவையேயில்லாமல்,,` and `ஊழல் நடத்திருக்கிறது`
- p.164 `ஸ்பெசிபிக் நேர்வு`
- p.167 `ராஜஸ்தான் ஷிப் அண்டு உல்::பெடரேஷன்`
- p.168 `வறுமை தேன் எனக் கொட்டுகிறது`, `side effects`, `anti-biotic`, `சிண்டாக்`
- p.169–170 State Planning Commission names and parenthetical roles

These are first-pass readings, not claims that every form has already passed strict verification.

## Exact next activity — Speech 5 Gate E

Begin strict Tamil source-fidelity verification against the scan.

### Gate E Batch 1

Audit **scan pp.136–150 / printed pp.135–149** directly against the controlling scan images.

For every page check words/characters, names/initials, numerals, dates, percentages, monetary values/units, printed English, headings, speaker labels, punctuation and page-transition continuity. Apply only source-supported corrections to canonical `transcript.md` and record each concrete correction in `verification-log.md`.

After Batch 1, continue Gate E with **pp.151–165**, then **pp.166–171**. Do **not** mark Tamil verified until the entire 36-page range passes Gate E. English remains blocked throughout Gate E. Do not start Speech 6 or Gate-H index/release work.

## End-of-session checkpoint

This handover records completion of Speech-5 Gate C and passage of Gate D. After this handover commit, the next work starts with **Gate E Batch 1, scan p.136**.
