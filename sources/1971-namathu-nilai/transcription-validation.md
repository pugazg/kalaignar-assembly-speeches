# நமது நிலை — source-level transcription consolidation validation

## Scope

This validation checks the **application/consolidation layer** created after the first complete word-by-word visual-fidelity pass of `ACL-CPL_01726_நமது_நிலை.pdf`.

It does not replace the rendered scan as authority and it does not convert the source-level transcription into a dated/House-specific canonical speech.

## Inputs

- controlling source: `ACL-CPL_01726_நமது_நிலை.pdf`
- physical scan pages: **60**
- first-pass baseline: user-supplied word-to-word transcription
- visual-fidelity audit: entries **1–175**
- corrected source transcription:
  - `transcription/scan-001-010.md`
  - `transcription/scan-011-020.md`
  - `transcription/scan-021-030.md`
  - `transcription/scan-031-040.md`
  - `transcription/scan-041-050.md`
  - `transcription/scan-051-060.md`
- application index: `correction-application-ledger.md`

## 1. Correction-ledger coverage

Result: **PASS**.

The application ledger assigns the complete discrepancy sequence from **1 through 175** without an intended gap or overlap. Each discrepancy number belongs to the same scan page on which it was discovered and points to exactly one bounded corrected-transcription file.

Pages on which the first visual pass recorded no discrepancy are retained explicitly in the ledger rather than being omitted.

## 2. Physical page-marker coverage

Result: **PASS at the source-level partition**.

The corrected source transcription is partitioned into six non-overlapping physical ranges:

- 1–10
- 11–20
- 21–30
- 31–40
- 41–50
- 51–60

Each represented physical page uses the established marker form:

```html
<!-- source-page: N -->
```

The source-level marker sequence is intended and checked as **1 through 60 in ascending order**, with one marker per represented physical scan page. Scan pages 1–2 are source cover/front matter; scan pages 3–60 contain the two mapped editorial units.

This source-level use of markers does not imply that cover/front matter belongs inside a future canonical speech transcript.

## 3. Editorial-unit boundary check

Result: **PASS**.

### Unit 1

- starts scan 3 / printed 1
- ends scan 37 / printed 35

### Unit 2

- begins scan 38 / printed 36 with the printed heading `நிதிநிலை அறிக்கை விவாதத்துக்கு முதல்வர் பதில்`
- ends scan 60 / printed 58

The corrected transcription preserves this boundary and does not silently merge the two editorial units.

## 4. Cross-file transition check

Result: **PASS**.

The six bounded files were checked at their joins so that the file split does not create a textual boundary of its own:

- scan 10 → 11: the murder/violence discussion continues normally;
- scan 20 → 21: the industrial/joint-sector discussion continues normally;
- scan 30 → 31: the Chennai special-problem/funding discussion continues normally;
- scan 40 → 41: the heading `குட்டியைக் கவ்வும் பூனை` at the end of scan 40 leads into its paragraph on scan 41;
- scan 50 → 51: the education-allocation calculation continues from `ரூ. 43.86 கோடி` into the percentage comparison;
- scan 59 → 60: the planning-question sentence continues from `கேள்வி வருமானால்,` to `அதற்கு இந்தத் திட்டக் குழுவின் அறிக்கை பயன்படும்.`

## 5. High-risk correction regression checks

Result: **PASS for the sampled high-risk forms**.

The consolidated files were rechecked for several forms that were especially vulnerable to OCR contamination, grammatical normalization or consolidation error:

- `விளக்குபான` is not retained; scan-supported `விளக்கமான` is used;
- `நிலயத்திற்குக்` is not retained; scan-supported `நிலையத்திற்குக்` is used;
- the OCR-only fragment beginning `நொட்டனைத்து...` is absent;
- the normalized ordinal `மூன்றாவதாக` is not used at the audited source occurrence where the scan prints `மூன்றுவதாக`;
- illustration-only `புன்செய்க்கு வரி நீக்கம்` is not promoted into the spoken-text layer;
- the OCR heading error `வன்முறையைச் சயோம்` is not retained; the source heading `வன்முறையைச் சகியோம்` is used;
- the scan-p.57 sentence is now `ஏதாவது செய்து அறுத்துக் கொள்ள வேண்டும் என்பது அவர்களுடைய ஆசை.`

## 6. Consolidation-generated error found and corrected

During this QA a **new assembly error introduced by the consolidation itself** was found on scan p.57. The source-level transcription had accidentally changed:

`ஏதாவது செய்து அறுத்துக் கொள்ள வேண்டும் என்பது அவர்களுடைய ஆசை.`

into a different construction by misapplying the neighboring audit-entry-162 compound form.

The scan page was reopened and the transcription was corrected. This is not a new first-pass discrepancy and therefore is not numbered 176. The neighboring entry-162 correction remains applied only to its actual sentence ending `வேண்டுமென்பதற்காகத்தான் இதனைச் சொல்லுகிறேன்.`

## 7. Non-speech/source-matter classification

Result: **PASS for the classifications established by the first visual pass**.

The corrected speech-text layer does not absorb:

- Connemara Public Library stamps;
- handwriting/later marks;
- the identified OCR contamination;
- the identified illustration-only signboard/heading wording.

The final library stamp on scan 60 remains excluded from publication/speech text.

## 8. Unsupported normalization check

Result: **PASS for the 175 audited correction loci and the transition QA performed here; not a claim of an independent second full visual reread**.

The purpose of this activity was to apply the already established audit findings without deliberately modernizing or improving the source. Source anomalies explicitly identified by the audit remain preserved, including forms that look grammatically unusual.

A future independent second word-by-word reread may still discover additional discrepancies. Any such discovery must receive a new audit record rather than being silently folded into this consolidation.

## 9. Gate/status conclusion

- Gate A: complete.
- Gate B: source editorial-unit mapping complete; exact underlying House/date split still unresolved.
- User-supplied first-pass transcription: completely traversed against the scan.
- First full source-level visual-fidelity pass: complete through scan 60.
- Confirmed first-pass discrepancies: **175**.
- Correction application to source-level transcription: **complete**.
- Consolidation/transition QA: **complete for this activity**.
- Unresolved character/word readings from the first pass: **0**.
- Canonical dated/House-specific Gate D/E: **not claimable yet**.
- English: **blocked**.
- Released 2007 Speech 1–10 material: **untouched**.

## Exact next activity

Perform a **focused House/date evidence pass** without changing the corrected source text:

1. re-read source-internal House/date clues in scans 3–60 and record all explicit evidence;
2. determine whether any reliable Assembly/Council transition can be established from this edition itself;
3. if the edition cannot establish the split, document that negative finding clearly;
4. only then use separately verified primary legislative records as an editorial metadata layer to resolve dates/House boundaries where possible;
5. do not merge or rewrite this source witness to match outside records.