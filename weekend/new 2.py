s=input('Enter a name:')
v='aeiou'
n=0
x=len(s)
count=0
while n<x:
    if s[n] in v:
        print('present')
        count+=1
    n=n+1
print(count)