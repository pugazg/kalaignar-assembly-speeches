# Next-chat prompt — Speech 7 Gate H / 14.05.1998

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Continue **Speech 7** from the 2007 anthology `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`. **Do not restart Tamil transcription, Gate E, Gate F or Gate G. Tamil and English are both fully verified.**

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Inspect the complete Speech-7 entry under `speeches/1998/1998-05-14-industries-debate/`.
4. Inspect `data/speeches.json` and the root README / speech index before editing them.
5. Preserve the verified Tamil source layer exactly; Gate H is release/canonicalisation work, not retranscription.

## Speech 7 state

- canonical ID: `1998-05-14-industries-debate`
- source scan pages: **199–240**
- printed pages: **198–239**
- Tamil Gate E: **passed — 42/42 pages verified against scan**
- Tamil unresolved readings: **0**
- English Gate F: **complete — 42/42 pages**
- English Gate G: **passed — complete 42-page fidelity check**
- Gate-G corrections: **0**
- unresolved translation questions: **0**
- English status: **verified against final verified Tamil**
- Speech-8 boundary: source p.241; excluded from Speech 7

Current checkpoints:

- Gate-F canonical completion: `8ce93472ccb01bb2efd41435d4745d3c97f9da1a`
- Gate-G review artifact: `acbfa87f6d806bcae98f51e4df7ad1709fc094ef`
- metadata after Gate G: `9bd37509faab5744c4f3b4bc840ebe394a5b6e3b`
- verification log after Gate G: `69dd7674401c3704bcf566efa76f80940e83c73e`
- README after Gate G: `2276060d962d0fd1811d1f97a86bd8d6fdb13e02`
- handover after Gate G: `b242d74f76095d9bd4917a1996ef314c28d89a7e`

## Exact next activity — Gate H / release canonicalisation

1. Reconcile the verified English layer into the canonical speech presentation required by `docs/ARCHIVAL_WORKFLOW.md`, following existing repository conventions. Do **not** alter the verified Tamil wording.
2. Inspect and update `data/speeches.json` for Speech 7 as appropriate.
3. Inspect and update the root README / speech index as appropriate.
4. Reconcile statuses and paths across Speech-7 `metadata.json`, README, `source-notes.md`, `verification-log.md`, `translation-review.md`, transcript/translation presentation and repository indexes.
5. Confirm exact source-page coverage **199–240**, printed pages **198–239**, 42/42 Tamil verified, 42/42 English verified, and zero p.241/Speech-8 spillover.
6. Leave Speech 7 release-ready and auditable.
7. Do not begin Speech 8 until Gate H for Speech 7 is complete.
