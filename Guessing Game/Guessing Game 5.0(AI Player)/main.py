#5.0 IS not a player program where it is a built in AI playing the game instead of a person
#5.0 uses an AI player that tackels the game using a linear approach when taking guesses. 
#It starts at 0 than the guesses keep increasing by one till the final answer is found

import random
import time



def creating_user_name():                                       #Creating User name
    print("Enter your full name: ")
    user = "AI Player"#input()                                                                                                                                                                          #AI
    user_name_verification = user.split()                       #User Name Condition
    if len(user_name_verification) != 2:                        #FirstName(space)LastName
        print("Invalid Entry: First_Last")
        return creating_user_name()
    else:
        return user                                             #Return user name


########################################################################################################################################################################################################## User Name


def choosing_difficulty():
    print("Please pick desired difficulty")                     #Picking dificulty 1-2-3-4 
    print("------------------------------")
    print("Easy         = 1 1-->10")
    print("Intermediate = 2 1-->100")
    print("Hard         = 3 1-->1000")
    print("Supreme      = 4 1-->10000")
        
    try:
        difficulty = 4#int(input())                                                                                                                                                                     #AI
    except ValueError:
        print("Not an int: try again")                          #Making Sure enterd ifficulty is within range and not a float or str
        choosing_difficulty()

        
    if 0<difficulty<5:
        return difficulty
    else:
        print("Invalid Level of difficulty")
        return choosing_difficulty()

########################################################################################################################################################################################################## Difficulty Level

def start_game():                                               #function that starts off the game
    print("Lets play the guessing game!!!!\n")
    
    name = creating_user_name()             #User_name
    difficulty = choosing_difficulty()      #difficulty level
    
    game_loop(name, difficulty)                                 #Taking declarations into the main game loop 


########################################################################################################################################################################################################## Start Game

def game_loop(name, difficulty):                                                                                        #In game Loop
    c = 10**difficulty                                  #Formula for setting range based on difficulty
    random_number = random.randint(1,c)                 #Setting the range 
    guess = 0                                           #Creating a variable for The quess user takes 
    total = 0                                           #Creating a variable for amount of tries it takes to end game
    
    start = time.time()                                                                                                                                             ##Timing Game##Start
    
    while guess != random_number:
        total += 1  #incrementing by one for each guess
        guess += 1
        
        #try:                                                          #
        #      guess = int(input(f"Pick a number between 1 and {c}: "))  #Handling error of a non int guess
        #except:                                                       #
         #   print("Not a number")                                     #
           # total += 1                                                #Making sure the amount of guesses increases by 1 for each mistake
            #continue                                                          #

        
        if guess > random_number:               # if guess high
            print("Too High: Try again")        #
        elif guess < random_number:             # if guess low
            print("Too Low: Try again")         #


    
        else:   #Once answer figures out
            stop = time.time()                                                                                                                                      ##Timing Game##Finish
            tIME = int(stop-start)             #Creating a solid variable for the amount of time it took to end game
            print("Correct !!!!!!! Way to go")
            print(f"\nIt took you {total} tries and {tIME} seconds to figure it out!!!!\n")




            #RECORDING DATA
            recording_data(name,total,tIME,difficulty) #prints data
            organize_file_data(difficulty)             #organizes file
            sorting_data(difficulty, total, tIME)      #creast two lists for main data (users amount,time,tries) and prints out how many users You did better than
            
            #Giving the user the ability to play again within the loop

            
            print("\nWould you like to play again? Yes = y || No = n/other")    #Choice of playing again
            replay = "y"#input()
            if replay.upper() == "Y":
                start_game()

            
            else:                                                               #Ending Game
                print("Thank You for Playing!!!!!")
                break


############################################################################################################################################################################################################# Game Loop

def recording_data(user_name , total_tries , game_time , difficulty_level):                                                 #Recording and sorting data into text files
    file = open(f"Guessing_Game_Data{difficulty_level}.txt","a+")                          #Opening a text file based on difficulty level (if no such text file exists a new one will be created)
    file.write(f"{user_name} {total_tries} {game_time}\n")           #Recoding name_tries_time into the text file
    file.close()                                                            #closing text file


def organize_file_data(difficulty_level):                                                                                                         #Making sure no error accure within the text file (such as empty line)
    with open(f"Guessing_Game_Data{difficulty_level}.txt") as reader, open(f"Guessing_Game_Data{difficulty_level}.txt", 'r+') as writer:
      for line in reader:
        if line.strip():
          writer.write(line)
      writer.truncate()
############################################################################################################################################################################################################## Data sorting

      
def sorting_data(difficulty_level, total, tIME ):
    file = open(f"Guessing_Game_Data{difficulty_level}.txt","r")
    read_file_lines = file.readlines()
    file.close()

    filtered_list = []                      #
    for i in read_file_lines:               # Creating sub lists for each line in file
        new_str = ""                        #
        for a in i:                         #
            if a != "\n":                   #
                new_str += a                #
        filtered_list.append(new_str)       #
    amount_of_users = len(filtered_list)    #
    sub_lists = []                          #
    for i in filtered_list:                 #
        sub_lists.append(i.split())         #



    #creating a varible for the amount of different user data
    amount_of_users = len(sub_lists)

    
    #Creating two different lists of data one for time and another for tries
    
    time_data_list = []
    tries_data_list = []
    

    
    #aPPENDIG each of the tries and time into its suitable list in order for later manipulation of data
    for i in range(len(sub_lists)):
        tries_data_list.append(int(sub_lists[i][2]))
        time_data_list.append(int(sub_lists[i][3]))


    user_total = total
    user_time  = tIME

    utp = 0
    
    for i in range(amount_of_users):
        if user_total < tries_data_list[i]:     #if your tries less than other treis utp + 1
            utp += 1             
        elif user_total == tries_data_list[i]:  #if amount of tries equal but time lessutp +1
            if user_time < time_data_list[i]:
                utp += 1
    percentage_of_better_results = int((utp/amount_of_users)*100)
    print(f"Out of {amount_of_users} users that played the game at level {difficulty_level} difficulty")
    print(f"You have done better than {percentage_of_better_results}% of users")         
############################################################################################################################################################################################################# Data Analasis


    
start_game()

########### Run Game









































































    
