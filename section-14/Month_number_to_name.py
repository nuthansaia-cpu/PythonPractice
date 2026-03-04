"""Convert month number (1-12) to month name."""

month = int(input("Enter month number (1-12): "))

month_map = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(month_map.get(month, "Invalid month number"))
