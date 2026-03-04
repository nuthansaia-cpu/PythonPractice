"""Rotate list to the left by n positions."""

values = [1, 2, 3, 4, 5, 6]
steps = 2

# Normalize steps so large values still work (e.g., 8 -> 2 for list of length 6).
steps = steps % len(values)
rotated = values[steps:] + values[:steps]

print("Original list:", values)
print("Rotated list:", rotated)
