"""Count how many numbers from 1..n are multiples of 3.

Two approaches are shown: for-loop and while-loop.
"""

n = int(input("Enter a number: "))

if n < 1:
    print("Count (for loop): 0")
    print("Count (while loop): 0")
else:
    count_for = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            count_for += 1

    count_while = 0
    current = 1
    while current <= n:
        if current % 3 == 0:
            count_while += 1
        current += 1

    print(f"Count (for loop): {count_for}")
    print(f"Count (while loop): {count_while}")
