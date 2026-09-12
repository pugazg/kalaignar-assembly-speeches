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

### Unit 1 — Assembly / 7-3-1973

- Gate A — **COMPLETE / PASS**
- Gate B — **COMPLETE / PASS / LOCKED**
- Gate C — **COMPLETE — scans 4–40 / printed pp.3–39**
- Gate C.5 — **PASS / COMPLETE — HG1–HG7; 5 cumulative corrections; 0 unresolved historical-glyph clusters**
- Gate D — **PASS / COMPLETE — 37/37 pages; 0 completeness corrections**
- Gate E — **PASS / COMPLETE — 9 cumulative source-fidelity corrections; 0 unresolved fidelity questions**
- Gate F — **COMPLETE — 37/37 pages**
- Gate G — **PASS / COMPLETE — 37/37 pages; 15 corrections; 0 unresolved; English verified**
- Gate H — **PASS / COMPLETE — canonical bilingual merge, indexing and release complete**
- Release — **RELEASED**

### Unit 2 — Legislative Council / 8-3-1973

- Gate A — **PASS at source-package level**
- Gate B — **PASS / LOCKED — scans 41–62 / printed pp.40–61**
- Gate C — **COMPLETE — C1–C3 scans 41–62 / printed pp.40–61; 22/22 pages**
- Gate C.5 — **PASS / COMPLETE — HG1–HG3 scans 41–62 / printed pp.40–61; 22/22 pages; 2 cumulative corrections; 0 unresolved**
- Gates D–H — **NOT STARTED / downstream**

### Gate-C source-condition notes

- scan pp.4–5 and 10–11 contain physical gutter-edge text loss; unrecoverable spans are marked `⟦scan-crop⟧` in the canonical transcript and are not reconstructed;
- scan p.13 contains a printed cartoon; confidently legible labels are represented, while smaller labels that are not securely readable remain explicitly unresolved;
- scans 14–19 and 22–23 introduce no new crop holds; printed English parliamentary exchanges on scans 15–17 are retained verbatim in the canonical Tamil source layer;
- scan pp.20–21 form a third gutter-crop pair (right edge on p.20, left edge on p.21); unrecoverable text is marked `⟦scan-crop⟧` and not reconstructed;
- printed illustration/cartoon text on scans 19, 21, 22, 23 and 24 is represented where securely readable from the source;
- scan pp.25–27 form a further gutter-crop run (left edge on p.25, right edge on p.26, left edge on p.27); unrecoverable text is marked `⟦scan-crop⟧` and not reconstructed;
- scan p.28 introduces no comparable crop hold and its printed English quotations are retained verbatim in the source layer;
- scans 29–33 introduce no new crop holds; printed English and securely readable illustration text are retained as source context;
- scans 34–35 are crop-affected at the gutter (lower right on p.34; left edge on p.35); unrecoverable text is marked `⟦scan-crop⟧` and not reconstructed;
- scans 36–40 introduce no comparable crop holds; p.38 ends during the `குன்றின் மேலிட்ட விளக்கு` discussion, and scans 39–40 complete that discussion and reach the source `முடிப்புரை` close on the locked Assembly boundary;
- Gate C.5 HG1 scans 4–8 passed with 2 historical `றா` corrections on scan p.4 (`பெறுமல்` → `பெறாமல்` twice) and 0 unresolved glyph clusters in the visible audited text;
- Gate C.5 HG2 scans 9–13 passed with 1 additional historical `றா` correction on scan p.12 (`மாற்றுந்தாய்` → `மாற்றாந்தாய்`) and 0 unresolved glyph clusters in the visible audited text;
- Gate C.5 HG3 scans 14–18 passed with 0 additional corrections and 0 unresolved historical-glyph clusters in the visible audited text;
- Gate C.5 HG4 scans 19–23 passed with 0 additional corrections and 0 unresolved historical-glyph clusters in the visible audited text; scan pp.20–21 crop losses remain separate source-loss holds;
- Gate C.5 HG5 scans 24–28 passed with 0 additional corrections and 0 unresolved historical-glyph clusters in the visible audited text; scan pp.25–27 crop losses remain separate source-loss holds;
- Gate C.5 HG6 scans 29–33 passed with 0 additional corrections and 0 unresolved historical-glyph clusters in the visible audited text; no new crop holds were introduced;
- Gate C.5 HG7 originally passed with 0 additional corrections; final Gate-E E4 later exposed two missed `ளை` identities on scans 36 and 40, both now retrospectively reconciled. Gate C.5 remains PASS / COMPLETE with 5 cumulative corrections and 0 unresolved historical-glyph clusters;
- Gate C.5 batch policy is now 10 scan pages per iteration, with a shorter final remainder at a gate or speech boundary;
- Gate E E4 scans 34–40 passed with 4 corrections: scan 36 `பத்துப் பாயிண்டுகளே வைத்துக்கொண்டு` → `பத்துப் பாயிண்டுகளை வைத்துக்கொண்டு`; scan 39 `பொது வாழ்வில் எப்படி இருக்கவேண்டும்` → `பொது வாழ்வில் எப்படி யிருக்கவேண்டும்`; scan 40 `வன்கண் நாதா` → `வன்கண நாதா`; scan 40 `நெருக்கடிகளே அலட்சியப்படுத்தாமல்` → `நெருக்கடிகளை அலட்சியப்படுத்தாமல்`; cumulative Gate-E corrections: 9;
- `verified_against_scan` is now true for the complete Assembly speech, scans 4–40 / printed pp.3–39.

## Gate F progress

- F1 — **COMPLETE** — scans **4–13** / printed pp. **3–12** — 10 pages
- F2 — **COMPLETE** — scans **14–23** / printed pp. **13–22** — 10 pages
- F3 — **COMPLETE** — scans **24–33** / printed pp. **23–32** — 10 pages
- F4 — **COMPLETE** — scans **34–40** / printed pp. **33–39** — 7 pages
- cumulative Gate-F coverage: **37 / 37 pages**, scans **4–40**
- English working file: `speeches/1973/1973-03-07-financial-statement-reply/translation.md`
- source-loss markers inherited from verified Tamil are retained and not reconstructed, including the final crop holds on scans 34–35;
- source-printed English on earlier Gate-F pages is carried through verbatim;
- source-page sequence in Gate F is **4→40**, exactly once each;
- Gate F is complete at the locked Unit-1 boundary; Unit 2 has not been entered.
- Gate G is **PASS / COMPLETE**.
- G1 — **PASS** — scans **4–13** / printed pp. **3–12** — 10 pages
- G2 — **PASS** — scans **14–23** / printed pp. **13–22** — 10 pages
- G3 — **PASS** — scans **24–33** / printed pp. **23–32** — 10 pages
- G4 — **PASS** — scans **34–40** / printed pp. **33–39** — 7 pages
- cumulative Gate-G coverage: **37 / 37 pages**
- cumulative Gate-G corrections: **15**
- unresolved English fidelity issues: **0**
- English `verified_against_tamil=true`

## Gate G result

The complete English translation for scans **4–40 / printed pp.3–39** has been re-read against the final verified Tamil. G4 corrected four final fidelity issues: the scan-36 social-category normalization, the scan 37→38 Subbu page-boundary displacement, an unsupported extra category in the scan-38 book/party sentence, and the scan 39→40 verse-boundary displacement. Known crop holds remain explicit and no lost text was reconstructed.

## Gate H result — Unit 1

Unit 1 is **RELEASED**. Canonical `transcript.md` contains the unchanged verified Tamil followed by the complete Gate-G-verified English. Tamil markers and English source-page sections each cover **4→40 exactly once and in order**. Repository indexes are synchronized and `translation.md` is retired to a pointer.

## Unit 2 Gate C result

- C1 — **COMPLETE** — scans **41–50** / printed pp. **40–49** — 10 pages
- C2 — **COMPLETE** — scans **51–60** / printed pp. **50–59** — 10 pages
- C3 — **COMPLETE** — scans **61–62** / printed pp. **60–61** — 2 pages
- cumulative Gate-C coverage: **22 / 22 pages**
- source-page sequence: **41→62 exactly once and in order**
- Unit-2 physical crop holds introduced during Gate C: **0**
- scan 62 closes with `வணக்கம்` and the printed ornament
- scan 63 is printer/imprint; scan 64 back cover; no third speech follows
- Tamil verification remains pending Gate C.5, D and E
- English remains blocked

## Gate C.5 result — Unit 2

- HG1 — **PASS** — scans **41–50** / printed pp. **40–49** — 1 correction
- HG2 — **PASS** — scans **51–60** / printed pp. **50–59** — 1 correction
- HG3 / FINAL — **PASS** — scans **61–62** / printed pp. **60–61** — 0 corrections
- pages audited: **22 / 22**
- cumulative historical-glyph corrections: **2**
- unresolved glyph clusters: **0**
- HG1 correction: scan 44 `மாறுக` → `மாறாக` (`றா`)
- HG2 correction: scan 58 `வேலதான்` → `வேலைதான்` (`லை`)
- Gate C.5: **PASS / COMPLETE**
- Gate D: **unblocked / next**
- Tamil remains not verified until Gate E passes

## Unit 2 downstream closure

- Gate D — **PASS / COMPLETE — 22/22**
- Gate E — **PASS / COMPLETE / REVALIDATED — 22/22; 18 cumulative Tamil corrections; 0 unresolved**
- Gate F — **COMPLETE — English 22/22**
- Gate G — **PASS / COMPLETE — 22/22; 3 English fidelity corrections; 0 unresolved**
- Gate H — **PASS / RELEASED**

## Gate H result — Unit 2

Canonical `transcript.md` contains verified Tamil followed by verified English.

- Tamil markers **41→62** — exactly once / in order;
- English sections **41→62** — exactly once / in order;
- source-printed English — verbatim;
- all 3 Gate-G corrections — rechecked after merge;
- `translation.md` — retired pointer;
- indexes — synchronized;
- Unit 2 — **RELEASED**.

## Package closure

`இருளும் ஒளியும்` is **COMPLETE / CLOSED**.

- Unit 1 — **RELEASED / REVALIDATED AFTER CROP RECOVERY**
- Unit 2 — **RELEASED**
- scans 63–64 — non-speech tail matter
- no third speech follows

Next repository activity: attach the next Assembly-speeches PDF and start Gate A/B using `docs/START_NEXT_ASSEMBLY_PDF_PROMPT.md`.
