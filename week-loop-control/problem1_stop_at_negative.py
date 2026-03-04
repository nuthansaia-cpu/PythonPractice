"""Read numbers repeatedly.

Rules:
1. Stop when a negative number is entered.
2. Skip printing when the input is 0.
3. Print positive numbers.
"""

while True:
    number = int(input("Enter a number: "))

    # break exits the loop immediately.
    if number < 0:
        print("Negative number entered. Stopping.")
        break

    # continue skips the remaining code in this loop iteration.
    if number == 0:
        continue

    print(number)
