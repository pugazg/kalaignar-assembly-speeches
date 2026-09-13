# நமது விளக்கம் — source archival release status

## Final source status

Controlling source:

`ACL-CPL_01732_நமது_விளக்கம்.pdf`

- publication title: `நமது விளக்கம்`
- publication date: **21-07-1971**
- issuing body: **செய்தி விளம்பரத் துறை, தமிழ் நாடு அரசு**
- physical scan pages: **61**
- SHA-256: `5e646d628f30a0c0ad9b1bf63d34e309995acb7359e4c7756e108f76717bd180`

## Locked source structure

| Source range | Printed range | Classification |
|---|---:|---|
| scans 1–3 | — | cover / title / publication introduction |
| scans 4–60 | implied pp.3–59 | booklet speech body |
| scan 61 | — | back cover / non-speech |

Scan **60** closes the speech body with `நன்றி.` / `வணக்கம்.`. Scan **61** is excluded from Tamil and English reader text.

## Booklet identity

This object is an **edited two-House compilation** of replies associated with:

- **29-06-1971** — Tamil Nadu Legislative Assembly;
- **30-06-1971** — Tamil Nadu Legislative Council.

The booklet has no single speech date. Reader metadata therefore correctly retains `date: null`.

It remains intentionally outside the canonical dated speech table and `data/speeches.json`. The dated House records under `events/` remain provenance references; no artificial single-House splice is created.

## Tamil archival state

**VERIFIED / COMPLETE — 57/57 speech-body pages.**

- source-page markers: **4→60 exactly once and in order**
- Gate E corrections: **101**
- unresolved source-fidelity questions: **0**
- current unresolved readings: **0**
- Gate C.5 corrections: **129 across 109 source sites**
- scan 60 speech terminus: **PASS**
- scan 61 exclusion: **PASS**

Two readings at scans **11** and **37** were resolved earlier by explicit user-authorized emendation from the 30-06-1971 Legislative Council Official Report. Those provenance exceptions remain documented in `cross-witness-audit.md`; they are not a general authority to normalize the booklet toward Official Reports.

## English archival state

**VERIFIED AGAINST THE VERIFIED TAMIL — 57/57.**

- Gate F: **PASS / COMPLETE 57/57**
- Gate G: **PASS / COMPLETE 57/57**
- cumulative Gate-G refinements: **42**
- blocking fidelity issues: **0**
- verified-Tamil changes during Gate G: **none**
- source-printed English on scans **35, 44, 46, 47, 48**: preserved as source material
- Official Report wording used to supply Gate-G English: **none**
- web wording used: **none**

## Gate H closure

**PASS / COMPLETE.**

Gate H confirmed:

1. Tamil markers 4→60 are complete, unique and ordered;
2. English markers 4→60 are complete, unique and ordered;
3. scan 60 is the locked speech-body terminus;
4. scan 61 remains excluded as non-speech;
5. Gate-G totals and verification flags are internally consistent;
6. metadata, reader/source READMEs, mapping, translation ledgers, handover and root status are synchronized;
7. the booklet-level indexing policy is preserved;
8. Gate H made **0 Tamil or English wording changes**.

## Final state

**SOURCE PACKAGE AND BOOKLET-DERIVED TAMIL/ENGLISH READER ENTRY RELEASED / CLOSED.**

There is no routine next activity. Future Tamil changes require direct controlling-source evidence or a separately authorized provenance correction. Future English changes must be derived only from the verified Tamil and immediate booklet context.
