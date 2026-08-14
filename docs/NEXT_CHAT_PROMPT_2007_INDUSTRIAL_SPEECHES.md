# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF scan pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil; OCR/extracted text is only a helper.

## Released anthology state

Speeches **1–5** are fully released with verified Tamil and verified English. Do not modify them absent a separately justified correction.

## Active unit — Speech 6

- source label: `உரை : 6`;
- printed date: `23.04.1997`;
- canonical ID: `1997-04-23-industries-debate`;
- locked range: **scan pp.172–198 / printed pp.171–197**;
- total mapped scan pages: **27**;
- scan/printed relationship: **scan page = printed page + 1**;
- Gate A: complete at anthology level;
- Gate B: complete / locked;
- Gate C Tamil first-pass transcription: **complete — 27/27 pages**;
- Tamil status: **transcribed**, not verified;
- source-page markers: **172–198**, assertion-checked as exact, unique and monotonic;
- explicit unreadable/`[REVIEW]` markers: **0**;
- Gate D: **not started**;
- Gate E: **not started**;
- Gate F English: **blocked until Gates D and E pass**;
- Gate G: not started;
- Gate H: not started.

Canonical folder: `speeches/1997/1997-04-23-industries-debate/`.

## Gate C retained state

Batch 1 covered scan pp.172–186 / printed pp.171–185. Batch 2 covered scan pp.187–198 / printed pp.186–197.

The p.186→187 continuation is:

- p.186 ends `அவற்றுள் சிலவற்றை`
- p.187 begins `மாத்திரம் இங்கே உங்கள் முன்னால் வைக்க விரும்புகிறேன்.`

Batch 2 retained source-supported wording and printed English rather than silently correcting it, including `Financial Time 10 ஏப்ரல் 1997`, the Mark Nicholson car-industry quotations, `Single Window Clearance`, `Industrial Township`, `Executive Authority`, `(Seigniorage fee)`, `(Transport Permit)`, `(Technology Parks)`, `(Software Techno Parks)`, `L.N.G. (Liquified Natural Gas)`, the complete 13-item LNG bidder list, `Singapore Indian Chamber of Commerce`, `(Naphtha Crackers & Olefins)`, `(Bopp)`, `(Bisphenol-A)`, `(Siscal)`, and source Tamil forms such as `விடிவுகாலம்`, `பல்க்டிரக் இண்டார்மீடியட்ஸ்`, and `விடேன் தொடேன்`.

Final boundary is visually confirmed: scan p.198 ends Speech 6 with `நன்றி, வணக்கம். (மேசையைத் தட்டும் ஒலி).` followed by the decorative ornament. Scan p.199 begins `உரை : 7`, `14.05.1998`. No Speech-7 text belongs in Speech 6.

## Exact next action — Speech 6 Gate D

Perform **full-speech Tamil completeness/page-marker audit** only. Do not start Gate E or English in the same activity.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, this prompt, `sources/2007-industrial-speeches/mapping.md`, and every Speech-6 canonical file.
2. Audit canonical `transcript.md` across the full locked range scan pp.172–198.
3. Confirm exactly 27 source-page markers, exactly **172–198**, with no duplicate, gap, reordering or p.199 marker.
4. Confirm the opening matches scan p.172 (`உரை : 6`, `நாள் : 23.04.1997`) and the ending matches scan p.198, with p.199 beginning Speech 7.
5. Confirm all printed speaker changes/interventions/desk-thump or other contextual markers represented in the first pass remain represented through the final page.
6. Confirm unresolved/`[REVIEW]` marker count and record it explicitly.
7. If Gate D passes, update Speech-6 `metadata.json`, `README.md`, `source-notes.md`, and `verification-log.md` to record Gate D passed while Tamil remains **transcribed**, not verified.
8. Refresh this prompt and the handover with Gate-D commits and set the exact next activity to **Gate E — strict page-by-page Tamil visual/source-fidelity verification**.
9. English remains blocked until Gate E passes.

## Gate-C Batch-2 commits

- temporary application workflow created — `62ae30a9107e95373ef0c105deb42a9660b7fea3`;
- Batch-2 staging file created — `de69f5c5ef4d97a41379685f3cb2738ecd8c85ec`;
- assertion-checked canonical transcript / staging removal — `1266549a60a491ce1baa62f897a5f70e30e5aa8a`;
- temporary workflow removed — `cdbf29dad7ebc181bcd35ca9dc53732db328904d`;
- metadata marked Gate-C complete — `ca5abf2f5ce23093f0b917e15239a83dcceb9c7f`;
- Speech-6 README Gate-C completion — `f80aba3725e84962c0a067b06ff3f0dcf42e645e`;
- source notes Batch-2 / Gate-C record — `f47dceb20bd3abb5c16b2e9257a781fbd319e401`;
- verification-log Gate-C closure — `ac2bdf4574c0dad7cb014478d373b5de044ffad6`;
- verification-log assertion-notation fix — `6500a89199cd2a161372ae7d196cc7b7b29dc15e`.

All temporary Batch-2 workflow/staging artifacts were removed after the successful assertion-checked transcript update.
