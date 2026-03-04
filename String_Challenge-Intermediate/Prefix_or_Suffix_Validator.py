"""Validate word using prefix/suffix rules.

Rule used here:
- first character must be a vowel,
- last character must be a digit.
"""

word = input("Enter a word: ").strip()
vowels = "aeiouAEIOU"

if not word:
    print("Invalid: empty input")
elif word[0] in vowels and word[-1].isdigit():
    print("Valid")
else:
    print("Invalid")
