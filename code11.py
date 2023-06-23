num1=88
num2=668
num3=99
'''
print(num1 if num1>num2 else num2)
'''
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)