n=int(input('Enter a number:'))
x=0
y=2
while y>x:
	if n==0:
		print('',end='')
	else:
		if n<0:
			print('',end='')
			break
		else:
			print(n)
	n=int(input('Enter a number:'))


'''n=int(input('Enter a number:'))
x=0
y=2
while y>x:
	if n>0 and n!=0:
		print(n)
	else:
		if n==0:
			print('',end='')
		else:
			if n<0:
				break
	n=int(input('Enter a number:'))'''