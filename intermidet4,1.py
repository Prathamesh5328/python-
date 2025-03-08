#vectors
import numpy as np 
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
aa = np.array([1,2,3])
bb = np.array([4,5,6])
'''the below aggrition just multiply every element of a array with another array 
  and add all the stuff'''

print(a.dot(b))

'''the below stuff will give the pallerl array to the both arrays provided '''
print(np.cross(aa,bb))

print(a*10)
