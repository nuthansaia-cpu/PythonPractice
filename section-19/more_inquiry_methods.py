"""Demonstrate isdigit, isdecimal, isnumeric, isascii, isalnum."""

# isdigit: True for digit characters (includes some Unicode digits).
s = "7\u20823\u2075"
print(s)
print(s.isdigit())
print("7235".isdigit())
print("71.23".isdigit())

print("-" * 50)

# isdecimal: stricter than isdigit.
s_decimal = "\u0969\u096A\u096B"
print(s_decimal)
print(s_decimal.isdecimal())

print("-" * 50)

# isnumeric: broader; includes numeric symbols like fractions.
s_numeric = "\u00BE\u215E"
print(s_numeric)
print(s_numeric.isnumeric())

print("-" * 50)

print("Hello123".isascii())
print("नमस्ते123".isascii())

print("-" * 50)

print("abc123".isalnum())
print("abc123!".isalnum())
