'''
print(1==1)
print(2>=3)
print(2*2)
print("hello"=="hello")
print(8>9)
a=int(input("Enter the first number:"))

b=int(input("Enter the second number:"))

sum=a+b

print("The sum of given numbers is",sum)
print(False==False or True)
print(False==(False or True))
print((False==False)or True)

words=["Hello", "World" ,"Whats" ,"up"]
print(words[0])
print(words[2])
empty_list=[]
print(empty_list)


things=["string",1,[0,1,2],4.87]
print(things[2][2])

m=[
    [1,2,3,4],
    [5,6,7,8]
  ]
print(m[1][2])
words=["Hello", "World" ,"Whats" ,"up"]
print("up" in words)

nums=["C++","Python","C","java"]
nums.append("Html")
print(nums[1])
print(len(nums))
nums.insert(2,11)
print(nums)

letters=['a','n','o','p','l']
print(letters.index('o'))


i=3
while i>=0:
    print(i)
    i=i-1
print("Finished program")

x=1
while x< 10:
    if x%2==0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1



x= 0
while x <=20 :
    print(str(x) + " is 2s multipiler")
    if x>=16:
        print("End Here")
        break

    x+=2
i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break



i = 0
while i<5:
  i += 1
  if i == 3:
      print("continue")
      continue
  print(i)


words=["hi","hello","bye","loo"]
for word in words:
    print(word + "!")

list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break
'''
n = int(input())
for x in range(1, n , 2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

