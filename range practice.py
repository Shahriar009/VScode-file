
'''numbers=list(range(10))
print(numbers)
numbers= list(range(3,8))
print(numbers)
print(range(20)==range(0,20))
nums = list(range(5, 8))
print(len(nums))
numbers=list(range(5,20,2))
print((numbers))
'''
n = int(input())
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)