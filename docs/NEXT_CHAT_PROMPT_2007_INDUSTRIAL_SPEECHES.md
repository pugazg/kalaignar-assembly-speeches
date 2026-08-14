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
- Gate G English fidelity verification: **passed — all 36 sections re-read against the final verified Tamil**.
- Gate-G fidelity corrections: **7**.
- English status: **verified**.
- Canonical `transcript.md`: **verified Tamil followed by verified English**.
- Gate H release/indexing: **not started**.

Gate-G corrections to retain:

1. p.144 remaining `potassium chlorate` → source-faithful `potassium chloride`.
2. pp.156–157 restored an omitted repeated Tamil gloss after the second *Business India* quotation, including the bribe/payment and “presiding deity” sequence.
3. p.157 `நினைவாகி` is preserved as “become a memory”, not silently repaired to “become reality”.
4. p.162 corrected to **an additional Rs. 200 per metric tonne**.
5. p.163 `பொதுப் பணித் துறை` is preserved as **Public Works Department**, not normalised to “public-sector”.
6. p.167 `ராஜஸ்தான் ஷிப்...` is preserved as **Rajasthan Ship and Wool::Federation**, not silently changed to `Sheep`.
7. p.167 source spelling distinction is preserved as **Allana Sons** / later **Alana Sons, Goa**.

Printed/source anomalies still intentionally retained include p.154–155 `Our closed historical and cultural ties` / `Sigapore`, p.156 `Tom, Tick & Harry`, p.157 `business-men`, pp.158–159 `Liquified Natural Gas` / `LNG Terminal (Liquified)`, p.163 `தேவையேயில்லாமல்,,`, p.167 the source-transliterated organisation/place sequence, and p.168 `வறுமை தேன் எனக் கொட்டுகிறது` / `side effects` / `anti-biotic` / `சிண்டாக்`.

## Next action — Gate H canonical release/indexing

Release Speech 5 only after a final cross-file consistency check.

1. Re-read `docs/ARCHIVAL_WORKFLOW.md`, this prompt, the handover, and all Speech-5 files: `README.md`, `metadata.json`, `source-notes.md`, `verification-log.md`, `transcript.md`, and `translation.md`.
2. Confirm the canonical ID/date/source range and statuses agree everywhere: `1996-08-14-industries-debate`, 14.08.1996, scan pp.136–171 / printed pp.135–170, Tamil verified, English verified.
3. Confirm canonical `transcript.md` contains exactly one complete Tamil layer and one complete English layer for all 36 source pages, with no Speech-6 spillover.
4. Update `data/speeches.json` using the exact established schema and ordering used by released Speeches 1–4.
5. Update the root `README.md` speech index in the same established style.
6. Do not alter released Speeches 1–4 unless a separately justified correction is required.
7. Record Gate-H release/index commits and then refresh both this file and `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md`.
8. Only after Speech 5 Gate H is complete may work begin on Speech 6 (`உரை : 6`, 23.04.1997, scan pp.172–198 / printed pp.171–197).

Gate-G commits to retain:

- temporary assertion workflow creation — `088fd95bc585e35490dbb911e3d82886b19943f7`;
- English fidelity corrections + canonical English merge — `1570d8781419c16b47ee60d93e9fbc76aab18d08`;
- temporary verification workflow removed — `9f37fde38e3ebf20af0f8e48a880add5a078b319`;
- metadata marked English verified — `e92019a434f4283f06d7a92f393d3d832e783fa8`;
- Speech-5 README advanced after Gate G — `6d3b469d6e4eb8061f6c40ce3bf172a939748a72`;
- source-notes / verification-log Gate-G ledger — `8ccc2d9b3407d5e64d6e415c404da0e3ace73cb1`;
- final temporary tracking workflow removed — `6e24a181f43bcf72906336f61a9e4b15afa84b88`.

A first temporary tracking-workflow attempt failed validation and was removed before the successful assertion-checked tracking update; no temporary Gate-G workflow remains in the repository.
