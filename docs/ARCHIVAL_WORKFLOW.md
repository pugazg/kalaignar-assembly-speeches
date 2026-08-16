# Archival workflow and repository guidelines

This document defines the default working method for `kalaignar-assembly-speeches`.

The repository is intended to be a **source-faithful, auditable digital archive**, not a cleaned-up modern edition. The scan or other identified primary source controls the transcription.

## 1. Core principles

1. **Source first.** Preserve the wording actually printed in the controlling source. Do not silently modernise spelling, grammar, punctuation, numerals, names or terminology.
2. **Visual evidence controls.** OCR, text extraction and language-model guesses are helpers only. For scanned sources, the rendered page image is authoritative.
3. **Uncertainty must be visible.** If a character or word cannot be read confidently, mark it for review. Do not manufacture a plausible reading.
4. **Provenance must survive.** Record publication metadata, scan filename/hash where available, scan-page ranges, printed-page ranges and source boundaries.
5. **Parliamentary context is part of the document.** Preserve speaker labels, member interventions, interruptions, quotations, headings, tables/lists, figures and other printed contextual material that belongs to the speech sequence.
6. **Tamil before English.** English translation is blocked until the complete Tamil transcription has passed the required Tamil audit gates.
7. **Completeness and verification are different.** A transcript can be complete without yet being verified.
8. **Released material is locked.** Once a speech has passed Gate H, do not restart, retranscribe, retranslate, normalise or otherwise alter its canonical Tamil/English while processing another source. Change a released layer only for a concrete, explicitly documented, source-supported correction.
9. **Kalaignar's voice must survive translation.** English is not a prose clean-up. Preserve argumentative sequence, repetitions, direct address, humour, irony, wordplay, metaphors, rhetorical accumulation, register shifts, parliamentary exchanges and stage markers wherever the verified Tamil supports them.

## 2. Canonical speech organisation

Each dated Assembly speech belongs under:

```text
speeches/YYYY/YYYY-MM-DD-event-slug/
```

The canonical ID is the folder basename.

A publication title and a canonical speech ID serve different purposes:

- **canonical ID:** date/event-oriented archive identity;
- **publication title:** historical source metadata;
- **source label:** exact editorial label in the book, such as `உரை : 4`.

Do not turn a later anthology title into the canonical title of every speech. If the exact legislative event is not established by the source, use a neutral subject slug and document that it is archival rather than an official printed event title.

## 3. Required files for a completed speech entry

Use the established structure:

```text
speeches/YYYY/YYYY-MM-DD-event-slug/
├── README.md
├── metadata.json
├── source-notes.md
├── transcript.md
├── verification-log.md
└── translation-review.md   # when English fidelity review produces a separate audit record
```

A `verification/` directory may be added for machine-readable or batch-level verification artifacts when useful.

### `metadata.json`

At minimum record:

- canonical `id`, ISO `date`, `year`;
- speaker names exactly/appropriately represented;
- legislature;
- source publication metadata;
- source printed date as printed when it differs in formatting from ISO;
- scan filename and source page ranges;
- transcription status;
- verification status;
- translation status;
- Gate H/release state once released.

Do not infer a historical office/role from memory merely because the speaker is known. Use the source label or a separately verified primary record.

### `source-notes.md`

Record source-specific facts and difficulties:

- publication/bibliographic details;
- scan condition;
- scan-page to printed-page relationship;
- known missing/damaged pages;
- ambiguous printing;
- source editorial conventions;
- boundaries and how they were established;
- any source-specific departures from the normal workflow.

### `transcript.md`

The canonical transcript should contain:

1. source/publication or speech heading as appropriate;
2. a short archival transcription note;
3. complete Tamil transcription;
4. explicit source-page markers;
5. only after Tamil verification: the English translation;
6. after Gate G, the final verified English rather than temporary batch drafts.

Use the established page marker:

```html
<!-- source-page: 18 -->
```

Physical line wrapping may be normalised into readable paragraphs. Do **not** use line-wrap normalisation as permission to rewrite punctuation or sentence structure.

## 4. Status model

### `in-progress`
Only part of the mapped speech has been transcribed.

### `transcribed`
A complete first-pass Tamil transcription exists for every source page in the mapped speech range. This does **not** mean source fidelity has been proven.

### `reviewed`
A separate review pass has checked the full speech and resolved obvious transcription problems, but the strict final visual audit is not yet complete.

### `verified`
The complete canonical Tamil transcript has passed a direct page-by-page visual comparison against the controlling scan, and the corrections discovered in that audit have been applied.

Never use `verified` merely because OCR completed, the text looks fluent, a previous model said it was correct, spot checks passed, or a first-pass transcription covered all pages.

Translation has its own status and must not inherit Tamil verification automatically.

### `released`
Use only after Gate H has passed: canonical Tamil and verified English are consolidated, indexes/statuses agree, boundaries and page coverage are audited, and temporary working material is retired or clearly non-canonical.

## 5. Workflow for a new source/PDF

### Mandatory new-PDF startup

Every newly supplied PDF is a **new controlling source until proven otherwise**. Before creating or changing a speech entry:

1. read this workflow completely;
2. read the most recent project/source handover and the dedicated next-PDF prompt if present;
3. inspect the repository for existing work matching the source, dates, labels or scan boundaries — continue existing work rather than creating duplicates;
4. inspect the **actual attached/rendered scan**, including title/front matter and the physical end of the PDF; do not derive metadata from the filename alone;
5. establish page count, filename, byte size and SHA-256 when the bytes are available;
6. identify publication metadata from the scan itself;
7. determine whether the source is a single speech or anthology;
8. if an anthology, complete Gate B mapping before transcription;
9. never alter already released speeches merely because a new anthology overlaps them — document the overlap and treat editions as separate source witnesses unless an explicit correction task is requested.

### Gate A — source preflight

Before transcription:

- establish the actual PDF/page count from the source bytes;
- record filename, size and cryptographic hash when practical;
- identify front/back matter;
- identify whether the source is one speech or an anthology;
- record scan quality and unusual page numbering;
- inspect the source itself for title, edition, publisher and printed-date evidence rather than trusting filename/catalogue shorthand.

Do not trust a viewer's rendered-page limit as the source's true page count.

### Gate B — structural mapping

For an anthology, map **all speech boundaries first**.

Track:

- source `உரை` number or equivalent label;
- date exactly as printed;
- ISO date;
- PDF scan start/end;
- printed page start/end;
- closing ornament/editorial evidence;
- next speech heading;
- front/back matter and non-speech pages.

Use bounded batches for long PDFs and record the exact continuation point after each batch. After the first full pass, do a focused second check of every start/end boundary before locking the inventory. Do not begin Gate C until the relevant boundary is locked.

### Gate C — Tamil first-pass transcription

Work speech by speech, preferably in chronological/source order unless the project specifies otherwise.

For long speeches, use bounded batches. At the end of every batch record source pages completed, first/last words or a safe continuation marker, whether the speech is partial or complete, unresolved readings and current Git commit if work was pushed.

Do not start a second speech merely to fill a batch size. Preserve natural speech boundaries. Do not reconstruct page continuations from memory or outside knowledge.

### Gate D — Tamil completeness audit

Before calling a speech `transcribed`, confirm every mapped source page is represented; all page markers are present and monotonic; no page is duplicated or skipped; start/end align with the locked map; all printed speaker changes/interventions are represented; and unresolved readings are explicitly marked.

### Gate E — Tamil source-fidelity verification

Perform a stricter visual audit against the scan, page by page. Check words/characters, names/initials, numerals/dates/percentages/money/units, embedded English, headings, speaker labels, punctuation where legible, and omissions/repetitions across page transitions.

Apply corrections to the canonical transcript and document them in `verification-log.md`. Only after this gate may Tamil be marked `verified`.

### Gate F — English translation

English translation begins **only after the Tamil audit gates are complete**.

Translate the verified Tamil, not OCR or an earlier draft. Preserve Kalaignar's language and parliamentary voice: argumentative sequence, repetitions, direct address, humour, wordplay, irony, metaphors, rhetorical rhythm, register shifts and interventions. Do not polish these into generic English. Do not improve factual claims or silently correct historical statements. Keep names, figures, technical terms, printed English and stage markers consistent with the verified Tamil.

### Gate G — English fidelity and voice check

Re-read the **entire** English translation against the final verified Tamil page by page. Check meaning, omissions, repetitions, page boundaries, speaker/intervention placement, figures, printed English, stage-marker position and preservation of Kalaignar's voice. Record corrections and unresolved questions. Only then mark English `verified`.

### Gate H — canonical merge, index and release

After Tamil and English are verified:

- keep the verified Tamil untouched at the start of canonical `transcript.md`;
- consolidate the complete Gate-G-verified English after it;
- verify Tamil markers and English source-page sections cover the complete locked range exactly once and in order;
- explicitly recheck every correction/boundary discovered during Gate G after the merge;
- inspect the merged page transitions for mechanical duplication or omission;
- update `metadata.json`, `README.md`, `verification-log.md`, `translation-review.md` where used, `data/speeches.json`, root README/index and source handover;
- retire temporary translation batches only after the canonical merge has been validated;
- mark `released` only after all these checks pass.

A source/PDF is **complete** only when every mapped speech in it has passed Gate H and all remaining physical pages have been classified as front matter, back matter or other non-speech content. Record explicitly whether another speech follows. Then lock the source and prepare the handover/prompt for the next PDF.

## 6. Source fidelity rules

### Preserve

- source spelling, including period spelling;
- source punctuation when legible;
- headings/subheadings;
- speaker names and labels;
- member interventions;
- printed English words/passages;
- printed numerals and symbols;
- obvious editorial ornaments/boundaries as notes where relevant;
- source-supported variation in spacing, compounds and auxiliary forms rather than silently regularising them.

### Normalise only where explicitly allowed

- physical line wraps into paragraphs;
- ISO date in metadata while retaining the printed date separately;
- repository paths/slugs;
- Markdown formatting needed to represent the source cleanly.

### Never silently do

- spelling correction;
- grammar correction;
- political/factual correction;
- expansion of abbreviations unless the source itself expands them;
- guessed missing text;
- removal of repeated wording because it looks accidental;
- replacement of period terminology with modern terminology.

If an obvious printer's error appears, retain it in the source-faithful transcript. A note may explain it separately if needed.

## 7. Handling unreadable or uncertain text

Prefer a controlled uncertainty marker over a guess. The exact marker can be source-specific, but it must be searchable and documented.

When resolving uncertainty: inspect the full page; inspect adjacent pages/context; inspect a higher-resolution crop if needed; compare repeated names/terms within the same source; use OCR only as a secondary clue. If still uncertain, leave it unresolved for later review.

## 8. Git and iteration discipline

- Work from existing `main` unless the user specifies otherwise.
- Fetch the current file before replacing it so the correct blob SHA is used.
- Prefer bounded, reviewable commits with descriptive messages.
- Never overwrite already verified/released speeches while processing a different source unless the requested change explicitly concerns them.
- Do not use temporary GitHub Actions workflows as a substitute for ordinary repository edits when direct file operations suffice. If a one-time workflow is genuinely necessary, remove it immediately after successful use and verify the resulting canonical files.
- Record a handover after long sessions, source completion or before switching chats.
- A handover must state exact source, hash/size where known, locked boundaries, completed ranges, gate statuses, correction counts, open uncertainties, release state and exact next action.

## 9. Research and enrichment

Primary-source transcription and external historical research are separate layers. The transcript must not be altered to match outside sources. If later research establishes a more precise motion name, office-holder role or institutional context, add that as metadata/editorial note with provenance.

## 10. Release invariant

A future contributor should be able to answer from the repository alone: What source was used? Which exact scan pages contain this speech? What is source transcription versus translation/editorial note? What has actually been verified? What remains uncertain? Where should work resume? Is the source itself complete?

If the repository cannot answer those questions, the archival task is not yet complete.
