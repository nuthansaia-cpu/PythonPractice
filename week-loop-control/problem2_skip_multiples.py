"""Print numbers from 1 to n, skipping multiples of 3."""

n = int(input("Enter a number: "))

current = 1
while current <= n:
    if current % 3 == 0:
        current += 1
        continue

    print(current)
    current += 1
