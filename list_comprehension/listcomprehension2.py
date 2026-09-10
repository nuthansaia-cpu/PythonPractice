'''5. Find numbers divisible by both 3 and 5'''
numbers = [10, 15, 20, 30, 45, 50, 60, 75, 82]
divisible=[ numbers[x] for x in range(len(numbers)) if numbers[x]%3==0 and numbers[x]%5==0 ]
print(divisible)


'''6. Extract vowels from a string'''
word = "programming"
vowles="aieou"
vowles_word=[ word[x] for x in range(len(word)) if word[x] in vowles]
print(vowles_word)


'''7. Convert words to uppercase'''
words = ["python", "java", "c", "javascript"]
upper=[ words[x].upper() for x in range(len(words))]
print(upper)


'''8. Get the length of every word'''
words = ["python", "java", "programming", "AI"]
length=[ len(words[x]) for x in range(len(words))]
print(length)