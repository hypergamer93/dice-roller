import random
amount = 1
dice = 4
choice = ""
mode = 0 #1 = add|2 = flat rolls|3 = stats
total = 0


def diceRoller(amount, dice, total, mode):
    try:
        choice = str(input("Would you like to 'add' your rolls(1), keep the 'flat' rolls(2), or roll 'stats'(3) :").lower())
    except ValueError:
        print("That is not an option")
    else:
        if choice == "add" or choice == "1":
            mode = 1
        elif choice == "flat" or choice == "2":
            mode = 2
        elif choice == "stats" or choice == "3":
            mode = 3
        if mode == 1 or mode == 2:
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
                if mode == 1:
                    while amount != 0:
                        roll = random.randint(1, dice)
                        total += roll
                        amount -= 1
                    print("The total of the dice was",total)
                elif mode == 2:
                    while amount != 0:
                        roll = random.randint(1, dice)
                        print("The dice rolled",roll)
                        amount -= 1                        
        elif mode == 3:
            amount = 4
            dice = 6
            lowNum = 6
            while amount != 0:
                roll = random.randint(1, dice)
                if roll < lowNum:
                    lowNum = roll
                total += roll
                print(roll)
                amount -= 1
            total -= lowNum
            print("Your stat number is", total)
        else:
            print("That is not an option")

while True:
    diceRoller(amount, dice, total, mode)
