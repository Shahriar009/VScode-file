
from random import randint

for x in range(1,7):

     guessnumber=int(input("Enter your guess between1 to 5:"))
     randomNumber=randint(1,5)

    if guessnumber==randomNumber:
          print("You have won")

    else:
          print("You have lost")
          print("Random number was:",randomNumber)

