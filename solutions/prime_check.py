"""Check if a number is prime.

A prime number has exactly two factors: 1 and itself.
"""

num = int(input("Enter a positive integer: "))

if num < 2:
    print("This number is not prime.")
else:
    divisor_count = 0
    candidate = 1

    # Count how many numbers divide num exactly.
    while candidate <= num:
        if num % candidate == 0:
            divisor_count += 1
        candidate += 1

    if divisor_count == 2:
        print("This number is a prime number.")
    else:
        print("This number is not a prime number.")
