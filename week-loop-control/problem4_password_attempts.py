n=input('Enter the Password:')
x='python123'
for i in range (1,6):
	if n==x:
		print('Access Granted')
		break
	else:
		if i!=5:
			print('Try again')
			n=input('Enter the Password:')
		else:
			print('Access Denied')
