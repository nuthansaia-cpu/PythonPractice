# Factors of a number. 
n=int(input('Enter a Number:'))
print('factors of the number are:',end='')
for i in range(1,n+1):
	if n%i==0:
		print(i,end=',')

print('-------------------------------------------------------------')

# prime numbers.
n=int(input('Enter a Number:'))
count=0
for i in range(1,n+1):
	if n%i==0:
		count+=1
if count<=2:
	print(n,'is a prime number')
else:
	print(n,'is not a prime number')
