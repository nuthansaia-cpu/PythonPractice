x=5
for i in range(x+1):
	if i>0:
		print(i)
for i in range(1,x+1):
	print(i)
for i in range(1,x+1,1):
	print(i)

print('-----------------------------------------------------')
x=5
for i in range(x,0,-1):
	print(i)
x=5
while x>0:
	print(x)
	x-=1
print('-----------------------------------------------------')
n=int(input('Enter a number:'))
for i in range(0,n+1,3):
	if i>0:
		print(i)
n=int(input('Enter a number:'))
x=0
while n>x:
	x+=1
	if x%3==0:
		print(x)
print('-----------------------------------------------------')
x=int(input('Enter a number:'))
y=int(input('Enter a number:'))
for i in range(0,y+1,2):
	if i>=x:
		print(i)
x=int(input('Enter a number:'))
y=int(input('Enter a number:'))
while x<y:
	if x%2==0:
		print(x)
	x+=1
