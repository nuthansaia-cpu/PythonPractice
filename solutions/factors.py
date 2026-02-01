num=int(input("Enter a Positive Integer: "))
factor=1
while factor<=num:
    if num%factor==0:
        print(factor)
    factor+=1