"""Count backward from n to 1 using for and while loops."""

n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    # for-loop solution.
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()

    # while-loop solution.
    current = n
    while current > 0:
        print(current, end=" ")
        current -= 1
    print()
