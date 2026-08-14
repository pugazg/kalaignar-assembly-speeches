# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

Active unit: `1996-08-14-industries-debate` (`உரை : 5`, 14.08.1996), locked to scan pp.136–171 / printed pp.135–170.

Current state:

- Gate C: **complete — 36/36 pages represented**.
- Gate D full-speech completeness/page-marker audit: **passed**.
- Gate E: **in progress**.
- Gate E Batch 1 complete: **scan pp.136–150 / printed pp.135–149** — 18 source-supported corrections.
- Gate E Batch 2 complete: **scan pp.151–165 / printed pp.150–164** — 4 source-supported corrections.
- Gate-E coverage: **30/36 pages**, scan pp.136–165.
- Cumulative Gate-E corrections: **22**.
- Explicit unresolved/`[REVIEW]` readings: **0**.
- Tamil status: **transcribed**, not fully verified.
- Next Gate-E page: **scan p.166 / printed p.165**.
- English / Gate F: **blocked until Gate E passes for the complete range and Tamil is verified**.
- Gates G/H: not started.

Gate E Batch 2 corrected:

- p.153 `தொழிற்சாலை உருவாவதற்குக் தேவை` → `தொழிற்சாலை உருவாவதற்குத் தேவை`;
- p.159 `ஒரு பிரஞ்சு கம்பெனி` → `ஒரு பிரெஞ்சு கம்பெனி`;
- p.164 later `அவர்களெல்லாம் உயர்மட்டக் குழுவிலே இருந்தார்கள்.` → `அவர்கள் எல்லாம் உயர்மட்டக் குழுவிலே இருந்தார்கள்.`;
- p.165 `கடைபிடித்து அதிக லாபத்தை, அதிக வருமானத்தை` → `கடைபிடித்து அதிகலாபத்தை, அதிக வருமானத்தை`.

Batch 2 visually confirmed and intentionally retained the printed forms p.154 `Our closed historical and cultural ties`, p.155 `Sigapore`, p.156 `Tom, Tick & Harry`, p.157 `business-men`, pp.158–159 `Liquified Natural Gas` / `LNG Terminal (Liquified)`, p.162 `அருணா ஷூகாஸ்`, p.163 `தேவையேயில்லாமல்,,` / `ஊழல் நடத்திருக்கிறது`, and p.164 `ஸ்பெசிபிக் நேர்வு`.

## Next action — Gate E Batch 3

Strictly audit the final **scan pp.166–171 / printed pp.165–170** directly against the controlling scan images.

For every page compare canonical Tamil against the scan, checking individual words/characters, names/initials, figures, dates, money/units, embedded English, speaker labels, punctuation where legible and page-transition continuity. Correct only where the scan proves the canonical text differs from the print. Do not modernise or normalise source anomalies.

Pay deliberate attention to the still-unverified first-pass forms:

- p.167 `ராஜஸ்தான் ஷிப் அண்டு உல்::பெடரேஷன்` and the full transliterated organisation/place sequence;
- p.168 `வறுமை தேன் எனக் கொட்டுகிறது`, `side effects`, `anti-biotic`, `சிண்டாக்` / `'சிண்டாக்'`;
- pp.169–170 State Planning Commission names and parenthetical roles;
- the final p.170–171 parliamentary intervention sequence and p.171 ending boundary.

Record every concrete correction in `verification-log.md`, apply it to canonical `transcript.md`, and update all five Speech-5 files. If the complete range pp.136–171 then passes with no unresolved reading, Gate E may be closed and Tamil marked `verified`; only after that may Gate F English translation begin. Do not start Speech 6 or Gate-H index changes before their required gates.

After the batch, refresh the handover and this continuation prompt with the final Gate-E status, correction count, unresolved readings, commit SHAs and exact next activity.
