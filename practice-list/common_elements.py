l1=[1, 2, 3, 4, 5]
l2=[3, 5, 7, 9]
for i in range(len(l1)):
	for x in range(len(l2)):
		if l1[i]==l2[x]:
			print(l1[i])