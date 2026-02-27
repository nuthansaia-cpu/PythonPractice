year = int(input('Enter a number:'))
reminder=year%4
if reminder<=2:
	print(year-reminder, "is the nearest leap year")
else:
	print(year+(4-reminder),"is the nearest leap year")