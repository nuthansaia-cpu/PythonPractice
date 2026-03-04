"""Print prime numbers from 1 to 100."""

for number in range(2, 101):
    is_prime = True

    # Try dividing the number by values from 2 to sqrt(number).
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
