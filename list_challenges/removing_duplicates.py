"""Remove duplicates from a list while preserving first occurrence order."""

values = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]
unique_values = []

for element in values:
    # Keep element only if we have not seen it already.
    if element not in unique_values:
        unique_values.append(element)

print("Deduplicated list:", unique_values)
