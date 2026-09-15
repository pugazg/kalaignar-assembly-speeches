# நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் — பாகம் 1

This source package preserves the 2007 anthology **`நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`** as a new controlling source witness.

## Gate A — source preflight

Status: **PASS / COMPLETE**.

### Controlling scan

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- actual physical PDF pages: **546**
- file size: **393,027,493 bytes**
- SHA-256: `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- usable parsed text layer: **none**
- controlling textual authority: **rendered scan pixels**
- interface note: the file viewer exposed only the first 150 rendered pages, but the actual PDF contains 546 pages; the PDF byte-level page count controls.

### Publication evidence from the scan

- printed title: `நிதிநிலை அறிக்கை மீது கலைஞரின் சட்டமன்ற உரைகள் (பாகம் - 1)`
- author attribution: `கலைஞர் மு. கருணாநிதி`
- publisher: `தமிழ்க்கனி பதிப்பகம்`, சென்னை - 600 004
- sales-rights imprint: `பூம்புகார் பதிப்பகம்`, 127 (ப.எண். 63), பிரகாசம் சாலை (பிராட்வே), சென்னை - 600 108
- first edition: **மே, 2007**
- printed price: **ரூ. 300/-**
- rights: **ஆசிரியருக்கே**
- printer / binder: **Eagle Press, Chennai - 600 013**

### Physical structure

- scans **1–17** — publication/front matter and internal title matter;
  - scan 1 — cover;
  - scan 2 — title/publisher page;
  - scan 3 — edition/price/printer page;
  - scans 4–9 — `என்னுரை`;
  - scans 10–14 — `பதிப்புரை`;
  - scans 15 and 17 — blank/verso leaves with heavy reverse show-through; no new speech body admitted;
  - scan 16 — internal section title;
- scans **18–545** — 19 numbered `உரை` units;
- scan **546** — closing portrait/back matter.

From scan 18 through scan 545, the printed-page relation is stable:

`printed page = PDF scan page - 1`.

### Source condition

The scan is image-only. Most speech pages are readable at source resolution. There is intermittent bleed-through and library stamping/handwriting that must be distinguished from printed text. The 2007 anthology is modern typesetting despite reprinting historical speeches; Gate C.5 historical-glyph review is therefore **provisionally N/A for this edition**, subject to reopening if a page-specific legacy typeform anomaly is actually encountered.

## Gate B — anthology structural mapping

Status: **PASS / COMPLETE / LOCKED**.

All **19** printed speech units were mapped and then boundary-rechecked. See:

[`mapping.md`](./mapping.md)

Speech 1 / 5.3.1958 Tamil is **VERIFIED — scans 18–24 / printed pp.17–23, 7/7 pages**. Gate F English first pass is also **COMPLETE — 7/7 pages**; English is not yet verified. No other speech has begun.

## Parallel-witness / released-material rule

This anthology contains dates already represented elsewhere in the repository:

- **29.03.1971 / உரை 9** overlaps the existing `நமது நிலை` event/provenance record;
- **29.06.1971 / உரை 10** overlaps the existing `நமது விளக்கம்` event/provenance record;
- **07.03.1973 / உரை 12** overlaps the already **RELEASED** canonical entry `1973-03-07-financial-statement-reply`.

These are separate source witnesses. Do **not** overwrite or silently normalize any previously released canonical Tamil/English from this 2007 anthology. Any overlap must be handled explicitly as parallel-witness evidence.

## Speech 1 current state

Reader/work entry:

[`../../speeches/1958/1958-03-05-financial-statement-debate/`](../../speeches/1958/1958-03-05-financial-statement-debate/)

- Gate C — **COMPLETE / 7 of 7 pages**
- source markers — **18→24 exactly once in first-pass transcript**
- unresolved first-pass readings — **0**
- Tamil — **VERIFIED / verified_against_scan=true**
- Gate D — **PASS / COMPLETE — 7/7 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 7/7 pages; 9 source-fidelity corrections; 0 unresolved readings**
- Gate F English — **COMPLETE / 7 of 7 pages; NOT YET VERIFIED**
- Gate G — **NOT STARTED / next**

## Speech 1 Tamil verification closure

Gate C and Gate D remain complete. Gate E is **PASS / COMPLETE — 7/7 pages**.

- Gate-E source-fidelity corrections — **9**
- unresolved readings — **0**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED for this modern 2007 typesetting; no legacy-glyph anomaly observed**

Correction sites: scan 19 ×2, scan 20 ×4, scan 23 ×1, scan 24 ×2. Full details are in the speech `verification-log.md`.

## Gate F result for Speech 1

**COMPLETE — 7/7 pages.**

The working first-pass English is in the speech entry's `translation.md`. It was translated only from verified Tamil; outside wording was not used. English `verified_against_tamil=false`.

## Exact next activity

Perform **Gate G full English fidelity and voice review** against the verified Tamil for scans **18–24 / printed pp.17–23**. Do not begin Speech 2 in the same iteration.
