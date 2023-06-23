
'''

birth_year=input('what is your birth year?')
age=int(input('The present year:'))-int(birth_year)
print("The age is " ,+ age)

weight_lbs=input('weight(lbs):')
weight_kg=int(weight_lbs)*0.45
print(weight_kg)
weight_kg=input('weight(kg):')
weight_lbs=float(weight_kg)/0.45
print(weight_lbs)

courses='My starting programing language is Python'

another=courses[:]
print(another)
'''
first='Shahriar'
last='Nobel'
message= first  +' ['   + last + '] is a engineer.'

msg=f'{first} [{last}] is a coder'
print(message)
print(msg)