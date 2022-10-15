#import choice from random module
from random import choice

while True:

    #computer input
    pick=['R','P','S']
    computer_input=choice(pick)

    #user input
    user_input=input('Chose your move([R]OCK/[P]APER/[S]CISSOR):')

    #all possibilities
    if computer_input=='R' and user_input=='R':
        print("It's a draw. computer chose rock")

    elif computer_input=='P' and user_input=='P':
        print("It's a draw. computer chose paper")

    elif computer_input=='S' and user_input=='S':
        print("It's a draw. computer chose scissors")

    elif computer_input=='R' and user_input=='S':
        print("You loose. computer chose rock")

    elif computer_input=='P' and user_input=='R':
        print("You loose. computer chose paper")

    elif computer_input=='S' and user_input=='P':
        print("You loose. computer chose scissors")

    elif computer_input=='R' and user_input=='P':
        print("You won the game. computer chose rock")

    elif computer_input=='P' and user_input=='S':
        print("You won the game. computer chose paper")

    elif computer_input=='S' and user_input=='R':
        print("You won the game. computer chose scissors")
    #if the input is invalid
    else:
        print("Give a valid input")
    option=int(input("Enter 0 if you want to play again:"))
    if (option):
        break