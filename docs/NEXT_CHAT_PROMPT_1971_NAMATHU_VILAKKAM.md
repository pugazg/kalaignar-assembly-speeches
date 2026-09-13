# NEXT CHAT PROMPT — 1971 நமது விளக்கம் / Gate D Tamil completeness audit

Continue directly in pugazg/kalaignar-assembly-speeches, branch main. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

ACL-CPL_01732_நமது_விளக்கம்.pdf — rendered scan pixels are authoritative.

## Durable state

- Gate A — **PASS / COMPLETE**
- Gate B — **PASS / LOCKED**
- Gate C — **PASS / COMPLETE — 57/57**
- Gate C.5 — **PASS / COMPLETE — 57/57**
- Gate C.5 cumulative corrections — **129 across 109 source sites**
- unresolved readings — **2**
  - scan 11 / printed p.10 — `⟦தெளிவில்லை: போக ஏ⟧`
  - scan 37 / printed p.36 — `⟦தெளிவில்லை: தேச பக்தி வேறு⟧`
- Tamil `verified_against_scan` — **false**
- Gate D — **NEXT**
- Gate E — **BLOCKED until Gate D completes**
- English — **BLOCKED**

## Exact next activity

Perform **Gate D — Tamil completeness audit** over the complete locked body, scans **4–60 / printed pp.3–59**.

Requirements:

1. confirm all **57 mapped source pages** are represented in the canonical transcript;
2. verify source-page markers **4→60** occur exactly once, in strict monotonic order, with no duplicate or missing marker;
3. confirm the transcript start/end align with the locked Gate-B/Gate-C map and scan 61 remains classified as back cover / later library matter, not speech text;
4. confirm no mapped page is skipped or duplicated across page transitions;
5. confirm all printed speaker changes/interventions in the body are represented;
6. confirm the unresolved markers at scans 11 and 37 remain explicit and are not silently reconstructed;
7. record any completeness defects and repair only definite source-supported omissions/duplications;
8. update metadata, verification log, READMEs, mapping, handover, root status and next-chat prompt;
9. if Gate D passes, mark it **PASS / COMPLETE** and set exact next to **Gate E — Tamil source-fidelity verification**;
10. do **not** begin Gate E in the same iteration.
