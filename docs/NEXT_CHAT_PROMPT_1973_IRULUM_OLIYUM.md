# NEXT CHAT PROMPT — 1973 `இருளும் ஒளியும்` / Unit 1 Gate E final remainder

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Do not reset to a stale checkpoint.

At prompt creation, live `main` was:

`7152bfbcd8f2eecc732d9cee77b734594226bc4f`

## Mandatory startup reading

Read completely before source-dependent work:

1. `docs/ARCHIVAL_WORKFLOW.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. `docs/HANDOVER_1973_IRULUM_OLIYUM.md`
4. this prompt
5. `sources/1973-irulum-oliyum/mapping.md`
6. `speeches/1973/1973-03-07-financial-statement-reply/README.md`
7. `speeches/1973/1973-03-07-financial-statement-reply/metadata.json`
8. `speeches/1973/1973-03-07-financial-statement-reply/verification-log.md`
9. `speeches/1973/1973-03-07-financial-statement-reply/historical-glyph-audit.md`
10. `speeches/1973/1973-03-07-financial-statement-reply/completeness-audit.md`
11. `speeches/1973/1973-03-07-financial-statement-reply/source-fidelity-audit.md`

## Controlling source

`TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

Locked identity:

- physical scans: **64**
- bytes: **101,602,456**
- SHA-256: `0330e70d6d7a62e2c84d712966a8436b91956d722134bc71ca0b2329283f8694`
- image-only controlling source
- source pixels are authoritative
- do not commit the PDF

If the PDF is not available in the new chat/runtime, retrieve the exact saved file if accessible; otherwise ask for the same PDF to be attached before performing visual verification. Do not substitute OCR, web text or another edition.

## Locked source mapping

Unit 1:

- heading: `சட்டப் பேரவையில்`
- date: **7-3-1973**
- canonical ID: `1973-03-07-financial-statement-reply`
- scans: **4–40**
- printed pp.: **3–39**

Unit 2:

- heading: `சட்டமன்ற மேலவையில்`
- date: **8-3-1973**
- scans: **41–62**
- printed pp.: **40–61**

**Do not cross into Unit 2.**

## Current durable state — Unit 1

- Gate A — **PASS**
- Gate B — **PASS / LOCKED**
- Gate C — **COMPLETE**
- Gate C.5 historical Tamil glyph audit — **PASS / COMPLETE**
  - 3 corrections
  - 0 unresolved glyph clusters
- Gate D Tamil completeness audit — **PASS / COMPLETE**
  - 37/37 source-page markers, scans 4→40
  - 0 completeness corrections
- Gate E Tamil source-fidelity verification — **IN PROGRESS**
  - E1 scans 4–13 — PASS, 0 corrections
  - E2 scans 14–23 — PASS, 2 corrections
  - E3 scans 24–33 — PASS, 3 corrections
  - cumulative Gate E corrections: **5**
  - new unresolved Gate-E fidelity questions: **0**
- `verified_against_scan=false`
- English translation — **not started / blocked**

Accepted Gate-E corrections already in canonical Tamil:

1. scan 14: `முதலமைச்சர் அவர்கள்` → `முதலமைச்சரவர்கள்`
2. scan 21 illustration: `வரிசலுகை` → `வரி ஏய்ப்பு`
3. scan 31 illustration: `கைத்தறியாளர்களுக்குத் நூல்கள்` → `கைத்தறியாளர்களுக்கு நூல்கள்`
4. scan 32 illustration: `விவசாயத்திற்கும் மின்சாரம்` → `விவசாயத்திற்கு மின்சாரம்`
5. scan 33: `மின் வெட்டு நிலமை` → `மின் வெட்டு நிலைமை`

Historical-glyph corrections already accepted before Gate E:

- scan 4: `பெறுமல்` → `பெறாமல்` twice
- scan 12: `மாற்றுந்தாய்` → `மாற்றாந்தாய்`

## Source-loss rule

Known physical gutter loss exists on scans 4–5, 10–11, 20–21, 25–27 and **34–35**.

Keep `⟦scan-crop⟧` for genuinely lost text. Never reconstruct from context.

Scan 13 also has smaller cartoon labels that remain intentionally unresolved.

## Batch rule

Normal iteration size: **10 scan pages**.

The current activity has only **7 scans** because scan 40 is the locked Unit-1 boundary. Do **not** cross into scan 41 to make ten.

## Exact next activity — Gate E final batch E4

Verify **scans 34–40 / printed pp.33–39** directly against high-resolution source pixels.

This is a strict source-fidelity pass, not retranscription and not editing for modern Tamil.

For every page check:

- every visible Tamil word and character;
- names and initials;
- numerals, dates, percentages, money and units;
- embedded English;
- headings;
- speaker labels/interventions;
- punctuation where legible;
- quoted material;
- omissions/repetitions across page transitions;
- source-loss markers.

Pay particular attention to:

- scan 34 lower-right crop and its final Karunanidhi intervention;
- scan 35 left-gutter crop and `குடியிருப்பு மனைப்பட்டா`;
- scans 36–37 headings / exemption comparison / Subbu intervention;
- scan 38 `குன்றின் மேலிட்ட விளக்கு` and Anna quotation;
- scan 39 Manali Kandasami / Karunanidhi exchange and first four `ஆரிய மாயை` verse lines;
- scan 40 remaining verse, `ஆரிய மாயை` attribution, `முடிப்புரை`, and complete Assembly closing paragraph.

Apply only source-proven corrections. Log every correction individually. Do not normalize source spelling, grammar, punctuation, compounds or spacing.

If E4 passes with no unresolved fidelity issue:

1. mark Gate E **PASS / COMPLETE — scans 4–40 / printed pp.3–39**;
2. set `transcription.verified_against_scan=true`;
3. record the final cumulative Gate-E correction total;
4. synchronize README, metadata, source notes if needed, verification log, `source-fidelity-audit.md`, and source mapping;
5. commit the bounded result to `main`;
6. verify live `main` after commit;
7. report source identity, Gate E result, exact corrections/unresolved questions, checkpoint SHA, and the exact next gate.

Do **not** begin Unit 2 or English translation in the same iteration unless separately authorized.
