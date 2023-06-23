
'''
def add(*numbers):
    sum=0
    for num in numbers:
         sum=sum+num
    print(sum)

add(29,1)
add(31,1,3)


def student(*details):
    print(details[1])

student(101,"Nobel")
student(9,"XXXX",3.79)


def add (*numbers):
    sum= 0
    for num in numbers:
        sum=sum+num
    print(sum)

add(2,3,2)
add(8,9,3,4)
'''

def student(**details):
    print(details["id"])



student(id=9,name="Nobel")












