l1=[-1,35,36,37,40,38,39,40,-2]
first_min = second_min = float('inf')
y=0
for i in range(len(l1)):
	y=l1[i]
	if y<first_min:
		second_min=first_min
		first_min=y
	elif first_min<y<second_min:
		second_min=y
print(second_min)