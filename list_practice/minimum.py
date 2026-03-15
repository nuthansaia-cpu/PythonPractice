'''l1=[-5,-10,-20,-30]
min=float('inf')
print(min)
y=0
z=0
for i in range(len(l1)):
	y=l1[i]
	if y<min:
		min=y
		z=i
print(min,'number found at index',z)'''

l1 = [-1, 35, 36, 37, 40, 38, 39, 40, -2]
res = []
y=0
z=0
for x in range(len(l1)):
    min = float('inf')
    for i in range(len(l1)):
        y=l1[i]
        if y<min:
            min = y
            z = i

    del l1[z]
    res.append(min)

    print(res)
    print(min, 'number found at index', z)