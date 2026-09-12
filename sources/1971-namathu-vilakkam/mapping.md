# Source mapping — நமது விளக்கம்

## Gate A — source preflight

Status: **PASS / COMPLETE**

### Controlling source

- filename: `ACL-CPL_01732_நமது_விளக்கம்.pdf`
- physical pages: **61**
- file size: **17,896,700 bytes**
- SHA-256: `5e646d628f30a0c0ad9b1bf63d34e309995acb7359e4c7756e108f76717bd180`
- parsed/OCR text layer: **no usable text**
- controlling authority: **rendered scan pixels**

### Publication evidence from the scan

- title: `நமது விளக்கம்`
- cover/title attribution: `தமிழக முதல்வர் கலைஞர் மு. கருணாநிதி`
- source introduction / imprint: `சென்னை 21-7-1971`
- issuing body in the source: `செய்தி விளம்பரத் துறை, தமிழ் நாடு அரசு`
- no separate edition statement was found in the inspected scan; record **1971** as publication year, not as an inferred numbered edition.

### Front/back matter

| Scan | Classification |
|---:|---|
| 1 | front cover |
| 2 | title / portrait page |
| 3 | publication introduction / imprint |
| 61 | back cover |

Library stamps and handwritten accession/catalogue marks visible on the scan are later library matter and are not source speech text.

### Body pagination

- body scans: **4–60**
- visible printed p.4 occurs on scan p.5
- stable relation from scans 5–60: **printed = scan − 1**
- scan p.4 is the unnumbered opening immediately before printed p.4 and is mapped as **implied printed p.3**
- locked body range: **implied printed pp.3–59**
- body pages: **57**

No missing, duplicated or blank physical pages were detected.

### Scan characteristics

- monochrome / high-contrast historical print;
- many pages contain editorial cartoons / illustrations integrated into the booklet layout;
- older Tamil glyph forms are present;
- source lineation is often dense and punctuation can be faint;
- Gate C.5 historical-glyph audit therefore applies.

---

## Gate B — structural mapping

Status: **PASS / LOCKED at booklet-witness level**

### Source-internal event statement

Scan p.3 states that the 1971–72 financial statement was presented on **1-6-1971** in both Houses, and that after the ensuing debates the Chief Minister replied:

| Underlying event | Printed date in source introduction | ISO date | House |
|---|---|---|---|
| Budget-debate reply | `29-6-71` | 1971-06-29 | Tamil Nadu Legislative Assembly |
| Budget-debate reply | `30-6-71` | 1971-06-30 | Tamil Nadu Legislative Council |

### Editorial-source unit

The body itself is one continuous printed unit:

| Unit | Printed/source label | PDF scans | Printed pages | Opening evidence | Closing evidence |
|---|---|---:|---:|---|---|
| 1 | `நமது விளக்கம்` | **4–60** | **implied 3–59** | scan 4: heading `நமது விளக்கம்`, followed by `தலைவர் அவர்களே!` | scan 60: concluding `நன்றி.`; scan 61 is back cover |

No printed second title, divider, dated subheading or editorial break securely separates an Assembly block from a Council block inside scans 4–60.

### Locked representation rule

The source is represented as an **edited two-House booklet compilation**, not as two invented booklet page-ranges.

- Do not infer a House splice from isolated occurrences of `பேரவை`, `மேலவை`, member names, topic changes or cartoon placement.
- Do not use an external Official Report to rewrite booklet wording.
- If primary Assembly/Council Official Reports are later retrieved, create a provenance/alignment ledger that records source relationships without changing the booklet source layer.
- The reader-facing booklet entry remains one source witness with `date: null`.

### Provenance event records

- `events/1971-06-29-assembly-budget-reply.md`
- `events/1971-06-30-council-budget-reply.md`

These are event/provenance records only. They are not complete canonical transcripts and are not added to `data/speeches.json` merely on the strength of the edited booklet.

---

## Gate status after mapping

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / LOCKED**
- Gate C — **IN PROGRESS — T1–T2 scans 4–23 COMPLETE; 20/57 pages; 1 unresolved**
- Gate C.5 — **MANDATORY after Gate C**
- Tamil verification — **blocked until Gate E**
- English — **blocked until Tamil verification**
- Gate H / release — **not reached**

## Exact continuation

Gate C T3: **scans 24–33 / printed pp.23–32**.

T1–T2 scans 4–23 are complete. The single scan-11 uncertainty remains unchanged. Do not begin provenance reconstruction of the 29/30 June House splices during T3.
