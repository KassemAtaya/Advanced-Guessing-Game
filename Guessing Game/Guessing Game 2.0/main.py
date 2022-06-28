#2.0 Has dificuly level feature which allows the user set the difficuly of the program.
#2.0 Has the ability to play again once done playing

import random

def guess(x):
    x = 10**x
    random_number = random.randint(1,x)
    guess = 0
    total = 0
    while guess != random_number:
        total += 1
        guess = int(input(f"Pick a number between 1 and {x}: "))
        if guess > random_number:
            print("Too High: Try again")
        elif guess < random_number:
            print("Too Low: Try again")
    
        else:
            print("Correct !!!!!!! Way to go")
            print(f"\nIt took you {total} tries to figure it out!!!!")
            print("\nWould you like to play again? Yes = y || No = n")
            replay = input()
            if replay == "n":
                print("Thank You for Playing!!!!!")
                break
            if replay == "y":
                difficulty()
            


def difficulty():
    print("Lets play the guessing game!!!!\n")
    print("Please pick desired difficulty")
    print("------------------------------")
    print("Easy         = 1 1-->10")
    print("Intermediate = 2 1-->100")
    print("Hard         = 3 1-->1000")
    print("Supreme      = 4 1-->10000")
    difficulty = int(input())
    guess(difficulty)
    
