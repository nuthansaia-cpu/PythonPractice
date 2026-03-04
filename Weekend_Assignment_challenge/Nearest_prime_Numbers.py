"""Find the nearest prime number to the given integer.

If two primes are equally near, this script returns the smaller one first.
"""


def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is already a prime number.")
else:
    offset = 1
    while True:
        lower = n - offset
        upper = n + offset

        lower_is_prime = is_prime(lower)
        upper_is_prime = is_prime(upper)

        if lower_is_prime and upper_is_prime:
            print(f"Nearest prime numbers: {lower} and {upper}")
            break
        if lower_is_prime:
            print(f"Nearest prime number: {lower}")
            break
        if upper_is_prime:
            print(f"Nearest prime number: {upper}")
            break

        offset += 1
