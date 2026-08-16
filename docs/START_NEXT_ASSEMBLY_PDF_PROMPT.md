# Start-next-PDF prompt — Kalaignar Assembly Speeches

Copy this prompt into a new chat together with the **next Assembly-speeches PDF**.

---

Continue the Kalaignar Assembly Speeches archival project.

GitHub repository:
`https://github.com/pugazg/kalaignar-assembly-speeches`

The next source PDF is attached. Treat the attached scan as a **new controlling source**. Work directly in the existing repository on `main`.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely before doing any work.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely. The 2007 industrial-speeches PDF recorded there is **finished and locked**; Speeches 1–10 are fully released through Gate H.
3. Inspect the repository before creating anything. Search for the new PDF/source, printed title, speech dates/labels and plausible canonical entries. If work already exists for this new source, continue it rather than creating duplicates.
4. Inspect the **actual attached PDF scan** before creating metadata. Do not rely on the filename, catalogue wording, OCR or assumptions from the previous anthology.
5. Inspect title/front matter, enough interior pages to understand structure, and the physical ending of the PDF.
6. Establish the actual PDF page count and, when the bytes are available, record exact filename, file size and SHA-256.

## Source authority

The rendered scan is the controlling textual authority for this edition.

Do not silently modernise, correct, normalise, reconstruct or improve the Tamil. Preserve source-supported historical spelling, punctuation, wording, names, initials, numerals, repetition, unusual grammar, spacing/compound variation, speaker labels, interventions, headings, stage markers and printed English.

Distinguish printed speech text from library stamps, handwriting, later annotations, bleed-through, damage and non-speech matter.

OCR/parsed text may assist transcription but is never authoritative. If a reading cannot genuinely be resolved from the scan, mark it explicitly rather than guessing.

## Released material is locked

Do **not** restart, retranscribe, retranslate or modify any already released Speech 1–10 from the completed 2007 industrial anthology merely because the new PDF overlaps a date, subject or speech.

If the new PDF contains material overlapping an existing released speech, treat the new PDF as a separate source witness during preflight/mapping. Document the overlap. Do not silently merge editions or replace the existing canonical source layer.

## Gate A — new-source preflight

Before transcription, determine from the scan itself:

- exact publication/title wording;
- edition/publication information visible in the source;
- publisher/location where printed;
- whether the PDF is a single speech or anthology;
- front matter and back matter;
- scan-page versus printed-page relationship, including any changes;
- missing, duplicated, blank, damaged or unusually numbered pages;
- scan quality/source-specific complications.

Record source facts only when supported by the scan. Do not fill missing bibliographic information from memory.

## Gate B — structural mapping

If this is an anthology, **map all speech boundaries before transcribing any speech**.

For every speech/unit record:

- source label such as `உரை : N`, if printed;
- printed date exactly as shown;
- ISO date;
- proposed canonical ID;
- scan/source start and end pages;
- printed start and end pages;
- opening evidence;
- closing ornament/editorial evidence;
- next-speech boundary evidence.

Perform a second focused boundary check before locking the mapping. Never infer the continuation or boundary from outside knowledge.

Create/update a source-specific mapping file under `sources/` using the repository's established conventions.

## Gates C–E — Tamil

After mapping is locked, process the first eligible speech using bounded, reviewable batches.

- Gate C: first-pass Tamil transcription directly from rendered scan pages.
- Gate D: complete page-marker, coverage, boundary, intervention and continuity audit.
- Gate E: strict page-by-page visual source-fidelity verification.

Use `<!-- source-page: N -->` exactly once for every represented source page.

A complete first pass is `transcribed`, **not verified**. Set `verified_against_scan=true` only after Gate E has passed for the complete speech.

Do not begin English before Gate E is complete.

## Gates F–G — English

Translate only from the **final verified Tamil**.

Retain Kalaignar's language and voice in English. Preserve his argumentative sequence, repetitions, direct address, humour, irony, wordplay, metaphors, rhetorical accumulation, parliamentary exchanges, register shifts and stage markers. Do not rewrite him into generic polished English. Do not silently correct the speaker's factual/historical claims.

Gate G must re-read the entire English against the verified Tamil page by page, including page boundaries, omissions/repetitions, names, figures, printed English and stage-marker placement. English is `verified` only after Gate G passes.

## Gate H — release

Only after Tamil and English are verified:

- merge verified English after the untouched verified Tamil in canonical `transcript.md`;
- validate complete Tamil marker and English page-section coverage exactly once and in order;
- recheck all Gate-G corrections after the merge;
- inspect page transitions for mechanical duplication/omission;
- update speech metadata/README/audit files;
- update `data/speeches.json`, root README/index and the source-specific handover;
- retire temporary translation batches only after canonical validation;
- mark released only when Gate H genuinely passes.

## Working discipline

Work directly on `main` unless explicitly instructed otherwise. Use bounded, reviewable commits. Do not create duplicate speech folders. Do not modify released entries unrelated to the new source. Do not begin the next speech merely to fill a batch.

At the end of each activity report exactly:

- source/PDF identity established so far;
- gate completed/in progress;
- exact scan and printed pages processed;
- corrections made;
- unresolved readings/questions;
- repository commit/checkpoint;
- exact next activity and continuation point.

For the **first activity with the newly attached PDF**, perform Gate A and, if it is an anthology, begin/complete Gate B mapping as the source size permits. Do not start transcription until the relevant boundaries are securely locked.

---
