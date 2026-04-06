'''l1=[1,2,3]
l2=l1
l3=len(l1)
count=0
count1=0
n=0
while n<=0:
	for x in range(len(l1)):
		if l2[n]<=l2[x]:
			count+=1
	if count==len(l2):
		count1+=1
	count=0
	del l2[n]
	if l2==[]:
		break
if count1==l3:
		print('It is a sorted list')
else:
		print('It is a unsorted list')'''

l1=[2,4,4,7,9,10]
count=1
for i in range(1,len(l1)):
	if l1[i]>=l1[i-1]:
		count+=1
	else:
		if l1[i]>l1[i-1]:
			break
if count==len(l1):
	print('It is a sorted list')
else:
	print('It is a unsorted list')