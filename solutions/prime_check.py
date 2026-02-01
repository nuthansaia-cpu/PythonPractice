num=int(input("Enter a Positive Integer: "))
factors=1
count=0
while factors<=num:
    if num%factors==0:
        print(factors)
        count+=1
    factors+=1
if count<=2:
    print("Then this numberis a Prime Number")
else:
    print("Then this number is not a Prime Number")