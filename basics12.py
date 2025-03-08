# def transmit_to_space(message):
#   "This is the enclosing function"
#   def data_transmitter():
#       "The nested function"
#       print(message)
#   return data_transmitter

# fun2 = transmit_to_space("Burn the Sun!")
# fun2()

def multiplier_of(n) :
   def multiplier(number):
      return number*n
   return multiplier 

multiply_with_5 = multiplier_of(5)
print(multiply_with_5(9))

#the above stuff is done below by using the lambda function 
simple_way = lambda x : x*5
print(simple_way(9))