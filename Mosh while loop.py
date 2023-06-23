
'''

i=3
while i<=10:
    print('*'*i)
    print(i)
    i=i+3

secret_number=10
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess:'))
    guess_count +=1
    if guess==secret_number:
        print('You won')
        break
else:
    print('You are fail')








secret_number=12
guess_count=0
guess_limit=4

while guess_count<guess_limit:
    guess=int(input(f'Guess:'))
    guess_count+=1
    if guess==secret_number:
        print("You Won")
        break


else:
    print("Sorry ! You are fail")

'''

command=""
started=False
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("The car already started")
        else:
            started=True
            print("car  started.")
    elif command=="stop":
        if not started:
            print("car is already  stopped.")
        else:
            started=False
            print("Car is stopped")
    elif command=="help":
        print("""
        Start-To Start the car
        Stop- To stop the car
        quit-to quit
        """)
    elif command=="quit":
        break
    else:
        print("Sorry ! I dont understand")






