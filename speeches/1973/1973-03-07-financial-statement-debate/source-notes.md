# Source notes — உரை : 12 / 07.03.1973

## Controlling source

Full anthology:

`TVA_BOK_0065523_நிதிநிலை_அறிக்கை_மீது_கலைஞரின்_சட்டமன்ற_உரை_1.pdf`

- 546 physical scans
- 393,027,493 bytes
- SHA-256 `e2bc9965ae2f03008e85abaedd7f601971a5699d8a92c044e9bd2346496c3932`
- textual authority — **rendered scan pixels**

Gate-C working splits:

| Split | SHA-256 | Size | Local pages | Global scans | Speech pages |
|---|---|---:|---|---|---:|
| part008 pages 176–200 | `a7e186a1f4f415410d462f39f50c75475a27ef3d1c386a8cf557ef39701dab47` | 17,513,705 | 16–25 | 191–200 | 10 |
| part009 pages 201–225 | `fe1df9ca2d41fd52219cd1fc97d0b6036f69b08aaad022ba2135c599088c40a7` | 17,778,702 | 1–25 | 201–225 | 25 |
| part010 pages 226–250 | `257b862a7ebe21d768f8e5a2f2d2f9e8bb6c4e7ca7f704800a6453f40d0a9b90` | 17,801,423 | 1–5 | 226–230 | 5 |

Coverage is **40/40** with no gap or overlap inside Speech 12.

## Locked boundaries

| Field | Value |
|---|---|
| Source label | `உரை : 12` |
| Printed date | `07.03.1973` |
| Global scans | **191–230** |
| Printed pages | **190–229** |
| Start | scan 190 Speech 11 close → scan 191 Speech 12 start — **PASS** |
| End | scan 230 Speech 12 close → scan 231 Speech 13 start — **PASS** |

Printed page = global scan - 1 throughout this unit.

## Parallel-witness provenance

The repository already contains a released record at `speeches/1973/1973-03-07-financial-statement-reply/`.

That record was inspected only to confirm that this anthology witness requires a separate non-overwriting path. It was **not** used to supply, repair, normalize or verify Tamil wording in this working entry. The released record remains unchanged.

## Gate-C transcription policy

- all 40 pages manually transcribed from the rendered anthology pixels;
- no OCR;
- no web copy;
- no Official Report;
- no alternate anthology;
- no released 1973 Tamil/English imported;
- physical line wrapping normalized into readable paragraphs;
- source spelling, punctuation, numerals, speaker interventions, printed English and visible repetition retained;
- running headers and printed page numbers excluded from speech wording;
- source markers `191→230` preserve physical scan sequence.

Gate C is a first pass, not a word-for-word verification.

## Gate C.5 applicability

**N/A / CLOSED.**

The controlling witness is modern 2007 anthology typesetting. The full 40-page Gate-D visual structural review did not reveal a legacy/reform-sensitive glyph condition requiring a separate historical-glyph pass.

## Gate D completeness / structure result

**PASS / COMPLETE — 40/40 pages; 0 completeness corrections.**

- source markers **191→230** — 40/40, exactly once, ordered
- hard boundaries **190→191 / 230→231** — PASS
- internal transitions — **39/39 PASS**
- missing pages — **0**
- duplicate long blocks — **0**
- speaker labels/interventions — structurally represented
- source-printed English — structurally represented, including scans **204, 205, 214, 217, 218**
- mixed-script terms such as `Money supply` and `ratification` — retained
- figures, dates and quotations — structurally represented
- scan **222** source-visible repeated cinema sentence — retained
- scan **228→229** poem continuation — retained
- scan **230** closing exchange and ornament — represented

Gate D is a completeness/structure audit, not word-for-word Tamil verification. No Gate-E claim is made.

## Same-scan settlement

The former first-pass uncertainty at scan **191**, `மறுபவழி`, was enlarged and re-read from the **same controlling anthology scan** during Gate D. The printed form supports `மறுபவழி`; transcript wording was therefore **unchanged**, and the unresolved count is now **0**. No alternate witness was consulted.

## Current gate state

- Gate C — **COMPLETE / 40/40**
- Tamil — **VERIFIED**
- `verified_against_scan=true`
- Gate C.5 — **N/A / CLOSED**
- Gate D — **PASS / COMPLETE / 40/40 / 0 completeness corrections**
- Gate E — **PASS / COMPLETE / 40/40**
- Gate-E correction ledger — **25 entries / 30 occurrences**
- unresolved readings — **0**
- English / Gate F — **COMPLETE / 40 of 40**
- Gate G — **PASS / COMPLETE / 40 of 40 / 12 refinements / 0 blockers / 0 Tamil changes**
- English — **VERIFIED AGAINST TAMIL / verified_against_tamil=true**
- Gate H — **PASS / COMPLETE — RELEASED / CLOSED**

## Gate E final source-fidelity result

Strict visual source-fidelity review was completed for **scans 191–230 / 40 of 40 pages** using only the controlling anthology pixels.

- correction entries — **25**
- correction occurrences — **30**
- affected scans — **16**
- unresolved readings — **0**
- transcript corrections batch-applied — **YES**
- post-edit source markers — **40 / 191→230 / exactly once / ordered**
- scan 222 source-visible repeated cinema sentence — **retained twice**
- scan 228→229 poem continuation — **confirmed / preserved**
- scan 230 final exchange, `வணக்கம்.` and ornament — **confirmed**
- released `1973-03-07-financial-statement-reply` — **not used for wording / unchanged**
- outside wording imported — **0**

The final adjudication added two speaker-label punctuation corrections on scans **229** and **230** beyond the earlier checkpoint ledger. Full before→after details are recorded in `verification-log.md` and `metadata.json`.

## Gate F / Gate G English result

Gate F is **COMPLETE / 40 of 40 pages** and Gate G is **PASS / COMPLETE / 40 of 40 pages**.

- English source — **verified anthology Tamil in `transcript.md` only**
- released parallel-witness English consulted/imported — **NO / 0**
- web / Official Report / alternate anthology English imported — **0**
- source-page alignment — **40 markers / 191→230 / ordered**
- Gate-G refinements — **12**
- blocking fidelity issues — **0**
- verified Tamil changes — **0**
- source-printed English changes — **0**
- source-printed English on scans **204, 205, 214, 217 and 218** — **preserved verbatim**
- scan 222 repeated cinema sentence — **preserved as two English occurrences**
- scan 228→229 poem transition — **preserved**
- English — **VERIFIED AGAINST TAMIL**
- `verified_against_tamil=true`

Detailed Gate-G refinements are recorded in `translation-review.md`.

## Gate H release result

- canonical bilingual `transcript.md` — **COMPLETE**
- `translation.md` — **retired to released pointer**
- Gate-H wording changes — **0 Tamil / 0 English**
- Tamil and English page sequences — **191→230 / complete / ordered**
- source-printed English — **preserved verbatim**
- parallel-witness provenance — **PRESERVED**
- released `1973-03-07-financial-statement-reply` — **UNCHANGED**
- `data/speeches.json` / root dated table — **unchanged intentionally to avoid a second canonical same-date index record**
- release — **RELEASED / CLOSED**

## Exact next activity

Begin **Speech 13 / 14.03.1974 source-boundary and Gate-C setup** from the same anthology. Do not reopen Speech 12 unless a source-backed defect is discovered.
