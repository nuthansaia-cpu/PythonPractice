"""Demonstrate identity operators: `is` and `is not`.

`is` checks whether two variables point to the same object in memory.
"""

a = "Hello"
b = "Hello"
print(a is b)      # Often True for small interned strings.
print(id(a))
print(id(b))

print("-" * 40)

c = "Hello World"
d = "hello"
print(a is not c)
print(id(c))
print(id(d))
