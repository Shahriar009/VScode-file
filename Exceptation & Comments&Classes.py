
'''
try:
    #kaksjdkjalc
    age=int(input("Age:"))
    income=200000
    risk=income/age
    print(f'His age is =',age)
except ValueError:
    print("That is not accept value")
except ZeroDivisionError:
    print("Can't divide by Z:")
    print("<,,,,")
'''

class point:
    def move(self):
        print("move")
    def hey(self):
        print("draw")


point1=point()
point1.x=88
point1.z=102011
print(point1.z)
point1.hey()
point2=point()
point2.y=71891991
point2.xxx=980989
print(point2.y)
point2.move()

