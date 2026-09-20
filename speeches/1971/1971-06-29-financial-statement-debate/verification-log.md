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

## Gate status

- Tamil — **NOT STARTED / NOT VERIFIED**
- `verified_against_scan=false`
- Gate C — **NOT STARTED**
- source-page markers — **not yet created**
- unresolved-reading count — **not assessed; do not treat as zero**
- Gate C.5 — **NOT STARTED**
- Gate D — **NOT STARTED**
- Gate E — **NOT STARTED**
- Gate F / English — **BLOCKED / NOT STARTED**
- Gate G — **NOT STARTED**
- Gate H / release — **NOT STARTED / NOT RELEASED**

The setup does not make any word-for-word fidelity claim.

## Whole-speech rule

Speech 10 has **35 source pages**. At Gate C it must be processed separately as **one intact 35-page speech unit**, using scans 117–151, rather than split solely to satisfy the normal 25-page activity limit.

## Exact next activity

**Speech 10 Gate C Tamil first-pass transcription — scans 117–151 / printed pp.116–150 / 35 pages**. Do not begin Gate C.5, Gate D, English work, or Speech 11 in the same activity.
