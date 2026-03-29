l1=[4,8,3,5,10,7,2,9,13,6]
even=[]
odd=[]
for i in range(len(l1)):
	if l1[i]%2==0:
		even.append(l1[i])
	else:
		odd.append(l1[i])
print('Even:',even)
print('Odd:',odd)

Odd=[x for x in l1 if x%2!=0]
Even=[x for x in l1 if x%2==0]
print('even:',Even)
print('odd:',Odd)