#index(element,start,end)
l1=[10,20,30,40,10,20,30,20]
l1.index(20)
l1.index(20,2)
print(l1)

#count(element)
l1=[10,20,30,40,10,20,30,20]
l1.count(20)
print(l1)

#reverse()
l1=[10,20,30,40,50,60,70]
l1.reverse()
print(l1)

#sort(*,key=None,reverse=False)
l1=[70,10,60,20,50,30,40]
l1.sort()
l1.sort(reverse=True)
print(l1)

l1=['coat','python','black','cat']
l1.sort()
print(l1)
l1.sort(key=len)
print(l1)

l1=['apple','Bat','cat','Dog']
l1.sort()
print(l1)