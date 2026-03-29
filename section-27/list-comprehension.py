l1=[x for x in range(1,5)]
print(l1)

l2=[x**2 for x in range(1,5)]
print(l2)

l3=[x.lower() for x in 'PyThoN']
print(l3)

l4=[int(x) for x in '12345']
print(l4)

l5=[x for x in 'ab*cd7e' if x.isalpha()]
print(l5)