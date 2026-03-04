"""Basic nested loop demonstrations."""

# Example 1: pair values with a dash separator.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "-", j)

print("-" * 40)

# Example 2: pair values with a comma separator.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, ",", j)
