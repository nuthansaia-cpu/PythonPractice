l1=input('Enter a number:')
l2=l1.replace('',' ')
l3=l2.split()
l3=[int(i) for i in l3]
print(l3)
y=0
for i in range(len(l3)):
	y=l3[i]**len(l3)+y
	print(y)
if y==int(l1):
	print('it is a armstrong number')
else:
	print('it is not a armstrong number')
print('--------------------------------------------------')
num=int(input('Enter a number:'))
digit=int(input('No of digits you entered:'))
l2=0
l3=num
sum=0
x=digit
for i in range(digit):
	l2=l3%10
	print(l2)
	l3=l3//10
	print(l3)
	digit-=1
	sum=l2**x+sum
	print(sum)
if sum==num:
	print('it is a armstrong number')
else:
	print('it is not a armstrong number')