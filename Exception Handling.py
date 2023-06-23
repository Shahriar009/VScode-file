
'''

try:
    list=[20,0,30]
    result= list[0] / list[0]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally:

    print("Successful")

try:
    num1=int(input("Enter the first value:"))
    num2=int(input("Enter the second value:"))
    result=num1/num2
    print(result)

except (ValueError,ZeroDivisionError):
      print("you have entered incorrect input.")

finally:

    print("Thanks!!")


def voter (age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"
try:
    print(voter(22))
    print(voter(17))
except ValueError as error:
    print(Error)
'''
def voter (age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "jkkkkk for vote0"
try:
    print(voter(22))
    print(voter(55))

except ValueError as error:
    print(error)