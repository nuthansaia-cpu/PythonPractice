s=input('Enter a name:')
v='aeiou'
n=0
x=len(s)
while n<x:
    if s[n] in v:
        print(s[n],'present')
        break
    n=n+1
    
print(ord('z'))