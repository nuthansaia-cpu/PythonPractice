"""Convert a single digit (0-9) into its word form."""

digit = int(input("Enter a digit (0-9): "))

digit_words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}

print(digit_words.get(digit, "Invalid digit"))
