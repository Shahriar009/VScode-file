def smart_multiplication(func):
    def inner(a,b):
        print("This method for multipy ",a ,"and",b)
        if b == 0:
            print("Sorry!  error")
            return
        return func(a,b)
    return inner
@smart_multiplication
def multiplication(a,b):
    print(a*b)

multiplication(2,4)
multiplication(5,0)
multiplication(0,9)
multiplication(9,1)
multiplication(10,0)