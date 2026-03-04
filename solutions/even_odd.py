"""Check whether a number is even or odd.

A number is even if dividing by 2 leaves remainder 0.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
