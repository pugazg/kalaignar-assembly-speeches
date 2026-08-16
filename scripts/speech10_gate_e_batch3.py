from pathlib import Path
import json

base = Path('speeches/2006/2006-08-23-industries-debate')
transcript = base / 'transcript.md'
text = transcript.read_text(encoding='utf-8')

repls = {
    'குற்றம் சுமத்திவிட்டாலேயே, குற்றவாளியாக ஆகிவிடமுடியாது.': 'குற்றம் சுமத்திவிட்டதாலேயே, குற்றவாளியாக ஆகிவிடமுடியாது.',
    'நமது நாட்டினுடைய சமூகாயப் பொருளாதார வளர்ச்சிக்கும்': 'நமது நாட்டினுடைய சமுதாயப் பொருளாதார வளர்ச்சிக்கும்',
    'பெற்று, உயர்கும் உன்னதமான வாய்ப்பு': 'பெற்று, உயரும் உன்னதமான வாய்ப்பு',
}
for old, new in repls.items():
    if text.count(old) != 1:
        raise SystemExit(f'expected exactly one occurrence: {old!r}; got {text.count(old)}')
    text = text.replace(old, new, 1)

old_note_start = '> **Tamil verification note:**'
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith(old_note_start):
        lines[i] = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batches 1–3 directly re-read source/scan pp.304–318 / printed pp.303–317 against the controlling rendered scan. Six definite source-supported corrections have been applied cumulatively; Batch 3 adds p.314 `சுமத்திவிட்டாலேயே` → `சுமத்திவிட்டதாலேயே`, p.315 `சமூகாயப் பொருளாதார` → `சமுதாயப் பொருளாதார`, and p.316 `உயர்கும் உன்னதமான` → `உயரும் உன்னதமான`. Gate-E coverage: **15/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
        break
else:
    raise SystemExit('Tamil verification note not found')
text = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
transcript.write_text(text, encoding='utf-8')

mp = base / 'metadata.json'
m = json.loads(mp.read_text(encoding='utf-8'))
t = m['transcription']
t['gate_e_status'] = 'in-progress'
t['gate_e_audited_scan_pages'] = '304-318'
t['gate_e_audited_printed_pages'] = '303-317'
t['gate_e_audited_page_count'] = 15
t['gate_e_total_page_count'] = 23
t['gate_e_correction_count'] = 6
t['gate_e_next_scan_page'] = 319
t['verified_against_scan'] = False
t['unresolved_readings'] = 0
t['completion_note'] = ('Gate C is complete for all 23 mapped Speech-10 pages and Gate D passed the structural completeness/page-marker/boundary audit. '
    'Gate E Batches 1-3 directly re-read source pp.304-318 / printed pp.303-317 against the controlling rendered scan. '
    'Six definite corrections have been applied cumulatively. Batch 3 corrections: p.314 `குற்றம் சுமத்திவிட்டாலேயே` → `குற்றம் சுமத்திவிட்டதாலேயே`; '
    'p.315 `சமூகாயப் பொருளாதார` → `சமுதாயப் பொருளாதார`; p.316 `உயர்கும் உன்னதமான` → `உயரும் உன்னதமான`. '
    'Gate E coverage is 15/23 pages; unresolved readings remain 0. Tamil is not verified until all 23 mapped pages pass Gate E.')
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

rp = base / 'README.md'
r = rp.read_text(encoding='utf-8')
import re
r = re.sub(r'- Gate E: \*\*in progress[^\n]*\*\*\.', '- Gate E: **in progress — 15/23 pages verified (source pp.304–318 / printed pp.303–317), 6 definite corrections, 0 unresolved readings**.', r, count=1)
r = r.replace('The next activity is **Gate E Batch 2 — direct source-fidelity verification of source pp.309–313 / printed pp.308–312**. Do not begin English yet.', 'The next activity is **Gate E Batch 4 — direct source-fidelity verification of source pp.319–323 / printed pp.318–322**. Do not begin English yet.', 1)
rp.write_text(r, encoding='utf-8')

sp = base / 'source-notes.md'
s = sp.read_text(encoding='utf-8')
s += '''\n## Gate E Batch 3 — source pp.314–318\n\nFive pages were directly re-read against the controlling rendered scan. Three definite source-supported corrections were applied to the canonical Tamil:\n\n1. p.314 `குற்றம் சுமத்திவிட்டாலேயே` → `குற்றம் சுமத்திவிட்டதாலேயே`;\n2. p.315 `சமூகாயப் பொருளாதார` → `சமுதாயப் பொருளாதார`;\n3. p.316 `உயர்கும் உன்னதமான` → `உயரும் உன்னதமான`.\n\nNo other definite correction was required on pp.314–318. The labour-rights passage, `T.N.P.L`, `F.I.R.`, industrial-revolution discussion, `Bio-Technology Revolution`, `State Industries Promotion Corporation of Tamil Nadu`, `park-கள் பூங்காக்கள்`, SIPCOT history, acreage/investment figures and stage markers were retained without normalisation. Cumulative Gate-E coverage: **15/23 pages**; cumulative corrections: **6**; unresolved readings: **0**.\n'''
sp.write_text(s, encoding='utf-8')

vp = base / 'verification-log.md'
v = vp.read_text(encoding='utf-8')
v = v.replace('Continue **Gate E Batch 2 — source/scan pp.309–313 / printed pp.308–312** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.', 'Continue **Gate E Batch 4 — source/scan pp.319–323 / printed pp.318–322** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.', 1)
v += '''\n### Batch 3 — source pp.314–318 / printed pp.313–317\n\n**Complete.** All five pages were directly re-read against the controlling rendered scan.\n\n- cumulative Gate-E coverage: **15/23 pages**;\n- definite corrections in Batch 3: **3**;\n- cumulative definite Gate-E corrections: **6**;\n- unresolved readings: **0**;\n- next source page: **319**.\n\nCorrections:\n\n1. p.314 `குற்றம் சுமத்திவிட்டாலேயே` → `குற்றம் சுமத்திவிட்டதாலேயே`;\n2. p.315 `சமூகாயப் பொருளாதார` → `சமுதாயப் பொருளாதார`;\n3. p.316 `உயர்கும் உன்னதமான` → `உயரும் உன்னதமான`.\n\nNo other definite correction was required in pp.314–318. Tamil remains **not verified** until all 23 mapped pages pass Gate E. English Gate F remains blocked.\n'''
vp.write_text(v, encoding='utf-8')

hp = Path('docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md')
h = hp.read_text(encoding='utf-8')
h = re.sub(r'- Gate E: \*\*in progress[^\n]*\*\*', '- Gate E: **in progress — 15/23 pages verified; 6 definite corrections; 0 unresolved readings**', h, count=1)
heading = '## Exact next activity — Speech 10 Gate E Batch 2'
start = h.find(heading)
if start != -1:
    h = h[:start] + '''## Exact next activity — Speech 10 Gate E Batch 4\n\n1. Directly compare rendered source/scan pp.319–323 / printed pp.318–322 against the canonical Tamil.\n2. Use the scan image as textual authority; do not normalise or externally correct source wording.\n3. Apply and document only definite source-supported corrections.\n4. Preserve humour, repetition, printed English, figures, speaker/intervention labels and unusual grammar.\n5. Keep `verified_against_scan=false` until all 23 pages pass Gate E.\n6. Do not begin English until Gate E is complete.\n'''
hp.write_text(h, encoding='utf-8')
