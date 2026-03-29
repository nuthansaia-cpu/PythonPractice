'''l1='hello world python'
l2=l1.replace(' ','-')
print(l2)'''

l1='hello world python'
l2=''
for i in l1:
	if i!=' ':
		l2+=i
	else:
		l2+='-'
print(l2)			