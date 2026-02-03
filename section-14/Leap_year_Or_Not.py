year = int(input("Enter the Year:"))
if year%4==0 and year%100!=0:
    print("It is a leap year")
if year%100==0 and year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
