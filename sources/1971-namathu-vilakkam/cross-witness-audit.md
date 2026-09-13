# Cross-witness audit — `நமது விளக்கம்`

Status: **COMPLETE / PROVENANCE-AND-AMBIGUITY PASS**

## Purpose

This ledger compares the controlling 21-07-1971 Government of Tamil Nadu booklet `நமது விளக்கம்` with the two retrieved contemporary Official Report witnesses for its underlying House replies.

The booklet remains the **canonical textual authority for the booklet transcript**. The Official Reports are secondary witnesses for provenance, structural comparison and ambiguous-reading support. They must not silently normalize, expand, reorder or replace booklet wording.

## Witnesses

### W0 — controlling booklet

- file — `ACL-CPL_01732_நமது_விளக்கம்.pdf`
- publication — Government of Tamil Nadu, 21-07-1971
- body — scans **4–60 / 57 pages**
- role — **controlling textual witness**

### W1 — Legislative Assembly Official Report

- supplied file — `713073.pdf`
- House/date — **Tamil Nadu Legislative Assembly / 29-06-1971**
- physical PDF pages — **88**
- bytes — **127,383,550**
- SHA-256 — `33557239d1084cfd20d5bbc1b68182091bf6c234475081acb321bdebba38c99c`
- Chief Minister's budget-reply witness — **PDF pp.61–86**
- PDF p.87 — post-reply clarification / adjournment material, outside the reply body
- role — **secondary cross-witness**

### W2 — Legislative Council Official Report

- supplied file — `900599.pdf`
- House/date — **Tamil Nadu Legislative Council / 30-06-1971**
- physical PDF pages — **52**
- bytes — **65,950,249**
- SHA-256 — `9ee1ecc81bff62e533bfb128bc0c69de0b937cfea49e47603aa41f4c082b9281`
- Chief Minister's budget-reply witness — **PDF pp.26–50**
- PDF p.51 — post-reply / adjournment material
- PDF p.52 — appendix
- role — **secondary cross-witness**

## Structural conclusion

The cross-witness comparison confirms the existing Gate-B decision: `நமது விளக்கம்` is an **edited two-House compilation**, not a verbatim reprint of either Official Report and not safely divisible by a single inferred splice.

Key evidence:

- the Assembly Official Report reply opens with an Assembly-specific participation count / party breakdown that the booklet suppresses;
- the Council Official Report reply separately opens with a Council-specific member count and explicitly refers back to what was said in the Assembly on the previous day;
- the booklet preserves Assembly-specific interventions and also preserves Council-specific connective language such as the Rajaji/state-autonomy passage referring to what was said in the Assembly “yesterday”;
- later prohibition, Anna-path, Kambaramayanam and closing material has parallel witnesses in both Reports, with wording and ordering differences.

Therefore the booklet must continue to be preserved **in booklet order**. Cross-witness evidence may identify provenance or support a difficult reading, but it does not create a secure monotonic Assembly/Council page split inside scans 4–60.

## Representative alignment anchors

| Booklet locus | Official witness support | Result |
|---|---|---|
| opening / budget-response framing | W1 PDF p.61; W2 PDF p.26 | both Houses contain related openings; booklet is editorially compressed and does not reproduce either opening verbatim |
| scan 11 / transport-loss explanation | W2 PDF p.32 | strong near-verbatim secondary witness; supports the ambiguous sentence without replacing booklet authority |
| scans 34–40 / Rajamannar, Rajaji, Centre-State relations, Cauvery | W2 PDF pp.37–40; W1 has parallel state-autonomy material | Council witness is especially close and contains explicit previous-day Assembly reference |
| scans 44–53 / prohibition debate | W1 and W2 both contain parallel prohibition material | booklet draws from shared and House-specific material; no safe splice inferred |
| scans 54–60 / Anna-path, prohibition consequences, Kambaramayanam, statistics, closing | W1 PDF pp.85–86 and W2 PDF pp.48–50 provide strong parallels | confirms composite editorial treatment and differing closure forms |

This table records **anchors**, not an invented page-by-page House allocation.

## Existing unresolved readings — secondary-witness findings

The booklet pixels remain controlling, so neither marker is silently replaced in `transcript.md`.

### Scan 11 / printed p.10

Booklet marker: `⟦தெளிவில்லை: போக ஏ⟧`

W2, Council Official Report, PDF p.32 gives the corresponding sentence as:

`ஆகவே வட்டிக்காக அரசுக்குக் கொடுக்கப்பட்ட தொகை போக ஏற்படுகிற நஷ்டம் தான் ...`

Cross-witness outcome: **SECONDARY WITNESS SUPPORT — HIGH CONFIDENCE; BOOKLET CANONICAL READING REMAINS UNRESOLVED.**

The Official Report shows that `போக` belongs after `தொகை` in its House witness. Because the booklet scan itself remains visually ambiguous and the booklet is an edited witness, this does not authorize silently rewriting the booklet sentence.

### Scan 37 / printed p.36

Booklet marker: `⟦தெளிவில்லை: தேச பக்தி வேறு⟧`

W2, Council Official Report, PDF p.38 gives the corresponding Rajaji quotation as:

`... என்ற கருத்தினாலெழும் தேசபக்தி வேறு. எனவே சமஷ்டி அமைப்பு ...`

Cross-witness outcome: **SECONDARY WITNESS SUPPORT — HIGH CONFIDENCE; BOOKLET CANONICAL READING REMAINS UNRESOLVED.**

The Council witness strongly supports `என்ற கருத்தினாலெழும் தேசபக்தி வேறு`, but the booklet marker remains until the controlling booklet pixels themselves justify a canonical reconstruction or an explicit editorial policy authorizes secondary-witness emendation.

## Canonical-text impact

- booklet transcript changed from Official Reports — **NO**
- unresolved markers removed — **NO**
- Official Report wording imported into booklet source layer — **NO**
- Gate-B booklet-level representation changed — **NO**
- provenance certainty improved — **YES**
- both unresolved passages now have documented high-confidence secondary readings — **YES**

## Workflow consequence

This cross-witness pass is provenance work outside the canonical source-fidelity gates. Gate C.5 remains **PASS / COMPLETE — 57/57**.

Exact next workflow activity remains **Gate D — Tamil completeness audit** against the controlling booklet. Gate D must keep the two booklet uncertainties explicit and must not treat secondary-witness wording as a source-pixel correction.
