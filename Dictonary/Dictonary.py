'''1. Largest value'''
marks={"A":78,"B":92,"C":65,"D":88}
largest=0
student=""
for i in marks:
    if marks[i]>largest:
        largest=marks[i]
        student=i
print(student,largest)


'''2. Average'''
marks={"A":80,"B":70,"C":90,"D":60}
total=0
count=0
for i in marks:
    total=total+marks[i]
    count=count+1
print("Average:",total/count)


'''3. Duplicate values'''
numbers={"a":10,"b":20,"c":10,"d":30,"e":20}
values=[]
for i in numbers:
    if numbers[i] in values:
        print(numbers[i])
    else:
        values.append(numbers[i])


'''4. Key with highest value'''
marks={"Rahul":78,"Amit":92,"Raj":65,"Arun":88}
highest=0
student=""
for i in marks:
    if marks[i]>highest:
        highest=marks[i]
        student=i
print(student)