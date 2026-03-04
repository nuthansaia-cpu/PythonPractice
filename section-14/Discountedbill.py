"""Calculate payable amount after discount slabs."""

amount = int(input("Enter the amount: "))

if amount < 1000:
    discount_rate = 0.10
elif amount < 5000:
    discount_rate = 0.15
elif amount < 10000:
    discount_rate = 0.20
else:
    discount_rate = 0.25

# Final amount after subtracting discount.
total = amount - (amount * discount_rate)
print("Pay:", total)
