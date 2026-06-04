l1=input("Enter a Word:")
l2="aieou"
l3="AIEOU"
count=0
countt=0
for i in range(len(l1)):
	if l1[i] in l2:
		count+=1
for i in range(len(l1)):
	if l1[i] in l3:
		countt+=1
print(l1,':',count+countt)