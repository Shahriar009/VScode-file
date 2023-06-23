# Banking System

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
        
Nobel_update = Bank("Nobel",25,"Male","01861.....")
Nobel_update.view_balance()
Nobel_update.withdraw(234422)
Bank_update=User("Shahriar",24,"Male","01861.....")
Bank_update.show_details()
'''
OUTPUT......


Secret Information.......................
..........................................
Name Nobel
Age 25
Gender Male
Phone 01861.....
Present Account Balance:$ 632563
Your Account Update fund now:$ 398141
Secret Information.......................
..........................................
Name Shahriar
Age 24
Gender Male
Phone 01861.....
'''