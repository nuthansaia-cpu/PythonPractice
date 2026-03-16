'''n=int(input('Enter a Number:'))
for x in range(1,n+1):
	for i in range(1,n+1):
		print(i,end=' ')
	print('')'''

'''n=int(input('Enter a Number:'))
for x in range(1,n+1):
	for i in range(1,n+1):
		print(x,end=' ')
	print('')'''

'''n=int(input('Enter a Number:'))
for x in range(1,n+1):
	for i in range(1,x+1):
		print(i,end=' ')
	print('')'''

n=int(input('Enter a Number:'))
for x in range(1,n+1):
	for i in range(1,n-x+2):
		print(i,end=' ')
	print('')