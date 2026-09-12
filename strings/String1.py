'''4. Count a particular character without knowing its value beforehand'''
word = "programming"
already_counted = []
repeat = 0
for i in range(len(word)):
    if word[i] not in already_counted:
        already_counted.append(word[i])
        for j in range(len(word)):
            if word[i] == word[j]:
                repeat += 1
        print(word[i], "was repeated", repeat, "times")
        repeat = 0


'''5. Find the first non-repeated character'''
word = "programming"
repeat = 0
for i in range(len(word)):
    repeat = 0
    for j in range(len(word)):
        if word[i] == word[j]:
            repeat += 1
    if repeat == 1:
        print("First non-repeated character:", word[i])
        break


'''6. Find the first repeated character10. Find the first repeated character'''
word = "programming"
repeat = 0
for i in range(len(word)):
    repeat = 0
    for j in range(len(word)):
        if word[i] == word[j]:
            repeat += 1
    if repeat > 1:
        print("First repeated character:", word[i])
        break