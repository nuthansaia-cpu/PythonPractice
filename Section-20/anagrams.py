S1 = 'snooze alarms'
S2 = "alas, no more Z's"

S1 = S1.lower()
S2 = S2.lower()

for x in S1:
    if x.isalpha():
        if S1.count(x) != S2.count(x):
            print('not anagrams')
            break
else:
    print('Anagrams')