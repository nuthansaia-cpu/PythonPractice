"""Examples of break, continue, pass, and loop else."""

# break: stop the loop immediately when a condition matches.
for value in range(1, 6):
    if value == 4:
        break
    print("break example:", value)

print("-" * 40)

# continue: skip current iteration and move to the next.
for value in range(1, 6):
    if value == 3:
        continue
    print("continue example:", value)

print("-" * 40)

# pass: placeholder statement when code block is intentionally empty.
for _ in range(3):
    pass
print("pass example: loop executed with placeholder body")

print("-" * 40)

# else with for-loop: runs only if loop does not break.
for value in range(1, 4):
    print("else-suite example:", value)
else:
    print("Loop finished normally, so else block ran.")
