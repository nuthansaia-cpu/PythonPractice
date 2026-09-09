numbers = [12, 7, 9, 20, 33, 44, 51, 60]
even=[]
odd=[]
for i in range(len(numbers)):   
  if numbers[i]%2==0:
    even.append(numbers[i])
  else:
    odd.append(numbers[i])
print(even)
print(odd)



a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
common=[]
for i in range(len(a)):
  if a[i] in b:
    common.append(a[i])
print(common)