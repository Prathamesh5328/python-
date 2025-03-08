import random 
#some sort of variables are been defined 
user_wins = 0
computer_wins = 0
the_ties = 0 
options =  ["rock" ,"paper", "scissors" ]

#the loop starts from here , which is takin the input from user 
while True:
    user_input = input("type Rock/paper/scissors or Q to quit .   ").lower()
    if user_input == "q":
        break
 
    if user_input  not in options :
        print("type somthing from the rock/paper/scissors")
        continue

#genreating som random number and taking computers input
    random_number = random.randint(0,2)
   # rock: 1, paper: 2, scissors: 3
    computer_pick = options[random_number]
    print("computer pick", computer_pick ," . ")

#defining the conditions where a user can win 
    if user_input == "rock" and computer_pick == "scissors" :
        print("you won!!")
        user_wins += 1
        continue 

    elif user_input == "paper" and computer_pick == "rock":
        print("you win!!")
        user_wins += 1
        continue
   
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win!!")
        user_wins += 1
        continue

#defining the conditions where its going to be tie 
    elif user_input == "rock" and computer_pick == "rock":
        print("its a tie!!")
        the_ties += 1
        continue

    elif user_input == "paper" and computer_pick == "paper":
        print("its a tie!!")
        the_ties += 1
        continue

    elif user_input == "scissors" and computer_pick == "scissors":
        print("its a tie!!")
        the_ties += 1
        continue

#else all conditions are where user loose
    else:
        print("you lost!!")
        computer_wins += 1

#printing all the end redults , how many wins ,looses and ties 
print("you won ",user_wins , "times .") 
print("computer won ", computer_wins , "times. ") 
print("it ties", the_ties ,"times.")
print("goodbye!!")
