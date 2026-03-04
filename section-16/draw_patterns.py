"""Draw common star patterns using nested loops."""

rows = 5

# 1) Solid square (5x5)
for _ in range(rows):
    print("*" * rows)

print("-" * 65)

# 2) Right triangle (increasing)
for i in range(1, rows + 1):
    print("*" * i)

print("-" * 65)

# 3) Inverted right triangle (decreasing)
for i in range(rows, 0, -1):
    print("*" * i)

print("-" * 65)

# 4) Hollow square pattern.
for i in range(rows):
    for j in range(rows):
        # Border positions become '*', inner cells become space.
        if i in (0, rows - 1) or j in (0, rows - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
