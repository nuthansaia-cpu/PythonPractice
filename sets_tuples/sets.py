'''1. Remove duplicate elements from a list using a set'''
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
numbers_set = set()
for i in range(len(numbers)):
    if numbers[i] not in numbers_set:
        numbers_set.add(numbers[i])
print(numbers_set)


'''2. Find common elements between two sets'''
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
common = set()
for x in a:
    if x in b:
        common.add(x)
print(common)


'''3. Find elements present in first set but not second set'''
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
result = set()
for i in a:
    if i not in b:
        result.add(i)
print(result)


'''4. Find elements present in either set but not both'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = set()
for i in a:
    if i not in b:
        result.add(i)
for i in b:
    if i not in a:
        result.add(i)

print(result)