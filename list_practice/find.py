l1=[-1,35,36,37,40,38,39,40,-2]
search=int(input('Enter a number to search:'))
pos=len(l1)
for i in range(len(l1)):
	if l1[i]==search:
		pos=i
		break

if pos==len(l1):
	print(search,'not found in array')
else:
	print(search,'found in index',pos)