# Creation:-

t1=(1,2,3,4,5,6)
print(t1)
print(type(t1))

t2=tuple([1,2,3,4,5,6])
print(t2)
print(type(t2))

t2=tuple('python')
print(t2)
print(type(t2))

t2=tuple(range(1,5))
print(t2)
print(type(t2))

t3=()
print(t3)
print(type(t3))

t4=(3)
print(t4)
print(type(t4))

t4=(3,)
print(t4)
print(type(t4))

t5=10,11,12,13,14
print(t5)
print(type(t5))

print('--------------------------------------------------------------------')

# Representation:-

t1=(6,5,4,3,2,1)
print(t1[2])
for x in t1:
	print(x)
