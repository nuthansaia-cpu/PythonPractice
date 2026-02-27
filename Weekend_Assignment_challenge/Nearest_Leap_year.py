n=int(input('Enter a Number:'))
x=0
y=0
for i in range(n,n+10):
	if i%4==0 and i%100!=0:
		break
	else:
		if i%400==0 and i%100==0:
			break
	x+=1
for z in range(n,n-10,-1):
	if z%4==0 and z%100!=0:
		break
	else:
		if z%400==0 and z%100==0:
			break
	y+=1
if x<y:
	print(i,'it is the nearest prime number')
else:
	print(z,'it is the nearest prime number')