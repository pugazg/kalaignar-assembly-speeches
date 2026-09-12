# NEXT CHAT PROMPT — 1973 `இருளும் ஒளியும்` / Unit 1 crop recovery page 20

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

Live checkpoint immediately before the scan-11 page-level pass:

`ace19d11d8dea0d731c66a23d9a6ec28623fdd28` — `Revalidate Unit 1 crop recovery page 10`

The scan-11 pass is committed together with this refreshed prompt; if live `main` is newer, preserve the newer state.

## Why Unit 1 is reopened

Unit 1 had already passed Gate H, but genuinely new official evidence is available:

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

### Scan 5 / printed p.4

**PASS / PAGE-LEVEL RECOVERY VERIFIED**

### Scan 10 / printed p.9

**PASS / PAGE-LEVEL RECOVERY VERIFIED**

### Scan 11 / printed p.10

**PASS / PAGE-LEVEL RECOVERY VERIFIED**

- pre-recovery block literal `⟦scan-crop⟧` occurrences: **16**
- actual line-level source-loss positions: **15**
- direct official-witness-supported left-gutter recoveries: **11**
- positions requiring no inserted fragment after witness check: **4**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- no contextual guessing
- TNLA evidence: PDF pp. **92–93** / proceedings pp. **490–491**
- Gopal industrial-development figures retained as booklet printed
- incoming boundary: scan 10 ends `வித்துக் கொள்கிறேன்.`; scan 11 begins `தொழில் அபிவிருத்தி`
- outgoing boundary: scan 11 ends `... என்பால் அன்பு வைத்து, அவர்கள்`; scan 12 begins `இந்த நிதி நிலை அறிக்கையில்...`

All four pages populated by the earlier bulk CR1 pass — **4, 5, 10, 11** — are now individually page-level revalidated.

Unit 2 Gate D D1 remains **paused**.

## Exact next activity

Work **only on booklet scan 20 / printed p.19**.

1. Read the pre-recovery scan-20 text and every line-level `⟦scan-crop⟧` position.
2. Visually inspect the controlling booklet scan at high resolution.
3. Compare only the matching official TNLA passage — mainly PDF pp. **100–101** / proceedings pp. **498–499**.
4. Recover only characters/words physically lost at the gutter.
5. Preserve every booklet-visible spelling, punctuation, numeral, spacing choice and physical line break.
6. Remove a crop marker only when the official witness confirms the exact continuation.
7. Recheck the national-income / money-supply continuation and the Ananthanayaki / Hande interventions without normalizing booklet wording to TNLA.
8. Record every recovered fragment plus incoming/outgoing page-boundary evidence in `crop-recovery-audit.md`.
9. Update metadata/README/handover and advance the next prompt.
10. **Do not process scan 21 or any other page in the same iteration.**
