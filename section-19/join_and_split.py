"""Demonstrate replace, join, split, rsplit, and splitlines."""

# replace(old, new, count)
email = "abc@gmail.com"
print("a-b-c-d-e".replace("-", ","))
print("a-b-c-d-e".replace("-", ",", 3))
print("a-b-c-d-e".replace("m", "m"))  # No change; 'm' is not present.
print(email.replace("gmail", "yahoo"))

print("-" * 50)

# join(iterable): separator joins items from an iterable of strings.
print("xyz".join("abc"))
print("/".join("abc"))

print("-" * 50)

# split(sep, maxsplit)
full_name = "John Smith Ajay"
print(full_name.split())
print(full_name.split("h"))

csv_name = "John,Smith,Ajay"
print(csv_name.split(","))

hyphen_data = "John-Smith-Ajay-Khan-James"
print(hyphen_data.split())        # No spaces, so full string as one item.
print(hyphen_data.split("-"))
print(hyphen_data.split("-", 3))

print("-" * 50)

# rsplit starts splitting from right side.
print(hyphen_data.rsplit("-", 4))

print("-" * 50)

# splitlines splits text at line boundaries.
multiline = "Line 1\nLine 2\nLine 3"
print(multiline.splitlines())
