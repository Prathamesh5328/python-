#numpy advance tutorial
#manupliting the arrya
import numpy as np

arr1 = np.array([1,2,3,4,5])
'''some of the manuplations r done below'''

print(arr1[0])#this prints the number '1'
print(arr1[3])#this prints the number '4'
print(arr1[1:3])#this prints the number '2,3'
print(arr1[0:2])#this prints the number '1,2,

'''modifing the exicisting arrya'''
arr1[2] = 132
print(arr1)#this will print arrya 1 [1,2,132,4,5]

