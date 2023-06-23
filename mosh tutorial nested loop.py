'''
for x in range(f'(*4)'* 4):
    for y in range(3):
        print(f'({x} {y})')

numbers=[5,2,5,2,2]
for x_count in numbers:
    print('x'*x_count)
'''
numbers=[5,2,5,2,2,9]
for y_count in numbers:
    output=''
    for count in range(y_count):
        output+='y'
    print('y'* y_count)