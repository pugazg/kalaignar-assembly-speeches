# Source notes — நமது விளக்கம்

## Controlling source

`ACL-CPL_01732_நமது_விளக்கம்.pdf`

The rendered source pixels are authoritative. The PDF has **no usable parsed text layer**.

## Bibliographic/source evidence

- title: `நமது விளக்கம்`
- cover/title attribution: `தமிழக முதல்வர் கலைஞர் மு. கருணாநிதி`
- introduction / imprint: `சென்னை 21-7-1971`
- issuing body in the scan: `செய்தி விளம்பரத் துறை, தமிழ் நாடு அரசு`
- physical scans: **61**
- file size: **17,896,700 bytes**
- SHA-256: `5e646d628f30a0c0ad9b1bf63d34e309995acb7359e4c7756e108f76717bd180`

The source introduction identifies the underlying reply events as **29-6-1971 Assembly** and **30-6-1971 Legislative Council**.

## Physical structure

| Scan pages | Content |
|---:|---|
| 1 | front cover |
| 2 | title / portrait page |
| 3 | publication introduction / imprint |
| 4–60 | continuous booklet speech compilation |
| 61 | back cover |

The visible printed pagination runs from p.4 on scan p.5 through p.59 on scan p.60. Scan p.4 is the unnumbered body opening and is mapped as implied printed p.3.

## Editorial construction

The body is not split by a printed second title or reliable internal House divider. The repository preserves `நமது விளக்கம்` as a booklet-level edited two-House witness.

Do not guess Assembly/Council splice points from member names, isolated House words, topic changes or illustrations.

Official Reports have now been retrieved and cross-witnessed. They remain separate witnesses and must not silently normalize the booklet. However, after explicit user authorization, the Council Official Report was used to resolve exactly two otherwise unreadable booklet loci (scans 11 and 37); both changes are documented as editorial emendations. See [`../../../sources/1971-namathu-vilakkam/cross-witness-audit.md`](../../../sources/1971-namathu-vilakkam/cross-witness-audit.md).

## Scan-specific features

- older Tamil typeforms: Gate C.5 mandatory;
- dense lineation and occasional faint punctuation;
- many editorial illustrations/cartoons integrated into the body;
- visible library stamps / handwriting are not source speech text;
- printed English passages, where present, must be preserved verbatim.

## Cross-witness status

- 29-06-1971 Assembly Official Report supplied as `713073.pdf` — reply witness PDF pp.61–86;
- 30-06-1971 Council Official Report supplied as `900599.pdf` — reply witness PDF pp.26–50;
- result — **edited two-House booklet construction independently confirmed**;
- scan 11 and scan 37 — both resolved from the official 30-06-1971 Council debate record by explicit user-authorized emendation; canonical unresolved markers removed.

## Current status

Gate A, Gate B, Gate C, Gate C.5, Gate D and Gate E are complete. Gate E closed **PASS / COMPLETE — 57/57 pages**, with **101 cumulative definite booklet-pixel-supported corrections**, **0 unresolved source-fidelity questions**, and **Tamil verified_against_scan=true**. Cross-witness audit and the two authorized Official-Report emendations remain separately documented. **Current unresolved readings: 0.**

Gate F is **PASS / COMPLETE — scans 4–60 / implied printed pp.3–59, 57/57 pages**, with **0 blocking translation questions**. Gate G is **PASS / COMPLETE — 57/57 reviewed, 42 cumulative English fidelity refinements, 0 blocking fidelity issues, and no verified-Tamil changes**. Source-printed English on scans 35, 44, 46, 47 and 48 remains preserved as source material, including verified quirks. Gate H is **PASS / COMPLETE** and the booklet-derived reader entry is **RELEASED / CLOSED**.

Scan **60 / printed p.59** is the locked speech-body terminus; scan **61** remains excluded as back cover / non-speech. The booklet remains an edited two-House compilation with `date: null` and is intentionally absent from the canonical dated speech table and `data/speeches.json`.

There is **no routine next activity**. Future Tamil changes require direct controlling-source evidence; future English changes must be derived only from the verified Tamil.
