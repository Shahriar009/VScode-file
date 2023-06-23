
'''base=float(input("enter the base="))
height=float(input("Enter height="))

area=0.5* base* height
print(area)

num1=input(int(The first number is:))

print(10+2)
print(10/2)
print(10%2)
print(4**2)

name=input("Enter your name:")
age=input("Enter your age:")
CGPA=input("Enter your CGPA:")


print("Student Information")
print("---------------------------")
print("Name : "+name)
print("Age  :  "+age)
print("GPA  : "+CGPAsss


num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))

result=int(num1) - int(num2)
print("The result is",result)

base=float(input("enter the base="))
height=float(input("Enter height="))

area=.5* base* height
print(area)


from math import*
print(max(20,12))
print(abs(-4))

print(pow(2,2))
print(sqrt(25))
print(round(3.9))
print(floor(3.9))
print(ceil(3.2))


num1= 33
num2=44

print(f"{num1}+{num2 } = {num1+num2}")
print("Shahriar Rahman.",end="")
print("0923902382389")

print(90!=20)



m

num=66
if num%2 == 0:
    print("Even")

else:
    print("odd")




mark=50

if mark >=80:
    print("A")

elif mark>=70:
    print("Good")

else :
    print("Fail")





num1=33
num2=54

print(num1 if num1>num2 else num2)


ch='s'

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vowel")

else:
    print("Consonant")


mark=99

if mark>=80 and mark<=100:
    print("A+")

elif mark>=70 and mark<=79:
    print("A")

else:
    print("B")

marks=77
if 80<=marks <=100:
    print("A+")
else:
    print("Fail")

i=3
while i<=100:
    print(i)
    i=i+3
print("program end")



num=29.9
print(type(num))



num1=33
num2=55
print("sum is",num1+num2)



num1=2
num2=3
num3=4

if num1>num2:
    if numm1>num3:
        print(num1)

    else:
        print(num3)

else:
    if num2>num3:
        print(num2)
    else:
        print(num3)


n=int(input("Enter tje last number:"))
sum=0
i=5
while i <= n :
    sum=sum+i
    i=i+5
print(sum)



i=0
while i<=300:
    print(i)
    i=i+3
    if i==30:
        break
print("Stop")


i=1
while i<=100:
    print(i)
    i = i + 1
    if i == 30:
     break





subjects=["c","C++","Python","Java","OS"]

print(subjects)
print(subjects[0])
print(subjects[2])
print(subjects[-4])
print(subjects[2:])
print(subjects[-1])
print("Javas" in  subjects)
print("Python" in subjects)
print(subjects+["JS,2"])
print(subjects*2)
print(len(subjects)

subjects=["c","C++","Python","Java","OS"]

subjects.append("JS")
print(subjects)
subjects.insert(4,"opp")
print(subjects)
subjects.remove("C++")
print(subjects)
subjects.sort()
print(subjects)
subjects.pop()
print(subjects)


subjects2=subjects.copy()
print(subjects2)
pos = subjects.index("Java")
print(pos)
pos=subjects.count("c")
print(pos)


num=list(range(20))
print(num)
print(num[19])
num=list(range(5,18,2))
print(num)

'''

num=[11,22,44,556,677,]

'''print(num)
index=0
n=len(num)
while index<n:
    print(num[index])
    index=index+1

sum=0

for x in num:
    sum=sum+x
    print(sum)







num=list(range(10))
print(num)
print(num[2])
num=list(range(11,33,3))
print(num)



num=[10,20,40,50,60]
print(num)
index=0
while index<5:
     print(num[index])
     index=index+1



num=[10,20,30,40,50]
sum=0
for x in num:
     sum=sum+x
print(sum)


n=int(input("Enter the last number:"))
sum=0
for x in range(1,n+1,1):
 sum=sum+x
print(sum)




n=int(input("Enter the final value:"))

sum=1

for x in range(1,n+1,1):
     sum=sum*x
print(sum)




n=5
for i in range(n+1):
     print((2*i-1)*"*")


n=3
for i in range(n+1):
     print(i*"n")




from random import randint



guessnumber=int(input("Enter your guess between1 to 5:"))
randomNumber=randint(1,5)

if guessnumber==randomNumber:
          print("You have won")

else:
          print("You have lost")
print("Random number was:",randomNumber)



from random import randint



guessnumber=int(input("Enter your guess between1 to 5:"))
randomNumber=randint(1,5)

if guessnumber==randomNumber:
          print("You have won")

else:
          print("You have lost")
print("Random number was:",randomNumber)





n=input("Enter a text of number:")
# 10 20 30 40
list=n.split() # 10,20,30,40
sum=0

for num in list:
    sum = sum+ int (num)

print(sum)






numofWords=0
numofLetters=0
numofDigits=0
text= input("Enter a text of numbers:")

for x in text:
    x=x.lower()
    if x>='a ' and x<='z':
        numofLetters=numofLetters+1
    elif x>='0' and x<='9':
        numofDigits=numofDigits+1
    elif x>='':
        numofWords==numofWords+1
print("Nmber of latters:",numofLetters)
print("NUmber of Digits:",numofDigits)
print("Number of word:",numofWords+1)






matrix=[
    [1,2,9],
    [5,6,7],
]

matrix[1][0]
print(matrix[1][0])

for row in matrix:
    for col in row:
        print(col)


studentId = {

    101:"aaaaaaa",
    102:"hjaha",
    102:"jsuwuiwui",


}
print(studentId.get(109,"Not a valid "))




students= (

    "AAAAAAA",
    "VVVVVVVV",
    "JYUGUYGUYHJ",


)
print(students[2])
'''
num1={1,2,3,4,5,6,7}
num2={6,7,8,9}


print(num1 | num2)
print(num1 & num2)
print(num1 - num2)