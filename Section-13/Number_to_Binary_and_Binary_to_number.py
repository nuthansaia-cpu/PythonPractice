"""Convert numbers to binary strings and back."""

number_a = 10
binary_a = format(number_a, "b")  # Binary string without 0b prefix.
print(binary_a)

number_b = 14
binary_b = format(number_b, "b")
print(binary_b)

print(format(25, "b"))

number_c = 25
print(bin(number_c))  # Includes `0b` prefix.

# bit_length() tells how many bits are needed to represent the number.
print("bit length of 25:", number_c.bit_length())

# Convert binary text to decimal integer using base 2.
binary_text = "1010"
print(f"binary {binary_text} -> decimal {int(binary_text, 2)}")
