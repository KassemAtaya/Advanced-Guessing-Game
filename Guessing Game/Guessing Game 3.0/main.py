#3.0 Has a time feature that times how long it took you to finish game 
#3.0 Has data base feature which saves your game run results to a text file which creats automatically if it does not exsits.

import random
import time
import sys

def guess(x, name):
    c = 10**x
    random_number = random.randint(1,c) 
    guess = 0
    total = 0
    start = time.time()
    while int(guess) != random_number:
        total += 1
        try:
            guess = int(input(f"Pick a number between 1 and {c}: "))
        except:
            print("Not a number")
            continue
        if guess > random_number:
            print("Too High: Try again")
        elif guess < random_number:
            print("Too Low: Try again")
    
        else:
            stop = time.time()
            tIME = int(stop-start)
            print("Correct !!!!!!! Way to go")
            print(f"\nIt took you {total} tries and {tIME} seconds to figure it out!!!!\n")
            guess_data(name,total,tIME,x)
            print("\nWould you like to play again? Yes = y || No = n/other")
            replay = input()
            if replay.upper() == "Y":
                run_game()
            else:
                print("Thank You for Playing!!!!!")
                break
            


def run_game():
    print("Lets play the guessing game!!!!\n")
    print("Enter your full name: ")
    user = input()
    print("Please pick desired difficulty")
    print("------------------------------")
    print("Easy         = 1 1-->10")
    print("Intermediate = 2 1-->100")
    print("Hard         = 3 1-->1000")
    print("Supreme      = 4 1-->10000")
    difficulty = int(input())
    guess(difficulty, user)



def guess_data(user_name,tries_count,time_to_complete,x):
    file = open(f"Guessing_Game_Data{x}.txt","a+")
    file.write(f"{user_name} {tries_count} {time_to_complete}\n")
    file.close()
    file = open(f"Guessing_Game_Data{x}.txt","r")
    read_file_lines = file.readlines()
    file.close()
    
    filtered_list = []
    for i in read_file_lines:
        new_str = ""
        for a in i:
            if a != "\n":
                new_str += a
        filtered_list.append(new_str)
    amount_of_users = len(filtered_list)
    sub_lists = []
    for i in filtered_list:
        sub_lists.append(i.split())


    #total of users #total of tries #total of time
    total_tries = 0
    total_seconds = 0
    for i in range(len(sub_lists)):
        v = int(sub_lists[i][2])
        total_tries += v
        vv = int(sub_lists[i][3])
        total_seconds += vv
    print(f" total tries: {total_tries} total seconds: {total_seconds}")



run_game()
