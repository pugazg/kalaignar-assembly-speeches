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
└── verification-log.md
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
- translation status.

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
5. only after Tamil verification: the English translation.

Use the established page marker:

```html
<!-- source-page: 18 -->
```

Physical line wrapping may be normalised into readable paragraphs. Do **not** use line-wrap normalisation as permission to rewrite punctuation or sentence structure.

## 4. Status model

Use these meanings consistently.

### `in-progress`

Only part of the mapped speech has been transcribed.

### `transcribed`

A complete first-pass Tamil transcription exists for every source page in the mapped speech range. This does **not** mean source fidelity has been proven.

### `reviewed`

A separate review pass has checked the full speech and resolved obvious transcription problems, but the strict final visual audit is not yet complete.

### `verified`

The complete canonical Tamil transcript has passed a direct page-by-page visual comparison against the controlling scan, and the corrections discovered in that audit have been applied.

Never use `verified` merely because:

- OCR completed;
- the text looks fluent;
- a previous model said it was correct;
- spot checks passed;
- a first-pass transcription covered all pages.

Translation has its own status and must not inherit Tamil verification automatically.

## 5. Workflow for a new multi-speech source

### Gate A — source preflight

Before transcription:

- establish the actual PDF/page count from the source bytes;
- record filename, size and cryptographic hash when practical;
- identify front/back matter;
- identify whether the source is one speech or an anthology;
- record scan quality and unusual page numbering.

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
- next speech heading.

Use bounded batches for long PDFs and record the exact continuation point after each batch.

After the first full pass, do a focused second check of every start/end boundary before locking the inventory.

### Gate C — Tamil first-pass transcription

Work speech by speech, preferably in chronological order unless the project specifies otherwise.

For long speeches, use bounded batches (for example 10–15 source pages at a time). At the end of every batch record:

- source pages completed;
- first/last words or a safe continuation marker;
- whether the speech is partial or complete;
- unresolved readings;
- current Git commit if work was pushed.

Do not start a second speech merely to fill a batch size. Preserve natural speech boundaries.

### Gate D — Tamil completeness audit

Before calling a speech `transcribed`, confirm:

- every mapped source page is represented;
- all page markers are present and monotonic;
- no page is duplicated or skipped;
- the start and ending align with the locked structural map;
- all printed speaker changes/interventions are represented;
- unresolved readings are explicitly marked.

### Gate E — Tamil source-fidelity verification

Perform a stricter visual audit against the scan, page by page.

Check at minimum:

- words and individual characters;
- names and initials;
- numerals, dates, percentages, monetary values and units;
- English passages embedded in Tamil text;
- headings;
- speaker labels;
- punctuation where the print is legible;
- omissions/repetitions across page transitions.

Apply corrections to the canonical transcript and document them in `verification-log.md`.

Only after this gate may Tamil be marked `verified`.

### Gate F — English translation

English translation begins **only after the Tamil audit gates are complete**.

Translation rules:

- translate the verified Tamil, not OCR and not an earlier draft;
- preserve argumentative sequence and parliamentary context;
- do not improve factual claims made by the speaker;
- do not silently correct historical statements;
- distinguish source wording from translator clarification;
- keep names, figures and technical terms consistent with the verified Tamil.

### Gate G — English fidelity check

Re-read the full English translation against the final verified Tamil. Only then mark translation `verified`.

### Gate H — index/release

After the speech has a complete canonical entry:

- update `data/speeches.json`;
- update the root speech index as appropriate;
- ensure statuses match the actual audit state;
- ensure source paths/page ranges match `metadata.json` and `source-notes.md`.

## 6. Source fidelity rules

### Preserve

- source spelling, including period spelling;
- source punctuation when legible;
- headings/subheadings;
- speaker names and labels;
- member interventions;
- printed English words/passages;
- printed numerals and symbols;
- obvious editorial ornaments/boundaries as notes where relevant.

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

When resolving uncertainty:

1. inspect the full page;
2. inspect adjacent pages/context;
3. inspect a higher-resolution crop if needed;
4. compare repeated names/terms within the same source;
5. use OCR only as a secondary clue, never as the deciding authority.

If still uncertain, leave it unresolved for later review.

## 8. Git and iteration discipline

- Work from the existing `main` state unless the user specifies a branch.
- Fetch the current file before replacing it so the correct blob SHA is used.
- Prefer bounded, reviewable commits with descriptive messages.
- Never overwrite already verified speeches while processing a different source unless the requested change explicitly concerns them.
- Record a handover after long sessions or before switching chats.
- A handover should state exact source, hash, locked boundaries, completed ranges, current statuses, open uncertainties and the exact next action.

## 9. Research and enrichment

Primary-source transcription and external historical research are separate layers.

The transcript must not be altered to match outside sources. If later research establishes a more precise motion name, office-holder role or institutional context, add that as metadata or an editorial note with provenance.

## 10. Release invariant

A future contributor should be able to answer all of these from the repository alone:

- What source was used?
- Which exact scan pages contain this speech?
- What text is source transcription versus translation/editorial note?
- What has actually been verified?
- What remains uncertain?
- Where should work resume?

If the repository cannot answer those questions, the archival task is not yet complete.
