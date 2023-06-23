#Encapsulation with public,private and protected data
class Player:
    def __init__(self,name,budget,team):
        #public data
        self.name=name
        #private data
        self.__budget=budget
        #protected data
        self._team=team

    # for display player's details
    def show(self):
        print("Name:",self.name,'Budget:$',self.__budget)

        #method
    def play(self):
        print(self.name,'is playing in',self._team)

#Object creating of a class
player_name=Player("CR7",200000,"Al Nasar")
player_name.show()
player_name.play()
player_name.name="KAKA"

#calling public method of a class
player_name.show()
player_name.play()