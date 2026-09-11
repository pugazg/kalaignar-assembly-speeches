# Historical Tamil glyph audit — 7-3-1973 Assembly reply

## Gate

**Gate C.5 — HISTORICAL TAMIL GLYPH AUDIT**

Status: **NOT STARTED / NEXT**

Controlling source: `TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

Locked Assembly range:

- scan pages: **4–40**
- printed pages: **3–39**

Controlling method: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Audit rule

> Read character identity, not modern visual resemblance.

This audit decodes historical Tamil typeforms into the correct modern Unicode character identity. It does **not** authorize modernization of spelling, grammar, vocabulary, punctuation, compounds or spacing.

Minimum known reform-sensitive families that must be checked on **every page**:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Requirements:

- inspect the complete page first at enlarged/native resolution;
- use source pixels as authority; OCR is discovery-only;
- compare same-edition/same-font examples for uncertain clusters;
- never global-replace;
- record each correction individually with scan provenance;
- keep glyph-identity corrections separate from ordinary transcription corrections;
- if identity remains uncertain, do not guess and do not pass the gate.

## Progress

| Scan range | Printed pages | Status | Glyph corrections | Unresolved clusters |
|---|---|---|---:|---:|
| 4–40 | 3–39 | NOT STARTED | 0 | not yet assessed |

## Correction ledger

| Scan | Printed page | Earlier/apparent reading | Source-supported reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|

## Exact next activity

Begin the Gate C.5 source-pixel audit at **scan p.4 / printed p.3**. Process in bounded page batches, check all 13 families on every page, synchronize this ledger and `verification-log.md` after each batch, and do not start Gate D until the full scans 4–40 audit passes.
