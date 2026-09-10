'''1. Square only even numbers'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square=[numbers[x]**2 for x in range(len(numbers)) if numbers[x]%2==0]
print(square)


'''2. Extract numbers greater than 50'''
numbers = [23, 67, 12, 89, 45, 72, 34, 91]
Extract=[numbers[x] for x in range(len(numbers)) if numbers[x]>50]
print(Extract)


'''3. Convert negative numbers to positive'''
numbers = [-5, 3, -8, 10, -2, 7, -9]
positive=[numbers[x]*(-1) if numbers[x] < 0 else numbers[x] for x in range(len(numbers)) ]
print(positive)


'''4. Replace negative numbers with 0'''
numbers = [10, -5, 7, -2, 8, -9, 4]
negative=[0 if numbers[x] < 0 else numbers[x] for x in range(len(numbers)) ]
print(negative)

