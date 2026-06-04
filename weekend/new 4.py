s=input('Enter a name:')
v='aeiou'
x=ord(s)
z=ord(s)
count=0
countt=0
while x>=97 and x<=122:
    if s[0] in v:
        print(s[0],'is a vowel')
        break
    elif chr(x) in v:    
        break
    else:
        x+=1
        count+=1
while z>=97 and z<=122:
    if chr(z) in v:
        break
    else:
        z-=1
        countt+=1
if count<countt:
    print(chr(x),'is the nearest vowel')
else:
    print(chr(z),'is the nearest vowel')
    
