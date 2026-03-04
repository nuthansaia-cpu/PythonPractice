"""Find nearest leap year using simple arithmetic distance."""


def is_leap(year: int) -> bool:
    """Return True if year is leap, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input("Enter a year: "))

if is_leap(year):
    print(f"{year} is already a leap year")
else:
    offset = 1
    while True:
        if is_leap(year - offset):
            print(f"Nearest leap year: {year - offset}")
            break
        if is_leap(year + offset):
            print(f"Nearest leap year: {year + offset}")
            break
        offset += 1
