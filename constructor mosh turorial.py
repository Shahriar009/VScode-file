'''
class point:
    def __init__(self,x,y,z,a,b):
        self.x=x
        self.y=y
        self.z=z
        self.y=y
        self.a=a
        self.b=b
    def move(self):
        print("Please stay away from here danger here")
    def read(self):
        print("If you are available please sit here")
#that is the code of constructor
point=point(10,20,9990,7878,909)
#alos can chng the valu of object by "point.x=20"
print(point.x)

print(point.y)
print(point.z)
print(point.a)
point.move()
print(point.b)
point.read()
#That is the code of classes

point3.stop="Jony"
point3.read()
print(point3.stop)
point1=point()
point1.u="Hi that is mine"
point1.move()
print(point1.u)
'''

'''
class person:
     def __init__(self,name,name2):
         self.name=name
         self.name2=name2
   '''      '''
     def name(self):
         print(int(input(f'what is the name:')))
'''
'''
         '''
'''
     def talk(self):
         print(f"Hi, i am {self.name}")
     def talk1(self):
         print(f"Hellooo my self {self.name2}")


nnn=person("Nobel","Siyam")

nnn.talk()
nnn.talk1()
Nobel=person("Tasin","Siyam")
Nobel.talk()
nnn.t="We r the booommmmm🦁🦁🐯🐯"

print(nnn.t)
'''

#inheritance

class mammal:
    def walk(self):
        print("walk")

class Dog(mammal):
    def bark(self):
        print("Barking")




class Cat(mammal):
    def meomeo(self):
        print("Hommie animal0")




dog1=Dog()
dog1.walk()
dog1.w="That animal walk using its 4 legs"
print(dog1.w)
cat=Cat()
cat.meomeo()
cat.c="Lovelyyy cattttttii"
print(cat.c)
