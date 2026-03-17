l1 = [-5, 10, -2, 8, 0, 3, -1]
count=0
countt=0
for i in range(len(l1)):
	if l1[i]>0:
		count+=1
	elif l1[i]<0:
		countt+=1
print('positive numbers:',count)
print('negative numbers:',countt)

	