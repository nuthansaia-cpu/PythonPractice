l1 = [4, 7, 2, 7, 9, 7, 1]
count=0
search = int(input('Enter a number from the list:'))
for i in range(len(l1)):
	if l1[i]==search:
		count+=1
print(search,'appears',count,'times in the list')