l1=input('Enter a letter:')
if 97<=ord(l1)<=122:
	l2='aieou'
else:
	l2='AIEOU'
letter=l1
letter1=l1
n=1
count=0
countt=0
while n>0:
	if letter in l2:
		break
	else:
		letter=chr(ord(letter) + 1)
		count+=1
		if ord(letter)==123:
			letter='u'
		elif ord(letter)==91:
			letter='U'
		continue
while n>0:
	if letter1 in l2:
		break
	else:
		letter1=chr(ord(letter1) - 1)
		countt+=1
		continue
if countt<=count:
	print(l1,'nearest value',letter1)
else:
	print(l1,'nearest value',letter)