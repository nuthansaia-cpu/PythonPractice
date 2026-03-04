"""Count forward from 1 to n using different range styles."""

n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    # style 1: range(stop) starts at 0, so use n+1 to include n.
    for i in range(n + 1):
        print(i, end=" ")
    print()

    # style 2: range(start, stop) with explicit start at 1.
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

    # style 3: range(start, stop, step) with step 1.
    for i in range(1, n + 1, 1):
        print(i, end=" ")
    print()
