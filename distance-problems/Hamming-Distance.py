count=0

a=input("Enter the String while separating the numbers by space: ")
l1=a.split()
l1=[float(i) for i in l1]
print("List a:", l1)


b=input("Enter the String while separating the numbers by space: ")
l2=b.split()
l2=[float(i) for i in l2]
print("List b:", l2)


if len(l1)>len(l2):
	x=len(l1)
else:
	x=len(l2)


for i in range(x):
	if l1[i]==l2[i]:
		print('Position',i,':', l1[i],'and',l2[i],'→ Same')
	else:
		count+=1
		print('Position',i,':', l1[i],'and',l2[i],'→ Different')

print('Hamming distance of the given two string is:',count)