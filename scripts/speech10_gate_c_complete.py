from pathlib import Path
import json, re

root = Path('.')
speech = root / 'speeches/2006/2006-08-23-industries-debate'
transcript = speech / 'transcript.md'
staged = root / 'tmp/speech10-gate-c-remaining.md'

text = transcript.read_text(encoding='utf-8').rstrip()
append = staged.read_text(encoding='utf-8').strip()
if '<!-- source-page: 309 -->' not in append or '<!-- source-page: 326 -->' not in append:
    raise SystemExit('staged transcription does not contain expected remaining-page boundaries')
if '<!-- source-page: 309 -->' in text:
    raise SystemExit('source p.309 already present in transcript; refusing duplicate append')

# Close Gate C note and append all remaining Speech-10 pages.
text = re.sub(
    r'> \*\*Gate C first-pass note:\*\*[^\n]*',
    '> **Gate C first-pass note:** Speech 10 Gate C is complete for source/scan pp.304–326 / printed pp.303–325. All 23 mapped pages have first-pass Tamil transcription from the controlling rendered scan. Tamil status: **transcribed; not verified**. Unresolved first-pass readings: **0**. Gate D has not yet begun.',
    text,
    count=1,
)
transcript.write_text(text + '\n\n' + append + '\n', encoding='utf-8')

# Structural Gate-C validation.
merged = transcript.read_text(encoding='utf-8')
markers = [int(x) for x in re.findall(r'<!-- source-page: (\d+) -->', merged)]
expected = list(range(304, 327))
if markers != expected:
    raise SystemExit(f'page marker mismatch: {markers}')
if merged.count('<!-- source-page: 326 -->') != 1:
    raise SystemExit('p.326 marker count is not one')
if 'குறிப்புகள்' in append:
    raise SystemExit('note pages accidentally included in staged Speech-10 transcription')

# Metadata.
mp = speech / 'metadata.json'
meta = json.loads(mp.read_text(encoding='utf-8'))
tr = meta['transcription']
tr.update({
    'status': 'transcribed',
    'gate_c_status': 'complete',
    'completed_scan_pages': '304-326',
    'completed_printed_pages': '303-325',
    'completed_page_count': 23,
    'total_page_count': 23,
    'next_scan_page': None,
    'page_markers_audited_for_completed_batch': True,
    'full_speech_page_markers_present': True,
    'gate_d_status': 'not-started',
    'gate_e_status': 'not-started',
    'verified_against_scan': False,
    'explicit_unresolved_reading_markers': 0,
    'unresolved_readings': 0,
    'completion_note': 'Gate C is complete for all 23 mapped Speech-10 pages, scan/source pp.304-326 / printed pp.303-325. Source-page markers 304-326 are present exactly once and in order. The continuation from p.308 through p.326 was read directly from rendered scan pages. Rendered p.326 closes the speech with the final desk-thumping marker and closing ornament. Rendered pp.327-328 are blank note pages headed `குறிப்புகள்`; p.329 is portrait/back matter and none are included in the speech transcript. Tamil remains unverified until Gates D and E.'
})
mp.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# README.
(speech / 'README.md').write_text('''# உரை : 10 — 23.08.2006

## தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்

**மூலத்தில் உள்ள பேச்சாளர் குறிப்பு:** மாண்புமிகு கலைஞர் மு. கருணாநிதி  
**மூல உரை எண்:** உரை : 10  
**மூலத்தில் அச்சிடப்பட்ட தேதி:** 23.08.2006  
**காப்பக ID:** `2006-08-23-industries-debate`

## Source and boundaries

- Controlling publication: `தொழில்துறை பற்றி கலைஞரின் சட்டமன்ற உரைகள்`, first edition May 2007.
- Locked scan/source pages: **304–326**.
- Locked printed pages: **303–325**.
- Scan p.303 closes released Speech 9.
- Rendered p.304 directly shows `உரை : 10` / `நாள் : 23.08.2006`.
- Rendered p.326 closes Speech 10 with the final desk-thumping marker and closing ornament.
- Rendered pp.327–328 are blank `குறிப்புகள்` pages; p.329 is portrait/back matter. They are not part of Speech 10.
- The scan image is authoritative for Tamil transcription.

## Current archival state

- Gate C: **complete — 23/23 pages, source pp.304–326 / printed pp.303–325**.
- Source-page markers: **304–326, exactly once and in order**.
- Unresolved first-pass readings: **0**.
- Tamil: **transcribed; not verified**.
- Gate D: **not started**.
- Gate E: **not started**.
- English Gate F: **blocked until verified Tamil is complete**.

The next activity is **Gate D — full Tamil completeness/page-marker/boundary audit**. Do not begin English yet.

## Files

- [`transcript.md`](./transcript.md) — complete Gate-C Tamil first-pass transcription.
- [`metadata.json`](./metadata.json) — source mapping and gate status.
- [`source-notes.md`](./source-notes.md) — source authority, boundaries and source-sensitive observations.
- [`verification-log.md`](./verification-log.md) — gate audit trail.
''', encoding='utf-8')

# Source notes: preserve Batch 1 details and add completion section.
sp = speech / 'source-notes.md'
s = sp.read_text(encoding='utf-8').rstrip()
s += '''\n\n## Gate C completion — source pp.309–326\n\nThe remaining eighteen mapped speech pages were read directly from the rendered scan and appended in one completion activity. Cumulative Gate-C coverage is now **23/23 pages, source pp.304–326 / printed pp.303–325**. No genuinely uncertain first-pass reading remains.\n\nSource-sensitive material deliberately retained includes the p.309 `வெட்டுத் தீர்மானங்கள்` / `வெட்டித் தீர்மானங்கள்` joke; the p.310 juice/party-symbol humour; p.312 printed `wine`; p.313 `Skill development` and `Special Economic Zone`; p.314 `T.N.P.L`, `F.I.R.` and labour-rights passage; p.316 `Bio-Technology Revolution`; p.317 `State Industries Promotion Corporation of Tamil Nadu` and `park-கள் பூங்காக்கள்`; pp.318–320 the exact SIPCOT acreage/investment/index figures and `Single Window System`; p.322 `Automotive Special Economic Zone` and `Reverse Osmosis`; p.323 `Co-generation`; p.324 `Natural gas distribution network`; p.325 `I.T. Task Force` and `e-governance`; and p.326 `I.T. Expressway`, road-length/cost figures and final closing words.\n\nRendered p.326 visibly ends Speech 10 with the final paragraph, desk-thumping marker and closing ornament. Rendered pp.327–328 were also inspected and are blank note pages headed `குறிப்புகள்`; p.329 is portrait/back matter. None were transcribed into Speech 10.\n\nGate C is a first-pass transcription only. The next activity is Gate D structural completeness/page-marker/boundary audit; Gate E source-fidelity verification has not started.\n'''
sp.write_text(s + '\n', encoding='utf-8')

# Verification log.
vp = speech / 'verification-log.md'
v = vp.read_text(encoding='utf-8')
if '## Later gates' in v:
    v = v.split('## Later gates', 1)[0].rstrip()
v += '''\n\n### Gate C completion — source pp.309–326 / printed pp.308–325\n\n**Complete.** All remaining eighteen Speech-10 pages were transcribed from the controlling rendered scan.\n\n- cumulative Gate-C coverage: **23/23 pages**;\n- mapped source range: **304–326**;\n- mapped printed range: **303–325**;\n- source-page markers: **304–326**, exactly once and in order;\n- unresolved first-pass readings: **0**;\n- Tamil status: **transcribed; not verified**;\n- next Gate-C page: **none**.\n\nRendered p.326 was inspected through the final desk-thumping marker and closing ornament. Rendered pp.327–328 are `குறிப்புகள்` pages and p.329 is portrait/back matter; they were explicitly excluded from the speech transcript.\n\n## Later gates\n\n- Gate D: **not started**;\n- Gate E: **not started**;\n- Gate F English: **blocked**;\n- Gate G English verification: **not started**;\n- Gate H release: **not started**.\n\n## Exact next activity\n\nRun **Gate D — full Tamil completeness/page-marker/boundary audit** for source pp.304–326. Confirm all 23 markers and speech boundaries structurally without treating Gate D as source-fidelity verification. Do not begin English.\n'''
vp.write_text(v + '\n', encoding='utf-8')

# Handover.
hp = root / 'docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md'
hp.write_text('''# Handover — 2007 industrial speeches anthology

## Source authority

Continue `pugazg/kalaignar-assembly-speeches` using the controlling scan `TVA_BOK_0065516_தொழில்துறை_பற்றி_கலைஞரின்_சட்டமன்ற_உரைகள்.pdf`.

The scan image is authoritative for Tamil transcription and verification. English must be translated and fidelity-reviewed against the final verified Tamil. Follow `docs/ARCHIVAL_WORKFLOW.md`.

Locked source: **329 PDF pages**, **217,124,211 bytes**, SHA-256 `c26003fe77b97adc6487ba0e4c00c9fa34a0a53839aa326d3ef5897f8616d370`.

## Released speeches

**Speeches 1–9 are fully released through Gate H with verified Tamil and verified English. Do not restart, retranscribe or modify those released source/translation layers unless a concrete correction is explicitly requested and source-supported.**

## Active archival unit — Speech 10

- source label: `உரை : 10`
- printed date: `23.08.2006`
- ISO date: `2006-08-23`
- canonical ID: `2006-08-23-industries-debate`
- scan/source pages: **304–326**
- printed pages: **303–325**
- scan p.303 closes Speech 9
- scan p.304 begins Speech 10
- scan p.326 closes Speech 10
- scan pp.327–328 are `குறிப்புகள்`; p.329 is portrait/back matter

Rendered p.304 was directly inspected at startup and reconfirmed the `உரை : 10` / `23.08.2006` opening. Rendered p.326 was inspected through the closing ornament; rendered pp.327–329 were inspected and confirmed as non-speech material.

## Current Speech-10 state

Gate C is **complete**:

- transcribed source/scan pages: **304–326**
- corresponding printed pages: **303–325**
- cumulative coverage: **23/23 pages**
- page markers: **304–326**, once and in order
- unresolved first-pass readings: **0**
- Tamil status: **transcribed; not verified**
- Gate D: **not started**
- Gate E: **not started**
- English Gate F: **blocked**

The completion activity continued directly from the p.308 ending `ஆக, 285 வெட்டுத் தீர்மானங்கள்;` through source p.326. Non-speech note/back-matter pages 327–329 were not included.

## Exact next activity — Speech 10 Gate D

1. Read `docs/ARCHIVAL_WORKFLOW.md`, this handover and the Speech-10 metadata/README/source notes/transcript/verification log.
2. Perform a **full Tamil completeness/page-marker/boundary audit** across source pp.304–326.
3. Confirm markers 304–326 occur exactly once and in order, with no Speech-9 spillover and no `குறிப்புகள்`/back-matter spillover.
4. Audit speaker/intervention continuity and page-crossing sentence continuity structurally.
5. Gate D is not Gate E: do not claim source-fidelity verification merely from this structural audit.
6. Do not begin English until Gate E has fully verified the Tamil against the scan.
''', encoding='utf-8')

print('Speech 10 Gate C completion reconstruction and validation succeeded.')
