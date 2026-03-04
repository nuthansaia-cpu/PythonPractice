"""Check whether a list reads the same forward and backward."""

values = [5, 4, 3, 3, 4, 5]

# Reverse copy using slicing.
reversed_values = values[::-1]

if values == reversed_values:
    print("Yes, palindrome")
else:
    print("Not a palindrome")
