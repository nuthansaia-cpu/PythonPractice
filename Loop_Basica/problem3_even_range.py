n=int(input('Enter a number:'))
x=int(input('Enter a number greater then the first entered number:'))

# using for loop
for i in range(n,x+1,1):
	if i%2==0:
		print(i,end=' ')
print(' ')

# using while loop
while n<=x:
	if n%2==0:
		print(n,end=' ')
	n+=1