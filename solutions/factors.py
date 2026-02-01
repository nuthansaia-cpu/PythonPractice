num=int(input("Enter a Positive Integer: "))
factor=0
while num>0:
    if num%factor==0:
        print(factor)
    factor+=1