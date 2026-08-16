from pathlib import Path
import json

base = Path('speeches/2006/2006-08-23-industries-debate')

# transcript
p = base/'transcript.md'
s = p.read_text(encoding='utf-8')
old = 'அனைத்துச் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு'
new = 'அனைத்துக் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு'
if s.count(old) != 1:
    raise SystemExit(f'expected one p312 correction target, got {s.count(old)}')
s = s.replace(old,new,1)
old_note = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batch 1 directly re-read source/scan pp.304–308 / printed pp.303–307 against the controlling rendered scan. Two definite source-supported corrections were applied (p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`; p.307 `சிறிய பகுதியாகும்` → `சிறிய பகுதியேயாகும்`). Gate-E coverage: **5/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
new_note = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batches 1–2 directly re-read source/scan pp.304–313 / printed pp.303–312 against the controlling rendered scan. Three definite source-supported corrections have been applied cumulatively: p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`; p.307 `சிறிய பகுதியாகும்` → `சிறிய பகுதியேயாகும்`; p.312 `அனைத்துச் கூட்டுறவுச்` → `அனைத்துக் கூட்டுறவுச்`. Gate-E coverage: **10/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
if old_note not in s:
    raise SystemExit('transcript verification note not found')
s = s.replace(old_note,new_note,1)
p.write_text(s,encoding='utf-8')

# metadata
mp = base/'metadata.json'
m = json.loads(mp.read_text(encoding='utf-8'))
t = m['transcription']
t['gate_e_status']='in-progress'
t['gate_e_audited_scan_pages']='304-313'
t['gate_e_audited_printed_pages']='303-312'
t['gate_e_audited_page_count']=10
t['gate_e_total_page_count']=23
t['gate_e_correction_count']=3
t['gate_e_next_scan_page']=314
t['verified_against_scan']=False
t['unresolved_readings']=0
t['completion_note']=('Gate C is complete for all 23 mapped Speech-10 pages and Gate D passed the structural completeness/page-marker/boundary audit. '
'Gate E Batches 1-2 directly re-read source pp.304-313 / printed pp.303-312 against the controlling rendered scan. '
'Three definite corrections have been applied cumulatively: p.305 `கடமைப்பட்டிருக்கின்றேன்` → `கடமைப் பட்டிருக்கின்றேன்`; '
'p.307 `Equity, சிறிய பகுதியாகும்.` → `Equity, சிறிய பகுதியேயாகும்.`; '
'p.312 `அனைத்துச் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு` → `அனைத்துக் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு`. '
'Gate E coverage is 10/23 pages; unresolved readings remain 0. Tamil is not verified until all 23 mapped pages pass Gate E.')
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# README
rp=base/'README.md'
r=rp.read_text(encoding='utf-8')
r=r.replace('- Gate E: **not started**.','- Gate E: **in progress — 10/23 pages verified (source pp.304–313 / printed pp.303–312), 3 cumulative definite corrections, 0 unresolved readings**.',1)
r=r.replace('The next activity is **Gate E Batch 2 — direct source-fidelity verification of source pp.309–313 / printed pp.308–312**. Do not begin English yet.','The next activity is **Gate E Batch 3 — direct source-fidelity verification of source pp.314–318 / printed pp.313–317**. Do not begin English yet.',1)
rp.write_text(r,encoding='utf-8')

# source notes
sp=base/'source-notes.md'
sn=sp.read_text(encoding='utf-8')
sn += '\n## Gate E Batch 2 — source pp.309–313\n\nFive pages were directly re-read against the controlling rendered scan. One definite source-supported correction was applied to the canonical Tamil:\n\n1. p.312 `அனைத்துச் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு` → `அனைத்துக் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு`.\n\nNo other definite correction was required on pp.309–313. The p.309 `வெட்டுத் தீர்மானங்கள்` / `வெட்டித் தீர்மானங்கள்` wordplay, p.310 juice/election-symbol humour, p.311 industrial-policy wording, p.312 printed `wine` passage, and p.313 `Skill development` / `Special Economic Zone` material were retained without normalisation. Cumulative Gate-E coverage: **10/23 pages**; cumulative definite corrections: **3**; unresolved readings: **0**.\n'
sp.write_text(sn,encoding='utf-8')

# verification log
vp=base/'verification-log.md'
v=vp.read_text(encoding='utf-8')
v=v.replace('Continue **Gate E Batch 2 — source/scan pp.309–313 / printed pp.308–312** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.','Continue **Gate E Batch 3 — source/scan pp.314–318 / printed pp.313–317** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.',1)
v += '\n### Batch 2 — source pp.309–313 / printed pp.308–312\n\n**Complete.** All five pages were directly re-read against the controlling rendered scan.\n\n- cumulative Gate-E coverage: **10/23 pages**;\n- definite corrections in Batch 2: **1**;\n- cumulative definite corrections: **3**;\n- unresolved readings: **0**;\n- next source page: **314**.\n\nCorrection:\n\n1. p.312 `அனைத்துச் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு` → `அனைத்துக் கூட்டுறவுச் சர்க்கரை ஆலைகளுக்கு`.\n\nNo other definite source-text correction was required on pp.309–313. Tamil remains **not verified** until all 23 mapped pages pass Gate E. English Gate F remains blocked.\n'
vp.write_text(v,encoding='utf-8')

# handover
hp=Path('docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md')
h=hp.read_text(encoding='utf-8')
h=h.replace('- Gate E: **not started**;','- Gate E: **in progress — 10/23 pages verified; 3 cumulative definite corrections; 0 unresolved readings**;',1)
start=h.find('## Exact next activity — Speech 10 Gate E Batch 2')
if start!=-1:
    h=h[:start]+'''## Exact next activity — Speech 10 Gate E Batch 3\n\n1. Directly compare rendered source/scan pp.314–318 / printed pp.313–317 against the canonical Tamil.\n2. Use the scan image as textual authority; do not normalise or externally correct source wording.\n3. Apply and document only definite source-supported corrections.\n4. Preserve humour, repetition, printed English, figures, speaker/intervention labels and unusual grammar.\n5. Keep `verified_against_scan=false` until all 23 pages pass Gate E.\n6. Do not begin English until Gate E is complete.\n'''
hp.write_text(h,encoding='utf-8')
