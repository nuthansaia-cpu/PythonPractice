# find(sub,start,end)
s='hello how are you'
x=s.find('o')
print(x)

s='hello how are you'
x=s.find('how')
print(x)

s='hello how are you'
x=s.find('K')
print(x)

s='hello how are you'
x=s.find('o',5)
print(x)

s='hello how areyou'
x=s.find('o',5,7)
print(x)

print('----------------------------------------------------------------')

# rfind(sub,start,end)
s='hello how are you'
x=s.rfind('o')
print(x)

s='hello how are you'
x=s.rfind('o',0,15)
print(x)

s='hello how are you'
x=s.rfind('kite')
print(x)

print('----------------------------------------------------------------')

# rindex(sub,start,end)
s='hello how are you'
x=s.rindex('o')
print(x)

s='hello how are you'
x=s.rindex('o',0,15)
print(x)

print('----------------------------------------------------------------')

# count(sub,start,end)
s='hello how are you'
x=s.count('o')
print(x)

s='hello how are you'
x=s.count('me')
print(x)

print('----------------------------------------------------------------')

# index(sub,start,end)
s='hello how are you'
x=s.index('o')
print(x)

s='hello how are you'
x=s.index('how')
print(x)

s='hello how are you'
x=s.index('k')
print(x)


