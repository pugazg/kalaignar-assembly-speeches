from pathlib import Path
import json

transcript_path = Path("speeches/1970/1970-09-09-no-confidence-motion/transcript.md")
text = transcript_path.read_text(encoding="utf-8")

# Compatibility/source-form fixups verified directly against the scan.  Most of
# the canonical corrections live in apply_udaya_kathir_verification.py; this
# small preflight handles source forms discovered in the final recheck and one
# p.28 quotation-boundary mismatch in the original guard.
fixups = [
    # p. 5
    ("சிண்டிகேட் காங்கிரஸ் கட்சியின் சார்பில் நம்பிக்கை இல்லாத தீர்மானம் ஒன்றும்", "சிண்டிகேட் காங்கிரஸ் கட்சியின் சார்பில் நம்பிக்கை இல்லாத் தீர்மானம் ஒன்றும்"),
    ("## நல்ல வாய்ப்பு\n\nநம்பிக்கையில்லாத தீர்மானம் இதற்கு முன்பு", "## நல்ல வாய்ப்பு\n\nநம்பிக்கையில்லாத் தீர்மானம் இதற்கு முன்பு"),
    ("அவர்கள் எங்கள் மீது நம்பிக்கையில்லாத தீர்மானம் கொண்டு வந்த பிறகு", "அவர்கள் எங்கள் மீது நம்பிக்கையில்லாத் தீர்மானம் கொண்டு வந்த பிறகு"),
    ("காங்கிரஸ் கட்சியின் சார்பில் கொண்டு வந்திருக்கின்ற நம்பிக்கையில்லாத தீர்மானம்", "காங்கிரஸ் கட்சியின் சார்பில் கொண்டு வந்திருக்கின்ற நம்பிக்கையில்லாத் தீர்மானம்"),

    # p. 6
    ("என்ற காரணத்தால் நம்பிக்கையில்லாத தீர்மானம் ஒருவகையிலே", "என்ற காரணத்தால் நம்பிக்கையில்லாத் தீர்மானம் ஒருவகையிலே"),
    ("என்ற வகையில்நான் மகிழ்ச்சியடைகிறேன்.", "என்ற வகையில் நான் மகிழ்ச்சியடைகிறேன்."),
    ("வன்மையாகக் கண்டித்துப் பேச முற்பட்ட எண்ணிடவில்லை.", "வன்மையாகக் கண்டித்துப் பேச முற்பட எண்ணிடவில்லை."),
    ("நம்பிக்கையில்லாத தீர்மானத்தில், புதிய காங்கிரஸ் கட்சியின் தலைவர்", "நம்பிக்கையில்லாத் தீர்மானத்தில், புதிய காங்கிரஸ் கட்சியின் தலைவர்"),
    ("இந்த நம்பிக்கையில்லாத தீர்மானத்தின் அடிப்படையிலே", "இந்த நம்பிக்கையில்லாத் தீர்மானத்தின் அடிப்படையிலே"),

    # p. 7
    ("இன்று ஆளும் கட்டில் அலங்கரிப்பதா?", "இன்று ஆளும் கட்டிலே அலங்கரிப்பதா?"),
    ("சாட்டப்பட்ட குற்றச்சாட்டுகளுக்கு நானோ அல்லது அமைச்சர்களோ கூட", "சாட்டப்பட்ட குற்றச்சாட்டுகளுக்கு நானே அல்லது அமைச்சர்களோ கூட"),
    ("இந்த இரண்டு தீர்மானங்களையும் ஆதரிக்காத நிலையில்கண்டனத்", "இந்த இரண்டு தீர்மானங்களையும் ஆதரிக்காத நிலையில் கண்டனத்"),
    ("பேசிய மற்றக்கட்சியினர்", "பேசிய மற்றக் கட்சியினர்"),

    # p. 8
    ("என்று எதிர்க்கட்சித் தலைவர் அவர்களோ", "என்று எதிர்க் கட்சித் தலைவர் அவர்களோ"),
    ("நம்முடைய எதிர்க்கட்சித் தலைவர் அவர்கள் கூட", "நம்முடைய எதிர்க் கட்சித் தலைவர் அவர்கள் கூட"),
    ("எதிர்க்கட்சியில் இருக்கிற உறுப்பினர்களோ", "எதிர்க் கட்சியில் இருக்கிற உறுப்பினர்களோ"),
    ("இந்தக் கட்சியின்மீது அல்லது", "இந்தக் கட்சியின் மீது அல்லது"),
    ("தென்சென்னை நாடாளுமன்ற இடைத்தேர்தல் வந்தது.", "தென்சென்னை நாடாளுமன்ற இடைத் தேர்தல் வந்தது."),
    ("அந்த இடைத்தேர்தலில், இவர்களுக்கு", "அந்த இடைத் தேர்தலில், இவர்களுக்கு"),
    ("தப்பித் தவறி ஓட்டுப்போட்டு விட்டார்கள்.", "தப்பித் தவறி ஓட்டுப் போட்டு விட்டார்கள்."),
    ("தென்சென்னை பாராளுமன்ற இடைத்தேர்தலில்", "தென்சென்னை பாராளுமன்ற இடைத் தேர்தலில்"),

    # p. 9
    ("தென்காசியில் நடைபெற்ற இடைத்தேர்தல்.", "தென்காசியில் நடைபெற்ற இடைத் தேர்தல்."),
    ("பிறகு நடைபெற்ற தென்காசி இடைத்தேர்தலில்", "பிறகு நடைபெற்ற தென்காசி இடைத் தேர்தலில்"),
    ("பின்னர் சாத்தூரில் நடைபெற்ற இடைத்தேர்தல்.", "பின்னர் சாத்தூரில் நடைபெற்ற இடைத் தேர்தல்."),
    ("புதுவை மாநிலத்தில் நடைபெற்ற இடைத்தேர்தலில்", "புதுவை மாநிலத்தில் நடைபெற்ற இடைத் தேர்தலில்"),

    # p. 10
    ("ஊராட்சி ஒன்றியத் தேர்தல்கள்பற்றி எதிர்க்கட்சித் தலைவர் அவர்கள் சொன்னார்கள்.", "ஊராட்சி ஒன்றியத் தேர்தல்கள்பற்றி எதிர்க் கட்சித் தலைவர் அவர்கள் சொன்னார்கள்."),
    ("தவறான கணக்குகள் எல்லாம் காட்டுகிறார்கள்", "தவறான கணக்குகளை எல்லாம் காட்டுகிறார்கள்"),

    # p. 28
    ("வைக்கவில்லை கொண்டு வா", "ஃபைல்களைக் கொண்டு வா"),
]

for old, new in fixups:
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError(f"Preflight source form not found: {old}")

transcript_path.write_text(text, encoding="utf-8")

# Correct a stale note left over from the first-pass stage.  Status promotion is
# still performed by the main consolidation script.
metadata_path = Path("speeches/1970/1970-09-09-no-confidence-motion/metadata.json")
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata["transcription"]["verification_note"] = (
    "Second-pass page-by-page visual verification completed against scan pp. 5-46; "
    "confirmed corrections applied to the canonical transcript."
)
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# The first version of the consolidation script encoded the p.28 replacement
# with quote characters immediately around the phrase. In the printed source,
# the opening quote begins much earlier in the sentence. Patch only the runtime
# copy so the guard checks the phrase itself and preserves source punctuation.
script_path = Path("scripts/apply_udaya_kathir_verification.py")
script = script_path.read_text(encoding="utf-8")
old_guard = '("p28 files", "\'வைக்கவில்லை கொண்டு வா\'", "\'ஃபைல்களைக் கொண்டு வா\'", True, 1),'
new_guard = '("p28 files", "வைக்கவில்லை கொண்டு வா", "ஃபைல்களைக் கொண்டு வா", True, 1),'
if old_guard in script:
    script = script.replace(old_guard, new_guard, 1)
elif new_guard not in script:
    raise RuntimeError("Could not locate p28 guard in consolidation script")
script_path.write_text(script, encoding="utf-8")

print("Applied Udhaya Kathir preflight/source-form fixups.")
