# Verification log — உரை : 9 / 8.05.2000

## Source preflight and locked boundaries

Controlling PDF: **329 pages**; Speech-9 scan range **278–303**, printed range **277–302**. Scan image is authoritative for Tamil. Final verified Tamil is authoritative for English translation and fidelity review. Scan p.277 closes Speech 8; p.278 begins Speech 9; p.303 closes Speech 9; p.304 begins Speech 10 (`உரை : 10`, `23.08.2006`).

## Gate C — Tamil first pass

**Complete: 26/26 pages.**

## Gate D — Tamil completeness/page-marker audit

**Passed.** Source-page markers 278–303 occur exactly once and in strict order; no Speech-8 or Speech-10 spillover.

## Gate E — strict Tamil source-fidelity verification

**Passed: 26/26 pages.** Cumulative definite Tamil corrections: **3**.

1. p.279 `பிள்ளைகளை யெல்லாம்` → `பிள்ளைகளையெல்லாம்`.
2. p.293 `இன்னொன்றியில்` → `இஃதன்னியில்`.
3. p.303 `வெட்டுத் தீர்மானங்களையும்` → `வெட்டுத்தீர்மானங்களையும்`.

Unresolved Tamil readings: **0**. Canonical verified Tamil blob: `ac00a79863c0b0bdbaac6d9fb7b03f7e4c1bb577`.

## Gate F — English first-pass translation

**Complete: 26/26 mapped source pages, pp.278–303 / printed pp.277–302.**

Translation source: final Gate-E-verified Tamil only. Kalaignar's parliamentary voice was explicitly retained: argumentative sequencing, long rhetorical movement, repetition for emphasis, direct address, humour, irony, wordplay, metaphors, political register shifts and stage markers were not intentionally smoothed into generic prose. Printed English embedded in the Tamil source was retained as printed; source-supported oddities, figures and dates were not externally reconciled.

Working segments:

- `translation.md` — pp.278–285
- `translation-gate-f-batch-2.md` — pp.286–290
- `translation-gate-f-batch-3.md` — pp.291–295
- `translation-gate-f-batch-4.md` — pp.296–300
- `translation-gate-f-batch-5.md` — pp.301–303

`translation-consolidated.md` records the consolidation manifest for Gate G / Gate H.

## Gate G — English fidelity and Kalaignar-voice verification

**Passed: 26/26 pages, source pp.278–303 / printed pp.277–302.**

Cumulative definite English fidelity corrections: **2**. Unresolved translation questions: **0**.

### Gate G Batch 1 — pp.278–280

No definite correction required. The review retained the newspaper/life-subscription wordplay, `Whose life is that?`, mother-practising-thrift metaphor, repetition, direct parliamentary address and political contrast.

### Gate G Batch 2 — pp.281–285

One definite correction on p.284. Gate F had replaced Kalaignar's actual transition after the Internet/scientific-development passage with a generic statement about information technology being the driving force of the world economy. The verified Tamil instead says that, as scientific development advances, `we must create a situation in which we can join it and compete with it`, followed by the assertion that everyone and all newspapers praise Tamil Nadu as having attained first place in India. The English was corrected to restore that exact argumentative sequence.

### Gate G pp.286–302

One definite correction on p.286. The verified Tamil/source-sensitive form `இந்தக் கேமிரா கழுவும்போது` had been interpretively rendered as `When this camera develops`; it was corrected to the deliberately source-odd `When this camera is washed` so that the English does not silently improve or reinterpret Kalaignar/source wording.

The remaining pp.286–302 passed without another definite correction. The review re-confirmed TIDEL figures and camera/light humour; TamilNet/Unicode and High Court material; `four, just four`; WorldTel and *Economic and Political Weekly* passages; printed Polaris English including `more then 100% per year`; the two-Periyasamy joke; Nanguneri birth/death humour and `My dear, my precious one`; biotechnology and industrial-project figures; anomalous printed `24-3-2001`; Ariyalur anti-privatisation/socialist rhetoric; printed Counter Affidavit English; production figures; wage comparison; Rs.85/Rs.145 cement comparison; and the p.302 lead-in to the 111 joke.

### Gate G final page — source p.303 / printed p.302

**Passed with no English correction.** The final comparison against the verified Tamil confirmed:

- `The number is not good. (Loud laughter.)` as the completion of the `111` joke;
- the request that all 111 cut motions be withdrawn and the grant supported;
- `I take my seat` for `கேட்டு அமைகிறேன்` in context;
- Chair call to P. R. Sundaram;
- Sundaram's `2,000 crore` correction to `2,000 lakh, that is, 20 crore`;
- interrupted `Rasipuram.....`;
- the Speaker's separately stated `200 crore, 20 lakh, 2,000 crore` sequence;
- the final instruction to sit down.

No Speech-10 material is present.

## Gate G final result

- reviewed source range: **278–303**
- reviewed printed range: **277–302**
- reviewed pages: **26/26**
- cumulative definite Gate-G corrections: **2**
- unresolved translation questions: **0**
- `verified_against_tamil`: **true**
- English status: **verified**
- Kalaignar voice-retention policy: **explicitly applied and fidelity-reviewed**

## Exact next activity

Proceed to **Gate H — release preparation and canonical merge**, following `docs/ARCHIVAL_WORKFLOW.md` and the established Speech-1–8 release pattern. Gate H must merge the final verified English after the verified Tamil in the canonical release form, run the required release checks, update README/metadata/audit artefacts as prescribed, and only then mark Speech 9 fully released. Do not begin Speech 10 in the same bounded activity unless explicitly requested.


## English gates

### Gate F — translation

**Complete: 26/26 pages, source pp.278–303 / printed pp.277–302.** Translation was made only from the final Gate-E-verified Tamil, with source-page correspondence and Kalaignar’s parliamentary voice retained.

### Gate G — fidelity and voice verification

**Passed: 26/26 pages.** All English page sections were re-read against the final verified Tamil. Two definite corrections were required:

1. p.284 — removed an unsupported generic “driving force of the world economy” transition and restored Kalaignar’s actual scientific-advance / join-and-compete / Tamil Nadu-first-place argumentative sequence.
2. p.286 — `இந்தக் கேமிரா கழுவும்போது` is retained in the source-sensitive English as “When this camera is washed,” rather than the interpretive Gate-F rendering “When this camera develops.”

Unresolved translation questions/fidelity issues: **0**. `verified_against_tamil=true`.

### Gate H — canonical release

**Passed.** The complete verified English was reconstructed from the Gate-G-reviewed working segments, validated to contain source pages **278–303 exactly once and in order**, and merged after the untouched verified Tamil in canonical `transcript.md`. Tamil source markers were revalidated as **278–303 exactly once and in order**. Split working translation files were retired to a single pointer file, `translation.md`; `translation-review.md` remains as the fidelity record. `data/speeches.json` and the root README speech index were updated.

Speech 9 is fully released with verified Tamil and verified English. Speech 10 was not started during this release activity.

