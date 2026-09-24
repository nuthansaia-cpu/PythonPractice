'''1. Create a tuple and print all elements'''
numbers = (10, 20, 30, 40, 50)
for i in range(len(numbers)):
    print(numbers[i])


'''2. Find the largest element in a tuple'''
numbers = (10, 25, 7, 45, 32, 18)
largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
print("Largest:", largest)


'''3. Find the smallest element in a tuple'''
numbers = (10, 25, 7, 45, 32, 18)
smallest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
print("Smallest:", smallest)


'''4. Count how many times an element occurs'''
numbers = (1, 2, 2, 3, 2, 4, 2, 5)
already_counted = []
repeat = 0
for i in range(len(numbers)):
    if numbers[i] not in already_counted:
        already_counted.append(numbers[i])
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                repeat += 1
        print(numbers[i], "was repeated", repeat, "times")
        repeat = 0