# Next-chat prompt — Speech 8 Gate G Batch 5 / 29.04.1999

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speech 7 (`14.05.1998`) is fully released through Gate H. **Do not restart or modify Speech 7.** Speech 8 Tamil Gates C–E are complete and verified, Gate F English translation is complete for all 37 pages, and Gate G fidelity review Batches 1–4 are complete. Continue the existing Speech-8 entry; do not create duplicates.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Read current `speeches/1999/1999-04-29-industries-debate/metadata.json`, `README.md`, `translation-review.md`, canonical `translation.md`, and final verified `transcript.md`.
5. Use the **final verified Tamil** in canonical `transcript.md` as the sole textual authority for Gate G. Do not use OCR or outside historical information to override it.

## Speech 8 locked mapping

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- scan/source pages: **241–277**
- printed pages: **240–276**
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Current Speech-8 state

- Gate C: **complete — 37/37 pages**
- Gate D: **passed**
- Gate E: **passed — 37/37 pages**
- Gate-E cumulative corrections: **29**
- unresolved Tamil readings: **0**
- Tamil status: **verified against scan**
- Gate F: **complete — source pp.241–277 / printed pp.240–276, 37/37 pages**
- final Gate-F merge checkpoint: `ed79a499ecb56f8fb750f5ea9d946d1b2a71fde3`
- Gate G: **in progress**
- Gate G Batches 1–4 reviewed: **source pp.241–260 / printed pp.240–259, 20/37 pages**
- Gate-G cumulative definite corrections: **1**
- Gate-G Batch-2 corrections: **0**
- Gate-G Batch-3 corrections: **0**
- Gate-G Batch-4 corrections: **0**
- Gate-G unresolved fidelity issues: **0**
- next Gate-G source page: **261**
- English overall status: **complete, not yet verified**
- current canonical English blob: `e80b5bfe9b1951d3780448cca3f8dfb3e9490b66`

## Gate-G corrections so far

Batch 1, source p.245: Gate F rendered `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்` as `You are taking the nameplate and going away with it.` Gate G corrected this definite over-literalisation to **`You are taking the credit for it.`** Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`.

Batches 2–4, source pp.246–260: **no further definite canonical English correction required**. Batch 4 specifically reconfirmed the Alangulam / Ranipet / Hosur SIPCOT chronology and figures, the 1989–90 factory list, the source's p.257 **`Rs. 1.125 crore`** versus p.258 **`Rs. 1,125 crore`** distinction, the 1991–96 versus 1996–99 comparison, Hyundai / Mitsubishi / Ford and the Irungattukottai component-industry list through p.260. Company-name forms were preserved from the verified Tamil rather than normalised externally.

## Exact next activity — Gate G Batch 5

Review **source/scan pp.261–265 / printed pp.260–264** against the final verified Tamil.

1. Fetch the exact Tamil and English ranges before review.
2. Compare page-by-page for omissions, additions, mistranslations, meaning shifts and cross-page continuations.
3. Check all names, dates, investment/employment figures, megawatt/tonnage figures, project/company names, technical terms, printed English and humour/idiom.
4. Preserve unusual source claims, figures and spellings; do not fact-correct or normalise them from outside knowledge.
5. Pay particular attention to the source's Pennar passage, which gives **Rs.320 crore** and subsequently calls it a **Rs.3,200 crore** factory; preserve the internal difference if the English reflects it.
6. Check Saint-Gobain, the Bangalore-road/Hyundai/glass-factory passage, Marqube / Covema Uttiplast / Autolec / Reynolds, `Blood bags`, `Bio-technology Park for women`, Mahindra Industrial Park, TIDEL, SISCOL, Ennore L.N.G. and Jayankondam carefully against the verified Tamil.
7. Check the p.265 C.M.I.E. ranking figures, percentages, horse-race comparison, Maharashtra/Tamil Nadu .02% / .01% statements, tug-of-war rhetoric and the `Economic Times` lead-in dated 28-4-1999.
8. Apply only definite English fidelity corrections.
9. Inspect the canonical translation commit/diff before advancing reviewed coverage whenever a correction is made. If no correction is required, record the unchanged canonical blob checkpoint.
10. Update `translation-review.md`, metadata, README, handover and this prompt truthfully.
11. If Batch 5 passes, Gate G advances to **25/37 pages**, next source page **266**.
12. Do not mark English fully verified until all source pp.241–277 pass Gate G.
13. Do not begin Gate H or Speech 9 until Speech 8 Gate G passes unless the user explicitly changes priority.

Batch 5 begins on source p.261 with Karur Yarn Links / Taurus Novelties / Sriram Auto Components and associated projects, continues through Saint-Gobain and the newer project list, and ends on source p.265 with the C.M.I.E. State-wise industrial-investment comparison and the `Economic Times` lead-in dated 28-4-1999.
