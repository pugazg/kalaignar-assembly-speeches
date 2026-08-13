# Handover — 2007 industrial speeches anthology

## Purpose

Authoritative continuation point for:

`TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`

Repository: `pugazg/kalaignar-assembly-speeches`

The structural map is complete and locked. The scan image is authoritative for Tamil transcription; OCR is only a helper and is never canonical. English must be translated from and verified against the final verified Tamil.

## Controlling source

- Publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- First edition: மே, 2007
- PDF pages: **329**
- File size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

Locked map: [`../sources/2007-industrial-speeches/mapping.md`](../sources/2007-industrial-speeches/mapping.md)  
Workflow: [`ARCHIVAL_WORKFLOW.md`](ARCHIVAL_WORKFLOW.md)

## Locked speech inventory

| # | Printed date | ISO date | PDF scan pages | Printed pages | Canonical ID |
|---:|---|---|---:|---:|---|
| 1 | 21.03.1963 | 1963-03-21 | 18–26 | 17–25 | `1963-03-21-industries-debate` |
| 2 | 16.04.1981 | 1981-04-16 | 27–61 | 26–60 | `1981-04-16-industries-debate` |
| 3 | 03.05.1989 | 1989-05-03 | 62–98 | 61–97 | `1989-05-03-industries-debate` |
| 4 | 18.04.1990 | 1990-04-18 | 99–135 | 98–134 | `1990-04-18-industries-debate` |
| 5 | 14.08.1996 | 1996-08-14 | 136–171 | 135–170 | `1996-08-14-industries-debate` |
| 6 | 23.04.1997 | 1997-04-23 | 172–198 | 171–197 | `1997-04-23-industries-debate` |
| 7 | 14.05.1998 | 1998-05-14 | 199–240 | 198–239 | `1998-05-14-industries-debate` |
| 8 | 29.04.1999 | 1999-04-29 | 241–277 | 240–276 | `1999-04-29-industries-debate` |
| 9 | 8.05.2000 | 2000-05-08 | 278–303 | 277–302 | `2000-05-08-industries-debate` |
| 10 | 23.08.2006 | 2006-08-23 | 304–326 | 303–325 | `2006-08-23-industries-debate` |

## Fully released work

### Speech 1 — released

`1963-03-21-industries-debate`, scan pp.18–26 / printed pp.17–25.

- Tamil: **verified**
- English: **verified**
- release/index commit: `ff2d8d5bb09f07925f8da791b138132041a92f52`

### Speech 2 — released

`1981-04-16-industries-debate`, scan pp.27–61 / printed pp.26–60.

- Tamil: **verified**
- English: **verified**
- root README release commit: `ac49ce2e4696573569816e1dbd747c4dbef74a99`
- `data/speeches.json` release commit: `eb5dda73afbcdf63bfb3735badd04e81b976502c`

### Speech 3 — released

`1989-05-03-industries-debate`, scan pp.62–98 / printed pp.61–97.

Gate state:

- Gate C Tamil first-pass: **complete**
- Gate D completeness: **passed**
- Gate E Tamil visual/source-fidelity verification: **passed**
- Tamil status: **verified**
- unresolved Tamil readings: **0**
- Gate F English translation: **complete**
- Gate G English fidelity verification: **passed**
- English status: **verified**
- Gate H release/index: **passed**
- release status: **fully released**

Gate-G fidelity corrections retained in the final English:

1. p.86 `aluminium sheets and strips` → `aluminium sheets and pattadaigal (பட்டாடைகள், as printed in the Tamil source)`;
2. p.94 `SIPCOT and TIIC` → `SIPCOT and TIC (டிக் in the Tamil source)`.

Gate-H release validation:

- root README contains one Speech 3 released entry with Tamil/English `Verified` and scan range **62–98**;
- `data/speeches.json` contains one `1989-05-03-industries-debate` record;
- machine-readable status is `transcription_status: verified`, `verified_against_scan: true`, `translation_status: verified`, languages `ta` and `en`;
- JSON parsed successfully after release;
- the pre-existing Speech 1, 1970 and Speech 2 machine-readable records remained unchanged; Speech 3 was appended as the fourth record.

Speech-3 Gate-H/release commits:

- root README release: `3e3dfe207435dd8d78ef263d472798e2acc248e5`
- `data/speeches.json` release: `a83d671fb6d313e30c3846658f38546eff049796`
- Speech 3 README final release status: `3cef665ace36720a29b06710799810e985a59143`
- Speech 3 source notes final release status: `94a5fd5610157440e0cc0630dab4493f26790b22`
- Speech 3 verification log final release status: `8c5dac2bf2d563d9fbb4f50bc69c65706e67ac0c`

Do not alter Speeches 1–3 unless separately requested.

## Current active work — Speech 4

- Source label: `உரை : 4`
- Printed date: `18.04.1990`
- Canonical ID: `1990-04-18-industries-debate`
- Locked source range: **scan pp.99–135 / printed pp.98–134**
- Expected mapped pages: **37**
- Gate C: **not started**
- Tamil status: **not started**
- English: **blocked until Tamil Gates C–E are complete**
- Speech 4 folder: **not yet created**

The Speech 3 ending boundary is locked: scan p.98 ends Speech 3. Scan p.99 / printed p.98 begins `உரை : 4`, dated `18.04.1990`.

## Immediate next action — Speech 4 Gate C Batch 1

Start Speech 4 with a bounded Tamil first-pass batch covering **scan pp.99–113 / printed pp.98–112**.

Before editing:

1. Read current `docs/ARCHIVAL_WORKFLOW.md`, this handover, `sources/2007-industrial-speeches/mapping.md`, and a completed released anthology speech folder as the structural precedent.
2. Reconfirm scan p.99 is the Speech 4 opening and preserve the printed heading/date/speaker label exactly as visible.
3. Create `speeches/1990/1990-04-18-industries-debate/` with the standard five files: `README.md`, `metadata.json`, `source-notes.md`, `transcript.md`, `verification-log.md`.
4. Transcribe scan pp.99–113 directly from rendered scan images. OCR may assist but is never canonical.
5. Add explicit `<!-- source-page: N -->` markers for every transcribed page.
6. Preserve source wording, period spelling, punctuation, numerals, printed English, speaker changes/interventions and page-transition continuities. Use an explicit review marker for anything genuinely unreadable instead of guessing.
7. Record the exact end-of-batch continuation point from scan p.113 and set the next page to **114**.
8. Keep the speech `in-progress`; do not run Gate D until the full mapped Speech 4 range pp.99–135 has been transcribed.
9. Do not begin English translation and do not touch Speech 5.

## Content to leave untouched

Unless explicitly requested otherwise:

- `speeches/1963/1963-03-21-industries-debate/`;
- `speeches/1970/1970-09-09-no-confidence-motion/`;
- `speeches/1981/1981-04-16-industries-debate/`;
- `speeches/1989/1989-05-03-industries-debate/`;
- released root index/data entries for Speeches 1–3 and the 1970 speech;
- unrelated sources/speeches;
- Speech 5 and later speeches while Speech 4 is active.

## End-of-session handover requirement

Always record canonical ID, exact pages completed/reviewed, current gate, Tamil status, unresolved readings, English status, files changed, commit SHA and exact next action.
