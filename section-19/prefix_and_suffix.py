# startswith(prefix,start,end)
s1 = 'python is very easy'
print(s1.startswith('python'))  
 
print(s1.startswith('is'))       

print(s1.startswith('is', 7))    

print(s1.endswith('easy'))       

print('----------------------------------------------------------')

# endswith(suffix,start,end)
s1 = 'abc@gmail.com'

print(s1.endswith('gmail.com'))  

print(s1.endswith('.com'))       

print(s1.endswith('yahoo.com'))  

print('----------------------------------------------------------')

# removeprefix(prefix)
s1 = 'python programming'
s2 = s1.removeprefix('py')
print(s2)  

s3 = s1.removeprefix('java')
print(s3)  

print('----------------------------------------------------------')

# removesuffix(suffix)
s1 = 'python programming'
s2 = s1.removesuffix('ing')
print(s2)  

print('----------------------------------------------------------')

# partition(sep)
s1 = 'python is easy'
s2 = s1.partition('is')
print(s2)  

print('----------------------------------------------------------')

# rpartition(sep)
s1 = 'python is easy'
s2 = s1.rpartition('s')
print(s2) 