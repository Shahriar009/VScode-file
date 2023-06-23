# Get and set in encapsulation for private data method

class Actor:
    def __init__(self,name,rltn_status):
        self.name=name
        self.__rltn_status=rltn_status

        #getter method
    def get__rltn_status(self):
        return self.__rltn_status

    #setter method

    def set__rltn_status(self,rltn_status):
        self.__rltn_status=rltn_status

Actor_n=Actor("TOM Cruse","Married")

# retrieving rltn_status by using getter method

print('Name:',Actor_n.name, '\n'"Rltn_Status:",Actor_n.get__rltn_status())
Actor_n.get__rltn_status()

#by using setter changing rltn_status
Actor_n.set__rltn_status("Single")

# retrieving rltn_status by using getter method

print('Name:',Actor_n.name, '\n'"Rltn_Status:",Actor_n.get__rltn_status())
Actor_n.get__rltn_status()