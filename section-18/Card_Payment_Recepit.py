"""Mask a card number and show only the last 4 digits.

Example:
Input: 1234567812345678
Output: XXXX XXXX XXXX 5678
"""

card_no = input("Enter card number: ").strip()

# Keep only digit characters so spaces/hyphens do not break indexing.
clean_card = "".join(ch for ch in card_no if ch.isdigit())

if len(clean_card) < 4:
    print("Please enter at least 4 digits.")
else:
    last_digits = clean_card[-4:]
    masked = "XXXX XXXX XXXX " + last_digits
    print(masked)
