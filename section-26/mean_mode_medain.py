import statistics as st
lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
mean = st.mean(lst)
median = st.median(lst)
mode = st.mode(lst)
print('Mean:', mean)
print('Median:', median)
print('Mode:', mode)


print('_____________________________________________________________________________')

lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
sum=0
for i in range(len(lst)):
	sum=lst[i]+sum
mean=sum/len(lst)
print('Mean:',mean)

print('_____________________________________________________________________________')

lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
count=0
count1=0
for i in range(len(lst)):
	print(lst[i])
	for x in range(len(lst)):
		print(lst[x])
		if lst[i]==lst[x]:
			count=count+1
			print(count)
		continue
	if count>count1:
		count1=count
		mode=lst[i]
		print(mode)
	print(count1)
	count=0
	print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('Mode:',mode)

print('_____________________________________________________________________________')

lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
l1 = []
z=0
for x in range(len(lst)):
    min = float('inf')
    for i in range(len(lst)):
        if lst[i]<min:
            min = lst[i]
            z = i
    del lst[z]
    l1.append(min)
    print(l1)
    print(min, 'number found at index', z)

if len(l1)%2==0:
	y=int(len(l1)/2)
	median=(l1[y-1]+l1[y])/2
	print(median)

else:
	y=int((len(l1)-1)/2)
	median=l1[y]
	print('Median',median)



























