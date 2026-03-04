"""Print a simple restaurant menu with aligned prices."""

# Store menu items as (name, price) tuples for cleaner iteration.
menu_items = [
    ("Hot Dog", 30),
    ("Donut", 40),
    ("Burger", 35),
    ("Pizza", 65),
]

line_width = 24

for name, price in menu_items:
    # Build `name .... $price` style output with dot padding.
    left = f"{name}"
    right = f"${price}"
    dots_needed = max(1, line_width - len(left) - len(right))
    print(left + "." * dots_needed + right)
