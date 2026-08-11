from pathlib import Path

transcript_path = Path("speeches/1970/1970-09-09-no-confidence-motion/transcript.md")
text = transcript_path.read_text(encoding="utf-8")

# Small compatibility fixups for first-pass strings whose surrounding quote
# punctuation differs from the verification log. These are themselves verified
# directly against the scan; the main consolidation script still performs the
# source-status checks and metadata promotion.
fixups = [
    ("வைக்கவில்லை கொண்டு வா", "ஃபைல்களைக் கொண்டு வா"),
]

for old, new in fixups:
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError(f"Preflight source form not found: {old}")

transcript_path.write_text(text, encoding="utf-8")

# The first version of the consolidation script encoded the p.28 replacement
# with quote characters immediately around the phrase. In the printed source,
# however, the opening quote begins much earlier in the sentence. Patch only the
# runtime copy of the script so its guard checks the verified phrase itself; the
# canonical result therefore preserves the source punctuation exactly.
script_path = Path("scripts/apply_udaya_kathir_verification.py")
script = script_path.read_text(encoding="utf-8")
old_guard = '("p28 files", "\'வைக்கவில்லை கொண்டு வா\'", "\'ஃபைல்களைக் கொண்டு வா\'", True, 1),'
new_guard = '("p28 files", "வைக்கவில்லை கொண்டு வா", "ஃபைல்களைக் கொண்டு வா", True, 1),'
if old_guard in script:
    script = script.replace(old_guard, new_guard, 1)
elif new_guard not in script:
    raise RuntimeError("Could not locate p28 guard in consolidation script")
script_path.write_text(script, encoding="utf-8")

print("Applied Udhaya Kathir preflight fixups.")
