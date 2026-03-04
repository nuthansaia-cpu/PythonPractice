"""Find the nearest leap year to the given year.

If two leap years are equally near, this script returns the earlier year.
"""


def is_leap(year: int) -> bool:
    """Return True if year is leap, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input("Enter a year: "))

# Search outward from the target year.
distance = 0
while True:
    lower = year - distance
    upper = year + distance

    if is_leap(lower):
        print(f"Nearest leap year: {lower}")
        break

    if is_leap(upper):
        print(f"Nearest leap year: {upper}")
        break

    distance += 1
