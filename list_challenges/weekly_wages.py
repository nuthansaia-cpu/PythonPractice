"""Calculate weekly wages with overtime.

Input format for hours:
- enter space-separated daily hours, e.g. `8 8 8 8 8`

Rules:
- up to 40 hours: normal wage
- above 40 hours: overtime paid at 1.5x wage
"""

hours_text = input("Enter daily hours (space-separated): ")
hourly_wage = int(input("Enter hourly wage: "))

# Convert each token into an integer hour value.
week_hours = [int(value) for value in hours_text.split()]
total_hours = sum(week_hours)

if total_hours <= 40:
    total_wages = total_hours * hourly_wage
else:
    overtime = total_hours - 40
    total_wages = 40 * hourly_wage + overtime * hourly_wage * 1.5

print("Total wages:", total_wages)
