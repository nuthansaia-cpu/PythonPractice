"""Demonstrate inquiry methods that return True/False."""

print("Hello".isalpha())
print("Hello123".isalpha())
print("-" * 50)

print("hello".islower())
print("Hello".islower())
print("-" * 50)

print("HELLO".isupper())
print("Hello".isupper())
print("-" * 50)

print("Hello World".istitle())
print("Hello world".istitle())
print("-" * 50)

spaces = "       "
empty = ""
newline_tab = "\n\t"
mixed = " abc "
print(spaces.isspace())
print(empty.isspace())
print(newline_tab.isspace())
print(mixed.isspace())
print("-" * 50)

print("Hello World".isprintable())
print("Hello\nWorld".isprintable())
print("-" * 50)

print("item1".isidentifier())
print("1item".isidentifier())
print("item_1".isidentifier())
print("item-1".isidentifier())
