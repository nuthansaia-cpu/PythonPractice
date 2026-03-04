"""Print multiples of a chosen value within a range.

This script asks for:
1. start value
2. end value (must be >= start)
3. multiple value m
Then it prints numbers divisible by m in that interval.
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number (>= start): "))
multiple = int(input("Enter a multiple value: "))

if end < start:
    print("End must be greater than or equal to start.")
elif multiple == 0:
    print("Multiple cannot be 0.")
else:
    # Find the first number >= start that is divisible by multiple.
    remainder = start % multiple
    first = start if remainder == 0 else start + (multiple - remainder)

    for value in range(first, end + 1, multiple):
        print(value)
