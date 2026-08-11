from pathlib import Path

path = Path("speeches/1970/1970-09-09-no-confidence-motion/transcript.md")
text = path.read_text(encoding="utf-8")

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

path.write_text(text, encoding="utf-8")
print("Applied Udhaya Kathir preflight fixups.")
