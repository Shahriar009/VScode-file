# Parent and child class
'''
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("Secret Information.......................")
        print("..........................................")
        print("Name",self.name)
        print("Age",self.age)
        print("Gender",self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=632563163
    def deposite(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account balance has been updated:$",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if amount>self.balance:
            print("Balance is less then your amount & Available Balance is:$",self.balance)
        else:
            self.balance=self.balance - self.amount
            print("Your Account Update fund now:$",self.balance)
    def view_balance(self):
        self.show_details()
        print("Present Account Balance:$",self.balance)

bank = Bank("Nobel",25,"Male")
bank.view_balance()
'''

class User():
    def __init__(self,name,age,gender,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone

    def show_details(self):
        print("Secret Information.......................")
        print("..........................................")
        print("Name",self.name)
        print("Age",self.age)
        print("Gender",self.gender)
        print("Phone",self.phone)

class Bank(User):
    def __init__(self,name,age,gender,phone):
        super().__init__(name,age,gender,phone)
        self.balance=632563
    def deposite(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account balance has been updated:$",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if amount>self.balance:
            print("Balance is less then your amount & Available Balance is:$",self.balance)
        else:
            self.balance=self.balance - self.amount
            print("Your Account Update fund now:$",self.balance)
    def view_balance(self):
        self.show_details()
        print("Present Account Balance:$",self.balance)

Bank_update = Bank("Nobel",25,"Male","01861.....")
Bank_update.view_balance()
Bank_update.withdraw(234422)
User_update=User("Shahriar",24,"Male","01861.....")
User_update.show_details()