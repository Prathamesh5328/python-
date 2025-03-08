#exception handling 
#try:
# #example 1 
# try:
#     a = b#here the b will throw error as it is not defined
# except:
#     print('no value for b')
'''even if there is an error in this coad it wil
      not show the error insted it will print th written
       line which we have given 'no value for b ' '''
    
#    #example 2  
# try:
#     a = b #here the b will throw error as it is not defined 
#     '''therefore i am commenting out all the code that the error is throeing the
#        notification on my screen and its boddering me . '''
# except Exception as e:
#   print(e)

#example 3 
try:
    a = 5 
    b = 6 
    c = a+b 
except Exception as e:
    print(e)
else :
    print('code is running succesfully ')

#example 4
try:
    a = int(input('enter a number \n '))
    b = int(input('enter a number \n '))
    # c = a + b 
except Exception as e:
      print(e)
else:
    print(a+b)
