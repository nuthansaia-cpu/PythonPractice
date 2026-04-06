n=int(input('Enter a number:'))
for i in range(1,n+1):
	y=1
	for x in range(1,n+1):
		print(i*y,end=' ')
		y+=1
	print('')