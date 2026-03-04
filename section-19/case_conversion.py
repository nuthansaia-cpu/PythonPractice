"""Demonstrate common string case-conversion methods."""

sample = "hello dear"
print(sample.capitalize())  # First character uppercase.
print("-" * 50)

print(sample.upper())       # All letters uppercase.
print("-" * 50)

print("HELLO DEAR".lower()) # All letters lowercase.
print("-" * 50)

print("hello how are you".title())   # First letter of each word uppercase.
print("-" * 50)

print("Hello How Are You".swapcase()) # Upper <-> lower swap.
print("-" * 50)

print("HELLO how are you".casefold()) # Stronger lowercase for comparisons.
