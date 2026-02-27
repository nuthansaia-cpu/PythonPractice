n=int(input('Enter a number:'))
x=1
count=0
count1=0

# using for loop
for i in range(1,n+1):
	if i%3==0:
		count+=1
print(count)

# using while loop
while n>=x:
	if x%3==0:
		count1+=1
	x+=1
print(count1)