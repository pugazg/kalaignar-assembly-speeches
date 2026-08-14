# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released anthology state

Speeches **1–5** are fully released with verified Tamil and verified English:

- Speech 1 — `1963-03-21-industries-debate`, scan pp.18–26;
- Speech 2 — `1981-04-16-industries-debate`, scan pp.27–61;
- Speech 3 — `1989-05-03-industries-debate`, scan pp.62–98;
- Speech 4 — `1990-04-18-industries-debate`, scan pp.99–135;
- Speech 5 — `1996-08-14-industries-debate`, scan pp.136–171.

Do not modify those released speeches absent a separately justified correction.

## Active unit — Speech 6

- source label: `உரை : 6`;
- printed date: `23.04.1997`;
- canonical ID: `1997-04-23-industries-debate`;
- locked range: **scan pp.172–198 / printed pp.171–197**;
- total mapped scan pages: **27**;
- scan/printed relationship: **scan page = printed page + 1**;
- Gate A source preflight: **complete at anthology level**;
- Gate B structural mapping: **complete and locked**;
- Gate C Tamil first-pass transcription: **in progress — Batch 1 complete, 15/27 pages**;
- completed Gate-C pages: **scan pp.172–186 / printed pp.171–185**;
- remaining Gate-C pages: **scan pp.187–198 / printed pp.186–197**;
- current source-page markers: **172–186**, unique and monotonic;
- explicit unreadable/`[REVIEW]` markers in Batch 1: **0**;
- Tamil status: **in-progress**, not verified;
- Gate D: **not started**;
- Gate E: **not started**;
- Gate F English translation: **blocked until complete Tamil passes Gates D and E**;
- Gate G: **not started**;
- Gate H: **not started**.

Canonical Speech-6 folder now exists at `speeches/1997/1997-04-23-industries-debate/` with `README.md`, `metadata.json`, `source-notes.md`, `transcript.md`, and `verification-log.md`.

## Gate C Batch 1 retained state

Batch 1 directly transcribed **scan pp.172–186 / printed pp.171–185** from rendered images of the controlling scan.

The first pass preserves source wording, historical spelling, punctuation where legible, numerals, figures, headings, speaker/context labels, interventions and embedded English. It includes the public-sector discussion, export/W.T.O. figures, SIPCOT/SIDCO/TIDCO/ELCOT history, the p.180–181 15-item joint-sector list, North Chennai Thermal Power Station, industrial-estate discussion, granite/minor-mineral tender policy, and the p.185–186 *Economist Intelligence Unit* passage.

Printed English/source forms retained include `Capital Subsidy`, `State Industries Promotion Corporation of Tamil Nadu`, `World Trade Organisation (W.T.O.)`, `Small Industries Development Corporation`, `Joint Sector`, `Associate Sector`, `Electronic Corporation of Tamil Nadu`, `Economist Intelligence Unit`, `India uncaged`, `Seeking opportunities in the South`, `Industry-Friendly Policies`, and the source form `transparent appoach`.

### Exact continuation

Scan p.186 / printed p.185 ends:

`அவற்றுள் சிலவற்றை`

Scan p.187 / printed p.186 begins:

`மாத்திரம் இங்கே உங்கள் முன்னால் வைக்க விரும்புகிறேன்.`

The p.187 line was inspected only to establish continuity and has **not yet** been added to canonical `transcript.md`.

## Exact next action — Speech 6 Gate C Batch 2

Complete the remaining **12 pages**, scan pp.187–198 / printed pp.186–197.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, this prompt, all Speech-6 tracking files and `sources/2007-industrial-speeches/mapping.md`.
2. Render and inspect scan pp.187–198 directly from the controlling PDF; the scan image remains authoritative.
3. Continue the p.186 sentence exactly from `அவற்றுள் சிலவற்றை` into p.187.
4. Append explicit `<!-- source-page: 187 -->` through `<!-- source-page: 198 -->` markers and transcribe all remaining source text.
5. Preserve source wording, historical spelling, punctuation, numerals, names, headings, interventions and printed English. Mark uncertainty rather than guessing.
6. Confirm the closing boundary on p.198 and that scan p.199 begins Speech 7 (`உரை : 7`, `14.05.1998`).
7. After all **27/27** Speech-6 pages are represented, update `metadata.json`, `README.md`, `source-notes.md`, and `verification-log.md` to Gate-C complete / Tamil `transcribed` as appropriate.
8. Then the exact next gate is **Gate D — full-speech completeness/page-marker audit**. Do not start Gate E or English translation in the same first-pass activity unless separately requested.

## Gate-C Batch-1 commits

- canonical Tamil transcript, scan pp.172–186 — `c7868e2a823bb414db06944f1da4c799fa0a3f43`;
- metadata / Gate-C progress — `4969c29e39185696cb3ed8289802d18c0597813b`;
- Speech-6 README — `72a39a311e495e7407b1a01787a9aa5528fadf6c`;
- source notes — `7405f636200b4c48e42e8b90461d562ceed1a9dc`;
- verification log — `bb08fb1f97ec913928a16fb8e660461de3c4f7f4`;
- handover updated for Batch 1 — `a24965898334df8f2f061b0b3a0f5c48abf1de9c`.
