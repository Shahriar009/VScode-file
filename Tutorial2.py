
'''

subjects=["C","C++","Java","JS","Python"]
print(subjects[2])
print(subjects[0:4])
subjects.append("HTML")
print(subjects)
subjects.insert(2,"OS")
print(subjects)
subjects.remove("Java")

print(subjects)
subjects.reverse()
print(subjects)
subjects.pop()
print(subjects)
subjects.pop()
print(subjects)
subjects.pos()
print(subjects)
print("JS"  in subjects)

course='Python for beginer'

print(course.upper())
print(course.lower())
print(course.find('r'))
print(course.replace('for','2'))

temperature=9
if temperature > 30:
    print("The day is hot")
    print("drink cold water")
elif temperature > 20:
    print("The day is nor,mal")
elif temperature > 10:
    print("the dai bit cold")
else:
    print("Tha day is cold")
print("Done")


weight=int(input("Weight:"))
unit=input("(K)g or (L)bs:")
if unit.upper()=="k":
    converted = weight / 0.45
    print("Weight in Lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs:" + str(converted))
'''
'''
numbers=(1,2,3,4,5)
numbers.index(3)
print(numbers)
print(len(numbers))
print(10 in numbers)

numbers=[1,2,3,4,5,6]
for item in numbers:
    print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i=i+1
numbers=range(8,14,2)
for number in range(8):
    print(number)
    '''
numbers=(1,2,3,4,5)
numbers.count()