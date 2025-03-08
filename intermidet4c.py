#numpy advance tutorial
#oprations 
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#doing the arithmitic opprations on the above array 
res1 = arr1 + arr2
res2 = arr1 * arr2
res3 = arr1 - arr2
res4 = arr1 / arr2
print(res1)
print(res2)
print(res3)
print(res4)


#doing aggregition  on the above array 
res5 = np.sum(arr1)
res6 = np.mean(arr2)
res7 = np.median(arr2)
res8 = np.max(arr2)
res9 = np.min(arr2)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)


# numpy advance tutorial
#univercal functions


arr3 = np.array([ 30 , 60  ,90 , np.pi  ])
print(arr3)

'''trignometric functions '''
res1 = np.sin(arr3)
print(res1)
res2 = np.cos(arr3)
print(res2)
res3 = np.tan(arr3)
print(res3)

'''exponants and logramathic functions '''

res4 = np.exp(arr3)
print(res4)
res5 = np.log(arr3)
print(res5)
