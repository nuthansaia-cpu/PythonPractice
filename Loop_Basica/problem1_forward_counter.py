n=int(input('Enter a number:'))

# range(stop)
for i in range(n+1):
	print(i,end=' ')
print(' ')

# range(start,stop)
for i in range(1,n+1):
	print(i,end=' ')
print(' ')

# range(start,stop,step)
for i in range(1,n+1,1):
	print(i,end=' ')