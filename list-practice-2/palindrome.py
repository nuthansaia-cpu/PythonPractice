l1=[5, 4, 3, 2, 1, 2, 6, 4, 5]
l=0
r=len(l1)-1
count=0
countt=0
x=True
while l<=r:
	if l1[l]==l1[r]:
		countt+=1
	else:
		x=False
	l+=1
	r-=1
	count+=1
if count==countt:
	print('It is a palindrome list')
else:
	print('It is not a palindrome list')