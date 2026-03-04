"""Examples of ordering/comparison for Python data types."""

# String (lexicographic/dictionary) comparison.
s1 = "software"
s2 = "Hardware"
print(s1 > s2)

s1 = "python"
s2 = "pycharm"
print(s1 < s2)

s1 = "integr"
s2 = "integr"
print(s1 == s2)

s1 = "printer"
s2 = "print"
print(s1 > s2)

print("-" * 60)

# Boolean comparison (False -> 0, True -> 1 internally).
print(True > False)
print(True == True)
print(False < True)
print(False == False)

print("-" * 60)

# Integer comparison.
print(10 > 5)
print(10 == 10)
print(5 < 10)
print(5 != 10)
print(5 >= 5)
print(3 <= 2)

print("-" * 60)

# Float comparison.
print(10.5 > 5.2)
print(10.5 == 10.5)
print(5.3 < 10.1)
print(5.3 != 10.4)
print(5.6 >= 5.6)
print(3.2 <= 2.9)

print("-" * 60)

# Complex supports equality/inequality only.
print((2 + 3j) == (2 + 3j))
print((2 + 3j) != (3 + 2j))
print("Complex numbers cannot be compared using <, >, <=, >=")
