n=int(input('Enter a number:'))
x=int(input('Enter a number greater then the first entered number:'))
m=int(input('multiple:'))
rem=n%m
add=m-rem
z=add+n
for i in range(z,x+1,m):
	print(i)
'''# using for loop
for i in range(n,x+1,1):
	if i%2==0:
		print(i,end=' ')
print(' ')

# using while loop
while n<=x:
	if n%2==0:
		print(n,end=' ')
	n+=1
if n%m==0:
	z=n
elif n%m==1:
    z=n+2
else:
    z=n+1
for i in range(z,x+1,m):
	print(i)'''
