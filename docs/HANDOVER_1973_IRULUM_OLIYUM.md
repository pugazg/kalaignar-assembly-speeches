# Handover — 1973 `இருளும் ஒளியும்`

## Repository

`pugazg/kalaignar-assembly-speeches`, branch `main`.

**LIVE MAIN IS AUTHORITATIVE.** Fetch live `main` first and preserve newer durable work.

Checkpoint before this handover rewrite:

`996f2e7fdae5f3d373ad784451a614f2b2df0b6d` — `Set next crop recovery page to scan 5`

## Active work

Current priority is **Unit 1 post-release crop recovery, one booklet page per iteration**.

Unit 1 had previously passed Gate H and was released. It is now legitimately reopened because a newly supplied official TNLA Assembly Debates volume provides primary-source text for wording physically lost at the gutter of the `இருளும் ஒளியும்` scan.

**Unit 2 Gate D is paused.**

## Source hierarchy

### Primary controlling publication

`TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

- 64 scans
- 101,602,456 bytes
- SHA-256: `0330e70d6d7a62e2c84d712966a8436b91956d722134bc71ca0b2329283f8694`
- Unit 1: scans **4–40** / printed pp. **3–39**
- Unit 2: scans **41–62** / printed pp. **40–61**
- visible booklet pixels remain controlling

### Official crop-recovery witness

`927193.pdf`

- Tamil Nadu Legislative Assembly Debates
- sitting date: **7 March 1973**
- 119 PDF pages
- 184,860,788 bytes
- SHA-256: `b56b0e2d70fb64ec026312ca62d925cb2ef7df32feb8a9578848df97461c54b4`
- Karunanidhi reply begins around TNLA PDF p.86 / proceedings p.484

### Recovery rules

1. Booklet pixels win wherever legible.
2. TNLA may supply only text physically missing because of gutter crop.
3. Do not normalize visible booklet wording to TNLA.
4. Do not recover from OCR alone.
5. Never reconstruct from grammar/context.
6. Preserve exact booklet page boundaries.
7. Record page-specific provenance in `crop-recovery-audit.md`.

## Recovery inventory

Original actual Tamil `⟦scan-crop⟧` markers:

| Scan | Count |
|---:|---:|
| 4 | 38 |
| 5 | 16 |
| 10 | 29 |
| 11 | 16 |
| 20 | 41 |
| 21 | 29 |
| 25 | 38 |
| 26 | 37 |
| 27 | 38 |
| 34 | 6 |
| 35 | 37 |

Original total: **325**.

Bulk CR1 populated scans **4, 5, 10 and 11**, removing **99** markers. Remaining actual markers: **226** on scans **20–21, 25–27, 34–35**.

The user then changed the workflow to **strict page-by-page revalidation**. Bulk-populated pages do not count as individually closed until their own turns.

## Page 4 — PASS / CLOSED

Booklet scan **4** / printed p.**3** has been individually revalidated.

Durable checkpoints:

- `fc5735436e30009bb2f6d82e7908610f8209cf82` — revalidated page-4 transcript
- `380462a399c0ed1d543856a6fd7e9c91df754f49` — page-4 recovery audit
- `eed0f0b487b963755e8eda0e2d23735d61860964` — page-by-page metadata state
- `bb415982708f2eb123629c7fb18cfd593490fe4b` — README advanced to page 5

Result:

- old page-4 crop markers reviewed: **38**
- direct missing-fragment recoveries: **10**
- markers remaining: **0**
- source line breaks preserved
- figures **81 / 175 / 38 / 58 / 43** checked
- `திரு தங்கமணி வழக்கு` checked
- boundary confirmed: scan 4 ends `சுதந்திரக்`; scan 5 starts `கட்சியின் சார்பில்...`
- contextual guesses: **0**
- global replacements: **0**

## Exact next activity — scan 5 only

Process **booklet scan 5 / printed p.4** and stop.

Current scan-5 state:

- original crop markers: **16**
- current markers: **0**, because bulk CR1 already populated the gutter text
- **NOT YET individually revalidated**
- TNLA witness: mainly PDF p. **87** / proceedings p. **485**

Verify:

- continuation `கட்சியின் சார்பில்...`
- Hande / Ananthanayaki / Ponnappa Nadar passages
- Congress governance comparison
- `20 ஆண்டுக் காலம்`
- `62 நாட்கள்`
- booklet-supported illustration text
- page end `பாளையங்`
- scan 6 begins `கோட்டைச் சிறைச்சாலையில்...`

Do **not** process scan 10 in the same iteration.

## Required files

Read before scan-5 work:

1. this handover
2. `docs/NEXT_CHAT_PROMPT_1973_IRULUM_OLIYUM.md`
3. `speeches/1973/1973-03-07-financial-statement-reply/crop-recovery-audit.md`
4. `speeches/1973/1973-03-07-financial-statement-reply/transcript.md`
5. `speeches/1973/1973-03-07-financial-statement-reply/metadata.json`
6. `speeches/1973/1973-03-07-financial-statement-reply/README.md`
7. `speeches/1973/1973-03-07-financial-statement-reply/verification-log.md`
8. `speeches/1973/1973-03-07-financial-statement-reply/source-notes.md`

If either PDF is missing in the new chat, retrieve it from conversation/Library before asking the user to upload again.

## Remaining page sequence

After scan 5, continue exactly one page per iteration:

**10 → 11 → 20 → 21 → 25 → 26 → 27 → 34 → 35**

After all affected pages are individually revalidated:

1. whole-Tamil crop-recovery integrity audit;
2. Gate-E Tamil fidelity recheck for affected pages/spans;
3. English repair/retranslation for recovered spans;
4. Gate-G English fidelity recheck;
5. Gate-H canonical bilingual revalidation;
6. restore RELEASED only after all checks pass;
7. resume Unit 2 Gate D D1.

## Current Unit 1 release state

- `transcription.status = crop-recovery-in-progress`
- `transcription.verified_against_scan = false`
- Gate E — recheck required
- English `verified_against_tamil = false`
- Gate G — recheck required
- Gate H — reopened
- release — recovery in progress

## Unit 2 paused state

`சட்டமன்ற மேலவையில்` / 8-3-1973:

- Gate A — PASS
- Gate B — PASS / LOCKED
- Gate C — COMPLETE — 22/22
- Gate C.5 — PASS / COMPLETE — 22/22
- historical-glyph corrections — 2
- unresolved glyph clusters — 0
- Gate D — NOT STARTED / PAUSED
- English — BLOCKED

Do not resume Unit 2 until Unit-1 crop recovery/revalidation is complete.
