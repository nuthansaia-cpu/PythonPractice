# Finding Maximum Element.
n=int(input('Number of Elements:'))
i=0
max=float('-inf')
print('Enter',n,'Numbers:')
while i<n:
	i=i+1
	x=int(input())
	if x>max:
		max=x
print('Max Element is:',max)

print('--------------------------------------------------------')

# Finding Maximum and Minimum Element.
n=int(input('Number of Elements:'))
i=0
max=float('-inf')
min=float('inf')
print('Enter',n,'Numbers:')
while i<n:
	i=i+1
	x=int(input())
	if x>max:
		max=x
	if x<min:
		min=x
print('Max Element is:',max)
print('Min Element is:',min)