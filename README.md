# kalaignar-assembly-speeches

தமிழகச் சட்டமன்றத்தில் கலைஞர் மு. கருணாநிதி ஆற்றிய உரைகளை, கிடைக்கக்கூடிய அச்சு/scan மூலங்களின் அடிப்படையில், தேதிவாரியாகவும் நிகழ்வுவாரியாகவும் பாதுகாக்கும் digital archive.

This repository is a source-faithful digital archive of M. Karunanidhi's speeches in the Tamil Nadu Legislative Assembly. Each speech is organised primarily by **date and legislative event**, while historical publication titles are preserved as source metadata.

## Archival principles

- **Source first:** Tamil transcription follows the scanned publication; wording and spelling are not silently modernised.
- **Traceability:** source-page transitions are retained in the transcript.
- **Parliamentary context:** printed headings, speaker labels, interjections, figures and exchanges are retained where present in the source.
- **Uncertainty is explicit:** unclear readings should be marked for review rather than guessed.
- **Verification states:** `transcribed` → `reviewed` → `verified`.
- **Translation:** the complete Tamil source transcription comes first; an English translation is included **after** it.
- **Canonical organisation:** folder names use `YYYY-MM-DD-event` so the collection can scale independently of later booklet/publication titles.

## Speech index

| Date | Publication / speech | Assembly event | Tamil | English | Verification |
|---|---|---|---|---|---|
| 09-09-1970 | [உதயக் கதிர்](./speeches/1970/1970-09-09-no-confidence-motion/) | நம்பிக்கையில்லாத் தீர்மான விவாதத்திற்கான பதிலுரை | Verified | Verified | Verified against scan pp. 5–46 |

Machine-readable index: [`data/speeches.json`](./data/speeches.json)

## Repository structure

```text
kalaignar-assembly-speeches/
├── README.md
├── data/
│   └── speeches.json
└── speeches/
    └── 1970/
        └── 1970-09-09-no-confidence-motion/
            ├── README.md
            ├── metadata.json
            ├── source-notes.md
            └── transcript.md
```

## Current verification convention

A file marked **transcribed** has a complete first-pass transcription from the scan. It is not labelled **verified** until a separate, stricter page-by-page/character-level comparison has been completed. This distinction is intentional: archival completeness and archival certainty are tracked separately.
