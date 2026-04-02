lst = [6, 8, 4, 9, 3, 10, 8, 11, 5, 7, 8, 4, 2]
l1 = []
z=0
for x in range(len(lst)):
    min = float('inf')
    for i in range(len(lst)):
        if lst[i]<min:
            min = lst[i]
            z = i
    del lst[z]
    l1.append(min)
    print(l1)
    print(min, 'number found at index', z)

if len(l1)%2==0:
	y=int(len(l1)/2)
	median=(l1[y-1]+l1[y])/2
	print(median)

else:
	y=int((len(l1)-1)/2)
	median=l1[y]
	print('Median',median)
