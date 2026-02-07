# Infinite Loop Examples.
'''i=0
while True:
	i=i+1
	print(i)

i=0
while i>=0:
	i=i+1
	print(i)

n=10
while n==10:
	print(n)'''

print ('----------------------------------------------------------------------')

# Break Examples.
i=0
while True:
	i=i+1
	if i>10:
		break
	print(i)

print ('----------------------------------------------------------------------')

# Continue Statement Examples.
i=0
while i<10:
	i=i+1
	if i%3==0:
		continue
	print(i)
