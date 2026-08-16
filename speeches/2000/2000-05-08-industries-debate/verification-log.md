# Verification log — உரை : 9 / 8.05.2000

## Source preflight and locked boundaries

Controlling PDF: **329 pages**; Speech-9 scan range **278–303**, printed range **277–302**. Scan image is authoritative. Scan p.277 closes Speech 8; p.278 begins Speech 9; p.303 closes Speech 9 with the printed ornament; p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`).

## Gate C — Tamil first pass

**Complete: 26/26 pages.** Canonical Gate-C-complete transcript commit: `1014c9528404a6334a94ab811d1b0b1142637d72`.

## Gate D — Tamil completeness/page-marker audit

**Passed.** Source-page markers 278–303 occur exactly once and in strict order; no Speech-8 or Speech-10 spillover; unresolved reading markers: 0.

## Gate E — strict Tamil source-fidelity verification

### Batch 1 — source pp.278–282 / printed pp.277–281

**Complete.** Definite correction: p.279 `பிள்ளைகளை யெல்லாம்` → `பிள்ளைகளையெல்லாம்`.

### Batch 2 — source pp.283–287 / printed pp.282–286

**Complete.** No canonical Tamil correction required.

### Batch 3 — source pp.288–292 / printed pp.287–291

**Complete.** No canonical Tamil correction required.

### Batch 4 — source pp.293–297 / printed pp.292–296

**Complete.** Definite correction: p.293 `இன்னொன்றியில்` → `இஃதன்னியில்`. Canonical checkpoint: `16f04ca171609602ea0cff3a73801df229020cb6`.

### Batch 5 — source pp.298–302 / printed pp.297–301

**Complete.** All five pages were visually re-read against the controlling scan. The source-sensitive p.298 forms were re-confirmed as:

- `சுப்பராயன் ஏற்றுக்கொள்கிறாரோ`
- `பழனிசாமி ஏற்றுக் கொள்கிறாரோ`
- `டி. மணி ஏற்றுக் கொள்கிறாரோ`
- `ஹேமச்சந்திரன் ஏற்றுக்கொள்கிறாரோ`

A subsequent pre-close canonical re-fetch established that `பழனிசாமி ஏற்றுக் கொள்கிறாரோ` and `டி. மணி ஏற்றுக் கொள்கிறாரோ` were already present in the canonical transcript. The earlier Batch-5 note describing those two forms as a current regression was therefore a **comparison-state error**, not an actual repository regression. No p.298 restoration was required.

The reread also re-confirmed p.299 `'TANCEM'`, `12-12-1994`, the Counter Affidavit English and Tamil explanation; p.300 both Government English sentences and `தயார் செய்வதன்` / `தயார் செய்து`; p.301 the full Ariyalur production sequence; and p.302 `அம்புஜா`, 85/145 rupees, `50 சதவிகிதத்திலே`, and the ending `111. நம்பர்`. Unresolved readings: **0**.

### Final Batch 6 — source p.303 / printed p.302

**Complete. Gate E passed.** The final page was directly verified against the rendered controlling scan through the final Chair intervention and the printed closing ornament.

One definite source-supported correction was required on p.303:

- `வெட்டுத் தீர்மானங்களையும்` → `வெட்டுத்தீர்மானங்களையும்`

The scan prints the compound continuously in the sentence beginning `இல்லாவிட்டாலும் கூட 111 ...`. The remainder of p.303 was confirmed as transcribed, including:

- `கேட்டு அமைகிறேன்.`;
- Chair call `திரு. பி. ஆர். சுந்தரம்.`;
- Sundaram's `2,000 கோடி` → `2,000 இலட்சம்`, explicitly `20 கோடி`;
- interrupted `ராசிபுரம்.....`;
- Chair's separately printed `200 கோடி, 20 இலட்சம், 2,000 கோடி`;
- final `அனுமதி கொடுத்துவிட்டேன், மாற்றிவிட்டார்கள். இனிமேல் உட்காருங்கள்.`;
- closing ornament confirming the end of Speech 9.

Scan p.304 was not included; it begins Speech 10.

## Gate E final result

- audited source range: **278–303**
- audited printed range: **277–302**
- verified pages: **26/26**
- cumulative definite Gate-E corrections: **3**
- unresolved readings: **0**
- `verified_against_scan`: **true**
- Tamil status: **verified**

Canonical Gate-E-complete transcript commit: `8ab00921d9e8e3d7c0742ee9c4f3943ae1b7b109`, blob `ac00a79863c0b0bdbaac6d9fb7b03f7e4c1bb577`.

## English gates

- Gate F: **not started; now unblocked**
- Gate G: **not started**

## Exact next activity

Begin **Gate F — English translation from the final verified Tamil only**, following `docs/ARCHIVAL_WORKFLOW.md` and the established Speech-1–8 release pattern. Preserve source-page correspondence and do not use OCR or the scan as the translation source where it conflicts with the final verified Tamil. Do not begin Speech 10.
