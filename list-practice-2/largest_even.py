l1 = [3, 17, 8, 22, 5, 14]
largest=0
for i in range(len(l1)):
	if l1[i]%2==0:
		if largest<l1[i]:
			largest=l1[i]
print(largest)