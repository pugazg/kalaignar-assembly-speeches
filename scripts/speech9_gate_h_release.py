from pathlib import Path
import json
import re
import subprocess

root = Path('.')
speech = root / 'speeches/2000/2000-05-08-industries-debate'
transcript_path = speech / 'transcript.md'


def extract(text, start_page, end_page=None):
    start = f'### Source page {start_page}'
    if start not in text:
        raise RuntimeError(f'missing start marker {start}')
    part = start + text.split(start, 1)[1]
    if end_page is not None:
        stop = f'### Source page {end_page + 1}'
        if stop in part:
            part = part.split(stop, 1)[0]
    part = re.split(r'\n> \*\*Gate G(?: review)? note', part, maxsplit=1)[0]
    return part.strip()


# Recover the complete pre-placeholder Gate-F pp.278-285 blob from repository history.
old = subprocess.check_output(
    ['git', 'cat-file', '-p', 'd3101a463187dbfd96460bac371d06e745555551'],
    text=True,
)
p278_283 = extract(old, 278, 283)

# Use Gate-G-corrected current pp.284-285, then reviewed split segments.
current_1 = (speech / 'translation.md').read_text(encoding='utf-8')
p284_285 = extract(current_1, 284, 285)
p286_290 = extract((speech / 'translation-gate-f-batch-2.md').read_text(encoding='utf-8'), 286, 290)
p291_295 = extract((speech / 'translation-gate-f-batch-3.md').read_text(encoding='utf-8'), 291, 295)
p296_300 = extract((speech / 'translation-gate-f-batch-4.md').read_text(encoding='utf-8'), 296, 300)
p301_303 = extract((speech / 'translation-gate-f-batch-5.md').read_text(encoding='utf-8'), 301, 303)

english = '\n\n'.join(
    [p278_283, p284_285, p286_290, p291_295, p296_300, p301_303]
).strip()
expected = list(range(278, 304))
pages = [int(x) for x in re.findall(r'^### Source page (\d+)\s*$', english, flags=re.M)]
if pages != expected:
    raise RuntimeError(f'English page sequence mismatch: {pages}')
if '[Translation retained' in english or '[UNCHANGED_BODY_PLACEHOLDER]' in english:
    raise RuntimeError('placeholder found in reconstructed English')

# Merge verified English after untouched verified Tamil.
transcript = transcript_path.read_text(encoding='utf-8')
if '# English translation' in transcript:
    transcript = transcript.split('\n---\n\n# English translation', 1)[0].rstrip()

release_note = (
    '> **Archival transcription and translation note:** This canonical release contains the complete Tamil transcription '
    'for scan/source pp.278–303 / printed pp.277–302, verified page-by-page against the controlling May 2007 scan, '
    'followed by the complete English translation verified page-by-page against that final Tamil. Tamil Gate E passed '
    'with 3 definite source-supported corrections and 0 unresolved readings. English Gate G passed with 2 definite '
    'fidelity corrections and 0 unresolved translation questions. Kalaignar’s parliamentary voice, argumentative '
    'sequence, repetition, humour, rhetoric, direct address, register shifts, source-sensitive oddities, figures and '
    'printed English are retained rather than silently modernised or fact-corrected. Tamil and English status: **verified**.'
)
transcript = re.sub(
    r'> \*\*Gate E verification note:\*\*[^\n]*', release_note, transcript, count=1
)

english_header = (
    '\n\n---\n\n# English translation\n\n'
    '> **Gate G verification note:** This is the complete English rendering of the final verified Tamil transcription '
    'for scan/source pp.278–303 / printed pp.277–302. It preserves source-page correspondence, parliamentary context, '
    'names, figures, technical terminology, argumentative sequence, repetitions, humour, rhetorical movement, '
    'interventions, unusual source-supported wording and printed English without substituting external corrections. '
    'Gate F is complete and Gate G **passed** after a full page-by-page fidelity review of all 26 source-page sections. '
    'Gate-G correction count: **2**; unresolved translation questions: **0**. English status: **verified**.\n\n'
)
transcript_path.write_text(
    transcript.rstrip() + english_header + english + '\n', encoding='utf-8'
)

# Validate canonical release after merge.
merged = transcript_path.read_text(encoding='utf-8')
if merged.count('# English translation') != 1:
    raise RuntimeError('canonical English section count is not 1')
english_part = merged.split('# English translation', 1)[1]
merged_pages = [int(x) for x in re.findall(r'^### Source page (\d+)\s*$', english_part, flags=re.M)]
if merged_pages != expected:
    raise RuntimeError(f'canonical English page sequence mismatch: {merged_pages}')
tamil_markers = [
    int(x)
    for x in re.findall(
        r'<!-- source-page: (\d+) -->', merged.split('# English translation', 1)[0]
    )
]
if tamil_markers != expected:
    raise RuntimeError(f'Tamil source marker sequence mismatch: {tamil_markers}')

# Retire split working translations to one pointer, matching released Speech 8 practice.
(speech / 'translation.md').write_text(
    '# English translation — உரை : 9 / 8.05.2000\n\n'
    '> **Gate H canonicalisation note:** The complete English translation passed Gate G against the final verified Tamil '
    'and has been merged into canonical [`transcript.md`](./transcript.md), immediately after the verified Tamil source layer. '
    'English verification covered source/scan pp.278–303 / printed pp.277–302, 26/26 pages, with **2 Gate-G corrections** '
    'and **0 unresolved translation questions / fidelity issues**.\n\n'
    'This file was the Gate-F working companion. To avoid maintaining independently editable released copies, the verified '
    'English text is now maintained only in canonical [`transcript.md`](./transcript.md).\n\n'
    'See [`translation-review.md`](./translation-review.md) for the Gate-G fidelity record and '
    '[`verification-log.md`](./verification-log.md) for the audit trail.\n',
    encoding='utf-8',
)
for name in [
    'translation-gate-f-batch-2.md',
    'translation-gate-f-batch-3.md',
    'translation-gate-f-batch-4.md',
    'translation-gate-f-batch-5.md',
    'translation-consolidated.md',
]:
    p = speech / name
    if p.exists():
        p.unlink()

# Metadata release state.
mp = speech / 'metadata.json'
meta = json.loads(mp.read_text(encoding='utf-8'))
tr = meta['translation']
tr.update(
    {
        'placement': 'verified English follows the verified Tamil in canonical transcript.md',
        'working_file': 'translation.md',
        'working_file_status': 'retired pointer to canonical transcript after Gate H',
        'status': 'verified',
        'gate_f_status': 'complete',
        'gate_g_status': 'passed',
        'verified_against_tamil': True,
        'verification_gate': 'Gate G passed',
        'gate_g_reviewed_source_pages': '278-303',
        'gate_g_reviewed_printed_pages': '277-302',
        'gate_g_reviewed_page_count': 26,
        'gate_g_total_page_count': 26,
        'gate_g_next_source_page': None,
        'gate_g_correction_count': 2,
        'gate_g_unresolved_fidelity_issues': 0,
        'completion_note': (
            'Gate F translated all 26 verified Tamil source-page sections. Gate G re-read source pp.278-303 '
            'against the final verified Tamil and passed with two definite fidelity corrections and zero unresolved issues. '
            'Gate H reconstructed the complete verified English from the reviewed working segments, merged it after the '
            'verified Tamil in canonical transcript.md, validated exact 278-303 page correspondence, and retired split '
            'working translations to a pointer.'
        ),
    }
)
for k in ['working_files', 'consolidation_file', 'gate_g_unresolved_questions']:
    tr.pop(k, None)
meta['release'] = {
    'gate_h_status': 'passed',
    'canonical_transcript_contains_verified_tamil_and_english': True,
    'indexed': True,
    'release_ready': True,
}
mp.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Machine-readable index.
dp = root / 'data/speeches.json'
data = json.loads(dp.read_text(encoding='utf-8'))
data = [x for x in data if x.get('id') != '2000-05-08-industries-debate']
data.append(
    {
        'id': '2000-05-08-industries-debate',
        'date': '2000-05-08',
        'year': 2000,
        'speaker_ta': 'மு. கருணாநிதி',
        'speaker_en': 'M. Karunanidhi',
        'title_ta': 'தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 9',
        'title_en': "Kalaignar's Legislative Assembly Speeches on Industry — Speech 9",
        'event_ta': 'தொழில்துறை மானிய விவாத உரை',
        'event_en': 'Speech in the Industries grant debate',
        'path': 'speeches/2000/2000-05-08-industries-debate',
        'languages': ['ta', 'en'],
        'transcription_status': 'verified',
        'verified_against_scan': True,
        'translation_status': 'verified',
    }
)
data.sort(key=lambda x: x['date'])
dp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Speech README.
(speech / 'README.md').write_text(
    """# உரை : 9 — 8.05.2000

## தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்

**மூலத்தில் உள்ள பேச்சாளர் குறிப்பு:** மாண்புமிகு கலைஞர் மு. கருணாநிதி  
**மூல உரை எண்:** உரை : 9  
**மூலத்தில் அச்சிடப்பட்ட தேதி:** 8.05.2000  
**காப்பக ID:** `2000-05-08-industries-debate`

## Source and boundaries

- Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition May 2007.
- PDF scan pages: **278–303**.
- Printed pages: **277–302**.
- Scan p.277 closes Speech 8; p.278 begins Speech 9; p.303 closes Speech 9; p.304 begins Speech 10.
- Scan image is authoritative for Tamil; final verified Tamil is authoritative for English.

## Release status

Speech 9 is **fully released through Gate H**.

- Gate C: complete — 26/26 Tamil pages.
- Gate D: passed — complete ordered page-marker and boundary audit.
- Gate E: passed — 26/26 pages directly verified against the scan; **3 definite corrections**, **0 unresolved readings**.
- Gate F: complete — English translation for all 26 verified Tamil page sections.
- Gate G: passed — 26/26 English page sections fidelity-reviewed against final Tamil; **2 definite corrections**, **0 unresolved translation questions**.
- Gate H: passed — verified English merged after verified Tamil in canonical `transcript.md`; index updated; split working translations retired.
- Tamil: **verified**.
- English: **verified**.

The English translation deliberately retains Kalaignar’s parliamentary language and voice — argumentative sequence, repetition, humour, rhetoric, direct address, register shifts and source-supported oddities — rather than polishing it into generic modern English.

## Files

- [`transcript.md`](./transcript.md) — canonical verified Tamil followed by canonical verified English.
- [`metadata.json`](./metadata.json) — source, audit, translation and release state.
- [`source-notes.md`](./source-notes.md) — source authority, boundaries and source-sensitive observations.
- [`verification-log.md`](./verification-log.md) — Tamil and English gate audit trail.
- [`translation-review.md`](./translation-review.md) — Gate-G fidelity/voice review.
- [`translation.md`](./translation.md) — retired pointer to canonical English in `transcript.md`.
""",
    encoding='utf-8',
)

# Verification log: preserve Tamil audit, replace stale English tail.
vp = speech / 'verification-log.md'
v = vp.read_text(encoding='utf-8')
if '## English gates' in v:
    v = v.split('## English gates', 1)[0].rstrip()
v += """

## English gates

### Gate F — translation

**Complete: 26/26 pages, source pp.278–303 / printed pp.277–302.** Translation was made only from the final Gate-E-verified Tamil, with source-page correspondence and Kalaignar’s parliamentary voice retained.

### Gate G — fidelity and voice verification

**Passed: 26/26 pages.** All English page sections were re-read against the final verified Tamil. Two definite corrections were required:

1. p.284 — removed an unsupported generic “driving force of the world economy” transition and restored Kalaignar’s actual scientific-advance / join-and-compete / Tamil Nadu-first-place argumentative sequence.
2. p.286 — `இந்தக் கேமிரா கழுவும்போது` is retained in the source-sensitive English as “When this camera is washed,” rather than the interpretive Gate-F rendering “When this camera develops.”

Unresolved translation questions/fidelity issues: **0**. `verified_against_tamil=true`.

### Gate H — canonical release

**Passed.** The complete verified English was reconstructed from the Gate-G-reviewed working segments, validated to contain source pages **278–303 exactly once and in order**, and merged after the untouched verified Tamil in canonical `transcript.md`. Tamil source markers were revalidated as **278–303 exactly once and in order**. Split working translation files were retired to a single pointer file, `translation.md`; `translation-review.md` remains as the fidelity record. `data/speeches.json` and the root README speech index were updated.

Speech 9 is fully released with verified Tamil and verified English. Speech 10 was not started during this release activity.
"""
vp.write_text(v + '\n', encoding='utf-8')

# Root README index + active source statement.
rp = root / 'README.md'
r = rp.read_text(encoding='utf-8')
r = re.sub(
    r'\*\*Speeches 1–8, through 29\.04\.1999, are fully released with verified Tamil and verified English\. Speech 9 \(8\.05\.2000\) is the next archival unit\.\*\*',
    '**Speeches 1–9, through 8.05.2000, are fully released with verified Tamil and verified English. Speech 10 (23.08.2006) is the next archival unit.**',
    r,
)
row9 = '| 08-05-2000 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 9](./speeches/2000/2000-05-08-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 278–303 |'
if row9 not in r:
    anchor = '| 29-04-1999 | [தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள் — உரை : 8](./speeches/1999/1999-04-29-industries-debate/) | தொழில்துறை மானிய விவாத உரை | Verified | Verified | Verified against scan pp. 241–277 |'
    r = r.replace(anchor, anchor + '\n' + row9)
rp.write_text(r, encoding='utf-8')

# Handover now points to Speech 10 without starting it.
(root / 'docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md').write_text(
    """# Handover — 2007 industrial speeches anthology

## Source authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

Locked source: **329 PDF pages**, **217,124,211 bytes**, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Released speeches

**Speeches 1–9 are fully released through Gate H with verified Tamil and verified English. Do not restart, retranscribe or modify those released source/translation layers unless a concrete correction is explicitly requested and source-supported.**

Speech 9 (`2000-05-08-industries-debate`) is released across scan pp.278–303 / printed pp.277–302. Gate E passed with 3 Tamil corrections and 0 unresolved readings. Gate G passed with 2 English fidelity corrections and 0 unresolved questions. Gate H merged verified English after verified Tamil in canonical `transcript.md`, retired split working translations, and indexed the speech.

## Next archival unit — Speech 10

Locked mapping from `sources/2007-industrial-speeches/mapping.md`:

- source label: `உரை : 10`
- printed date: `23.08.2006`
- ISO date: `2006-08-23`
- canonical ID: `2006-08-23-industries-debate`
- scan/source pages: **304–326**
- printed pages: **303–325**
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10
- scan p.326 closes Speech 10
- scan pp.327–328 are `குறிப்புகள்`; p.329 is closing portrait/back matter

The 303–304 and 326–327 boundaries were already re-checked during anthology mapping. **Speech 10 has not been started.**

## Exact next activity

Start Speech 10 according to the archival workflow without modifying released Speeches 1–9:

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover and `sources/2007-industrial-speeches/mapping.md` completely.
2. Inspect scan p.304 directly and reconfirm the `உரை : 10` / `23.08.2006` opening before creating the canonical entry.
3. Continue only within the locked Speech-10 range pp.304–326; do not include note pages 327–328.
4. Create/continue `speeches/2006/2006-08-23-industries-debate/` and begin Gate C from the rendered scan in a bounded first batch.
5. Preserve printed wording, punctuation, figures, English, speaker labels, interventions and source-supported oddities; record uncertainty rather than guessing.
6. Do not begin English until Tamil Gates C–E are complete.
""",
    encoding='utf-8',
)

# Fresh next-chat prompt for Speech 10 startup.
(root / 'docs/NEXT_CHAT_PROMPT_2007_INDUSTRIAL_SPEECHES.md').write_text(
    """# Next-chat prompt — Speech 10 startup / 23.08.2006

Continue the Kalaignar Assembly Speeches archival project in `pugazg/kalaignar-assembly-speeches`.

Speeches **1–9** from the 2007 industrial-speeches anthology are fully released through Gate H with verified Tamil and verified English. **Do not restart, retranscribe or modify those released entries.** Speech 10 is the final mapped speech and has not been started.

## Mandatory startup

1. Read `docs/ARCHIVAL_WORKFLOW.md` completely.
2. Read `docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md` completely.
3. Read `sources/2007-industrial-speeches/mapping.md`.
4. Inspect the controlling scan directly before creating Speech-10 metadata.

## Speech 10 locked mapping

- source label: `உரை : 10`
- printed date: `23.08.2006`
- ISO date: `2006-08-23`
- canonical ID: `2006-08-23-industries-debate`
- scan/source pages: **304–326**
- printed pages: **303–325**
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10
- scan p.326 closes Speech 10
- scan pp.327–328 are `குறிப்புகள்`
- scan p.329 is closing portrait/back matter

The anthology mapping already re-confirmed boundaries 303–304 and 326–327. The controlling PDF is locked at 329 pages, 217,124,211 bytes, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Exact next activity — Speech 10 Gate C Batch 1

Reconfirm the p.304 opening directly from the rendered scan, then create/continue `speeches/2006/2006-08-23-industries-debate/` and transcribe a bounded first batch beginning at source p.304. Preserve source wording, historical spelling, punctuation, numerals, headings, speaker labels, interventions, repetition, unusual grammar and printed English. Use explicit `<!-- source-page: N -->` markers. Record uncertain readings rather than guessing. Do not include scan pp.327–329 and do not begin English translation.
""",
    encoding='utf-8',
)

print('Speech 9 Gate H release reconstruction and validation succeeded.')
