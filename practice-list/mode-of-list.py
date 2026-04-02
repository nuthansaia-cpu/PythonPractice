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
		
	if count>count1:
		count1=count
		mode=lst[i]
		print(mode)
	print(count1)
	count=0
	print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('Mode:',mode)