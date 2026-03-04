"""Convert day number (1-7) to day name."""

day_no = int(input("Enter the day number (1-7): "))

day_map = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
}

# dict.get(key, default) returns default when key is not present.
print(day_map.get(day_no, "Invalid day number"))
