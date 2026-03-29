l1='163'
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