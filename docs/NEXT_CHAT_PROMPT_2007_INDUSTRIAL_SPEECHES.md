# Next-chat prompt — 2007 industrial speeches transcription

Continue `pugazg/kalaignar-assembly-speeches` from `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` and follow `docs/ARCHIVAL_WORKFLOW.md`.

Active unit: `1996-08-14-industries-debate` (`உரை : 5`, 14.08.1996), locked to scan pp.136–171 / printed pp.135–170.

Current state:

- Gate C: **complete — 36/36 pages represented**.
- Gate D: **passed**.
- Gate E: **passed — 36/36 pages directly verified against the scan**.
- Tamil status: **verified**; unresolved readings: **0**.
- Gate-E source-supported corrections: **23**.
- Gate F English translation: **complete — 36/36 source-page sections, exactly 136–171**.
- English working file: `speeches/1996/1996-08-14-industries-debate/translation.md`.
- English status: **translated**, not yet verified.
- Gate G English fidelity verification: **not started**.
- Gate H release/indexing: **not started**.

Gate F translated only from the final verified Tamil in canonical `transcript.md`. Source-page headings in `translation.md` were assertion-checked as exactly **136–171**. Speaker/intervention structure, figures, dates, monetary values, industrial/technical terminology, argument sequence and printed English passages were carried into the working translation.

Printed English/source anomalies intentionally preserved for Gate-G review include p.154–155 `Our closed historical and cultural ties` / `Sigapore`, p.156 `Tom, Tick & Harry`, p.157 `business-men`, and pp.158–159 `Liquified Natural Gas` / `LNG Terminal (Liquified)`. Unusual verified Tamil/source forms must not be silently repaired using outside knowledge.

Before Gate-F completion was recorded, two first-draft translation issues were corrected: p.144 was restored to source-faithful `potassium chloride`, and the Tamil continuation after the p.157 printed `business-men` sentence was translated instead of being left untranslated.

## Next action — Gate G English fidelity verification

Re-read the **complete working English translation, source pages 136–171**, against the **final verified Tamil** in canonical `transcript.md`.

For every source-page section check:

1. complete coverage with no addition or omission;
2. page-boundary correspondence and continuation across pages;
3. speaker labels, member interventions, interruptions and closing sequence;
4. names and initials;
5. figures, dates, percentages, monetary values and units;
6. industrial/company/project and technical terminology;
7. printed English passages and quotations;
8. source anomalies and internally inconsistent claims, which must not be silently corrected;
9. the p.170–171 final intervention sequence and p.171 ending reply.

Document every concrete Gate-G correction in `verification-log.md` and apply it to `translation.md`. Only after all 36 sections pass may English be marked `verified`.

After Gate G passes, merge the corrected verified English after the verified Tamil in canonical `transcript.md`, following the released-speech precedent, and update metadata/README/source notes/verification log. Gate H remains blocked until that verified canonical entry is ready. Do not begin Speech 6 while Speech 5 remains in Gate G/H.

Gate-F commits to retain:

- complete working `translation.md` — `12eb080fc1ad442a986c23b2d32eec041b4406e3`;
- assertion check + two first-draft corrections + transcript Gate-F note — `074f69f930e708204d4a458808853c03d91ccd85`;
- metadata Gate-F state — `6911094ab926edd797c8ff291f20e5502bd03115`;
- README/source-notes/verification-log Gate-F tracking — `9d2dc62a7ec9b0c4a992d1a91bda1092f8b7d161`;
- temporary Gate-F workflows were removed (`b300ecf06f615f01bebbba0ae86cae3c0a569289`, `32f8ecd1a18d4d6cc813c1816499286169f4905b`) and are not project infrastructure.
