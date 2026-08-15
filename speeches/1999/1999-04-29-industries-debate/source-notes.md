# Source notes — உரை : 8 / 29.04.1999

## Source used

Controlling scanned publication: `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

- title: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`
- first edition: `மே, 2007`
- publisher: தமிழ்க்கனி பதிப்பகம், சென்னை - 600 004
- sales rights: பூம்புகார் பதிப்பகம்
- actual PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`

The rendered scan image is authoritative for the Tamil source layer. OCR/extracted text and contextual reconstruction are helper material only.

## Locked boundary for Speech 8

| Field | Value |
|---|---|
| Source label | `உரை : 8` |
| Printed date | `29.04.1999` |
| Canonical ID | `1999-04-29-industries-debate` |
| PDF scan pages | **241–277** |
| Printed pages | **240–276** |

For this speech: `PDF scan page = printed page + 1`.

Boundary confirmation:

- scan p.240 closes Speech 7;
- scan p.241 begins `உரை : 8`, `நாள் : 29.04.1999`;
- scan p.277 closes Speech 8;
- scan p.278 begins Speech 9, `உரை : 9`, `நாள் : 8.05.2000`.

## Tamil Gates C–E

Gate C completed all **37/37** mapped pages, scan pp.241–277 / printed pp.240–276, with **0** unresolved readings. Gate D passed the complete source-page-marker and boundary audit with no gap, duplication, reordering or p.278 spillover.

Gate E then completed strict direct visual verification across all 37 pages. Batch correction counts were 5 + 6 + 12 + 2 + 1 + 1 + 1 + 1, for **29 definite source-supported corrections** and **0 unresolved readings**.

The final Gate-E correction on scan p.276 changed the Speaker line `மாண்புமிகு எதிர்க்கட்சித் தலைவர்.` to the source form `மாண்புமிகு எதிர்க் கட்சித் தலைவர்.` Scan p.277 required no correction. The High Court quotation, `8-ஏ`, `டாமின்`, Kalaignar's `வணக்கம்`, Speaker transition, `திரு. சோ. பாலகிருஷ்ணன்` intervention, figures `5,000`, `29`, `429`, `ஒன்றரை கோடி`, `400`, closing `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay and exact p.277→278 boundary were checked.

Canonical Gate-E completion checkpoint: `7ddf8745a4c3417750c0c7130ae20edb8b4cca62`.

Tamil status: **verified against scan**.

## English Gates F–G

Gate F translated all **37/37** source pages only from the final verified Tamil, preserving source-page correspondence, parliamentary context, figures, names, printed English, technical/company terminology, humour and source-specific claims. Gate-F unresolved translation questions: **0**. Final Gate-F canonical completion checkpoint: `ed79a499ecb56f8fb750f5ea9d946d1b2a71fde3`.

Gate G then re-read all 37 English sections against the final verified Tamil. It applied **1 definite fidelity correction**, on source p.245: `You are taking the nameplate and going away with it.` → `You are taking the credit for it.` for `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்`. Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`.

Batches 2–8 required no further canonical English change. Final Gate-G review commit: `f5377bc997871550d7ddba180d0d6542af632190`.

- verified English pages: **241–277, 37/37**
- missing/duplicate/reordered pages: **0**
- unresolved translation/fidelity issues: **0**
- definite Gate-G corrections: **1**
- p.278 / Speech-9 spillover: **0**

English status: **verified against final verified Tamil**.

## Gate H — release canonicalisation

Gate H is **passed**.

- verified English was merged after the verified Tamil in canonical `transcript.md` — commit `b632cc665da8f9dc1569c0cd756c345d4b1c82bb`;
- the former Gate-F `translation.md` working copy was retired to a canonical-pointer note — commit `77646efdc22ca29115cba4d031f015bb82e39e8d`;
- `data/speeches.json` was updated with Speech 8 — commit `61631e199df7c2711266d3490e264bf2caab48ef`;
- the root README/speech index was updated through Speech 8 — commit `8f84fd5ea6b1ca0f1df8f6a97f6a7da2845a2ac2`;
- `metadata.json` records verified Tamil, verified English and Gate-H release-ready status — commit `0523d96d9ecc01b19701b1f42202bc55d612b0d5`;
- the Speech-8 README records Gates C–H complete — commit `666e3725a3d22486441e92df4995eb8a3be2f22a`.

Canonical source range remains exactly scan pp.241–277 / printed pp.240–276, and no Speech-9 content is present in Speech 8.

## Next anthology unit

Speech 8 is complete and release-ready. The next locked unit is **உரை : 9 / 8.05.2000**, canonical ID `2000-05-08-industries-debate`, scan pp.278–303 / printed pp.277–302. Process Speech 9 separately; do not modify this released Speech-8 source layer.
