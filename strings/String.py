'''1. Count vowels and consonants'''
word = "programming"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for i in range(len(word)):
    if word[i] in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


'''2. Check whether a string is palindrome'''
word = "madam"
reverse = ""
for i in range(len(word)-1, -1, -1):
    reverse = reverse + word[i]
if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


'''3. Count uppercase and lowercase characters'''
word = "PyThOn"
upper = 0
lower = 0
for i in range(len(word)):
    if word[i] >= 'A' and word[i] <= 'Z':
        upper += 1
    elif word[i] >= 'a' and word[i] <= 'z':
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)