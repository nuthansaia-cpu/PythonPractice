income=int(input("Enter The income:"))
tax=0
tax1=0
tax2=0
senior_citezien=input("Enter Yes(Y) or NO(N):")
if senior_citezien=='Y' or senior_citezien=='y':
	print("Free-income coupon=50000")
	income=income-50000
elif senior_citezien=='n' or senior_citezien=='N':
	print("No Free-income coupon")
else:
	print("invalid input")

if income>300000:
	tax=income-300000
	if tax>=300000:
		tax1=300000*0.05
		tax=tax-300000		
		if tax>0:
			tax2=tax*0.20

	else:
		tax1=tax*0.05

else:
	print("No tax")

print("Total tax:", tax1 + tax2)	