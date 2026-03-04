"""Compare find/rfind/index/rindex/count behavior."""

text = "hello how are you"

# find() returns -1 if substring is missing.
print(text.find("o"))
print(text.find("how"))
print(text.find("K"))
print(text.find("o", 5))
print(text.find("o", 5, 7))

print("-" * 64)

# rfind() searches from right side and returns -1 if not found.
print(text.rfind("o"))
print(text.rfind("o", 0, 15))
print(text.rfind("kite"))

print("-" * 64)

# rindex() is like rfind(), but raises ValueError when missing.
print(text.rindex("o"))
print(text.rindex("o", 0, 15))

print("-" * 64)

# count() returns how many times a substring appears.
print(text.count("o"))
print(text.count("me"))

print("-" * 64)

# index() is like find(), but raises ValueError when missing.
print(text.index("o"))
print(text.index("how"))

try:
    print(text.index("k"))
except ValueError:
    print("'k' not found -> index() raises ValueError")
