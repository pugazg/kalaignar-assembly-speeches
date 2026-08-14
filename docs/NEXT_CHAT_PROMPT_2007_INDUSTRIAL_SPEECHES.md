# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

Active unit: `1996-08-14-industries-debate` (`உரை : 5`, 14.08.1996), locked to scan pp.136–171 / printed pp.135–170.

Current state:

- Gate C: **complete — 36/36 pages represented**.
- Gate D full-speech completeness/page-marker audit: **passed**.
- Gate E: **passed — all 36 scan pages 136–171 strictly audited against the controlling scan**.
- Gate E Batch 1: pp.136–150 — **18** corrections.
- Gate E Batch 2: pp.151–165 — **4** corrections.
- Gate E Batch 3: pp.166–171 — **1** correction.
- Cumulative Gate-E corrections: **23**.
- Explicit unresolved/`[REVIEW]` readings: **0**.
- Tamil status: **verified**.
- `verified_against_scan`: **true**.
- `verified_scan_pages`: **136–171**.
- Gate F English translation: **ready / not started**.
- Gate G English fidelity verification: **not started**.
- Gate H release/indexing: **not started**.

Gate E Batch 3 corrected p.167 `உங்களுக்கு சொல்லவேண்டுமேயானால்` → the visibly printed `உங்களுக்குச் சொல்லவேண்டுமேயானால்`.

Gate E also visually confirmed and intentionally retained the source forms p.167 `ராஜஸ்தான் ஷிப் அண்டு உல்::பெடரேஷன்` and the transliterated organisation/place sequence; p.168 `வறுமை தேன் எனக் கொட்டுகிறது`, `side effects`, repeated `anti-biotic`, `சிண்டாக்` / `'சிண்டாக்'`; and the p.169–170 State Planning Commission names/roles. The final p.170–171 parliamentary interventions were checked. Scan p.171 ends after the final `திரு. ஆர். சொக்கர்` / Kalaignar exchange and decorative ornament; scan p.172 begins `உரை : 6`, dated `23.04.1997`.

## Next action — Gate F English translation

Translate the **complete final verified Tamil** for Speech 5, scan pp.136–171 / printed pp.135–170, into English.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, this handover, Speech-5 `metadata.json`, `source-notes.md`, `verification-log.md`, and the final verified Tamil in canonical `transcript.md`.
2. Treat the verified Tamil after Gate E as the sole translation source. Do not translate from OCR or any older first-pass text.
3. Translate all **36 source-page sections** in order and preserve explicit source-page correspondence in the English layer.
4. Preserve argumentative sequence, figures, dates, percentages, monetary values/units, names, industrial/technical terms, speaker labels, member interventions, interruptions, quotations and printed English where relevant.
5. Do not silently correct factual/historical claims or source anomalies. Translator clarification, if absolutely needed, must be visibly distinguished from source wording.
6. Preserve the distinction between source anomalies and translator English; never rewrite the verified Tamil while translating.
7. Keep the final p.170–171 intervention sequence complete and preserve the p.171 ending boundary.
8. When all 36 English sections are complete, update all five Speech-5 files plus this continuation prompt and the handover with Gate-F status, exact page coverage, unresolved translation issues if any, and commit SHAs.
9. After Gate F is complete, the exact next activity is Gate G English fidelity verification against the verified Tamil.
10. Do not begin Speech 6 or Gate-H index/release work while Speech 5 remains in Gate F/G.

The canonical Tamil correction commit that closed Gate E is `298d8e1e2d33b9ae5bf9e71a50d114220c545bd2`. The temporary workflow used only for assertion-checked replacement was removed immediately afterward and must not be treated as project infrastructure.
