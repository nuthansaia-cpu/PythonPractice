"""Print first n Fibonacci numbers.

Fibonacci starts as: 0, 1, 1, 2, 3, 5, ...
Each next term = sum of previous two terms.
"""

n = int(input("Enter how many terms to print: "))

if n <= 0:
    print("Please enter a number greater than 0.")
else:
    first = 0
    second = 1

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second
    print()
