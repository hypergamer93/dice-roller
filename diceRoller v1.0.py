import random
amount = 1
dice = 4
choice = ""

def diceRoller(amount, dice):
    try:
        choice = int(input("How many dice would you like to roll? :"))
    except ValueError:
        print("That is not a number")
    else:
        amount = choice
        try:
            choice = int(input("What is the hightst number on the dice you would like to roll? :"))
        except ValueError:
            print("That is not a number")
        else:
            dice = choice
    
    while amount != 0:
        roll = random.randint(1, dice)
        print("The dice rolled",roll)
        amount -= 1

while True:
    diceRoller(amount, dice)
