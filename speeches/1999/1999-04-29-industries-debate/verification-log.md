# Verification log — உரை : 8 / 29.04.1999

## Source preflight and boundaries

- controlling PDF pages: **329**
- file size: **217,124,211 bytes**
- SHA-256: `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`
- Speech-8 scan range: **241–277**
- printed range: **240–276**
- p.241 begins `உரை : 8`, `நாள் : 29.04.1999`
- p.277 closes Speech 8
- p.278 begins `உரை : 9`, `நாள் : 8.05.2000` and is excluded

## Gate C — Tamil first pass

**Passed / complete.** All **37/37** mapped pages were transcribed. Canonical Gate-C completion checkpoint: `d0fd3ea71f29838299eb5d7008e4149b7399498c`. Unresolved `REVIEW` readings: **0**.

## Gate D — Tamil completeness/page-marker audit

**Passed.** All **37** source-page markers 241–277 are present exactly once and in strict order, with no gaps, duplicates, reordering or Speech-9 spillover.

## Gate E — strict Tamil source-fidelity verification

**Passed.** All **37/37** pages were directly compared against the controlling rendered scan.

Batch results:

- Batch 1, pp.241–245: **5 corrections** — `201b5eff42382bcb6192475be75e01a6865ed921`
- Batch 2, pp.246–250: **6 corrections** — `bcddfa24237941596f5acaab0531974b783e7b77`
- Batch 3, pp.251–255: **12 corrections** — `856297ff79dcb3f2539ac569941e09a27aaeccde`
- Batch 4, pp.256–260: **2 corrections** — `03f32ed5460c118007693539e32db100af07ffe6`
- Batch 5, pp.261–265: **1 correction** — `a1a90353a222507c4a14a926ce0d856b25741c65`
- Batch 6, pp.266–270: **1 correction** — `2d43d163d6c7ac9e470ae08299d0d20e91ebe089`
- Batch 7, pp.271–275: **1 correction** — `d3106a9d88ed7d5c801398b14e1705eff446a18c`
- Batch 8, pp.276–277: **1 correction** — `7ddf8745a4c3417750c0c7130ae20edb8b4cca62`

Final Batch-8 correction: p.276 Speaker line `மாண்புமிகு எதிர்க்கட்சித் தலைவர்.` → `மாண்புமிகு எதிர்க் கட்சித் தலைவர்.` Scan p.277 required **0 corrections**.

Gate-E closure:

- verified scan range: **241–277**
- verified printed range: **240–276**
- verified pages: **37/37**
- cumulative corrections: **29**
- unresolved readings: **0**
- Tamil status: **verified against scan**

## Gate F — English translation

**Complete.** English was translated only from the final verified Tamil in bounded batches, covering **37/37 source pages, pp.241–277**. Source-page correspondence, parliamentary context, source claims, figures, technical/company names, printed English, humour and cross-page continuations were preserved. Unresolved translation questions: **0**.

Final Gate-F canonical merge checkpoint: `ed79a499ecb56f8fb750f5ea9d946d1b2a71fde3`.

## Gate G — English fidelity verification

**Passed.** The complete 37-page English translation was re-read against the final verified Tamil.

Findings:

- pages checked: **37/37**
- missing/duplicate/reordered English pages: **0**
- cross-page continuation defects: **0**
- p.278/Speech-9 spillover: **0**
- unresolved translation/fidelity issues: **0**
- definite Gate-G corrections: **1**

The sole correction was on source p.245: `You are taking the nameplate and going away with it.` → `You are taking the credit for it.` for `நீங்கள் பெயர்தட்டிக் கொண்டு போகிறீர்கள்`. Canonical correction commit: `badea74b3e3bf9e3c561a75550560caec8ef2bab`.

Batches 2–8 required no further canonical English change. Final Gate-G review artifact commit: `f5377bc997871550d7ddba180d0d6542af632190`.

English status: **verified against final verified Tamil**.

## Gate H — index/release canonicalisation

**Passed.**

Release actions:

- verified English was merged after the verified Tamil in canonical `transcript.md` — commit `b632cc665da8f9dc1569c0cd756c345d4b1c82bb`; its inspected diff changed only the archival note and appended the verified English layer, leaving the Tamil source text untouched;
- the old Gate-F `translation.md` working copy was retired to a canonical-pointer note — commit `77646efdc22ca29115cba4d031f015bb82e39e8d`;
- `data/speeches.json` was updated with the Speech-8 verified Tamil/English entry — commit `61631e199df7c2711266d3490e264bf2caab48ef`;
- the root README and speech index were updated through Speech 8 — commit `8f84fd5ea6b1ca0f1df8f6a97f6a7da2845a2ac2`;
- `metadata.json` was reconciled to verified Tamil, verified English, canonical placement, retired working-copy status and Gate-H release readiness — commit `0523d96d9ecc01b19701b1f42202bc55d612b0d5`;
- Speech-8 README was reconciled to Gates C–H complete — commit `666e3725a3d22486441e92df4995eb8a3be2f22a`;
- source notes were reconciled through release — commit `a256abf6d8e1adc02a2c36eba39bd5143d146968`.

### Final release invariant

- canonical ID: `1999-04-29-industries-debate`
- source pages: **241–277**
- printed pages: **240–276**
- Tamil: **verified**
- English: **verified**
- unresolved Tamil readings: **0**
- unresolved English questions/fidelity issues: **0**
- Gate-E corrections: **29**
- Gate-G corrections: **1**
- Speech-9 spillover: **0**
- Gate H: **passed**
- Speech 8: **release-ready**

## Next anthology unit

Proceed next with **உரை : 9 / 8.05.2000**, canonical ID `2000-05-08-industries-debate`, scan pp.278–303 / printed pp.277–302. Re-confirm its exact start/end boundaries before beginning the first bounded Gate-C Tamil transcription batch. Do not alter the released Speech-8 entry.
