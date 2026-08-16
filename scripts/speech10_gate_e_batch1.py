from pathlib import Path
import json

base = Path('speeches/2006/2006-08-23-industries-debate')
transcript = base/'transcript.md'
text = transcript.read_text(encoding='utf-8')
repls = {
    'எடுத்துக்கூறக் கடமைப்பட்டிருக்கின்றேன்.': 'எடுத்துக்கூறக் கடமைப் பட்டிருக்கின்றேன்.',
    'Equity, சிறிய பகுதியாகும்.': 'Equity, சிறிய பகுதியேயாகும்.',
}
for old,new in repls.items():
    if text.count(old) != 1:
        raise SystemExit(f'expected exactly one occurrence: {old!r}, got {text.count(old)}')
    text = text.replace(old,new,1)
old_note = '> **Gate C first-pass note:** Speech 10 Gate C is complete for source/scan pp.304–326 / printed pp.303–325. All 23 mapped pages have first-pass Tamil transcription from the controlling rendered scan. Tamil status: **transcribed; not verified**. Unresolved first-pass readings: **0**. Gate D has not yet begun.'
new_note = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batch 1 directly re-read source/scan pp.304–308 / printed pp.303–307 against the controlling rendered scan. Two definite source-supported corrections were applied (p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`; p.307 `சிறிய பகுதியாகும்` → `சிறிய பகுதியேயாகும்`). Gate-E coverage: **5/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
if old_note not in text:
    raise SystemExit('transcript header note not found')
text = text.replace(old_note,new_note,1)
transcript.write_text(text,encoding='utf-8')

mp = base/'metadata.json'
m = json.loads(mp.read_text(encoding='utf-8'))
t = m['transcription']
t['gate_d_status'] = 'passed'
t['gate_e_status'] = 'in-progress'
t['gate_e_audited_scan_pages'] = '304-308'
t['gate_e_audited_printed_pages'] = '303-307'
t['gate_e_audited_page_count'] = 5
t['gate_e_total_page_count'] = 23
t['gate_e_correction_count'] = 2
t['gate_e_next_scan_page'] = 309
t['verified_against_scan'] = False
t['unresolved_readings'] = 0
t['completion_note'] = ('Gate C is complete for all 23 mapped Speech-10 pages and Gate D passed the structural completeness/page-marker/boundary audit. '
    'Gate E Batch 1 directly re-read source pp.304-308 / printed pp.303-307 against the controlling rendered scan. '
    'Two definite corrections were applied: p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`; '
    'p.307 `Equity, சிறிய பகுதியாகும்.` → `Equity, சிறிய பகுதியேயாகும்.`. '
    'Gate E coverage is 5/23 pages; unresolved readings remain 0. Tamil is not verified until all 23 mapped pages pass Gate E.')
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

rp = base/'README.md'
r = rp.read_text(encoding='utf-8')
old = '- Gate D: **passed**.\n- Gate E: **not started**.\n- English Gate F: **blocked until verified Tamil is complete**.'
if old not in r:
    old = '- Gate D: **not started**.\n- Gate E: **not started**.\n- English Gate F: **blocked until verified Tamil is complete**.'
new = '- Gate D: **passed**.\n- Gate E: **in progress — 5/23 pages verified (source pp.304–308 / printed pp.303–307), 2 definite corrections, 0 unresolved readings**.\n- English Gate F: **blocked until verified Tamil is complete**.'
if old not in r:
    raise SystemExit('README gate block not found')
r = r.replace(old,new,1)
r = r.replace('The next activity is **Gate D — full Tamil completeness/page-marker/boundary audit**. Do not begin English yet.', 'The next activity is **Gate E Batch 2 — direct source-fidelity verification of source pp.309–313 / printed pp.308–312**. Do not begin English yet.',1)
rp.write_text(r,encoding='utf-8')

sp = base/'source-notes.md'
s = sp.read_text(encoding='utf-8')
s += '\n## Gate E Batch 1 — source pp.304–308\n\nFive pages were directly re-read against the controlling rendered scan. Two definite source-supported corrections were applied to the canonical Tamil:\n\n1. p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`;\n2. p.307 `Equity, சிறிய பகுதியாகும்.` → `Equity, சிறிய பகுதியேயாகும்.`.\n\nNo other definite correction was required on pp.304–308. Source-sensitive wording, figures, printed English, humour and stage markers were retained without normalisation. Cumulative Gate-E coverage: **5/23 pages**; unresolved readings: **0**.\n'
sp.write_text(s,encoding='utf-8')

vp = base/'verification-log.md'
v = vp.read_text(encoding='utf-8')
v = v.replace('- Gate D: **not started**;', '- Gate D: **passed**;',1)
v = v.replace('- Gate E: **not started**;', '- Gate E: **in progress**;',1)
v = v.replace('Run **Gate D — full Tamil completeness/page-marker/boundary audit** for source pp.304–326. Confirm all 23 markers and speech boundaries structurally without treating Gate D as source-fidelity verification. Do not begin English.', 'Continue **Gate E Batch 2 — source/scan pp.309–313 / printed pp.308–312** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.',1)
v += '\n## Gate E — strict Tamil source-fidelity verification\n\n### Batch 1 — source pp.304–308 / printed pp.303–307\n\n**Complete.** All five pages were directly re-read against the controlling rendered scan.\n\n- cumulative Gate-E coverage: **5/23 pages**;\n- definite corrections in Batch 1: **2**;\n- unresolved readings: **0**;\n- next source page: **309**.\n\nCorrections:\n\n1. p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`;\n2. p.307 `Equity, சிறிய பகுதியாகும்.` → `Equity, சிறிய பகுதியேயாகும்.`.\n\nTamil remains **not verified** until all 23 mapped pages pass Gate E. English Gate F remains blocked.\n'
vp.write_text(v,encoding='utf-8')

hp = Path('docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md')
h = hp.read_text(encoding='utf-8')
h = h.replace('- Gate D: **not started**\n- Gate E: **not started**\n- English Gate F: **blocked**', '- Gate D: **passed**\n- Gate E: **in progress — 5/23 pages verified; 2 definite corrections; 0 unresolved readings**\n- English Gate F: **blocked**',1)
start = h.find('## Exact next activity — Speech 10 Gate D')
if start != -1:
    h = h[:start] + '''## Exact next activity — Speech 10 Gate E Batch 2\n\n1. Directly compare rendered source/scan pp.309–313 / printed pp.308–312 against the canonical Tamil.\n2. Use the scan image as textual authority; do not normalise or externally correct source wording.\n3. Apply and document only definite source-supported corrections.\n4. Preserve humour, repetition, printed English, figures, speaker/intervention labels and unusual grammar.\n5. Keep `verified_against_scan=false` until all 23 pages pass Gate E.\n6. Do not begin English until Gate E is complete.\n'''
hp.write_text(h,encoding='utf-8')
