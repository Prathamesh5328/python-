import random 
#asking the user for the input which is a number and need to be greater than 0 
top_of_range = input(" please type a number upto u want to guess.   ")

if top_of_range.isdigit():
   top_of_range = int(top_of_range)

   if top_of_range <= 0 :
      print("please type a number larger than 0 next time. ")
      quit()

else:
   print("please type a number next ")
   quit()
   
random_number = random.randrange(0,top_of_range)
guesses = 0


#asking the user to guess the randon number which is going to get gunreted 
while True:
   guesses += 1
   user_guess = input("make a guess.   ")
   if user_guess.isdigit():
     user_guess = int(user_guess)
   else:
      print("please type a number next time!!")

   if user_guess == random_number:
      print("you got it right !!")
      break
   
   elif user_guess > random_number :
           print("you were above the number")
   elif user_guess < random_number:
        print("you were below the number ")
        
   
print("you got it in ", guesses , "guesses . ")