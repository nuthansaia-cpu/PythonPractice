l1=[-5,-10,-20,-30]
min=float('inf')
print(min)
y=0
z=0
for i in range(len(l1)):
	y=l1[i]
	if y<min:
		min=y
		z=i
print(min,'number found at index',z)
