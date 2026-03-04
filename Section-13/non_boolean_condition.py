"""Show truthy/falsy behavior for `and` and `or` with non-boolean values.

In Python:
- `and` returns the first falsy operand, else the last operand.
- `or` returns the first truthy operand, else the last operand.
"""

print(5 and 10)   # 10 (both truthy, so last value)
print(5 and 0)    # 0  (first falsy encountered)
print(0 and 10)   # 0  (first value already falsy)

print(5 or 10)    # 5  (first truthy value)
print(0 or 10)    # 10 (first is falsy, so second)
