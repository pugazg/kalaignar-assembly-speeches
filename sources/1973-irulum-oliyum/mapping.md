# Source mapping — இருளும் ஒளியும்

## Gate A — source preflight

- **Printed title:** `இருளும் ஒளியும்`
- **Cover / title-page attribution:** `தமிழக முதல்வர் டாக்டர் மு. கருணாநிதி`
- **Source character:** anthology of **two** legislative reply speeches, not one continuous canonical speech.
- **Preface evidence:** the preface states that the financial statement was presented on `26-2-1973` in both Houses and that the subsequent debates were answered by the Chief Minister in the Legislative Assembly on `7-3-1973` and in the Legislative Council on `8-3-1973`; it explicitly says these two speeches are collected in this book.
- **Publication / issuing body visible in source:** `செய்தி, மக்கள் தொடர்புத்துறை, தமிழ்நாடு அரசு.`
- **Place/date printed with preface:** `சென்னை, 16-3-1973.`
- **Printer/imprint on scan p.63:** printed by the Director, Information and Public Relations Department, Chennai, at the Tamil Arasu Press (`தமிழரசு அச்சகம்`).
- **Edition statement:** no edition statement was found in the inspected scan; do not infer one.
- **Scan filename:** `TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`
- **Actual PDF pages:** **64**
- **File size:** **101,602,456 bytes**
- **SHA-256:** `0330e70d6d7a62e2c84d712966a8436b91956d722134bc71ca0b2329283f8694`
- **Text layer:** no usable parsed text layer; rendered scan pixels are controlling.

### Physical structure

| PDF scan pages | Classification | Printed pagination / evidence |
|---:|---|---|
| 1 | front cover | unpaginated; title and author/office attribution |
| 2 | title/photo page | unpaginated; title and author/office attribution |
| 3 | `பதிப்புரை` | unpaginated; establishes the two-House dates and anthology character |
| 4–40 | Speech 1 — `சட்டப் பேரவையில்` | body pagination runs to printed p.39; scan p.4 is an unnumbered section-opening page, followed by scan p.5 = printed p.4, so it occupies printed p.3 in the continuous sequence |
| 41–62 | Speech 2 — `சட்டமன்ற மேலவையில்` | scan p.41 is an unnumbered section-opening page, followed by scan p.42 = printed p.41, so it occupies printed p.40; scan p.62 = printed p.61 |
| 63 | printer/imprint page | unpaginated; mostly blank with imprint line at foot |
| 64 | back cover | unpaginated; later donor/gift sticker visible and treated as non-source annotation matter |

### Scan-page / printed-page relationship

Within the paginated speech body, the stable relationship is **printed page = PDF scan page − 1**. The section-opening scans 4 and 41 do not visibly print their page numbers, but the immediately following numbered pages and uninterrupted pagination identify them as printed pp.3 and 40 respectively. No pagination offset change was found.

### Missing / duplicate / damaged-page check

- No missing or duplicated physical scan was found in the 64-page source.
- No blank page interrupts either speech.
- Covers show staple/edge wear; some interior pages show light bleed-through or uneven/faint printing, but the inspected structure and boundaries remain readable.
- Illustrations/cartoons and printed English passages occur within the speeches and must be preserved as source context where represented during transcription.
- Scan p.64 contains a donor/gift sticker (`பேராசிரியர். தி.வ. மெய்கண்டார் அவர்களின் அன்பளிப்பு`); this is treated as later annotation/non-speech matter, not part of the speech text.

## Repository duplicate / overlap preflight

Before creating this source package, live `main` was checked for:

- source identifier `TVA_BOK_0064058`;
- title `இருளும் ஒளியும்`;
- dates `1973-03-07` and `1973-03-08`;
- `1973` speech work and finance/budget wording.

No matching source package, canonical speech entry or `speeches/1973/` directory was found. Nothing from the locked 2007 industrial anthology is modified or reused. This PDF is therefore retained as a new, independent source witness.

## Gate B — locked structural mapping

The source does **not** print `உரை : N` labels. Its two units are distinguished by explicit House headings, and their dates are established by the source's own `பதிப்புரை` on scan p.3.

The proposed `*-financial-statement-reply` slug is a neutral archival label derived from the source's statement that these are replies to the debates following the financial statement. It is not asserted to be an official motion title.

| Unit | Source heading | Printed date evidence | ISO date | House | PDF scan pages | Printed pages | Proposed canonical ID |
|---|---|---|---|---|---:|---:|---|
| 1 | `சட்டப் பேரவையில்` | `7-3-1973` (source `பதிப்புரை`) | 1973-03-07 | Legislative Assembly | **4–40** | **3–39** | `1973-03-07-financial-statement-reply` |
| 2 | `சட்டமன்ற மேலவையில்` | `8-3-1973` (source `பதிப்புரை`) | 1973-03-08 | Legislative Council | **41–62** | **40–61** | `1973-03-08-financial-statement-reply` |

### Boundary evidence

#### Unit 1 — Assembly / 7-3-1973

- **Opening:** scan p.4 begins with the explicit heading `சட்டப் பேரவையில்`, followed immediately by the Chief Minister speaker label and parliamentary reply text.
- **Closing:** scan p.40 / printed p.39 contains the `முடிப்புரை` section and closes the Assembly reply at the bottom of the page.
- **Next-unit evidence:** scan p.41 starts a fresh page with the explicit new heading `சட்டமன்ற மேலவையில்` and a new opening address to the Council Chairman.

#### Unit 2 — Legislative Council / 8-3-1973

- **Opening:** scan p.41 begins with the explicit heading `சட்டமன்ற மேலவையில்`, followed by the Chief Minister addressing the Council Chairman.
- **Closing:** scan p.62 / printed p.61 closes with the final statement and a centered closing ornament (`○` between horizontal rules).
- **Physical-end evidence:** scan p.63 is the printer/imprint page and scan p.64 is the back cover. **No third speech follows.**

## Focused second boundary check

A second visual boundary pass was completed at the critical transitions:

- scan **3 → 4**: `பதிப்புரை` ends; Assembly speech begins;
- scan **40 → 41**: Assembly `முடிப்புரை` closes; Legislative Council speech begins under a new House heading;
- scan **62 → 63**: Council speech closes with ornament; printer/imprint matter begins.

Result: **PASS — no boundary changed. Gate B is locked for both units.**

## Gate status

- Gate A — **COMPLETE / PASS**
- Gate B — **COMPLETE / PASS / LOCKED**
- Gate C — **IN PROGRESS — Unit 1 scans 4–18 / printed pp.3–17**
- Gate D — not started
- Gate E — not started
- Gates F–H — blocked

### Gate-C source-condition notes

- scan pp.4–5 and 10–11 contain physical gutter-edge text loss; unrecoverable spans are marked `⟦scan-crop⟧` in the canonical transcript and are not reconstructed;
- scan p.13 contains a printed cartoon; confidently legible labels are represented, while smaller labels that are not securely readable remain explicitly unresolved;
- scans 14–18 introduce no new crop holds; printed English parliamentary exchanges on scans 15–17 are retained verbatim in the canonical Tamil source layer;
- `verified_against_scan` remains false until Gate E is completed for the entire Assembly speech.

## Exact next activity

Continue **Gate C** on Unit 1, `சட்டப் பேரவையில்` / `7-3-1973`, from **PDF scan p.19 / printed p.18** in the next bounded batch. Preserve each `<!-- source-page: N -->` marker exactly once, mark any genuinely unreadable source text explicitly rather than reconstructing it, and do not begin Unit 2 or English before the Assembly speech reaches the required later gates.
