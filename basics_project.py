#our quiz game starts hers 
#lets start the game by welcoming the players 
# and asking the players that do they want to play out game or not 
print("Welcome to my computer quiz!")

playing = input("Do you want to play ?  ")
if playing.lower() != "yes":
    quit()
print("okay! let's play :) ")
score = 0 

#asking the first question of this quix game 
answer1 = input(" what is colour of sky ") 
if answer1.lower() == "blue" :
    print("correct!")
    score += 1
else:  
    print("incorrect!")
    
    #asking the second question of this quix game 
answer1 = input(" what is colour of skin ?  ") 
if answer1.lower() == "skin" :
    print("correct!")
    score += 1
else:  
    print("incorrect!")

    #asking the third question of this quix game 
answer1 = input(" what is colour of human teeth ?   ") 
if answer1.lower() == "white" :
    print("correct!")
    score += 1
else:  
    print("incorrect!")

 #asking the fourth question of this quix game 
answer1 = input(" what is colour of black soil ?   ") 
if answer1.lower() == "black" :
    print("correct!")
    score += 1
else:  
    print("incorrect!")

score_you_scored = ("you answer " + str(score) + "  question out of you solved")
print(score_you_scored)

percent_you_score = ("you score" + str((score*25)) + " %.")
print(percent_you_score)