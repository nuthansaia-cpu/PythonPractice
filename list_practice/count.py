l1=[0,1,1,0,0,0,1,1]
count=0
countt=0
for i in range(len(l1)):
	if l1[i]==1:
		count+=1
	else:
		countt+=1
print(count)
print(countt)
