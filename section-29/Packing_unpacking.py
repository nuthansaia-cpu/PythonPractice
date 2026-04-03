# Concatenation(+):-
t1=(1,2,3)
t2=(8,9,10)
t3=t1+t2
print(t3)

# Repetition(*):-
t1=(1,2,3)
t2=t1*3
print(t2)

# Packing Unpacking(*):-

# Packing:-
t1=1,2,3,4,5
print(t1)

# Unpacking:-
t1=1,2,3,4,5
a,b,c,d,e=t1
print(a,b,c,d,e)

a,b,*c=t1
print(a,b,c)

*a,b,c=t1
print(a,b,c)

a,*b,c=t1
print(a,b,c)

