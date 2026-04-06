l1=["apple", "banana", "cat", "orange"]
count=0
for i in range(len(l1)):
	if len(l1[i])>5:
		count+=1
print(count,'Strings are Longer Than Five Characters')