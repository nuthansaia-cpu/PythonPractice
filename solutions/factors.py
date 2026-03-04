"""Print all factors of a positive integer.

A factor divides the number exactly (remainder 0).
"""

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a number greater than 0.")
else:
    factor = 1
    while factor <= num:
        if num % factor == 0:
            print(factor)
        factor += 1
