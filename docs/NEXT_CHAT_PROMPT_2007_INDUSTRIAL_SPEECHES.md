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
- Gate D completeness/page-marker audit: **passed**;
- Tamil status: **transcribed**, not verified;
- source-page markers: **27 markers, exactly 172–198**, no gaps, duplicates or reordering;
- Speech-7/p.199 spillover: **none**;
- explicit unreadable/`[REVIEW]` markers: **0**;
- Gate E strict visual/source-fidelity verification: **not started**;
- Gate F English: **blocked until Gate E passes**;
- Gate G: not started;
- Gate H: not started.

Canonical folder: `speeches/1997/1997-04-23-industries-debate/`.

## Gate D retained result

Gate D audited the complete Speech-6 transcript as a structural unit. It confirmed:

- every mapped scan page **172–198** is represented exactly once and in order;
- the opening matches scan p.172: `உரை : 6`, `நாள் : 23.04.1997`, followed by `மாண்புமிகு கலைஞர் மு. கருணாநிதி :`;
- the source remains one continuous Kalaignar speech after the opening speaker label, with no later separate speaker-change heading in the mapped pages;
- printed contextual markers such as `(மேசையைத் தட்டும் ஒலி)` and p.197 `(சிரிப்பு)` remain represented;
- p.198 ends with the Krishnagiri mango-factory assurance and `நன்றி, வணக்கம். (மேசையைத் தட்டும் ஒலி).`, followed by the decorative ornament;
- scan p.199 begins `உரை : 7`, dated `14.05.1998`, and no Speech-7 material is present in Speech 6;
- unresolved/`[REVIEW]` markers remain **0**.

Gate D made no wording changes. It proves completeness/structure only; Tamil remains `transcribed`, not `verified`.

## Exact next action — Speech 6 Gate E Batch 1

Begin **strict page-by-page Tamil visual/source-fidelity verification** for **scan pp.172–186 / printed pp.171–185** only.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, this prompt, `sources/2007-industrial-speeches/mapping.md`, and every Speech-6 canonical file.
2. Use the rendered controlling scan pages 172–186 as authority; OCR/extracted text may only assist.
3. Compare each page directly against canonical `transcript.md` for words/characters, names/initials, numerals, dates, percentages, monetary values, units, headings, opening speaker label, embedded English, transliterations, punctuation where legible, contextual markers and page transitions.
4. Preserve unusual source spelling/wording when visually supported; do not silently modernise or repair source forms.
5. Apply every source-supported correction to canonical `transcript.md` and itemise it in `verification-log.md`.
6. Record explicitly confirmed unusual source forms and any unresolved readings.
7. At the end of Batch 1, record exact verified range **172–186**, correction count, unresolved count, and the next Gate-E continuation page **187**.
8. Update `metadata.json`, `README.md`, `source-notes.md`, `verification-log.md`, the handover and this prompt.
9. Do not mark Tamil `verified` until Gate E covers the entire **172–198** range.
10. Do not begin English translation; it remains blocked until Gate E passes completely.

## Gate-D commits

- metadata Gate-D state — `60b8dd4c91593525ecf53e4ddbda911d28fd6923`;
- Speech-6 README Gate-D state — `6e9056baeb6336354702ac2a0a12e356465c979e`;
- source-notes Gate-D record — `60a6ffb4a6199d206fb869152fef99912aeb052f`;
- verification-log Gate-D closure — `58a8be43b8c960a7ac7ed84bbeddc2edcf2325bf`.

Gate C's assertion-checked canonical transcript commit remains `1266549a60a491ce1baa62f897a5f70e30e5aa8a`. No transcription wording was changed during Gate D.
