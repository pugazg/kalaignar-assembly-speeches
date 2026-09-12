# NEXT CHAT PROMPT — 1973 `இருளும் ஒளியும்` / Unit 1 crop recovery page 10

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

Latest page-5 durable checkpoints when this prompt was refreshed:

- `a3df57ef76ddf8169629ed9309f1af4b427152ed` — revalidate scan-5 transcript
- `96da715ea00d07cd7adaf16d9b7266c206830ae4` — record scan-5 recovery audit
- `47bb9852a18c3f5bd155f8005ec46fdb3048084f` — advance crop-recovery metadata
- `31d17e4b003c7e3c768b8d24998724019c11ff82` — advance README to scan 10

## Why Unit 1 is reopened

Unit 1 had already passed Gate H, but genuinely new official evidence is now available:

`927193.pdf` — **Tamil Nadu Legislative Assembly Debates, 7 March 1973**

SHA-256: `b56b0e2d70fb64ec026312ca62d925cb2ef7df32feb8a9578848df97461c54b4`

It is an independent official witness for the same Assembly reply and may be used **only to recover wording physically missing from the cropped gutter of the controlling booklet scan**.

## Controlling booklet

`TVA_BOK_0064058_இருளும்_ஒளியும்.pdf`

- Unit 1 scans: **4–40**
- printed pp.: **3–39**
- visible booklet wording remains controlling
- do not normalize to TNLA wording where booklet pixels are legible

## Durable crop-recovery state

Workflow: **one booklet page per iteration**.

### Scan 4 / printed p.3

**PASS / PAGE-LEVEL RECOVERY VERIFIED**

- old literal crop-marker occurrences reviewed: **38**
- direct source-supported missing-fragment recoveries: **10**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- no contextual guessing
- TNLA evidence: PDF pp.86–87 / proceedings pp.484–485

### Scan 5 / printed p.4

**PASS / PAGE-LEVEL RECOVERY VERIFIED**

- pre-recovery block literal `⟦scan-crop⟧` occurrences: **16**
- line-level source-loss positions: **15**
- direct source-supported left-gutter recoveries: **15**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- no contextual guessing
- TNLA evidence: PDF p.87 / proceedings p.485
- earlier bulk-CR1 `தலைவரான பொன்னப்ப நாடார்` join corrected to the physical two-line sequence:
  - `நம்முடைய நிறுவன காங்கிரஸ் கட்சியின் தலைவர்`
  - `திரு. பொன்னப்ப நாடார் அவர்கள் என்னை 62 நாட்கள் பாளையங்`
- outgoing boundary confirmed: scan 5 ends `பாளையங்`; scan 6 begins `கோட்டைச் சிறைச்சாலையில்...`

### Other pages

Earlier bulk recovery touched scans **10–11**, but under the strict page-by-page protocol they are **not yet individually revalidated**.

Unit 2 Gate D D1 remains **paused**.

## Exact next activity

Work **only on booklet scan 10 / printed p.9**.

1. Read the pre-recovery scan-10 text and every line-level `⟦scan-crop⟧` position.
2. Visually inspect the controlling booklet scan at high resolution.
3. Compare only the matching official TNLA passage — mainly PDF pp. **91–92** / proceedings pp. **489–490**.
4. Recover only characters/words physically lost at the gutter.
5. Preserve every booklet-visible spelling, punctuation, numeral, spacing choice and physical line break.
6. Remove a crop marker only when the official witness confirms the exact continuation.
7. Recheck the Kasiraman land-tax comparison and the transition into the agricultural-income-tax explanation without normalizing booklet wording to TNLA.
8. Record every recovered fragment plus incoming/outgoing page-boundary evidence in `crop-recovery-audit.md`.
9. Update metadata/README/handover and advance the next prompt.
10. **Do not process scan 11 or any other page in the same iteration.**
