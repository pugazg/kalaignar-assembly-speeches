# Verification log — உரை : 9 / 8.05.2000

## Source preflight and locked boundaries

Controlling PDF: 329 pages; Speech-9 scan range **278–303**, printed range **277–302**. Scan image is authoritative.

## Gate C — Tamil first pass

**Complete: 26/26 pages.** Canonical Gate-C-complete transcript commit: `1014c9528404a6334a94ab811d1b0b1142637d72`.

## Gate D — Tamil completeness/page-marker audit

**Passed.** Source-page markers 278–303 are present exactly once and in strict order; no Speech-8 or Speech-10 spillover; unresolved reading markers: 0.

## Gate E — strict Tamil source-fidelity verification

### Batch 1 — source pp.278–282 / printed pp.277–281

**Complete.** Five pages directly re-read. One definite correction: p.279 `பிள்ளைகளை யெல்லாம்` → `பிள்ளைகளையெல்லாம்`. Unresolved: 0.

### Batch 2 — source pp.283–287 / printed pp.282–286

**Complete.** No canonical Tamil source-text correction required. Cumulative coverage: 10/26.

### Batch 3 — source pp.288–292 / printed pp.287–291

**Complete.** No canonical Tamil source-text correction required. Cumulative coverage: 15/26.

### Batch 4 — source pp.293–297 / printed pp.292–296

**Complete.** One definite correction applied: p.293 `இன்னொன்றியில்` → `இஃதன்னியில்`. Cumulative coverage: 20/26; cumulative Gate-E corrections: 2; unresolved: 0. Canonical transcript commit: `16f04ca171609602ea0cff3a73801df229020cb6`.

### Batch 5 — source pp.298–302 / printed pp.297–301

**Visual source-fidelity reread complete.** All five pages were rendered from the controlling 329-page scan and compared directly with the current canonical transcript.

- pages visually checked in Batch 5: **5**;
- cumulative visual Gate-E coverage: **25/26**;
- audited source range: **278–302**;
- audited printed range: **277–301**;
- unresolved readings: **0**;
- next source page: **303**.

The rendered scan re-confirms the source-sensitive p.298 auxiliary spacing established earlier:

- `பழனிசாமி ஏற்றுக் கொள்கிறாரோ`
- `டி. மணி ஏற்றுக் கொள்கிறாரோ`

During this Batch-5 comparison, the current canonical transcript was found to contain a **regression**: both forms currently appear as `ஏற்றுக்கொள்கிறாரோ`, even though correction commit `8ed2c3685857e16b368139252386b623875284ab` had previously restored the scan-supported spacing. These are not new source readings; they are two pending canonical repairs caused by later transcript-state regression. Gate E must not be closed until they are restored.

No other definite Batch-5 discrepancy was found. Direct visual reread re-confirmed without normalization or external reconciliation:

- p.298 `ரைட்`, `சுப்பராயன் ஏற்றுக்கொள்கிறாரோ`, `ஹேமச்சந்திரன் ஏற்றுக்கொள்கிறாரோ`, and the source's varying auxiliary spacing;
- p.299 `'TANCEM'`, `12-12-1994`, `Counter Affidavit`, the printed English beginning `In the present situation, there is no shortage of cement...`, and `மூன்றாவது பிரதிவாதியான டான்செம் நிறைவேற்றவில்லை.`;
- p.300 the printed Government English sentences `The Government of Tamil Nadu are not in a position...` and `The Government have taken a decision...`, plus `சிமெண்ட் தயார் செய்வதன்` / `குறைந்த விலையில் தயார் செய்து`;
- p.301 production figures `3,33,000`, `4,13,000`, `4,34,000`, `3,77,000`, `4,29,000`, `4,63,000`, `5,38,000`, `4,87,000`, `4,46,000` tons;
- p.302 `அம்புஜா`, `85 ரூபாய்`, `145 ரூபாய்`, `50 சதவிகிதத்திலே`, and the ending `வெட்டுத் தீர்மானங்களுடைய எண்ணிக்கை 111. நம்பர்`.

### Current Gate-E truth

Gate E remains **in progress**. Visual comparison is complete through source p.302, but the two p.298 canonical spacing regressions above must be repaired before final closure. Tamil remains **not verified**.

## English gates

- Gate F: **blocked / not started**;
- Gate G: **not started**.

## Exact next activity

Before closing Gate E, restore the two scan-supported p.298 canonical forms `பழனிசாமி ஏற்றுக் கொள்கிறாரோ` and `டி. மணி ஏற்றுக் கொள்கிறாரோ`, documenting the repair as restoration of the already-established correction commit `8ed2c3685857e16b368139252386b623875284ab`. Then directly verify the final source/scan p.303 / printed p.302 against the controlling scan. Only after both repairs and p.303 verification may Gate E be marked complete and `verified_against_scan=true`. Do not begin English or Speech 10 in that bounded activity.
