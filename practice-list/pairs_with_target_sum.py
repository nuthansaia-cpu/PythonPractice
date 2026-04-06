l1=[2, 4, 3, 5, 7, 8]
l2=l1
Target=int(input('Enter the Target:'))
for i in range(len(l1)):
	for x in range(len(l2)):
		if l1[0]+l2[x]==Target:
			print((l1[0],l2[x]))
	del l1[0]