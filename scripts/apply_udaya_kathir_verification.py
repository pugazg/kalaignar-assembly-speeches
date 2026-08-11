from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEECH_DIR = ROOT / "speeches/1970/1970-09-09-no-confidence-motion"
TRANSCRIPT = SPEECH_DIR / "transcript.md"
METADATA = SPEECH_DIR / "metadata.json"
INDEX = ROOT / "data/speeches.json"
ROOT_README = ROOT / "README.md"
SPEECH_README = SPEECH_DIR / "README.md"


def apply_replacement(text: str, old: str, new: str, label: str, *, required: bool = True, count: int | None = 1) -> str:
    """Apply a verified source correction without silently guessing.

    If the old form is absent but the verified new form is already present, the
    correction is treated as already applied. Otherwise a required correction
    raises so the repository cannot be promoted to `verified` accidentally.
    """
    occurrences = text.count(old)
    if occurrences:
        if count is not None and occurrences != count:
            raise RuntimeError(f"{label}: expected {count} occurrence(s) of old text, found {occurrences}")
        return text.replace(old, new, occurrences if count is None else count)
    if new in text:
        return text
    if required:
        raise RuntimeError(f"{label}: neither first-pass nor verified source text was found")
    print(f"WARNING: optional replacement not found: {label}")
    return text


def apply_many(text: str, replacements: list[tuple[str, str, str, bool, int | None]]) -> str:
    for label, old, new, required, count in replacements:
        text = apply_replacement(text, old, new, label, required=required, count=count)
    return text


raw = TRANSCRIPT.read_text(encoding="utf-8")
marker = "\n# English translation\n"
if marker not in raw:
    raise RuntimeError("English translation marker not found")
tamil, english_tail = raw.split(marker, 1)
english = marker + english_tail

# Corrections confirmed by the page-by-page visual review against scan pp. 5–46.
# Physical line wrapping is not reconstructed, except where a source-page marker
# itself falls inside a printed word.
tamil_replacements: list[tuple[str, str, str, bool, int | None]] = [
    # pp. 5–10
    ("p5 opening of final line", "ஒன்றொன்று, குறைகாண வெளியிடங்களில், பொதுக் கூட்டங்களில் எடுத்துச் சொல்லுகிற நேரத்தில், அந்த", "ஏனென்றால், குறைகள் வெளியிடங்களில், பொதுக் கூட்டங்களில் எடுத்துச் சொல்லுகிற நேரத்தில், அந்த", True, 1),
    ("p6 விளக்கங்களே", "நாங்கள் நேரடியாக விளக்கங்களை அளிப்பதாலே", "நாங்கள் நேரடியாக விளக்கங்களே அளிப்பதாலே", True, 1),
    ("p6 விவாதங்கள்", "காவல் துறையின் போக்கைக் கண்டித்து பலத்த விவாதங்களை இங்கே நடத்தியிருக்கிறார்கள்.", "காவல் துறையின் போக்கைக் கண்டித்து பலத்த விவாதங்கள் இங்கே நடத்தியிருக்கிறார்கள்.", True, 1),
    ("p7 பதில்கள்", "அழுத்தந்திருத்தமான பதில்களை அளித்திருக்கிறார்கள்.", "அழுத்தந்திருத்தமான பதில்கள் அளித்திருக்கிறார்கள்.", True, 1),
    ("p7→8 source-page boundary", "அவர்கள் அனைவருக்கும் இதயபூர்வமான நன்றியறிதலைத் தெரிவித்துக் கொள்கிறேன்.\n\n<!-- source-page: 8 -->", "அவர்கள் அனைவருக்\n\n<!-- source-page: 8 -->\n\nகும் இதயபூர்வமான நன்றியறிதலைத் தெரிவித்துக் கொள்கிறேன்.", True, 1),
    ("p8 நம்பிக்கையையும்", "அந்தப் பாராட்டை அவர்கள் நிச்சயமாகத் திரும்பப் பெறமாட்டார்கள் என்று நம்பிக்கையாய் எனக்கு உண்டு.", "அந்தப் பாராட்டை அவர்கள் நிச்சயமாகத் திரும்பப் பெற மாட்டார்கள் என்ற நம்பிக்கையையும் எனக்கு உண்டு.", True, 1),
    ("p9 ஆறுவது மாதத்தில்", "அது அறுபது மாதத்தில் மக்கள் திராவிட முன்னேற்றக் கழகத்தின் பால் கொண்டிருந்த நம்பிக்கைக்கு ஒரு சான்றாகும்.", "அது ஆறுவது மாதத்தில் மக்கள் திராவிட முன்னேற்றக் கழகத்தின் பால் கொண்டிருந்த நம்பிக்கைக்கு ஒரு சான்றாகும்.", True, 1),
    ("p9 ஏழெட்டு", "நகராட்சி மன்றங்களில் நடைபெற்ற தேர்தல்களில் ஏறத்தாழ இடங்கள் தான் முன்பு இருந்தன.", "நகராட்சி மன்றங்களில் நடைபெற்ற தேர்தல்களில் ஏழெட்டு இடங்கள் தான் முன்பு இருந்தன.", True, 1),

    # pp. 11–16
    ("p11 என்றால்", "காங்கிரஸ்காரர் தான் செய்தார்கள் என்றெல்லாம் அதை நீங்களும் செய்யலாமா என்று கேட்டலாம்.", "காங்கிரஸ்காரர் தான் செய்தார்கள் என்றால் அதை நீங்களும் செய்யலாமா என்று கேட்டலாம்.", True, 1),
    ("p11 broken என்பதையும்", "நடைபெற்றிருக்கின்றன என்பதை, யும்", "நடைபெற்றிருக்கின்றன என்பதையும்,", True, 1),
    ("p12 பிறகு", "தங்களுடைய கோரிக்கைகள் நிராகரிக்கப்பட்ட பிறகோ கிளர்ச்சிகள் நடைபெற்றன அப்போது.", "தங்களுடைய கோரிக்கைகள் நிராகரிக்கப்பட்ட பிறகு கிளர்ச்சிகள் நடைபெற்றன அப்போது.", True, 1),
    ("p12 கவனிக்கப்பட்டு", "தொழிலாளர்களின் கோரிக்கைகள் இந்த அரசால் ஏற்றுக்கொள்ளப்பட்டு", "தொழிலாளர்களின் கோரிக்கைகள் இந்த அரசால் கவனிக்கப்பட்டு", True, 1),
    ("p12 பேச்சுவார்த்தைகள்", "பேசுவார்த்தைகள் முடிவுற்று", "பேச்சுவார்த்தைகள் முடிவுற்று", True, 1),
    ("p12 உத்தியோக உயர்வு", "மின்சார வாரிய ஊழியர்கள் ஊதியோடு உயர்வு வேண்டுமென்று கேட்ட நேரத்தில்", "மின்சார வாரிய ஊழியர்கள் உத்தியோக உயர்வு வேண்டுமென்று கேட்ட நேரத்தில்", True, 1),
    ("p12 ஊதியத்தினை", "பத்து பதினைந்து ஆண்டுகளாக உயர்த்தப்படாமல் இருந்த ஊழியத்தின் அவர்களுக்கெல்லாம்", "பத்து பதினைந்து ஆண்டுகளாக உயர்த்தப்படாமல் இருந்த ஊதியத்தினை அவர்களுக்கெல்லாம்", True, 1),
    ("p14 தேவஅன்பு", "தேவன்பு என்றவர் இறந்து விட்டார்.", "தேவஅன்பு என்றவர் இறந்து விட்டார்.", True, 1),
    ("p14 நுழைந்தது தவறு", "குறிப்பிடப்பட்ட அதிகாரி குப்பத்திலே போய் நுழைந்துதவறான் என்று குறிப்பிடப்பட்டிருக்கிறார்கள்.", "குறிப்பிடப்பட்ட அதிகாரி குப்பத்திலே போய் நுழைந்தது தவறு என்று குறிப்பிடப்பட்டிருக்கிறார்கள்.", True, 1),
    ("p14 heading", "## கோவை கிளர்ச்சி", "## கோவைக் கிளர்ச்சி", True, 1),
    ("p14 sentence stop", "அவர்களுடைய கோரிக்கைகளை அரசு அறியும் அதில் என்ன சங்கடங்கள் இருக்கின்றன என்பதும் தெரியும்.", "அவர்களுடைய கோரிக்கைகளை அரசு அறியும். அதில் என்ன சங்கடங்கள் இருக்கின்றன என்பதும் தெரியும்.", True, 1),
    ("p14 முடிவை", "ஒரு முடிவு வெளியிட்டோம்.", "ஒரு முடிவை வெளியிட்டோம்.", True, 1),
    ("p14 பாதி கிணறு", "மாதி கிணறு தாண்டி இருக்கிறார்கள் என்றாலும் பரவாயில்லை.", "பாதி கிணறு தாண்டி இருக்கிறீர்கள் என்றாலும் பரவாயில்லை.", True, 1),
    ("p15 சென்ற", "அவர் பார்த்து விட்டுச் சென்று ஓரிரண்டு நாட்களுக்குள் அறிக்கை விட்டார்கள்.", "அவர் பார்த்து விட்டுச் சென்ற ஓரிரண்டு நாட்களுக்குள் அறிக்கை விட்டார்கள்.", True, 1),
    ("p15 எழுதிவிட்டு", "கடிதம் எழுதியிட்டு, கிளர்ச்சியில் ஈடுபட்டார்கள்.", "கடிதம் எழுதிவிட்டு, கிளர்ச்சியில் ஈடுபட்டார்கள்.", True, 1),
    ("p15 என்று செய்தி", "3 பேர் துப்பாக்கிக் குண்டுக்கு இரையானார்கள் என்ற செய்தி வந்தது.", "3 பேர் துப்பாக்கிக் குண்டுக்கு இரையானார்கள் என்று செய்தி வந்தது.", True, 1),
    ("p15 கௌரவப் பிரச்சினை", "இதை அரசு கொள்கைப் பிரச்சினையாகப் பார்க்காமல், ஆணவத்தோடு இதைச் சொல்லாமல்", "இதை அரசு கௌரவப் பிரச்சினையாகப் பார்க்காமல், ஆணவத்தோடு பதில் சொல்லாமல்", True, 1),
    ("p15 பக்தவத்சலம்", "திரு. கருத்திருமன் அவர்கள் பக்குவத்திலாம் என்று நினைக்கலாம்.", "திரு. கருத்திருமன் அவர்கள் பக்தவத்சலம் என்று நினைக்கலாம்.", True, 1),
    ("p15 காமராசர்", "மதிப்பிற்குரிய திரு. காமராஜ் காலத்திலிருந்து இருந்த காங்கிரஸ் ஆட்சி", "மதிப்பிற்குரிய திரு. காமராசர் காலத்திலிருந்து நடைபெற்ற காங்கிரஸ் ஆட்சி", True, 1),
    ("p15 உணர்வோடு", "அப்படிப்பட்ட உணர்வாக செய்ய வேண்டிய காரியங்களைச் செய்து இருக்கிற வரலாறு", "அப்படிப்பட்ட உணர்வோடு செய்ய வேண்டிய காரியங்களைச் செய்து இருக்கிற வரலாறு", True, 1),
    ("p16 திருச்சியிலிருந்து", "அவரை திரு.சசியிலிருந்து சென்னைக்கு அழைத்துக் கொண்டு வர வேண்டும்", "அவரை திருச்சியிலிருந்து சென்னைக்கு அழைத்துக் கொண்டு வர வேண்டும்", True, 1),

    # pp. 17–22
    ("p17 நடைபெற்றது", "இது இரண்டாம் தேதி நடைபெறுகிறது.", "இது இரண்டாம் தேதி நடைபெற்றது.", True, 1),
    ("p17 போடப்பட்ட", "புறம்போக்கு நிலத்தில் போட்டப்பட்ட 700 குடிசைகளை", "புறம்போக்கு நிலத்தில் போடப்பட்ட 700 குடிசைகளை", True, 1),
    ("p17 மார்க்சிஸ்டு", "மார்க்சிஸ்ட் ஆகிர", "மார்க்சிஸ்டு ஆகிர", True, 1),
    ("p18 வன்முறையில் ஈடுபட்டால்", "நாங்கள் வன்முறையில் ஈடுபட்டார்கள் அடக்கலாமா, ஒடுக்கலாமா என்று கேட்டார்கள்.", "நாங்கள் வன்முறையில் ஈடுபட்டால் எங்களை அடக்கலாமா, ஒடுக்கலாமா என்று கேட்டிருக்கிறார்கள்.", True, 1),
    ("p18 குடிகிடப்புக்காரர்கள்", "குடியிருப்புதாரர்கள் ஆளுக்கு 10 சென்ட் நிலத்தை வேலி போட்டுக் கொண்டார்கள். ஆளுக்கு 10 சென்ட் நிலத்தை எடுத்துக் கொண்டார்கள்", "குடிகிடப்புக்காரர்கள் ஆளுக்கு 10 செண்டு நிலத்தை வேலி போட்டுக் கொண்டார்கள், ஆளுக்கு 10 செண்டு நிலத்தை எடுத்துக் கொண்டார்கள்", True, 1),
    ("p18 punctuation", "இது கம்யூனிஸ்டுகள் அந்த ஆட்சி எப்படி அணுகியிருக்கிறது?", "இது கம்யூனிஸ்டுகள். அந்த ஆட்சி எப்படி அணுகியிருக்கிறது?", True, 1),
    ("p18 நல்லசிவம்", "திரு. நல்லசிவம் அவர்கள் அதிக 3000 பேர்கள் அவர்களே அல்ல, வேறு சார்பில் இருந்தவர்களை பிடித்துவிட்டார்கள் என்று சொன்னார்கள்.", "திரு. நல்லசிவம் அவர்கள் அதில் 3000 பேர்கள் அவர்களே அல்ல, வேறு சாலையில் இருந்தவர்களை பிடித்துவிட்டார்கள் என்று சொன்னார்கள்.", True, 1),
    ("p20 நடைபெற்றது முடிந்த", "கீழ்வெண்மணியில் நடைபெற்ற முடிந்த காரியம் என்று நாங்கள் சும்மா இருந்து விடவில்லை.", "கீழ்வெண்மணியில் நடைபெற்றது முடிந்த காரியம் என்று நாங்கள் சும்மா இருந்து விடவில்லை.", True, 1),
    ("p21 வாயிலில்", "5 மறவர்கள் ஒரு கோவிலின் வாயில் கை கட்டப்பட்டு", "5 மறவர்கள் ஒரு கோவிலின் வாயிலில் கை கட்டப்பட்டு", True, 1),

    # pp. 23–28
    ("p23 சட்ட சபை", "இந்த சட்டசபை நடவடிக்கைகளையெல்லாம்", "இந்த சட்ட சபை நடவடிக்கைகள் எல்லாம்", True, 1),
    ("p23 அதைக் கேட்டால்", "அதை கேட்டால்", "அதைக் கேட்டால்", True, 1),
    ("p23 அப்போது", "ஆட்சி அப்போதும் இருந்து", "ஆட்சி அப்போது இருந்து", True, 1),
    ("p23 இப்போது", "ஆட்சி இப்பொழுது இருக்கிறது", "ஆட்சி இப்போது இருக்கிறது", True, 1),
    ("p23 police suspension", "போலீஸ் அதிகாரிகள் இப்பொழுது வேலையில் இல்லாமல், சஸ்பெண்ட் செய்யப்பட்டிருக்கிறார்கள்.", "போலீஸ் அதிகாரிகள் இப்பொழுது வேலையில் இல்லாமல், ஸஸ்பெண்ட் செய்யப்பட்டிருக்கிறார்கள்.", True, 1),
    ("p24 police suspension", "போலீஸ் அதிகாரி சஸ்பெண்ட் செய்யப்பட்டிருக்கிறார்.", "போலீஸ் அதிகாரி ஸஸ்பெண்ட் செய்யப்பட்டிருக்கிறார்.", True, 1),
    ("p24 காட்டுக் கருப்பனென்ற", "காட்டுக் கருப்பன் என்ற அரிஜன்", "காட்டுக் கருப்பனென்ற அரிஜன்", True, 1),
    ("p25 பரிசு அளிப்பு", "எம்.எல்.ஏக்கள் பரிசளிப்பு விழாக்கள் நடத்துகிறார்கள்", "எம்.எல்.ஏக்கள் பரிசு அளிப்பு விழாக்கள் நடத்துகிறார்கள்", True, 1),
    ("p25 allotment exchange", "நாங்கள் வலுவிலே போடுவோம். நீங்கள் கேட்டுக்கொண்டே அலாட்மெண்ட் போடப்படுகிறது.", "நாங்கள் வலுவிலேயா போட்டோம். நீங்கள் கேட்டுத்தானே அலாட்மெண்ட் போடப்படும்.", True, 1),
    ("p26 பரிசு அளிப்பாக", "பரிசளிப்பாக.", "பரிசு அளிப்பாக.", True, 1),
    ("p26 தரப்பில்", "எங்கள் தாப்பில் இருக்கிறவர்கள்", "எங்கள் தரப்பில் இருக்கிறவர்கள்", True, 1),
    ("p26 இதன் காரணமாக", "அதன் காரணமாக நிர்வாகம்", "இதன் காரணமாக நிர்வாகம்", True, 1),
    ("p26 ஆக்ரமிப்பு", "நிலங்கள் ஆகிரமிப்பு நடந்திருந்தால்", "நிலங்கள் ஆக்ரமிப்பு நடந்திருந்ததால்", True, 1),
    ("p26 சேகரித்திருப்பதால்", "அவர் தகவல் சேகரித்திருப்பதாக", "அவர் தகவல் சேகரித்திருப்பதால்", True, 1),
    ("p27/28 ஹாண்டே", "டாக்டர் ஹண்டே", "டாக்டர் ஹாண்டே", True, None),
    ("p27 colon", "பிரமாதமானதல்ல.", "பிரமாதமானதல்ல:", True, 1),
    ("p28 1968-69", "1968-69ல் தொடங்கப்பட்டுள்ளதாகவும்", "1968-69ல் தொடங்கப்பட்டுள்ளது என்றும்", True, 1),
    ("p28 கூறியிருக்கிறார்கள்", "ஆர். கிருஷ்ணசாமி நாயுடு அவர்கள் மேலவையில் கூறியிருக்கிறார்", "ஆர். கிருஷ்ணசாமி நாயுடு அவர்கள் மேலவையில் கூறியிருக்கிறார்கள்", True, 1),
    ("p28 quote restoration", "இதைத்தான் மணக்கிறது, மணக்கிறது கூவம் மணக்கிறது என்று நாம் சொன்னோம்.", "இதைத்தான் 'மணக்கிறது, மணக்கிறது கூவம் மணக்கிறது' என்று நாம் சொன்னோம்.", True, 1),
    ("p28 வேண்டாமென்று", "வேண்டாம் என்று சொல்லும்", "வேண்டாமென்று சொல்லும்", True, 1),
    ("p28 files", "'வைக்கவில்லை கொண்டு வா'", "'ஃபைல்களைக் கொண்டு வா'", True, 1),
    ("p28 குற்றச்சாட்டுக்களை", "குற்றச்சாட்டின் பத்திரிகையில் மிகப் பயங்கரமாக எழுதியிருக்கிறார்.", "குற்றச்சாட்டுக்களை பத்திரிகையில் மிகப் பயங்கரமாக எழுதுகிறார்கள்.", True, 1),
    ("p28 ஊழல் quote", "ஊழல் நாற்றமெடுத்தும் கூவம்", "ஊழல் நாற்றமெடுக்கும்கூவம்", True, 1),

    # pp. 29–34
    ("p29 கரைகளில்", "கரைகள் போடப்பட்டிருந்த ஸ்லாப்புகள்", "கரைகளில் போடப்பட்டிருந்த ஸ்லாப்புகள்", True, 1),
    ("p29 பேசுகிறீர்களே", "கூவம் திட்டத்தினைப் பற்றி இப்படிப் பேசினீர்களே", "கூவம் திட்டத்தினைப் பற்றி இப்படிப் பேசுகிறீர்களே", True, 1),
    ("p31 தயார் செய்யப்பட்ட 1", "அப்படி தயாரிக்கப்பட்ட குழாய்கள் 11 சதவிகிதத்திலிருந்து 48 சதவிகிதம்", "அப்படி தயார் செய்யப்பட்ட குழாய்கள் 11 சதவிகிதத்திலிருந்து 48 சதவிகிதம்", True, 1),
    ("p31 தயார் செய்யப்பட்ட 2", "ஆகையினால் சுழற்சி முறையில் தயாரிக்கப்பட்ட குழாய்கள்தான்", "ஆகையினால் சுழற்சி முறையில் தயார் செய்யப்பட்ட குழாய்கள்தான்", True, 1),
    ("p31 நிபுணர்களது", "நிபுணர்கள் கருத்து.", "நிபுணர்களது கருத்து.", True, 1),
    ("p31 தயார் செய்து", "இந்த முறையை யொட்டி தயார்செய்து உபயோகிக்கிறார்கள்.", "இந்த முறையை யொட்டி தயார் செய்து உபயோகிக்கிறார்கள்.", True, 1),
    ("p31 தயார் செய்த", "இரண்டு விதத்திலும் தயார்செய்த குழாய்கள்", "இரண்டு விதத்திலும் தயார் செய்த குழாய்கள்", True, 1),
    ("p32 தேவையினை", "அந்நியச் செலாவணித் தேவையின் நூற்று இருபது லட்சமாகக்", "அந்நியச் செலாவணித் தேவையினை நூற்று இருபது லட்சமாகக்", True, 1),
    ("p32 கேட்டிருந்தார்கள்", "சத்தியநாராயண பிரதர்ஸ் ரூபாய் 181 லட்சம் அந்நியச் செலாவணி கேட்டிருந்தார்.", "சத்தியநாராயண பிரதர்ஸ் ரூபாய் 181 லட்சம் அந்நியச் செலாவணி கேட்டிருந்தார்கள்.", True, 1),
    ("p32 தயார் செய்வதற்கு", "இவைகளைத் தயார்செய்யக் கூடிய", "இவைகளைத் தயார் செய்யக் கூடிய", True, 1),
    ("p32 யந்திரங்களும்", "தளவாடங்களும் இயந்திரங்களும்", "தளவாடங்களும் யந்திரங்களும்", True, 1),
    ("p33 உண்மையா", "இது உண்மையானன்று பரிசீலனை செய்து பார்க்கப்பட்டது.", "இது உண்மையா என்று பரிசீலனை செய்து பார்க்கப்பட்டது.", True, 1),
    ("p34 ஸ்டீல்", "ஸ்மால் எஃகு தகடு விலை தவிர", "ஸ்டீல் எஃகு தகடு விலை தவிர", True, 1),

    # pp. 35–40
    ("p35 ஆவடியில்", "க்வார்டர்ஸ் ஆவையில் கட்டுவதற்காக", "க்வார்டர்ஸ் ஆவடியில் கட்டுவதற்காக", True, 1),
    ("p35 எதற்காக", "ஏதற்காக தாராப்பூர் கம்பெனிக்குக் கொடுக்கப்பட்டது.", "எதற்காக தாராப்பூர் கம்பெனிக்குக் கொடுக்கப்பட்டது.", True, 1),
    ("p36 எஞ்ஜினியரிங்", "2315 பேர் என்ஜினியரிங் பட்டதாரிகள்.", "2315 பேர் எஞ்ஜினியரிங் பட்டதாரிகள்.", True, 1),
    ("p37 அறிவித்தவுடனே", "பல முதலாளிகள் வேலை நிறுத்தம் செய்யப் போவதாக அறிவித்துவிட்டனே", "பல முதலாளிகள் வேலை நிறுத்தம் செய்யப் போவதாக அறிவித்தவுடனே", True, 1),
    ("p37 அவசரச் சட்டம்", "அவர்களே சட்டம் போட்டு அவர்கள் வேலை நிறுத்தம் செய்ய முடியாது", "அவசரச் சட்டம் போட்டு அவர்கள் வேலை நிறுத்தம் செய்ய முடியாது", True, 1),
    ("p37 வைதிகமனப்பான்மை", "இந்த அரசு அதிகமனப்பான்மையைக் காட்டவில்லை.", "இந்த அரசு வைதிகமனப்பான்மையைக் காட்டவில்லை.", True, 1),
    ("p37 வளரப் பெருக", "தொழில் வளர வேண்டும்.", "தொழில் வளரப் பெருக வேண்டும்.", True, 1),
    ("p37 எங்கோ", "நாங்கள் எங்கே உள்ள தொழில் அதிபர்களை அழைப்பதாக", "நாங்கள் எங்கோ உள்ள தொழில் அதிபர்களை அழைப்பதாக", True, 1),
    ("p37 மாநிலத்திலே வந்து", "அவர்கள் அவர்களது மாநிலத்திலே இருந்து தொழில் ஆரம்பிக்க பீர்லாவை அழைத்திருக்கிறார்.", "அவர்கள் அவர்களது மாநிலத்திலே வந்து தொழில் ஆரம்பிக்க பீர்லாவை அழைத்திருக்கிறார்.", True, 1),
    ("p38 நாங்கள்", "கடவுள் ஏற்றுக் கொள்கிற வகையில் நாம் காரியங்களைச் செய்கிறோம்.", "கடவுள் ஏற்றுக் கொள்கிற வகையில் நாங்கள் காரியங்களைச் செய்கிறோம்.", True, 1),
    ("p39 உள்ளவர்கட்கும்", "5 ஆயிரம் ரூபாய் பெறுமானம் உள்ளவர்களுக்கும் கடன் கொடுக்கலாம்", "5 ஆயிரம் ரூபாய் பெறுமானம் உள்ளவர்கட்கும் கடன் கொடுக்கலாம்", True, 1),
    ("p39 நீர்ப்பாசன கழகங்களின்", "கூட்டுறவு நீர்ப்பாசனக் கழகங்களின் மூலம்", "கூட்டுறவு நீர்ப்பாசன கழகங்களின் மூலம்", True, 1),
    ("p39 குடி மராமத்து", "821 குடிமராமத்து வேலைகள்", "821 குடி மராமத்து வேலைகள்", True, 1),
    ("p39 கிராமப் புற", "8 லட்சத்திற்கும் மேற்பட்ட கிராமப்புற மக்களுக்கு", "8 லட்சத்திற்கும் மேற்பட்ட கிராமப் புற மக்களுக்கு", True, 1),
    ("p40 grant-aided teachers 1", "நகர ஈட்டுப் படித் திட்டம் மாதம் பெறும் பள்ளியாசிரியர்களுக்கும் நீட்டிக்கப்பட்டிருக்கிறது.", "நகர ஈட்டுப் படித் திட்டம் மானியம் பெற்று வரும் பள்ளியாசிரியர்களுக்கும் நீட்டிக்கப்பட்டிருக்கிறது.", True, 1),
    ("p40 grant-aided teachers 2", "மாதம் பெறும் பள்ளியாசிரியர்களுக்கும் ஈட்டிய விடுப்புப் பெற வசதி அளிக்கப்பட்டுள்ளது.", "மானியம் பெறும் பள்ளியாசிரியர்களுக்கும் ஈட்டிய விடுப்புப் பெற வசதி அளிக்கப்பட்டுள்ளது.", True, 1),

    # pp. 41–46
    ("p41 துயரைத்", "அந்தத் துயரத் துடைக்கும் வகையில்", "அந்தத் துயரைத் துடைக்கும் வகையில்", True, 1),
    ("p41 அமுலுக்கு", "இந்த புதிய அரசில் அமலுக்கு வந்துள்ளது.", "இந்த புதிய அரசில் அமுலுக்கு வந்துள்ளது.", True, 1),
    ("p41 பணியாளர்களின்", "அரசுப் பணியாளரின் இரகசியக் குறிப்பேடு முறையை", "அரசுப் பணியாளர்களின் இரகசியக் குறிப்பேடு முறையை", True, 1),
    ("p41 மகன் மகள்", "அரசுப் பணியாளரது மகன், மக்கள் ஆகியோரது திருமணங்களுக்கென", "அரசுப் பணியாளரது மகன், மகள் ஆகியோரது திருமணங்களுக்கென", True, 1),
    ("p41 மேற்கொண்டும்", "அரசுப் பணியாளர்கள் மேற்கொள்ளும் சட்டக் கல்லூரியில்", "அரசுப் பணியாளர்கள் மேற்கொண்டும் சட்டக் கல்லூரியில்", True, 1),
    ("p41 rental housing", "பட்டினப்பாக்கம் பீட்டர்ஸ் சாலைக் குடியிருப்பில் அரசு வாடகை வீட்டு மின்கட்டணியுள்ளது.", "பட்டினப்பாக்கம் பீட்டர்ஸ் சாலைக் குடியிருப்பில் அரசு வாடகை வீட்டு மனைகளைக் கட்டியுள்ளது.", True, 1),
    ("p41 நலன்கள்", "பின்தங்கியோர் நலன்கண் அறிய ஒரு குழு அமைக்கப்பட்டிருக்கிறது.", "பின்தங்கியோர் நலன்கள் அறிய ஒரு குழு அமைக்கப்பட்டிருக்கிறது.", True, 1),
    ("p42 electrification", "1972-ம் ஆண்டுக்குள் மின்வெளி இல்லா தமிழகம் என்றே இருக்கக்கூடாதென்று தீவிரமாகத் திட்டமிடப்பட்டு நிறைவேற்றப்பட்டு வருகிறது.", "1972-ம் ஆண்டுக்குள் மின்வெளி இல்லா தமிழகமே இருக்கக்கூடாதுன்னு தீவிரமாகத் திட்டமிடப்பட்டு நிறைவேற்றப்பட்டு வருகிறது.", True, 1),
    ("p43 Ramalingam request", "அவர் அது போதாது என்று இரண்டு நாட்களுக்கு முன்பு கேட்டு 250 ரூபாய் தர வேண்டுமென்று கேட்டார், அதுவும் சேங்ஷன் செய்யப்பட்டிருக்கிறது.", "அவர் அது போதாது என்று இரண்டு நாட்களுக்கு முன்பு கேட்டு 250 ரூபாய் தர வேண்டுமென்றுகேட்டு, அதுவும் சேங்ஷன் செய்யப்பட்டிருக்கிறது.", True, 1),
    ("p43 Parali Nellaiyappar", "பாலி நெல்லையப்பர்", "பரலி நெல்லையப்பர்", True, 1),
    ("p43 Kattabomman", "கட்டபொம்மன் சிலையைத் திறந்து வைத்தார் அவர்கள் பொறுப்பிலே தவிர", "கட்ட பொம்மன் சிலையைத் திறந்து வைத்ததான் அவர்கள் பொறுப்பிலே தவிர", True, 1),
    ("p43 இலட்சத்திற்கு", "4 ஆண்டுகளுக்கு 82.91 லட்சத்திற்கு", "4 ஆண்டுகளுக்கு 82.91 இலட்சத்திற்கு", True, 1),
    ("p44 heading", "## சுற்றே விலகியிரும் பிள்ளாய்", "## சற்றே விலகியிரும் பிள்ளாய்", True, 1),
    ("p44 body phrase", "வழி மறைத்திருக்கிறது. சுற்றே விலகியிரும் பிள்ளாய்.", "வழி மறைத்திருக்கிறது, சற்றே விலகியிரும் பிள்ளாய்.", True, 1),
    ("p44 Malaya", "மலேசியாவிலிருந்து இவைகளெல்லாம் வந்திருக்கின்றன.", "மலேயாவிலிருந்து இவைகளெல்லாம் வந்திருக்கின்றன.", True, 1),
    ("p44 roughly", "ஒவ்வொரு மாநிலமும் சுற்றேற்குறைய தமிழகத்திலுள்ள", "ஒவ்வொரு மாநிலமும் சற்றேறக்குறைய தமிழகத்திலுள்ள", True, 1),
    ("p45 உங்களோடு", "நாங்கள் உங்கள் நோடு இருக்க மாட்டோம்", "நாங்கள் உங்களோடு இருக்க மாட்டோம்", True, 1),
    ("p45 கூறியிருக்கிறார்கள்", "திரு. ராஜாஜியிடம் அனுமதி வாங்கித்தான் சொன்னேன் என்று கூறியிருக்கிறார்.", "திரு ராஜாஜியிடம் அனுமதி வாங்கித்தான் சொன்னேன் என்று கூறியிருக்கிறார்கள்.", True, 1),
    ("p45 பணிவன்போடு", "நான் மிகுந்த பணிவுடன் கேட்டுக் கொள்கிறேன்.", "நான் மிகுந்த பணிவன்போடு கேட்டுக் கொள்கிறேன்.", True, 1),
    ("p45 சுதந்திராக்", "சுதந்திரா கட்சியின் தலைவர்", "சுதந்திராக் கட்சியின் தலைவர்", True, 1),
    ("p45 M.K. corruption", "அந்த ராஜாக்களுக்கு மானியம் கொடுக்க வேண்டுமென்று மட்டும் சொன்ன குற்றத்திற்காக திரு. மு. கருணாநிதி மட்டும் சொன்ன என்று சொல்லி விட்டு, சிண்டிகேட்டுடன் சேரும் ராஜாஜி", "அந்த ராஜாக்களுக்கு மானியம் கொடுக்க வேண்டுமென்று மட்டும் சொன்ன குற்றத்திற்காக திரு. மு. க.வுடன் சேர மாட்டோம் என்று சொல்லி விட்டு, சிண்டிகேட்டுடன் சேரும் ராஜாஜி", True, 1),
    ("p45 முன்வருவார்களா", "ராஜாஜி அவர்கள் முன்வருவாரா?", "ராஜாஜி அவர்கள் முன்வருவார்களா?", True, 1),
    ("p45 இடது சாரிக்கட்சிகளும்", "நாங்களும், இது சரிக்கட்சிகளும்", "நாங்களும், இடது சாரிக்கட்சிகளும்", True, 1),
    ("p46 கம்யூனிஸ்ட்", "இடதுசாரி கம்யூனிஸ்டு கட்சியினரும்", "இடதுசாரி கம்யூனிஸ்ட் கட்சியினரும்", True, 1),
    ("p46 closing form", "கண்டனத் தீர்மானத்தைத் திரும்பப் பெறுமாறு கேட்டுக் கொள்கிறேன்.", "கண்டனத் தீர்மானத்தைத் திரும்பப் பெறுமாறு கேட்டுக்கொள்கிறேன்.", True, 1),
]

tamil = apply_many(tamil, tamil_replacements)

# English corrections are intentionally limited to points where the verified Tamil
# changes meaning, restores omitted source material, a name/place, or a major
# rhetorical distinction. The English remains a translation rather than a literal
# diplomatic transcription.
english_replacements: list[tuple[str, str, str, bool, int | None]] = [
    ("EN p9 sixth month", "That victory was evidence of the confidence the people had in the DMK.", "That victory, in the sixth month, was evidence of the confidence the people had in the DMK.", True, 1),
    ("EN p9 seven/eight municipalities", "Nor can anyone forget that after we assumed office, the DMK won sufficient seats in the Corporation to take responsibility there, and that in municipal elections DMK chairmen came to preside over more than fifty municipalities.", "Nor can anyone forget that after we assumed office, the DMK won sufficient seats in the Corporation to take responsibility there. In municipal elections there had previously been only seven or eight such places; now DMK chairmen preside over more than fifty municipal councils.", True, 1),
    ("EN p12 considered demands", "some of the agitations began only after this Government had accepted the workers' demands, accepted their representations, completed negotiations and fulfilled those demands.", "some of the agitations began only after this Government had considered the workers' demands, accepted their representations, completed negotiations and fulfilled those demands.", True, 1),
    ("EN p12 service advancement", "When they asked for higher wages, I held discussions with them for four or five days.", "When they asked for advancement in service, I held discussions with them for four or five days.", True, 1),
    ("EN p14 Deva Anbu", "and Devanbu died.", "and Deva Anbu died.", True, 1),
    ("EN p14 half-well sentence", "Representatives of the farmers' association led by Mr Manradiyar came to us and we announced a decision. I did not refuse to consider the farmers' problem.", "Representatives of the farmers' association led by Mr Manradiyar came to us and we announced a decision. The Leader of the Opposition later said in this very House, in effect: even if you have crossed half the well, cross the whole well. I did not refuse to consider the farmers' problem.", True, 1),
    ("EN p15 prestige", "We did not treat it as a prestige or policy issue.", "We did not treat it as a prestige issue.", True, 1),
    ("EN p15 Bhaktavatsalam", "One must ask whether earlier Congress governments, including in the period of the respected Kamaraj, had a record of acting with the same feeling.", "When I say 'Congress rule,' Mr Karuthiruman may think I mean Bhaktavatsalam. But one must ask whether Congress rule from the period of the respected Kamarajar onward had a record of acting with that same feeling.", True, 1),
    ("EN p16 Tiruchi", "When it was said that he should be brought to Madras, I said: do not bring him in a police lorry as I was once taken to Palayamkottai; bring him by car.", "When it was said that he should be brought from Tiruchi to Madras, I said: do not bring him in a police lorry as I was once taken to Palayamkottai; bring him by car.", True, 1),
    ("EN p28 bring the files", "Then came allegations of corruption in the Cooum scheme, corruption in the Veeranam scheme—“corruption everywhere, corruption in everything.”", "Then came allegations of corruption in the Cooum scheme, corruption in the Veeranam scheme—“corruption everywhere, corruption in everything; bring the files.”", True, 1),
    ("EN p34 ECC qualification", "Engineering Construction Corporation: tender Rs 12,64,85,844 for the stated scope, with Rs 40,00,000 foreign exchange for the pipes/material component specified.", "Engineering Construction Corporation: tender Rs 12,64,85,844. Excluding the price of steel plates, for the pipes alone they sought Rs 40,00,000 in foreign exchange.", True, 1),
    ("EN p35 Avadi", "about six crores for various quarters,", "about six crores for various quarters at Avadi,", True, 1),
    ("EN p37 emergency law", "It enacted measures preventing them from stopping work.", "It enacted emergency legislation preventing them from stopping work.", True, 1),
    ("EN p37 vaidika mentality", "Our industrial policy is not one of rigid dogmatism. Industry must grow.", "In industrial matters this Government does not display a vaidika—an orthodox—mentality. Industry must grow and expand.", True, 1),
    ("EN p37 EMS Birla", "E. M. S., of his own party, invited Birla to establish industry in his State.", "E. M. S., of his own party, invited Birla to come to his State and establish industry.", True, 1),
    ("EN p40 grant-aided teachers", "Whenever dearness allowance was given to others it was extended to teachers. City compensatory allowance and house-rent allowance were extended to categories of school teachers, including local-body school teachers, and earned-leave facilities were widened.", "Whenever dearness allowance was given to others it was extended to teachers. City compensatory allowance was extended to grant-aided school teachers; house-rent allowance was extended to local-body school teachers; and grant-aided school teachers were given earned-leave facilities.", True, 1),
    ("EN p41 Pattinapakkam housing", "Housing and related concessions have been extended to categories of Government servants, and, at the request of lower-division clerks, their designation was changed to “Junior Assistant.”", "For Government servants drawing more than Rs 250 a month, Government rental housing units were built in the Pattinapakkam Peters Road settlement. At the request of lower-division clerks, their designation was changed to “Junior Assistant.”", True, 1),
    ("EN p42 electrification", "The Government is pursuing an intensive programme so that by 1972 Tamil Nadu should have no village without electricity.", "The Government is intensively planning and implementing a programme so that by 1972 Tamil Nadu should not remain without electricity.", True, 1),
    ("EN p43 Parali", "Similarly we are providing assistance to Bali Nellaiyappar.", "Similarly we are providing assistance to Parali Nellaiyappar.", True, 1),
    ("EN p44 heading", "## Move aside, child!", "## Move a little aside, child!", True, 1),
    ("EN p44 body phrase", "The road is blocked—move aside.", "The road is blocked—move a little aside, child.", True, 1),
    ("EN p44 Malaya/Malaysia", "You speak about the demand for a separate State flag. Look at Malaysia. A letter from there points out that Malaysia, with a population only a fraction of Tamil Nadu's and only somewhat larger in land area, has thirteen States.", "You speak about the demand for a separate State flag. These materials have come from Malaya. Look: Malaysia has fewer people than Tamil Nadu. The letter from Malaysia says that, with land area only somewhat greater than Tamil Nadu's and a population only a fraction of Tamil Nadu's, their small country has thirteen States.", True, 1),
    ("EN p45 Rajaji passage", "Seemaisamy angrily said that if we continue to support Indira Gandhi they will no longer remain with us, and he said he had obtained Rajaji's permission before saying so. Rajaji too has made comments. I respectfully appeal to Seemaisamy, to the Swatantra Party leadership here and to the senior leader Rajaji. They are prepared to join the Syndicate over the issue of privy purses for two hundred princes. I ask Rajaji: will he join the Syndicate that voted in a manner affecting the life, language, rights, prosperity and future of four-and-a-half crore Tamil people? We and our allied parties supported Mrs Indira Gandhi in opposing continued grants to the princes. I ask Rajaji to consider once, and then again, whether that was right or wrong.", "Seemaisamy, speaking angrily, said, ‘If from now on you support Indira Gandhi, we will not remain with you,’ and said that he had spoken only after obtaining Rajaji's permission. Rajaji too has commented. With great humility I ask Seemaisamy, as the Swatantra Party leader here, and I ask the elder leader Rajaji as well. There are two hundred princes. For the sole ‘offence,’ as printed here, of saying that grants should be given to those princes, having said ‘we will not join M.K.,’ Rajaji now joins the Syndicate. I ask Rajaji: will he join the Syndicate that voted against the life, language, rights, prosperity and future of four-and-a-half crore Tamil people? We and the left parties supported Mrs Indira Gandhi there in saying that grants should not be given to the two hundred princes. Was that right or wrong? I ask Rajaji to think about it not once but twice.", True, 1),
]

english = apply_many(english, english_replacements)

# Final structural sanity checks.
if "�" in tamil or "�" in english:
    raise RuntimeError("Unicode replacement character remains in transcript")
if tamil.count("<!-- source-page:") != 42:
    raise RuntimeError(f"Expected 42 Tamil source-page markers (5–46), found {tamil.count('<!-- source-page:')}")

TRANSCRIPT.write_text(tamil + english, encoding="utf-8")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
metadata["transcription"]["status"] = "verified"
metadata["transcription"]["verified_against_scan"] = True
metadata["transcription"]["verified_scan_pages"] = "5-46"
metadata["translation"]["status"] = "verified"
metadata["translation"]["verified_against_tamil"] = True
METADATA.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

index = json.loads(INDEX.read_text(encoding="utf-8"))
entry = next(item for item in index if item["id"] == "1970-09-09-no-confidence-motion")
entry["transcription_status"] = "verified"
entry["verified_against_scan"] = True
entry["translation_status"] = "verified"
INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

root_readme = ROOT_README.read_text(encoding="utf-8")
root_readme = root_readme.replace(
    "| 09-09-1970 | [உதயக் கதிர்](./speeches/1970/1970-09-09-no-confidence-motion/) | நம்பிக்கையில்லாத் தீர்மான விவாதத்திற்கான பதிலுரை | Complete first pass | Complete | Not yet character-level verified |",
    "| 09-09-1970 | [உதயக் கதிர்](./speeches/1970/1970-09-09-no-confidence-motion/) | நம்பிக்கையில்லாத் தீர்மான விவாதத்திற்கான பதிலுரை | Verified | Verified | Verified against scan pp. 5–46 |",
)
ROOT_README.write_text(root_readme, encoding="utf-8")

speech_readme = SPEECH_README.read_text(encoding="utf-8")
status_start = speech_readme.index("## Verification status")
status_end = speech_readme.index("## Archival note")
verified_status = """## Verification status

- Scan pp. **5–46** — second-pass page-by-page visual review completed against the September 1970 scan.
- Recorded source corrections have been applied to the canonical Tamil text in `transcript.md`.
- English translation — re-checked against the corrected Tamil for every meaning-bearing correction identified during verification.
- Transcription status: **verified against scan**.
- Translation status: **verified against corrected Tamil**.

Detailed audit records are retained in `verification-log.md` and the `verification/` directory.

"""
speech_readme = speech_readme[:status_start] + verified_status + speech_readme[status_end:]
SPEECH_README.write_text(speech_readme, encoding="utf-8")

print(f"Applied {len(tamil_replacements)} Tamil corrections/checks and {len(english_replacements)} English corrections/checks.")
print("Udhaya Kathir is ready for repository status promotion to verified.")
