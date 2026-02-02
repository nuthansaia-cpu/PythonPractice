num=int(input("Enter a number:"))
sum=0
def sum_of_numbers(num):
    if num==0:
        return 0
    else:
        return num + sum_of_numbers(num-1)
sum=sum_of_numbers(num)
print("The sum of all numbers is:",sum)

print("--------------------------------------------------------------------------------------------")

n=int(input("Enter a number:")) 
sum=n*(n+1)//2
print("The sum of all numbers is:",sum)
    