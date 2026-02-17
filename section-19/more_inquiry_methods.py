# isdigit()
s = '7\u20823\u2075'  
print(s)         
print(s.isdigit())    

s2 = '7235'
print(s2.isdigit()) 

s2 = '71.23'
print(s2.isdigit())   

print('----------------------------------------------------------')

# isdecimal()
s3 = '\u0969\u096A\u096B'   
print(s3)                   
print(s3.isdecimal())       

print('----------------------------------------------------------')

# isnumeric()
s4 = '\u00BE\u215E' 
print(s4) 
print(s4.isnumeric()) 

print('----------------------------------------------------------')

# isascii()
s5 = 'Hello123'
print(s5.isascii())  

s6 = 'नमस्ते123'  
print(s6.isascii())   

print('----------------------------------------------------------')

# isalnum()
s7 = 'abc123'
print(s7.isalnum()) 

s8 = 'abc123!'
print(s8.isalnum())    
