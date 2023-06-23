
'''

def my_func():
   print("             spam")
   print("     spam")
   print("                      spam")
my_func()

def print_with_exclamation(word):
    print(word+"!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
def print_double(x):
   print(2 * x)

print_double(3)

def print_sum_twice(x,y):
    print(x+y)
    print(x+y)
print_sum_twice(4,8)

def function(variable):
    variable += 1
    print(variable)
function(1)

def print_numbers():
  print(1)
  print(2)
  return
  print(5)
  print(6)


import random
for i in range(5):
    value=random.randint(1,6)
    print(value)

import math
num = 10
print (math.sqrt(num))

import math as m
print(math.sqrt(25))
'''
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))