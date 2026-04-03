t1=(*(x for x in range(1,5)),)
print(t1)

t2=tuple(x for x in range(1,5))
print(t2)

t3=tuple(x**2 for x in range(1,5))
print(t3)

t4=(*(x.lower() for x in 'PyThoN'),)
print(t4)

t5=(*(int(x) for x in '12345'),)
print(t5)

t6=(*(x for x in 'ab*cd7e' if x.isalpha()),)
print(t6)

