x=0
a=input("Enter the point while separating the numbers by space: ")
l1=a.split()
l1=[float(i) for i in l1]
print("List of numbers:", l1)


b=input("Enter the point while separating the numbers by space: ")
l2=b.split()
l2=[float(i) for i in l2]
print("List of numbers:", l2)


x=abs(l1[0]-l2[0])+abs(l1[1]-l2[1])
print('Manhattan Distance of the given points is:',x)