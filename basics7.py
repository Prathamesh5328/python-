import numpy as np 

l = np.array([2,4,7,3,14,19])
for i in l :
    my_lambda  = lambda x : (x%2) == 1
    print(my_lambda(i))

