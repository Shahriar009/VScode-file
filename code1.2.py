"""

i=1

while i <= 30:
   if i == 22:
     break
     print(i)
     i=i+1
print("End")

subjects=["c","c++","Python","Java","OOP"]
print( "Python" in subjects)

num=list(range(10))
print(num)
print(num[2])
num=list(range(5,11))
print(num)
num=list(range(2,104,2))
print(num)

num=list(range(11))
print(num)
print(num[2])
num=list(range(2,101,2))
print(num)
num=list(range(6,11))
print(num)



n=9

for i in range(1+n):
 print("*"*(2*i-1))
from random import randint
for x in range(1,8):
    guessNumber=int(input("Enter your guess between 1 to 5:"))
    randomNumber=randint(1,5)
    if guessNumber==randomNumber:
        print("You have wom")
    else:
        print("You have lost")
        print("Random number was:",randomNumber)
    """
