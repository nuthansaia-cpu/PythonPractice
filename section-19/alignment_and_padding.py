"""Demonstrate alignment/padding and trimming string methods."""

text = "Hello"

# ljust(width, fillchar): pad on right side.
print(text.ljust(7, "*"))
print("-" * 60)

# rjust(width, fillchar): pad on left side.
print(text.rjust(7))
print(text.rjust(7, "-"))
print("-" * 60)

# center(width, fillchar): keep content centered.
print(text.center(7))
print(text.center(7, "*"))
print("-" * 60)

# zfill(width): left pad with zeros (useful for numeric text).
print(text.zfill(7))
print("-" * 60)

# lstrip/rstrip/strip remove characters from edges (not middle).
print("  Hello".lstrip())
print("$$Hello".lstrip("$"))
print("Hello!!".rstrip("!"))
print("#Hello#".strip("#"))
print("#!Hello  $ *".strip("#! $*"))
