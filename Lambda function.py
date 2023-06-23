
'''
def calculate(a,b):
    return a*a+2*a*b+b*b


print(calculate(2,2))

a=(lambda a,b: a*a + 3*a*b + b*b)(2,3)

print(a)
'''
a=(lambda x:x*x*x*2)(2)
print(a)