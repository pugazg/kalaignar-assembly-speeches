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
- secondary witness support — **HIGH CONFIDENCE for both unresolved loci**
  - scan 11 — Council Official Report PDF p.32: `... வட்டிக்காக அரசுக்குக் கொடுக்கப்பட்ட தொகை போக ஏற்படுகிற நஷ்டம் தான் ...`
  - scan 37 — Council Official Report PDF p.38: `என்ற கருத்தினாலெழும் தேசபக்தி வேறு`
  - these do **not** replace the controlling booklet readings
- Tamil `verified_against_scan` — **false**
- cross-witness — **COMPLETE** against 29-06-1971 Assembly and 30-06-1971 Council Official Reports; canonical booklet text unchanged
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
6. confirm the unresolved markers at scans 11 and 37 remain explicit and are not silently reconstructed; the completed Official Report cross-witness readings are provenance support only;
7. record any completeness defects and repair only definite source-supported omissions/duplications;
8. update metadata, verification log, READMEs, mapping, handover, root status and next-chat prompt;
9. if Gate D passes, mark it **PASS / COMPLETE** and set exact next to **Gate E — Tamil source-fidelity verification**;
10. do **not** begin Gate E in the same iteration.
