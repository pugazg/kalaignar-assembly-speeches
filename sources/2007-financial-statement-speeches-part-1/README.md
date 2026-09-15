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

No Tamil transcription has begun for this source.

## Parallel-witness / released-material rule

This anthology contains dates already represented elsewhere in the repository:

- **29.03.1971 / உரை 9** overlaps the existing `நமது நிலை` event/provenance record;
- **29.06.1971 / உரை 10** overlaps the existing `நமது விளக்கம்` event/provenance record;
- **07.03.1973 / உரை 12** overlaps the already **RELEASED** canonical entry `1973-03-07-financial-statement-reply`.

These are separate source witnesses. Do **not** overwrite or silently normalize any previously released canonical Tamil/English from this 2007 anthology. Any overlap must be handled explicitly as parallel-witness evidence.

## Exact next activity

Begin **Gate C for உரை 1 / 5.3.1958**, source scans **18–24 / printed pp.17–23**.

Because the entire first speech is only seven pages, process the complete speech in one bounded Gate-C first-pass transcription. Preserve exact source wording, punctuation, numerals, speaker/intervention labels and printed English. Use `<!-- source-page: N -->` markers. Do not begin Gate D/E or English in the same iteration.
