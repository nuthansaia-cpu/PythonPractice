# Summation Logic.
n=5
i=0
sum=0
while i<n:
     i=i+1
     sum+=i
print(sum)

print('--------------------------------------------------------')

# Sum of 'N' numbers.
n=int(input('Number of Elements:'))
i=0
sum=0
print('Enters',n,'Numbers:')
while i<n:
     i=i+1
     x=int(input())
     sum+=x
print('Sum:',sum)
