lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
sum=0
for i in range(len(lst)):
	sum=lst[i]+sum
mean=sum/len(lst)
print('Mean:',mean)