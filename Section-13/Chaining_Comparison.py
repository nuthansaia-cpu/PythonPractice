"""Show how comparison chaining works in Python.

`a < b < c` is equivalent to `(a < b) and (b < c)`.
"""

a = 3
b = 5
c = 7
print(a < b and a < c)  # Two separate comparisons joined with and.
print(a < b < c)         # Chained comparison.

print("-" * 40)

a = b = 5
c = 7
print(a == b and b < c)
print(a == b < c)
