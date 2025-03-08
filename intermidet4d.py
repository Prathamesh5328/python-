# numpy advance tutorial
# advance numpy ferures 
 
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[4],[5],[6]])

'''broadcasting'''
ress1 = arr1 + arr2
print(ress1)

'''masking'''
mask = arr1 > 2 
ress2 = arr1[mask]
print(ress2)

#sorting and scerching 
import numpy as np 
arr3 = ([2,9,5,7,3,42,61])
sort_arr3 = np.sort(arr3)
print(sort_arr3)

indices = np.argsort(arr3)
print(indices)



