# Verification log — உரை : 10 / 29.6.71

## Source-boundary and Gate-C setup

**Status: PASS / COMPLETE — setup only**

No Tamil transcription or downstream gate work was performed in this activity.

### Locked coverage

| Split | Local pages | Global scans | Printed pages | Count | SHA-256 |
|---|---:|---:|---:|---:|---|
| part005 / pages 101–125 | 17–25 | 117–125 | 116–124 | 9 | `1ae9039952b35b70035365de3774cdf3df5ae6c62cb38d030683ce93e2456ade` |
| part006 / pages 126–150 | 1–25 | 126–150 | 125–149 | 25 | `67f71bd3d4bce3c2fe9c258daaa307e29b3a5a195c848b4597c4844066ca8043` |
| part007 / pages 151–175 | 1 | 151 | 150 | 1 | `e6fc152ccc1953d829438fafb6bdcfe5865633033662924518366c05a844f906` |

Total Speech-10 source coverage: **35/35 pages**.

### Boundary checks

- **116→117 — PASS**
  - scan 116 = Speech 9 closing page, excluded;
  - scan 117 = `உரை : 10 / நாள் : 29.6.71`, admitted as Speech 10 start.
- **151→152 — PASS**
  - scan 151 / printed 150 = Speech 10 closing page with closing ornament;
  - scan 152 / printed 151 = `உரை : 11 / நாள் : 10.3.1972`, excluded.
- printed-page relationship **printed = global scan - 1** — PASS across the locked range.

### Split relation checks

- part005 local page 17 = global scan 117; local page 25 = global scan 125 — PASS;
- part006 local page 1 = global scan 126; local page 25 = global scan 150 — PASS;
- part007 local page 1 = global scan 151; local page 2 = global scan 152 boundary witness — PASS;
- no source-page gap or overlap in Speech-10 controlling coverage — **PASS**;
- supplied part008 begins at global scan 176 and is not part of Speech 10.

## Parallel-witness check

- related earlier source layer — `நமது விளக்கம்`;
- related repository record — `sources/1971-namathu-vilakkam/events/1971-06-29-assembly-budget-reply.md`;
- existing source layer overwritten — **no**;
- earlier-witness wording imported — **0**;
- OCR / Official Report / web / alternate-anthology wording imported — **0**;
- 2007 anthology status — **independent source witness**.

## Gate C Tamil first pass

**Status: COMPLETE — transcription coverage only / NOT VERIFIED**

The complete Speech-10 first pass was transcribed from the rendered 2007 anthology pixels only.

### Coverage and marker checks

- global scans — **117–151**
- printed pages — **116–150**
- represented pages — **35/35**
- source-page markers — **117→151**
- marker count — **35**
- duplicate markers — **0**
- missing markers — **0**
- order — **PASS**
- scan 116 admitted — **no**
- scan 152 admitted — **no**
- first-pass unresolved readings explicitly flagged — **0**
- `verified_against_scan=false`

### First-pass reconciliation before commit

- page-boundary drift around **123–125** — corrected;
- page-boundary drift around **136–138** — corrected;
- scan 120 — `பொதுத்துறை`;
- scan 127 — `திட்டம்`;
- scan 139 — `அளவுக்கும் மீறிய`;
- scan 142 — `கட்டளைக் கொள்கைகள்`;
- scan 144 — `கல்லூரிகள்`;
- scan 149 — `குல்காபூரில்`.

These are Gate-C first-pass transcription corrections made directly from the same source pixels. They are **not** a Gate-E word-for-word verification ledger.

### Source-content representation

- speaker labels / interventions — represented in the first pass;
- source-printed English quotations/interventions — represented;
- figures / dates / quotations / parenthetical stage reactions — retained at first pass;
- source-visible repetitions — retained rather than silently deduplicated;
- `நமது விளக்கம்` wording imported — **0**;
- Official Report / OCR / web / alternate-anthology wording imported — **0**;
- existing parallel-witness source layer overwritten — **no**.

## Gate status after Gate C

- Tamil — **TRANSCRIBED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C — **COMPLETE / 35 of 35 pages**
- Gate C.5 — **NOT STARTED**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- Gate F / English — **BLOCKED / NOT STARTED**
- Gate G — **NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**

Gate C makes no word-for-word fidelity claim beyond completion of the first-pass source transcription.

## Exact next activity

Perform the **Speech 10 Gate C.5 applicability decision** from the actual scan typography. If Gate C.5 is N/A / closed, perform the **Gate D structural completeness audit — scans 117–151 / 35 pages**. Do not begin Gate E, English work, Gate H, or Speech 11 in that activity.
