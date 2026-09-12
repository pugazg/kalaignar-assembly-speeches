# NEXT CHAT PROMPT — 1973 `இருளும் ஒளியும்` / Unit 1 crop recovery page 11

Continue directly in `pugazg/kalaignar-assembly-speeches`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

Live checkpoint immediately before the scan-10 page-level pass:

`19f36549022045cd9dde718cb08f21effa759634` — `Close page 5 crop recovery and hand off scan 10`

The scan-10 pass is committed together with this refreshed prompt; if live `main` is newer, preserve the newer state.

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

- pre-recovery block literal `⟦scan-crop⟧` occurrences: **29**
- actual line-level source-loss positions: **28**
- direct source-supported right-gutter recoveries: **12**
- positions requiring no inserted fragment after witness check: **16**
- source-loss markers remaining: **0**
- booklet physical line breaks preserved
- no contextual guessing
- TNLA evidence: PDF pp. **91–92** / proceedings pp. **489–490**
- bulk-CR1 omission corrected:
  - `ஆகவே நில வரியை குறைத்தோம்`
  - → booklet line `ஆகவே நில வரியைக்`
  - next line `குறைத்தோம் என்று சொல்லுவது ஒரு மாயை; ‘Myth’ என்று`
- outgoing boundary confirmed: scan 10 ends `வித்துக் கொள்கிறேன்.`; scan 11 begins `தொழில் அபிவிருத்தி`

### Other pages

Earlier bulk recovery touched scan **11**, but under the strict page-by-page protocol it is **not yet individually revalidated**.

Unit 2 Gate D D1 remains **paused**.

## Exact next activity

Work **only on booklet scan 11 / printed p.10**.

1. Read the pre-recovery scan-11 text and every line-level `⟦scan-crop⟧` position.
2. Visually inspect the controlling booklet scan at high resolution.
3. Compare only the matching official TNLA passage — mainly PDF pp. **92–93** / proceedings pp. **490–491**.
4. Recover only characters/words physically lost at the gutter.
5. Preserve every booklet-visible spelling, punctuation, numeral, spacing choice and physical line break.
6. Remove a crop marker only when the official witness confirms the exact continuation.
7. Recheck the `தொழில் அபிவிருத்தி` / Gopal figures and transition into the James passage without normalizing booklet wording to TNLA.
8. Record every recovered fragment plus incoming/outgoing page-boundary evidence in `crop-recovery-audit.md`.
9. Update metadata/README/handover and advance the next prompt.
10. **Do not process scan 20 or any other page in the same iteration.**
