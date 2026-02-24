s1=input('Enter a word:')
s2='aieou'
if s1[0] in s2 and s1[-1].isdigit():
	print('valid')
else:
	print('invalid')