"""Find the nearest vowel for a given alphabet letter.

If two vowels are equally near, this script returns the earlier vowel alphabetically.
"""

letter = input("Enter a letter: ").strip().lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter exactly one alphabet letter.")
else:
    vowels = ["a", "e", "i", "o", "u"]

    # Convert letters to positions: a->0, b->1, ...
    letter_pos = ord(letter) - ord("a")

    best_vowel = vowels[0]
    best_distance = abs((ord(best_vowel) - ord("a")) - letter_pos)

    for vowel in vowels[1:]:
        vowel_pos = ord(vowel) - ord("a")
        distance = abs(vowel_pos - letter_pos)

        if distance < best_distance:
            best_distance = distance
            best_vowel = vowel

    print(f"Nearest vowel to '{letter}' is '{best_vowel}'")
