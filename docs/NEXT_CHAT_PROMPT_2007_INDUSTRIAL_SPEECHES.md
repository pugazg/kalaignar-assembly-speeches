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
- Gate E strict Tamil visual/source-fidelity verification: **passed — 27/27 pages**;
- Gate-E corrections: **6 total**;
- Tamil unresolved/`[REVIEW]` markers: **0**;
- Tamil status: **verified against the scan**;
- Gate F English translation: **complete — 27/27 source-page sections, 172–198**;
- Gate G English fidelity verification: **passed — 27/27 sections**;
- Gate-G corrections: **12**;
- unresolved English fidelity issues: **0**;
- English status: **verified against the final verified Tamil**;
- canonical `transcript.md`: **complete verified Tamil followed by complete verified English**;
- `translation.md`: retained as the verified English working companion;
- Gate H release/indexing: **not started**.

Canonical folder: `speeches/1997/1997-04-23-industries-debate/`.

## Gate E retained Tamil result

Gate E directly compared the complete Tamil scan range 172–198 against canonical `transcript.md` and applied six source-supported corrections. No unresolved Tamil readings remain. The ending boundary remains locked: scan p.198 ends `நன்றி, வணக்கம். (மேசையைத் தட்டும் ஒலி).` followed by the decorative ornament; scan p.199 begins `உரை : 7`, `நாள் : 14.05.1998`. No Speech-7 spillover is present.

Important source-supported forms deliberately retained include `transparent appoach`, `(Flori-Culture)`, `ப்ளை ஆஷ்பேஸ்ட் பிளாக்ஸ்`, `Financial Time 10 ஏப்ரல் 1997`, `Bernard Fintlay`, the Mark Nicholson quotations/headline, `Single Window Clearance`, `Industrial Township`, `Executive Authority`, `Load`, `(Seigniorage fee)`, `(Transport Permit)`, `(Technology Parks)`, `(Software Techno Parks)`, `L.N.G. (Liquified Natural Gas)`, the p.193 13-item bidder list, `விடிவுகாலம்`, `Singapore Indian Chamber of Commerce`, `(Window)`, `(Naphtha Crackers & Olefins)`, `Biaxially oriented poly propylene - (Bopp)`, `பிஸ்பினால்-ஏ (Bisphenol-A)`, `(Siscal)`, `பல்க்டிரக் இண்டார்மீடியட்ஸ்`, `'டான்சம்'`, `(சிரிப்பு)`, and `விடேன் தொடேன்`.

## Gates F–G — completed English layer

Gate F produced a complete English translation from the final verified Tamil with exactly **27 `### Source page N` sections, 172–198**. Gate G then re-read every English section against its corresponding verified Tamil section and passed with **12 concrete fidelity corrections** and **0 unresolved English fidelity issues**.

Gate-G corrections:

1. p.172 moved `(Sound of desk-thumping.)` to immediately after the request to borrow Anna's heart, matching the verified Tamil sequence.
2. p.177 `industrial complex` → `industrial undertaking` for `தொழில் நிறுவனம்`.
3. p.178 restored the explicit 1972 `Tamil Nadu Electronics Corporation — ‘ELCOT’` clause while retaining the later 1975 `Electronic Corporation of Tamil Nadu ... ‘ELCOT’` statement, preserving the source's internal chronology rather than reconciling it.
4. p.181 `Inter Continental Leathers Limited` → `Indar Continental Leathers Limited`, preserving `இண்டார்`.
5. p.182 `foundation ceremony` → `commencement ceremony` for `தொடக்க விழா`.
6. p.184 `Vigilance Wing` → `Vigilance Task Force` for `விழிப்புப் பணிக்குழு`.
7. p.191 `each over 50 hectares` → `each covering 50 hectares`.
8. pp.194–195 changed the Jayankondam passage from `lignite` to `coal` throughout, preserving `நிலக்கரி` without adding specificity.
9. p.195 `a single window (Window)` → `a window (Window)`.
10. p.197 `TANCEM` → `Tansam`, preserving printed/transliterated `'டான்சம்'` rather than normalising from outside knowledge.
11. p.197 `go back to their constituencies` → `go back home` for `ஊருக்குப் போவோம்`.
12. p.197 restored verified odd wording `விடேன் தொடேன்` as `I will not leave it; I will not touch it` rather than smoothing it away.

Printed English/source anomalies such as `Financial Time`, `Bernard Fintlay`, `transparent appoach`, `Liquified Natural Gas` and the Mark Nicholson material remain deliberately source-faithful.

Gate-G final assertions:

- English source-page sections: **27/27**, exactly **172–198**;
- missing / duplicate / reordered English sections: **0 / 0 / 0**;
- p.199 / Speech-7 spillover: **none**;
- unresolved English fidelity issues: **0**;
- `verified_against_tamil`: **true**;
- English status: **verified**;
- corrected English is incorporated after verified Tamil in canonical `transcript.md`.

## Exact next action — Speech 6 Gate H

Perform **Gate H — canonical release/indexing** for Speech 6.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, the handover, this prompt, and all Speech-6 files: `README.md`, `metadata.json`, `source-notes.md`, `verification-log.md`, `translation.md`, and canonical `transcript.md`.
2. Reconcile canonical identity and source metadata across all files: `1997-04-23-industries-debate`, printed date `23.04.1997`, scan pp.172–198 / printed pp.171–197.
3. Confirm canonical `transcript.md` contains exactly the complete verified Tamil source layer followed by exactly 27 verified English source-page sections 172–198, with no p.199/Speech-7 spillover.
4. Confirm Tamil status is `verified`, `verified_against_scan: true`, Tamil unresolved readings 0, English status `verified`, `verified_against_tamil: true`, and unresolved English fidelity issues 0.
5. Update root `README.md` to add/release Speech 6 using the existing released-speech format.
6. Update `data/speeches.json` with Speech 6 and at minimum `transcription_status: verified`, `verified_against_scan: true`, and `translation_status: verified`, matching the established records for released speeches.
7. Record Gate-H release checks in Speech-6 documentation and refresh this prompt/handover with the exact next continuation.
8. Only after Gate H closes may work begin on Speech 7: `உரை : 7`, `14.05.1998`, locked scan pp.199–240 / printed pp.198–239. Since anthology Gates A–B are already locked, Speech 7 should begin at **Gate C Tamil first-pass transcription, scan p.199**.
9. Do not modify released Speeches 1–5 absent a separately justified correction.

## Gate G commits / cleanup

- Gate-F completion handover HEAD — `bfe994661c0da19e194bc377a43909ef65691e38`;
- temporary Gate-G finalize workflow staged — `d599465b10c8ae484afa32aeb726572ee7901926`;
- temporary Gate-G retry workflow staged — `746338da3ac0903eb6b6801cb4d40f27538b168f`;
- Gate-G verified English + canonical merge + Speech-6 documentation — `921c196ba069ef90cc29b09e71b9700bfeccf2d6`;
- temporary finalize workflow removed — `adda2092f26538abb3e3998dcc5a157e1d02eaa2`;
- temporary retry workflow removed — `b22885f5f95cf13082714c49b135c483d071aeca`.

No temporary Speech-6 Gate-G workflow should remain in the repository tree.
