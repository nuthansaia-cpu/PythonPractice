n=int(input('Enter a Number:'))
count=0
for i in range(1,n+1):
	if n%i==0:
		count+=1
	if count<=2:
		print('It is a Prime Number')
	else:
		print('It is not a prime number')
		