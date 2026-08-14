# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

Active unit: `1996-08-14-industries-debate` (`உரை : 5`, 14.08.1996), locked to scan pp.136–171 / printed pp.135–170.

Current state:

- Gate C Batch 1 complete: scan pp.136–150.
- Gate C Batch 2 complete: scan pp.151–165.
- Gate C Batch 3 complete: scan pp.166–171.
- Gate C: **complete — 36/36 pages represented**.
- Gate D full-speech completeness/page-marker audit: **passed**.
- Tamil status: **transcribed**, not reviewed or verified.
- Explicit unresolved/`[REVIEW]` readings: **0**.
- Gate E: **not started; exact next activity**.
- English / Gate F: **blocked until Gate E passes and Tamil is verified**.
- Gates G/H: not started.

The controlling raw PDF is the full **329-page**, **217,124,211-byte** source. Scan p.171 / printed p.170 ends Speech 5 after the final `திரு. ஆர். சொக்கர்` intervention and Kalaignar reply, followed by the decorative ending ornament. Scan p.172 / printed p.171 begins `உரை : 6`, dated `23.04.1997`.

## Next action — Gate E strict Tamil verification

Begin a strict direct visual/source-fidelity audit of Speech 5 against the controlling scan. Use bounded review batches while treating Gate E as a full-speech gate:

1. Start with **scan pp.136–150 / printed pp.135–149**.
2. Compare the canonical Tamil page by page against the rendered scan images, checking individual words/characters, names/initials, figures, dates, percentages, money/units, embedded English, headings, speaker labels, punctuation and page-transition continuity.
3. Do not modernise, regularise or repair source anomalies. Correct only where the scan proves the first-pass transcription differs from the print.
4. Record every concrete correction in `verification-log.md` and apply it to canonical `transcript.md`.
5. Keep Tamil status `transcribed` until **all scan pp.136–171** have passed Gate E. Do not mark partial Gate-E batches as verified.
6. After pp.136–150, continue Gate E with pp.151–165 and then pp.166–171.
7. English remains blocked throughout Gate E. Do not start Speech 6 or Gate-H index changes.

First-pass unusual forms already recorded in `source-notes.md`—including `Sigapore`, `Tom, Tick & Harry`, `business-men`, `Liquified`, `தேவையேயில்லாமல்,,`, `ஊழல் நடத்திருக்கிறது`, `ராஜஸ்தான் ஷிப் அண்டு உல்::பெடரேஷன்`, `வறுமை தேன் எனக் கொட்டுகிறது`, `anti-biotic`, and `சிண்டாக்`—must be checked visually rather than automatically corrected.

After each Gate-E batch, update the five Speech-5 files plus the handover with the exact verified range, concrete corrections, unresolved readings, commit SHAs and next review page.
