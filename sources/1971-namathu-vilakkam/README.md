# நமது விளக்கம் — 1971 source package

This directory preserves the archival source package for the 1971 Government of Tamil Nadu booklet **`நமது விளக்கம்`**.

## Controlling textual source

`ACL-CPL_01732_நமது_விளக்கம்.pdf`

The rendered booklet scan is the controlling textual authority. OCR / parsed text is not usable for this PDF and must not control transcription.

## Source identity

- printed title: `நமது விளக்கம்`
- cover/title attribution: `தமிழக முதல்வர் கலைஞர் மு. கருணாநிதி`
- source introduction date / place: `சென்னை 21-7-1971`
- issuing body printed in the source introduction: `செய்தி விளம்பரத் துறை, தமிழ் நாடு அரசு`
- physical PDF pages: **61**
- file size: **17,896,700 bytes**
- SHA-256: `5e646d628f30a0c0ad9b1bf63d34e309995acb7359e4c7756e108f76717bd180`
- source text layer: **none / unusable**
- controlling authority: **rendered scan pixels**

## Source-internal event evidence

The publication introduction states that the 1971–72 financial statement was presented on **1-6-1971** in both Houses and that, after debate, Chief Minister M. Karunanidhi replied:

- in the **Legislative Assembly on 29-6-1971**;
- in the **Legislative Council on 30-6-1971**.

The booklet says those speeches are compiled here.

## Locked booklet structure

| Scan pages | Printed pages | Classification |
|---:|---:|---|
| 1 | — | front cover |
| 2 | — | title / portrait page |
| 3 | — | publication introduction, two-House/date evidence and imprint |
| 4–60 | implied p.3 through p.59 | `நமது விளக்கம்` — continuous edited speech compilation |
| 61 | — | back cover |

From scan p.5 through scan p.60, the stable visible relation is **printed page = scan page − 1**. Scan p.4 is the unnumbered body-opening page immediately before printed p.4 and is therefore retained as **implied printed p.3**.

No missing, duplicated or blank physical PDF pages were found in preflight.

## Gate A

**PASS / COMPLETE.**

## Gate B

**PASS / LOCKED at booklet-witness level.**

The booklet is not treated as two independently transcribed dated speeches. The source introduction identifies two underlying House/date events, but the body presents one continuous editorial compilation under the single heading `நமது விளக்கம்`; no printed second-speech title, divider or reliable internal House splice is asserted.

Therefore:

- reader-facing preservation follows **booklet order, scans 4–60**;
- exact Assembly/Council splice points are **not invented** from isolated speaker labels, House references, topic changes or illustrations;
- the two dated House events are recorded as provenance references only;
- the 29-06-1971 Assembly and 30-06-1971 Council Official Reports have now been retrieved and audited; see [`cross-witness-audit.md`](./cross-witness-audit.md). They remain separate witnesses. After explicit user authorization, the Council record was used for exactly **2 documented emendations** at booklet loci that remained unreadable after direct scan review (scans 11 and 37). No other Official-Report wording was imported.

This follows the repository's established edited-booklet treatment.

## Reader-facing entry

Booklet-level reader entry:

[`../../speeches/1971/1971-namathu-vilakkam/`](../../speeches/1971/1971-namathu-vilakkam/)

The entry has `date: null` because this source is an edited two-House compilation rather than one continuous dated Assembly transcript.

It is intentionally **not** added to the canonical dated speech table or `data/speeches.json` as a single Assembly event.

## Historical print

The 1971 source uses older Tamil print. Gate C.5 historical-glyph review is **mandatory** after Gate C and before Gate D.

## Current workflow state

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / LOCKED**
- Gate C — **PASS / COMPLETE — T1–T6 scans 4–60 / 57 of 57 pages**
- Gate C.5 — **PASS / COMPLETE — C.5-1–6 scans 4–60; 57/57 audited; 129 cumulative corrections across 109 source sites**
- cross-witness — **COMPLETE / 2 user-authorized Council-record emendations applied; current unresolved readings 0**
- Gate D — **PASS / COMPLETE — 57/57; 0 corrections; 0 unresolved completeness questions**
- Gate E — **PASS / COMPLETE — 57/57 verified; 101 corrections; 0 unresolved source-fidelity questions**
- Gate F — **PASS / COMPLETE — F1–F6 scans 4–60; 57/57 translated; 0 blocking questions**
- Gate G — **IN PROGRESS — G1–G5 scans 4–53 COMPLETE; 50/57 reviewed; 35 refinements; 0 blocking fidelity issues**
- Gate H — **BLOCKED / downstream**
- Tamil verified — **yes**
- English — **first pass complete / verification next**
- release — **not released**

## Exact next activity

Gate E and Gate F remain **PASS / COMPLETE**. Gate G G1–G5 is **COMPLETE through scans 4–53 / 50 of 57 pages reviewed**, with **35 cumulative English fidelity refinements** and **0 blocking fidelity issues**; verified Tamil remains unchanged. Exact next activity: **Gate G G6 / FINAL — scans 54–60 / printed pp.53–59**.
