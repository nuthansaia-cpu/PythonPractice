"""Check whether a given year is a leap year.

Leap year rules:
1. Divisible by 4 -> leap year,
2. except years divisible by 100 are NOT leap years,
3. except years divisible by 400 ARE leap years.
"""

year = int(input("Enter the year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print("It is a leap year")
else:
    print("It is not a leap year")
