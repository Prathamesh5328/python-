#example 2 of the vectorization 
# adding two arryas 
import numpy as np 

a = np.array([1,2,3,4,5,])
b = np.array([6,7,8,9,10])

'''adding both the arryas
 a and b by using the loop methode '''

'''c = np.zeros_like(a)
for i in range(len(a)):
    c[i] = a[i] + b[i]

    print(c)'''

'''this loop outputs the result below
   [7 0 0 0 0]
   [7 9 0 0 0]
   [ 7  9 11  0  0]
   [ 7  9 11 13  0]
   [ 7  9 11 13 15]'''

c = a + b

print(c)
'''this loop outputs the result below
   [ 7  9 11 13 15]'''

