name = input("what is your name.  ")
print("welcome to the game ", name ,".")

answer = input("you are at a dirt road , it has come  to an end and you can go left or right ,where you would like to go ?    ").lower()
if answer == "left":
   answer = input("ok! now you had come to an river, you can walk around it or swim swim across, type walk to walk and swim to swim across:  ").lower()
   if answer == "walk":
     print("oo! you walk many miles and you ran outof water and you loose.")
   elif answer == "swim":
     print("oo! you swim across and unfortunitly you were eaten by alligators.")
   else:
        print("its not a valid option. you lose")
        quit()
elif answer == "right":
   answer = input("ok now you come to a brich and it looks wobbly, would you like to cross or head back , type cross to cross and head back to head back").lower()
   if answer == "cross":
    print("oo!! the brich falls doun and you loose ")
   elif answer == "head back":
      print("o!! to wakking on a brich was only option to go so you loose")
   else:
      print("its not a valid option. you lose")
      quit()
      
else:
   print("its not a valid option. you lose")
   quit()

print("thankyou for trying the game , i hope you enjoy!!")


