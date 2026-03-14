arr=[-1,35,36,37,40,38,39,40,-2]

firstMax = secondMax = float('-inf')

for i in range(len(arr)):
    y = arr[i]

    if y > firstMax:
        secondMax = firstMax
        firstMax = y
    elif firstMax > y > secondMax:
        secondMax = y
    print('first=',firstMax,'second=',secondMax,'y=',y)	

print(secondMax)