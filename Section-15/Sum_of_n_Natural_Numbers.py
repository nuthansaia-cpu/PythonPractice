"""Compute the sum of first n natural numbers."""

n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print("Sum of n natural numbers:", total)
