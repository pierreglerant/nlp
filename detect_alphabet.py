import pandas as pd

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

# Load the CSV file (replace with your actual file path)
df = pd.read_csv("data/train_submission.csv")

# Add a new column "Script" with the detected alphabet type
df["Script"] = df["Text"].apply(detect_alphabet)

# Save the new CSV file with a header
output_file = "data/train_with_alphabet.csv"
df.to_csv(output_file, index=False, header=["Usage", "Text", "Label", "Script"])

print(f"The file with alphabet types has been generated: '{output_file}'")
