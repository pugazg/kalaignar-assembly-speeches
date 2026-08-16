from pathlib import Path
import json

base = Path('speeches/2006/2006-08-23-industries-debate')

# No canonical Tamil source-text correction was required in Gate E Batch 4.
# Update only archival status/documentation after direct scan verification of pp.319-323.

tp = base/'transcript.md'
t = tp.read_text(encoding='utf-8')
old_note = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batches 1–3 directly re-read source/scan pp.304–318 / printed pp.303–317 against the controlling rendered scan. Six definite source-supported corrections have been applied cumulatively; Batch 3 adds p.314 `சுமத்திவிட்டாலேயே` → `சுமத்திவிட்டதாலேயே`, p.315 `சமூகாயப் பொருளாதார` → `சமுதாயப் பொருளாதார`, and p.316 `உயர்கும் உன்னதமான` → `உயரும் உன்னதமான`. Gate-E coverage: **15/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
new_note = '> **Tamil verification note:** Gate C is complete and Gate D passed. Gate E Batches 1–4 directly re-read source/scan pp.304–323 / printed pp.303–322 against the controlling rendered scan. Six definite source-supported corrections have been applied cumulatively; Batch 4 (pp.319–323) required **no canonical Tamil correction**. Gate-E coverage: **20/23 pages**. Tamil status: **verification in progress; not verified**. Unresolved readings: **0**.'
if old_note not in t:
    raise SystemExit('transcript Gate-E note not found')
t = t.replace(old_note,new_note,1)
tp.write_text(t,encoding='utf-8')

mp = base/'metadata.json'
m = json.loads(mp.read_text(encoding='utf-8'))
tr = m['transcription']
tr['gate_e_status'] = 'in-progress'
tr['gate_e_audited_scan_pages'] = '304-323'
tr['gate_e_audited_printed_pages'] = '303-322'
tr['gate_e_audited_page_count'] = 20
tr['gate_e_total_page_count'] = 23
tr['gate_e_correction_count'] = 6
tr['gate_e_next_scan_page'] = 324
tr['verified_against_scan'] = False
tr['unresolved_readings'] = 0
tr['completion_note'] = ('Gate C is complete for all 23 mapped Speech-10 pages and Gate D passed the structural completeness/page-marker/boundary audit. '
    'Gate E Batches 1-4 directly re-read source pp.304-323 / printed pp.303-322 against the controlling rendered scan. '
    'Six definite corrections have been applied cumulatively. Batch 4 (source pp.319-323) required no canonical Tamil correction. '
    'The Batch-4 reread reconfirmed the CMIE infrastructure/index figures and 1989-96 industrial-ranking passage; the 1994-95/1999-2000 growth figures and Single Window System passage; the Paramapada Sopanam metaphor and 2,000-acre SIPCOT expansion announcement; Detroit/Automotive Special Economic Zone, Madurai industrial park, Reverse Osmosis and 250-acre leather SEZ announcements; and the TNPL paper-expansion, wind-power, Co-generation, ethanol and Perambalur integrated industrial park announcements. '
    'Gate E coverage is 20/23 pages; unresolved readings remain 0. Tamil is not verified until all 23 mapped pages pass Gate E.')
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

rp = base/'README.md'
r = rp.read_text(encoding='utf-8')
r = r.replace('- Gate E: **in progress — 15/23 pages verified (source pp.304–318 / printed pp.303–317), 6 definite corrections, 0 unresolved readings**.', '- Gate E: **in progress — 20/23 pages verified (source pp.304–323 / printed pp.303–322), 6 definite corrections, 0 unresolved readings**.',1)
r = r.replace('The next activity is **Gate E Batch 3 — direct source-fidelity verification of source pp.314–318 / printed pp.313–317**. Do not begin English yet.', 'The next activity is **Gate E final Batch 5 — direct source-fidelity verification of source pp.324–326 / printed pp.323–325**, including the Speech-10 closing boundary. Do not begin English yet.',1)
rp.write_text(r,encoding='utf-8')

sp = base/'source-notes.md'
s = sp.read_text(encoding='utf-8')
s += '''\n## Gate E Batch 4 — source pp.319–323 / printed pp.318–322\n\nFive pages were directly re-read against the controlling rendered scan. **No canonical Tamil source-text correction was required in this batch.**\n\nThe reread explicitly reconfirmed source-sensitive material without normalisation, including:\n\n- p.319 the listed industrial/company names, `Centre for Monitoring Indian Economy`, infrastructure index figures `145.62 / 106.12 / 104.01`, city figures `472.48 / 153 / 100.28`, and the `1989-1991` / `1991-1996` industrial-ranking argument;\n- p.320 `1994-1995`, `8.7`, `1999-2000`, `15.02`, `Single Window System`, the eight-permission sequence and the Paramapada Sopanam setup;\n- p.321 the Paramapada Sopanam continuation, the announcements transition, SIPCOT Thiruperumbudur/Oragadam expansion and `2000`-acre land-acquisition statement;\n- p.322 `ஆசியாவின் டெட்ராய்ட்` / `(Detroit)`, `35 சதவிகிதம்`, `Automotive Special Economic Zone`, the Madurai industrial-park announcement, `ரூபாய் 115 கோடி`, `11` common effluent-treatment plants, `Reverse Osmosis`, and the `250 ஏக்கர்` leather SEZ;\n- p.323 TNPL `2,30,000` / `1,20,000` metric-ton figures, `650 கோடி`, `30 கோடி`, `6.25 மெகாவாட்`, `Co-generation`, `13.50 கோடி`, `6 மெகாவாட்`, ethanol, and the Perambalur `5,000 கோடி` integrated industrial park / SEZ announcement.\n\nCumulative Gate-E coverage: **20/23 pages**; cumulative definite corrections: **6**; unresolved readings: **0**.\n'''
sp.write_text(s,encoding='utf-8')

vp = base/'verification-log.md'
v = vp.read_text(encoding='utf-8')
v = v.replace('Continue **Gate E Batch 4 — source/scan pp.319–323 / printed pp.318–322** by direct page-by-page comparison against the controlling rendered scan. Apply/document only definite source-supported corrections. Do not begin English.', 'Continue **Gate E final Batch 5 — source/scan pp.324–326 / printed pp.323–325** by direct page-by-page comparison against the controlling rendered scan, including the closing ornament/boundary. Apply/document only definite source-supported corrections. Do not begin English until Gate E closes.',1)
v += '''\n### Batch 4 — source pp.319–323 / printed pp.318–322\n\n**Complete.** All five pages were directly re-read against the controlling rendered scan.\n\n- cumulative Gate-E coverage: **20/23 pages**;\n- definite corrections in Batch 4: **0**;\n- cumulative definite Gate-E corrections: **6**;\n- unresolved readings: **0**;\n- next source page: **324**.\n\nNo canonical Tamil source-text correction was required in pp.319–323. The reread explicitly re-confirmed the CMIE/index figures and industrial-ranking argument; the `Single Window System` passage and Paramapada Sopanam metaphor; the SIPCOT 2,000-acre expansion announcement; Detroit / `Automotive Special Economic Zone`, Madurai park, `Reverse Osmosis` and leather-SEZ announcements; and the TNPL / wind-power / `Co-generation` / ethanol / Perambalur figures and wording.\n\nTamil remains **not verified** until final source pp.324–326 pass Gate E. English Gate F remains blocked.\n'''
vp.write_text(v,encoding='utf-8')

hp = Path('docs/HANDOVER_2007_INDUSTRIAL_SPEECHES.md')
h = hp.read_text(encoding='utf-8')
h = h.replace('- Gate E: **in progress — 15/23 pages verified; 6 definite corrections; 0 unresolved readings**', '- Gate E: **in progress — 20/23 pages verified; 6 definite corrections; 0 unresolved readings**',1)
marker = '## Exact next activity — Speech 10 Gate E Batch 4'
start = h.find(marker)
if start != -1:
    h = h[:start] + '''## Exact next activity — Speech 10 Gate E final Batch 5\n\n1. Directly compare rendered source/scan pp.324–326 / printed pp.323–325 against the canonical Tamil.\n2. Use the scan image as textual authority; do not normalise or externally correct source wording.\n3. Apply and document only definite source-supported corrections.\n4. Verify p.326 through the final paragraph, desk-thumping marker and closing ornament; exclude pp.327–329.\n5. If all three pages pass, close Gate E at 23/23 pages and set `verified_against_scan=true`; only then may English Gate F be unblocked.\n'''
hp.write_text(h,encoding='utf-8')
