"""Print factors of a number and check whether it is prime."""

n = int(input("Enter a number: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Factors of the number are:", end=" ")
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    print(", ".join(str(value) for value in factors))

    # Prime numbers have exactly two factors: 1 and itself.
    if len(factors) == 2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
