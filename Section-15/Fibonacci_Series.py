n=int(input('Enter a Number:'))
num=1
fib=0
for i in range(1,n+1):
	c=num+fib
	fib=num
	num=c
print(fib)