l1=int(input('Enter a Number:'))
count=0
for i in range(1,l1+1):
	n=l1%i
	if n==0:
		print(i)
		count+=1
		if count>2:
			l1+=1
			continue
	
if count<=2:
	print(l1,':','It is a prime number')
else:
	print(l1,':','it is not a prime number')
