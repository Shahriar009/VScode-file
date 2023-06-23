#relational operators

"""
mark=22
if mark>=30:
    print("pass")
    if mark>=50:
        print("low")
        if mark>60:
            print("good")
else:
    print("Fail")
#conditional
num1=67
num2=88
if num1>num2:
    print("num1")
else:
    print("num2")
    # even odd
    num=8
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        # elif
    marks=66
    if marks>=80:
        print("A+")
    elif marks>=70:
        print("A")
    elif marks>=60:
        print("B")
    elif marks>=50:
        print("C")
    elif marks>=40:
        print("D")
    else:
         print("Fail")
#inner  if
num1=88223
num2=11111
num3=333
if num1>num2:
   if num1>num3:
        print(num1)
   else:
        print("num3")
else:
   if num2>num3:
        print(num2)
   else:
        print(num3)
"""
i=1

while i <= 30:
   if i == 22:
     break
     print(i)
     i = i+1
print("End")