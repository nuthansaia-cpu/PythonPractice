# isalpha()
s = 'Hello'
x = s.isalpha()
print(x)  

s = 'Hello123'
x = s.isalpha()
print(x)  

print('----------------------------------------------------------')

# islower()
s = 'hello'
x = s.islower()
print(x)  

s = 'Hello'
x = s.islower()
print(x)  

print('----------------------------------------------------------')

# isupper()
s = 'HELLO'
x = s.isupper()
print(x)  

s = 'Hello'
x = s.isupper()
print(x)  

print('----------------------------------------------------------')

# istitle()
s = 'Hello World'
x = s.istitle()
print(x)  

s = 'Hello world'
print(s.istitle())  

print('----------------------------------------------------------')

# isspace()
s1 = '       '   
print(len(s1))        
print(s1.isspace())   

s2 = ''   
print(len(s2))       
print(s2.isspace())  

s3 = '\n\t'   
print(s3.isspace())   

s4 = ' abc '  
print(s4.isspace())  

print('----------------------------------------------------------')

# isprintable()
s = 'Hello World'
print(s.isprintable())  

s = 'Hello\nWorld'
print(s.isprintable())  

print('----------------------------------------------------------')

# isidentifier()
s = 'item1'
print(s.isidentifier())  

s = '1item'
print(s.isidentifier())  

s = 'item_1'
print(s.isidentifier())  

s = 'item-1'
print(s.isidentifier())  
