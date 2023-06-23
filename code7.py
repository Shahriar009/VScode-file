#1+2+3+4+...+n
#2+4+6+8+...+n
'''
num=int(input("Enter the last number:"))
sum=0
for x in range(1,num+1,1):
    sum=sum+x
print(sum)

num=int(input("Enter the last number:"))
sum=0
for x in range(1,num-1,2):
    sum=sum+x
print(sum)
'''
num=int(input("Enter the last number:"))
sum=1
for x in range(1,num+1,1):
    sum=sum*x*x
print(sum)