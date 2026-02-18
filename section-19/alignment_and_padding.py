# Alignment and padding methods
# ljust(width,fillchar)
s = 'Hello'
x = s. ljust (7, "*")
print(x)

print('-------------------------------------------------------------')

# rjust(width,fillchar)
x = s.rjust(7)
print(x)

x = s.rjust(7, '-')
print(x)

print('-------------------------------------------------------------')

# center(width,fillchar)
x = s.center(7)
print(x) 

x = s. center (7, '*')
print(x)

print('-------------------------------------------------------------')

# zfill(width,fillchar)
x = s.zfill(7)
print(x)

print('-------------------------------------------------------------')

# string method
#lstrip(chars)
s ='  Hello'
x = s.lstrip()
print(x)

s = '$$Hello'
x = s.lstrip('$')
print(x)

print('-------------------------------------------------------------')

# rstrip(chars)
s = 'Hello!!'
x = s.rstrip('!')
print(x)

print('-------------------------------------------------------------')

# strip(chars)
s = '#Hello#'
x = s.strip('#')
print(x)

s = '#!Hello  $ *'
x =s.strip('#! $*' )
print(x)