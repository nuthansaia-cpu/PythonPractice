"""Create a simple username from full name.

Rule:
- lowercase everything,
- take first 3 letters of first word,
- take first 3 letters of last word,
- combine both.
"""

name = input("Enter your full name: ").strip().lower()
parts = name.split()

if not parts:
    print("Please enter a valid name.")
else:
    first_part = parts[0][:3]
    last_part = parts[-1][:3]
    username = first_part + last_part
    print(username)
