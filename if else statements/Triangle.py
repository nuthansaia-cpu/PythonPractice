a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
largest = max(a, b, c)
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
	print("Valid Triangle")
	if a==b==c:
		print("Equilateral Triangle")

	elif a==b!=c or b==c!=a or a==c!=b:
		print("Isosceles Triangle")

	else:
		print("Scalene Triangle")


	if a**2 + b**2 + c**2 - largest**2 == largest**2:
    		print("Right-angled Triangle")

	else:
		print("Not a Right angled Triangle")

else:
	print("Invalid Triangle")

