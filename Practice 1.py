if 5 > 2:
  print("Five is greater than two!")

if 5>2:
    print("F is greater than 2")

a=2323
b="That is python practice file"

print(a)
print(b)

#Comment

'''
Hi my self Shahriar Rahman
And i love python
'''
#Python variables

name="Shahriar Rahman"
age=23
print(name)
print(age)
#Global scope
def myfunc():
    global x
    x="fantastic"
    print(x)

#Data type

q=11
a="Shahriar"
f=11.1

x=["CSS","HTML","Python"]
y=("CSS","HTML","Python")
z={"CSS","HTML","Python"}
d={"Python":11,
   "C++":22}
b=True
print(type(q))
print(type(a))
print(type(f))
print(type(x))
print(type(y))
print(type(z))
print(type(d))
print(type(b))

#python number

n=23
n=float(n)
print(n)
n=bool(n)
print(n)
m=2.6
m=int(m)
print(m)
w=2
w=complex(w)
print(w)

#Python String

l="Nobel"
print(len(l))
print(l[0])
print(l[3])
print(l[2:4])
#remove whitespace
j=" nobel sss "
print(j.strip())
print(j.upper())
print(j.lower())
#Replacing character
print(j.replace("n","s"))
#Add placeholder
age = 36
txt = "My name is Nobel,and I am {}"
print(txt.format(age))

#Boolean
print(10>9)
print(9==2)
print(bool("xyz"))
print(bool(0))

#Python
p=3
y=2
print(p*y)

print(p/y)

#remainder
x=5
x%=3
print(x)
#quatient
x=5
x//=3
print(x)
x&=3
print(x)

x=5
x**=3
print(x)

#single multiple
x=5
x*=3
print(x)

#substract
x=6
x-=2
print(x)
x=8
x+=2
print(x)
x=10
x/=2
print(x)
x=5
x>>=2
print(x)

x=8
y=2
e=x%y
print(e)

x=5
y=3
d=x//y
print(d)
x=5
x<<=2
print(x)

print((2*2)-(3*3))
print(9-4+2)

print(9%4)


#list

subject=["CSE","EEE","ICE","SWE","CSE"]
print(subject)
print(subject[1])
print(subject[2])
print(subject[4])
print(subject[1])
print(len(subject))

list=["SSS",77,True,"False"]

print(list)
print(type(list))
subject2=["CSE","EEE","ICE","SWE","CSE"]
print(type(subject2))

subject=("CSE","EEE","ICE","SWE","CSE")
print(type(subject))

'''
makelist=list(("CSE","EEE","ICE","SWE","CSE"))
print(makelist)
'''


#Access list iteam

list2=["CSE","EEE","ICE","SWE","CSE"]
print(list2[2:4])
print(list2[-1])
print(list2[2:4])
print(list2[-1:])
print(list2[:-1])
list2=["CSE","EEE","ICE","SWE","CSE"]
if "ICE" in list2:
    print("Yes, vvi")
else:
    print("NOOO")

list2=["CSE","EEE","ICE","SWE","CSE"]
if "BBA" in list2:
    print("Yes, vvi")
else:
    print("NOOO")

#Changing list iteam

list2=["CSE","EEE","ICE","SWE","CSE"]
list2[0]="BBA"
print(list2)
list2[3]="ETE"
print(list2)
print(list2[1:])
list2=["CSE","EEE","ICE","SWE","CSE"]
if "EE" in list2:
    print("My dep. is it")

else:
    print("NO")

cgpa=3.5
string="Shahriar Rahman, his cgpa is {}"
print(string.format(cgpa))

# Replaceing

list2=["CSE","EEE","ICE","SWE","CSE"]
list2[1]="BBA"
print(list2)
list2[0:4]=["AAA","BBB","CCC","DDD"]
print(list2)

list2.insert(2,"AAA")
print(list2)

#Add iteam

fruits=["apple","banana","orange"]
vegetable=["potato","begen","tomato"]

fruits.append("Chery")
print(fruits)
fruits.extend(vegetable)
print(fruits)
fruits.remove("banana")
print(fruits)
fruits1=["apple","banana","orange","watermalon"]
fruits1.pop(3)
fruits1.pop()
fruits1.clear()
print(fruits1)
fruits2=["apple","banana","orange","watermalon","Chery"]
for i in range(len(fruits2)):
    print(fruits2[i])

fruits1=["apple","banana","orange","watermalon"]
i=0
while i < len(fruits1):
    print(fruits1[i])
    i=i+1

fruits2=["apple","banana","orange","watermalon","Chery"]
fruits2.sort()
print(fruits2)
fruits1=fruits2.copy()
print(fruits1)
fruits2=["apple","banana","orange","watermalon","Chery"]
fruits1=["apple","banana","orange","watermalon"]
fruits3=fruits1+fruits2
print(fruits3)