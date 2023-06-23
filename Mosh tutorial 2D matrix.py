


'''
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
for row in  matrix:
    for range in row:
        print(range)

matrix[2][2]=12
print(matrix)
print(matrix[2][1])
'''
subjects=['CSC','EEE','ICE','SWE','NFE','hhh']
'''

subjects.index('ICE')

numbers1=subjects.copy()
print(subjects.count('ICE'))
print('NNN' in subjects)
print(numbers1)
'''
'''
numbers=[1,2,3,1,4,5,6,9,6,4,2]
numbers=list(dict.fromkeys(numbers))
print(numbers)
'''
numbers=[1,2,3,1,4,5,6,9,6,4,2]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
