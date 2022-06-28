import random
def guess():
    random_number = random.randint(1,100)
    guess = 0
    total = 0
    while guess != random_number:
        total += 1
        guess = int(input("Pick a number between 1 and 99: "))
        if guess > random_number:
            print("Too High: Try again")
        elif guess < random_number:
            print("Too Low: Try again")
    
        else:
            print("Correct !!!!!!! Way to go")
            print(f"\nIt took you {total} tries to figure it out!!!!")
            break
    
