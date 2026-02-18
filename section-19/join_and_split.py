# replace(old,new,count)
s1 = "a-b-c-d-e"
s2 = s1.replace("-", ",")
print(s2)

s2 = s1.replace("-", ",", 3)
print(s2)

s2 = s1.replace("m", "m")
print(s2) 

s1 = "abc@gmail.com"
s2 = s1.replace("gmail", "yahoo")
print(s2)

print('----------------------------------------------------------')

# join(iterable)
s1 = "xyz"
s2 = "abc"
s3 = s1.join(s2)
print(s3) 

s1 = "/"
s2 = 'abc'
s3 = s1.join(s2)
print(s3) 

print('----------------------------------------------------------')

# split(sep,maxsplit)
s1 = "John Smith Ajay"
s2 = s1.split()
print(s2)

s2 = s1.split("h")
print(s2) 

s1 = "John,Smith,Ajay"
s2 = s1.split(",")
print(s1) 

s1 = "John-Smith-Ajay-Khan-James"
s2 = s1.split()
print(s2) 

s1 = "John-Smith-Ajay-Khan-James"
s2 = s1.split("-")
print(s2) 

s1 = "John-Smith-Ajay-Khan-James"
s2 = s1.split("-", 3)
print(s2) 

print('----------------------------------------------------------')

# rsplit(sep,maxsplit)
s1 = "John-Smith-Ajay-Khan-James"
s2 = s1.rsplit("-", 4)
print(s2)

print('----------------------------------------------------------')

# splitlines(keepends)
s1 = "Line 1\nLine 2\nLine 3"
s2 = s1.splitlines()
print(s2)
