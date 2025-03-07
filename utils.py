import unicodedataplus

def scripture_guess(texts):
    #return scripture category for a batch of texts
    labels_guessed = []
    for text in texts:
        sample = text[:20]
        guess = []
        for c in sample:
            guess.append(unicodedataplus.script(c))

        labels_guessed.append(max(set(guess), key=guess.count))
    return labels_guessed

def detect_alphabet(text: str) -> str:
    """
    Detect the type of alphabet (script) used in the given text.

    Args:
        text (str): The text from which the script will be identified.

    Returns:
        str: The detected script name (e.g., "Latin", "Cyrillic", "Arabic", etc.).
    """
    if any("а" <= c <= "я" or "А" <= c <= "Я" for c in text):
        return "Cyrillic"
    elif any("א" <= c <= "ת" for c in text):
        return "Hebrew"
    elif any("ء" <= c <= "ي" for c in text):
        return "Arabic"
    elif any("ก" <= c <= "ฮ" for c in text):
        return "Thai"
    elif any("က" <= c <= "႟" for c in text):
        return "Burmese"
    elif any("一" <= c <= "龥" for c in text):
        return "Chinese/Japanese"
    elif any("α" <= c <= "ω" or "Α" <= c <= "Ω" for c in text):
        return "Greek"
    elif any("ა" <= c <= "ჰ" for c in text):
        return "Georgian"
    elif any("ᱚ" <= c <= "᱿" for c in text):
        return "Ol Chiki (Santali)"
    elif any("ଅ" <= c <= "ୱ" for c in text):
        return "Oriya"
    elif any("ह" <= c <= "ह" for c in text):
        return "Devanagari"
    else:
        return "Latin"
