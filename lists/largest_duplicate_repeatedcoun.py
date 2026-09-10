'''largest element'''
numbers = [10, 25, 7, 45, 32, 45, 18]
largest=0
largest2=0
for i in range(1,len(numbers)):
  if numbers[i] > largest:
    largest=numbers[i]
  if numbers[i] > largest2 and numbers[i] < largest:
    largest2=numbers[i]

print('First largest number in the list',largest)
print('Second largest number in the list',largest2)
    


'''Remove duplicates'''
numbers = [10, 25, 7, 45, 32, 45, 18]
largest=0
for i in range(1,len(numbers)):
  if numbers[i] > largest:
    largest=numbers[i]
print(largest)


'''Count frequency of elements'''
numbers = [1, 2, 2, 3, 1, 4, 2, 3, 5]
already_counted=[]
repeat=0
for i in range(len(numbers)):
  if numbers[i] not in already_counted:
    already_counted.append(numbers[i])
    for n in range(len(numbers)):
        if numbers[i]==numbers[n]:
          repeat+=1
    print(numbers[i],'was repeated',repeat,'time')
    repeat=0
    

