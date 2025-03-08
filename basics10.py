
import pickle as pk 
random_string = ([1,2,3,4,'a','b','c','d'])
breakdown_random_string = pk.dumps(random_string)
restruture_random_number = pk.loads(breakdown_random_string)
print(random_string)
print(breakdown_random_string)
print(restruture_random_number)

