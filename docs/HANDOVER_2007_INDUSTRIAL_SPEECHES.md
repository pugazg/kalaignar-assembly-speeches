# Handover — 2007 industrial speeches anthology

## Purpose and authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. OCR/extracted text is only a helper. English is translated from and verified against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

## Released through Speech 7

Speech 7 (`உரை : 7`, `14.05.1998`, canonical ID `1998-05-14-industries-debate`) is fully released through Gate H. Do not alter it while processing Speech 8.

## Active unit — Speech 8

- source label: `உரை : 8`
- printed date: `29.04.1999`
- canonical ID: `1999-04-29-industries-debate`
- PDF scan pages: **241–277**
- printed pages: **240–276**
- relationship: scan page = printed page + 1
- scan p.240 closes Speech 7
- scan p.278 begins Speech 9 (`8.05.2000`)

## Gate C — complete

Canonical coverage: **241–277 / 240–276 — 37/37 pages**. Unresolved `REVIEW` readings: **0**. Gate-C checkpoint: `d0fd3ea71f29838299eb5d7008e4149b7399498c`.

## Gate D — passed

All **37** source-page markers are present exactly once in strict sequence 241–277, with no gaps, duplicates, reordering or Speech-9 spillover.

## Gate E — final visual review complete; canonical closure pending

Batches 1–7 are canonically complete:

- Batch 1: pp.241–245 — 5 corrections — `201b5eff42382bcb6192475be75e01a6865ed921`
- Batch 2: pp.246–250 — 6 corrections — `bcddfa24237941596f5acaab0531974b783e7b77`
- Batch 3: pp.251–255 — 12 corrections — `856297ff79dcb3f2539ac569941e09a27aaeccde`
- Batch 4: pp.256–260 — 2 corrections — `03f32ed5460c118007693539e32db100af07ffe6`
- Batch 5: pp.261–265 — 1 correction — `a1a90353a222507c4a14a926ce0d856b25741c65`
- Batch 6: pp.266–270 — 1 correction — `2d43d163d6c7ac9e470ae08299d0d20e91ebe089`
- Batch 7: pp.271–275 — 1 correction — `d3106a9d88ed7d5c801398b14e1705eff446a18c`

Canonical state after Batch 7:

- verified scan range: **241–275**
- verified printed range: **240–274**
- verified pages: **35/37**
- cumulative applied corrections: **28**
- unresolved readings: **0**

### Final Batch 8 visual review — complete, merge pending

Scan pp.**276–277** / printed pp.**275–276** were visually re-read directly against the controlling rendered scan, both 2/2 pages.

One definite source-supported correction was found:

1. scan p.276 Speaker line: `மாண்புமிகு எதிர்க்கட்சித் தலைவர்.` → `மாண்புமிகு எதிர்க் கட்சித் தலைவர்.`

The scan clearly prints the spaced source form `எதிர்க் கட்சித் தலைவர்`. Scan p.277 required no definite correction.

Checks covered the p.276 printed High Court quotation, `8-ஏ`, `டாமின்`, Kalaignar's speech close and applause marker, the Speaker / `திரு. சோ. பாலகிருஷ்ணன்` transition, and the full p.277 salt-pan intervention and reply including `5,000`, `29`, `429`, `ஒன்றரை கோடி`, `400`, and the `உப்பளத் தொழில் / அப்பளத் தொழில்` wordplay.

Boundary checks passed:

- p.275→276: judgment lead-in → printed English quotation;
- p.276→277: Opposition Leader intervention continues from `இங்கே` → `குறிப்பிட விரும்புகிறேன்.`;
- p.277 closes after the final `(மேசையைத் தட்டும் ஒலி).`;
- p.278 was separately rendered and begins Speech 9: `உரை : 9`, `நாள் : 8.05.2000`.

Final Batch-8 unresolved readings: **0**.

For safety, the correction is staged in:

`speeches/1999/1999-04-29-industries-debate/gate-e-batch8-pp276-277.md`

Staging commit: `a0e45fd44f9da244c7e27f1a3c53736d6e996ab2`.

Do **not** mark Gate E passed until the p.276 correction has been merged into canonical `transcript.md` and the resulting diff has been inspected. Therefore canonical verified state remains **35/37 pages / 28 applied corrections**, even though all 37 pages have now been visually reviewed.

Current Tamil status: **reviewed, not fully verified**. English remains **blocked**.

## Exact next activity — close Gate E

1. Fetch current canonical `speeches/1999/1999-04-29-industries-debate/transcript.md` immediately before editing.
2. Merge exactly one source correction on scan p.276: `மாண்புமிகு எதிர்க்கட்சித் தலைவர்.` → `மாண்புமிகு எதிர்க் கட்சித் தலைவர்.`
3. Update only the archival note from Gate E verified through scan p.275 / printed p.274 to complete **scan pp.241–277 / printed pp.240–276 — 37/37 pages**, and change Tamil status there to verified.
4. Inspect the resulting canonical commit diff and confirm there are no unrelated Tamil changes.
5. Then reconcile metadata/README/source notes/verification log to:
   - Tamil status **verified**;
   - Gate E **passed**;
   - verified scan range **241–277**;
   - verified printed range **240–276**;
   - verified pages **37/37**;
   - cumulative Gate-E corrections **29**;
   - next verification page **null**;
   - unresolved readings **0**;
   - `verified_against_scan: true`;
   - translation Tamil prerequisite satisfied and Gate F no longer blocked, but still **not-started**.
6. Delete `gate-e-batch8-pp276-277.md` only after successful canonical merge and status closure.
7. Update handover and next-chat prompt to **Gate F English translation Batch 1** from the final verified Tamil.
8. Do not start translation until Gate E closure is fully reconciled.
