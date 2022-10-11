from random import choice
while True:
    dice_numbers=['1','2','3','4','5','6']
    computer_output=choice(dice_numbers)
    print("Dice rolled",computer_output)
    option=int(input("Enter 0 if you want to play again:"))
    if (option):
        break