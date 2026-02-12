# String Indexing
s1='Hello World'
print(s1[0],s1[-7])

# Note :- String is immutable

print('-----------------------------------------------------------------')

# String Slicing
# s1[start : stop : step]
s1='Hello World'
# start
print(s1[1])
# start,stop
print(s1[1 : 7])
print(s1[3 : 7])
print(s1[  : 7])
print(s1[  :  ])
print(s1[6 :  ])
print(s1[-5:  ])
print(s1[-5:-2])
# start,stop,step
print(s1[0 : 11 :  ])
print(s1[0 : 11 : 2])
print(s1[0 :    : 2])
print(s1[  :    : 2])
print(s1[  :    :  ])
# Negative index in step
s2=s1[  :  :  -1]
print(s2)
s2=s1[10 : 5 : -1]
print(s2)
s2=s1[-7 : -12 : -1]
print(s2)
