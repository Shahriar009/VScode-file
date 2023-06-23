#Class and object

class Calculator:
    def __init__(self,first_num, secnd_num):
        self.first_num=first_num
        self.secnd_num=secnd_num

    def addition(self):
        print("The addition is:",self.first_num + self.secnd_num)
    def substraction(self):
        print("The substraction is:",self.first_num - self.secnd_num)
    def multiplication(self):
        print("The multiplication is :",self.first_num * self.secnd_num)
x = Calculator(44,2)
x.addition()
x.substraction()
x.multiplication()