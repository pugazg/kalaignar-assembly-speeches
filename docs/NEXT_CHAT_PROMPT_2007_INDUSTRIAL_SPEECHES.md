# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

## Source authority

Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition மே 2007.

- PDF scan pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- scan image is authoritative for Tamil; OCR/extracted text is only a helper.
- English translation and verification must use the **final verified Tamil**, not OCR or an earlier draft.

## Released anthology state

Speeches **1–5** are fully released with verified Tamil and verified English. Do not modify them absent a separately justified correction.

## Active unit — Speech 6

- source label: `உரை : 6`;
- printed date: `23.04.1997`;
- canonical ID: `1997-04-23-industries-debate`;
- locked range: **scan pp.172–198 / printed pp.171–197**;
- total mapped scan pages: **27**;
- scan/printed relationship: **scan page = printed page + 1**;
- Gate C Tamil first-pass transcription: **complete — 27/27 pages**;
- Gate D completeness/page-marker audit: **passed**;
- Gate E strict visual/source-fidelity verification: **passed — 27/27 pages**;
- Gate-E corrections: **6 total**;
- Tamil unresolved/`[REVIEW]` markers: **0**;
- Tamil status: **verified against the scan**;
- Gate F English translation: **complete — 27/27 source-page sections, 172–198**;
- Gate-F working file: `speeches/1997/1997-04-23-industries-debate/translation.md`;
- Gate-F structural assertion: **passed** — exact English page headings 172–198, no p.199 spillover, no `[REVIEW]` marker;
- unresolved translation questions recorded at Gate F: **0**;
- English status: **complete-unverified**;
- Gate G English fidelity verification: **not started**;
- Gate H: **not started**.

Canonical folder: `speeches/1997/1997-04-23-industries-debate/`.

## Gate E retained result

The full Tamil transcript was directly compared page-by-page with the controlling scan for scan pp.172–198 / printed pp.171–197. Six source-supported corrections were applied and no unresolved readings remain. Important deliberately retained source forms include `transparent appoach`, `(Flori-Culture)`, `ப்ளை ஆஷ்பேஸ்ட் பிளாக்ஸ்`, `Financial Time 10 ஏப்ரல் 1997`, the printed Mark Nicholson quotations, `Single Window Clearance`, `Industrial Township`, `Executive Authority`, `Load`, `(Seigniorage fee)`, `(Transport Permit)`, `(Technology Parks)`, `(Software Techno Parks)`, `L.N.G. (Liquified Natural Gas)`, the p.193 13-item bidder list, `விடிவுகாலம்`, `Singapore Indian Chamber of Commerce`, `(Window)`, `(Naphtha Crackers & Olefins)`, `Biaxially oriented poly propylene - (Bopp)`, `பிஸ்பினால்-ஏ (Bisphenol-A)`, `(Siscal)`, `பல்க்டிரக் இண்டார்மீடியட்ஸ்`, `'டான்சம்'`, `(சிரிப்பு)`, and `விடேன் தொடேன்`.

The final Tamil boundary remains locked: scan p.198 ends `நன்றி, வணக்கம். (மேசையைத் தட்டும் ஒலி).` followed by the decorative ornament; scan p.199 begins `உரை : 7`, `நாள் : 14.05.1998`. No Speech-7 spillover is present.

## Gate F — completed English translation

A full first-pass English translation was created from the **final verified Tamil only**, in `translation.md`, with one `### Source page N` section for each source page **172 through 198**.

Gate-F translation principles/results:

- exact source-page correspondence: **27/27**, sequence **172–198**;
- missing / duplicate / reordered English page headings: **0 / 0 / 0**;
- p.199 / Speech-7 spillover: **absent**;
- unresolved translation questions: **0**;
- parliamentary sequence, names, figures, dates, percentages, rupee values, acreage, megawatts, technical terms, lists and context markers were preserved;
- printed English already embedded in the source was retained in source form rather than silently repaired, including `Financial Time`, `Bernard Fintlay`, `transparent appoach`, `Liquified Natural Gas`, the Mark Nicholson quotations/headline and other printed English institutional/technical forms;
- Gate F does **not** make English verified.

## Exact next action — Speech 6 Gate G

Perform **Gate G — full English fidelity verification** against the final verified Tamil.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, this prompt, all Speech-6 canonical files and `translation.md`.
2. Use canonical verified `transcript.md` as the Tamil authority and `translation.md` as the English working layer.
3. Re-read **all 27 English source-page sections, 172–198**, against the corresponding verified Tamil source-page sections.
4. Check completeness and omissions/additions; page-boundary continuity; names and initials; dates, percentages, money, acreage, megawatts and other figures; technical/industrial terminology; speaker/context markers; lists; quotations; humour; and source anomalies.
5. Printed English already present in the Tamil source must remain source-faithful. Do not silently correct `Financial Time`, `Bernard Fintlay`, `transparent appoach`, `Liquified Natural Gas` or other source-supported anomalies merely from outside knowledge.
6. Pay particular attention to the p.174 export passage; pp.180–181 15-item Joint Sector list; pp.185–186 *Economist Intelligence Unit* passage; p.188 Mark Nicholson quotations; pp.189–190 Single Window / quarry / I.T.I. passages; pp.192–193 LNG project and complete 13-item bidder list; pp.194–196 Jayankondam/Singapore/TIDCO projects; p.197 rubber-industry humour; and the p.198 front-row/backward-wordplay and final closing.
7. Apply every English correction to `translation.md` and itemise every concrete Gate-G correction in `verification-log.md`.
8. If all 27 sections pass and no unresolved English fidelity issues remain, mark English `verified`, update metadata/README/source notes/log, and incorporate the corrected verified English after the Tamil source layer in canonical `transcript.md`, following the released Speech-5 precedent.
9. Gate G completion does **not** itself perform Gate H. Do not update root `README.md` or `data/speeches.json` until the separate Gate-H release/index activity.
10. Do not begin Speech 7 while Speech 6 Gate G is active.

## Gate F commits

- complete first-pass `translation.md` — `1f253edca1b52269b0921f74a5ab916f2fa3be99`;
- metadata Gate-F state — `9ced35950c584c2017e7c9b15adba13894a9f949`;
- Speech-6 README Gate-F state — `f478438f86a242740436bcee1f6447750c7912c1`;
- temporary Gate-F validation/docs workflow staged — `6d0abc2a34ccf2dd4d458f91ec2327fd0378546e`;
- Gate-F structural assertion + source-notes/verification-log record — `607ca9c3eca73ff0cf51085b9f170daa7bdc1720`;
- temporary Gate-F validation workflow removed — `961495e28b21240a19d560e11b0ecd0460538363`.
