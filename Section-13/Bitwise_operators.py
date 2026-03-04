"""Demonstrate Python bitwise operators with examples.

Bitwise operators work on binary representations of integers.
"""

left = 10
right = 13

# AND: bit is 1 only when both bits are 1.
result_and = left & right
print("AND:", result_and, "binary:", format(result_and, "b"))
print("-" * 40)

# OR: bit is 1 when at least one bit is 1.
result_or = left | right
print("OR:", result_or, "binary:", format(result_or, "b"))
print("-" * 40)

# XOR: bit is 1 when bits are different.
result_xor = left ^ right
print("XOR:", result_xor, "binary:", format(result_xor, "b"))
print("-" * 40)

# NOT (~): inverts bits (two's complement behavior in Python ints).
result_not = ~left
print("NOT:", result_not, "binary:", format(result_not, "b"))
print("-" * 40)

# Left shift: moves bits to the left (roughly multiplies by 2 each shift).
for shift in range(1, 6):
    shifted = left << shift
    print(f"{left} << {shift} = {shifted}")
print("-" * 40)

# Right shift: moves bits to the right (roughly divides by 2 each shift).
print("10 >> 1 =", 10 >> 1)
print("5 >> 1 =", 5 >> 1)
print("10 >> 2 =", 10 >> 2)
print("320 >> 5 =", 320 >> 5)
