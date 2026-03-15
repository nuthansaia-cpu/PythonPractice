'''l1=[-1,35,36,37,40,38,39,40,-2]
res=[]
max=float('-inf')
y=0
z=0
for i in range(len(l1)):
	y=l1[i]
	if y>max:
		max=y
		z=i
print(max,'number found at index',z)'''
	
l1 = [-1, 35, 36, 37, 40, 38, 39, 40, -2]
res = []
y=0
z=0
for x in range(len(l1)):
    max = float('-inf')
    for i in range(len(l1)):
        y=l1[i]
        if y> max:
            max = y
            z = i

    del l1[z]
    res.append(max)
    print(res)
    print(max, 'number found at index', z)

 