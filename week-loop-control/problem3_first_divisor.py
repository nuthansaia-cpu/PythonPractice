"""Print the first non-trivial divisor of n.

A non-trivial divisor is any divisor other than 1 and n.
"""

n = int(input("Enter a number: "))

if n <= 3:
    print("No non-trivial divisor for this number.")
else:
    found = False
    for i in range(2, n):
        if n % i == 0:
            print(i)
            found = True
            break

    if not found:
        print("No non-trivial divisor found (number is prime).")
