l1=[[1,2,3],[1,1,1,1,1],[2,2,3,3]]
long=0
for i in range(len(l1)):
	if len(l1[i])>long:
		long=len(l1[i])
		x=l1[i]
print(x,':',long)

max_list=max(l1,key=len)
print(max_list,':',len(max_list))	