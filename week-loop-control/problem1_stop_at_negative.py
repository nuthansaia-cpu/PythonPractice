n=0
while n>=0:
	n=int(input('Enter a number:'))
	if n==0:
		continue
	else:
		if n<0:
			break
		else:
			print(n)