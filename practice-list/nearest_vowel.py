l1=input('Enter a letter:')
if 97<=ord(l1)<=122:
	l2='aieou'
else:
	l2='AIEOU'
l3=l1
l4=l1
n=1
count=0
countt=0
while n>0:
	if l3 in l2:
		break
	else:
		l3=chr(ord(l3) + 1)
		count+=1
		if ord(l3)==123:
			l3='u'
		elif ord(l3)==91:
			l3='U'
		continue
while n>0:
	if l4 in l2:
		break
	else:
		l4=chr(ord(l4) - 1)
		countt+=1
		continue
if countt<=count:
	print(l1,'nearest value',l4)
else:
	print(l1,'nearest value',l3)