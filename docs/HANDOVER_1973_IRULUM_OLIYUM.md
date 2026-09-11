# Handover — 1973 `இருளும் ஒளியும்`

## Repository

`pugazg/kalaignar-assembly-speeches` — branch `main`

**LIVE MAIN IS AUTHORITATIVE.** Fetch live `main` first in every continuation and preserve any newer durable work.

Active source package:

`sources/1973-irulum-oliyum/`

Active Unit 1 reader-facing entry:

`speeches/1973/1973-03-07-financial-statement-reply/`

## Controlling source

The only transcription/verification authority for this work is:

`TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

Locked identity:

- physical scans: **64**
- file size: **101,602,456 bytes**
- SHA-256: `0330e70d6d7a62e2c84d712966a8436b91956d722134bc71ca0b2329283f8694`
- publication title: `இருளும் ஒளியும்`
- cover attribution: `தமிழக முதல்வர் டாக்டர் மு. கருணாநிதி`
- issuing body: `செய்தி, மக்கள் தொடர்புத்துறை, தமிழ்நாடு அரசு`
- place/date: `சென்னை, 16-3-1973`
- printer: `தமிழரசு அச்சகம்`
- image-only controlling source; source pixels outrank OCR and context
- do not commit the PDF

## Locked source structure

| Scan pages | Printed pages | Classification |
|---:|---:|---|
| 1 | — | cover |
| 2 | — | title/photo |
| 3 | — | `பதிப்புரை` / source preface |
| 4–40 | 3–39 | Unit 1 — `சட்டப் பேரவையில்`, dated 7-3-1973 |
| 41–62 | 40–61 | Unit 2 — `சட்டமன்ற மேலவையில்`, dated 8-3-1973 |
| 63 | — | printer/imprint |
| 64 | — | back cover / later donor sticker |

Canonical Unit 1 ID:

`1973-03-07-financial-statement-reply`

Canonical Unit 2 ID is mapped as:

`1973-03-08-financial-statement-reply`

**Do not cross the scan-40 → scan-41 boundary while finishing Unit 1.**

## Mandatory workflow documents

Read before source-dependent continuation:

1. `docs/ARCHIVAL_WORKFLOW.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. this handover
4. `sources/1973-irulum-oliyum/mapping.md`
5. `speeches/1973/1973-03-07-financial-statement-reply/README.md`
6. `speeches/1973/1973-03-07-financial-statement-reply/metadata.json`
7. `speeches/1973/1973-03-07-financial-statement-reply/verification-log.md`
8. `speeches/1973/1973-03-07-financial-statement-reply/historical-glyph-audit.md`
9. `speeches/1973/1973-03-07-financial-statement-reply/completeness-audit.md`
10. `speeches/1973/1973-03-07-financial-statement-reply/source-fidelity-audit.md`

## Unit 1 durable gate state

`சட்டப் பேரவையில்` / 7-3-1973 / scans **4–40** / printed pp. **3–39**

- Gate A — **PASS**
- Gate B — **PASS / LOCKED**
- Gate C — **COMPLETE**, scans 4–40 / printed pp.3–39
- Gate C.5 historical Tamil glyph audit — **PASS / COMPLETE**
- Gate D Tamil completeness audit — **PASS / COMPLETE**
- Gate E Tamil source-fidelity verification — **IN PROGRESS**
- English Gates F–G — **BLOCKED**
- Gate H — **not reached**

Current Gate E coverage:

- E1 scans 4–13 / printed pp.3–12 — **PASS**, 0 corrections
- E2 scans 14–23 / printed pp.13–22 — **PASS**, 2 corrections
- E3 scans 24–33 / printed pp.23–32 — **PASS**, 3 corrections
- cumulative Gate E corrections: **5**
- new unresolved Gate-E fidelity questions through scan 33: **0**
- `verified_against_scan`: **false**
- exact remaining Gate E range: **scans 34–40 / printed pp.33–39**

## Historical-glyph gate

Gate C.5 was introduced specifically to prevent old Tamil typeforms from being read as modern look-alikes.

Full result:

- scans 4–40 audited
- all 13 minimum reform-sensitive families checked page by page
- cumulative historical-glyph corrections: **3**
- unresolved historical-glyph clusters: **0**
- global replacements: **0**

Accepted historical-glyph corrections:

1. scan 4 / printed p.3: `பெறுமல்` → `பெறாமல்` — first occurrence
2. scan 4 / printed p.3: `பெறுமல்` → `பெறாமல்` — second occurrence
3. scan 12 / printed p.11: `மாற்றுந்தாய்` → `மாற்றாந்தாய்`

These are already canonical and should not be reopened without direct contrary scan evidence.

## Gate E corrections accepted so far

### E2

1. scan 14 / printed p.13:
   - earlier: `மதிப்புக்குரிய முதலமைச்சர் அவர்கள் திரு கோபால்`
   - source-supported: `மதிப்புக்குரிய முதலமைச்சரவர்கள் திரு கோபால்`

2. scan 21 / printed p.20 illustration:
   - earlier: `வரிசலுகை`
   - source-supported: `வரி ஏய்ப்பு`

### E3

3. scan 31 / printed p.30 illustration:
   - earlier: `கைத்தறியாளர்களுக்குத் நூல்கள் அரசு நேரிடை விநியோகம்`
   - source-supported: `கைத்தறியாளர்களுக்கு நூல்கள் அரசு நேரிடை விநியோகம்`

4. scan 32 / printed p.31 illustration:
   - earlier: `விவசாயத்திற்கும் மின்சாரம்`
   - source-supported: `விவசாயத்திற்கு மின்சாரம்`

5. scan 33 / printed p.32 body:
   - earlier: `மின் வெட்டு நிலமை`
   - source-supported: `மின் வெட்டு நிலைமை`

## Known source-condition holds

Physical gutter loss is present on:

- scans 4–5
- scans 10–11
- scans 20–21
- scans 25–27
- scans 34–35

Unrecoverable text is marked `⟦scan-crop⟧` and must **not** be reconstructed from grammar, memory, parallel text, OCR or external sources.

Scan 13 contains a cartoon. Confident labels are already represented; smaller labels remain unresolved where the pixels do not support a secure reading.

Printed English belongs to the source layer and must be preserved verbatim. “No English yet” means **no English translation**, not removal of English printed in the source.

## Active batch policy

Process **10 scan pages per iteration**.

If fewer pages remain before a locked gate or speech boundary, process only the remaining pages. Never cross a speech/gate boundary merely to fill the batch.

## Exact next activity

Finish **Gate E — Tamil source-fidelity verification** for Unit 1 with:

- **scan pp.34–40**
- **printed pp.33–39**
- final **7-scan remainder**

For each page:

1. inspect the complete rendered page at high resolution;
2. compare every visible Tamil word/character with the canonical transcript;
3. verify names/initials, numerals, dates, percentages, money/units, embedded English, headings, speaker labels and punctuation where legible;
4. check page-to-page continuity for omissions or accidental repetition;
5. preserve the scan-34/35 crop holds exactly; do not infer lost text;
6. recheck the `குன்றின் மேலிட்ட விளக்கு` discussion, Manali Kandasami exchange, `ஆரிய மாயை` verse, `முடிப்புரை`, and the final Assembly closing paragraph;
7. apply only source-proven corrections and log each one;
8. do not enter Unit 2.

If scans 34–40 pass with no unresolved Gate-E fidelity issue:

- mark Gate E **PASS / COMPLETE — scans 4–40 / printed pp.3–39**;
- set `transcription.verified_against_scan=true`;
- record final Gate-E correction total;
- synchronize README, metadata, verification log, source-fidelity audit and source mapping;
- commit the bounded result;
- report the exact next gate, but do not begin Unit 2 or English translation in the same iteration unless separately authorized.

## Last known live checkpoint

At handover creation, live `main` is:

`7152bfbcd8f2eecc732d9cee77b734594226bc4f`

Message:

`Advance source mapping through Gate E batch E3`

If live `main` has advanced, preserve the newer state instead of resetting to this SHA.
