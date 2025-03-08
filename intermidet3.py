# difference between the loops and vectors 
# vctorization
# exmple one squring the number
import numpy as np 

x = np.array([1,2,3,4,5])

'''using lopps to get the squre of 
       the elements in the above arrya'''

'''for i in range(len(x)):
    x[i] = x[i] ** 2'''
  
   #print(x)
'''here the output we got was 
   [1 2 3 4 5]
   [1 4 3 4 5]
   [1 4 9 4 5]
   [ 1  4  9 16  5]
   [ 1  4  9 16 25]'''

'''using vectorization methode to get the 
    squre of the elements in the above arry '''

y = x ** 2
print(y)

'''here the output we gwt was
   [ 1  4  9 16 25]'''