l1=input('Enter a letter:')
if 97<=ord(l1)<=122:
	l2='aieou'
else:
	l2='AIEOU'
if l1 in l2:
	print('It is a Vowel')
elif 97<=ord(l1)<=122 or 65<=ord(l1)<=90:
	print('It is Consonant')
else:
	print('It is not a letter')