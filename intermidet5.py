#pandas basics to advance 
#data struture 
''' basically there are two data strutures in the pandas 
   1) serirs : produces the one dimantional array'''

import pandas as pd 


data = [10,20,30,40,50,60,70]  
series = pd.Series(data)
series.index = ["1", "2", "3", "4", "5",'6','7']
print(series) #this produce the one dimantional array
 
'''2) data frame: this produce the multidimantional array'''

data1 = {"country"   : ["Brazil",   "Russia", "India",     "China",   "South Africa"],
         "capital"   : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
         "area"      : [ 8.516,      17.10,    3.286,       9.597,     1.221],
         "population": [ 200.4,      143.5,    1252,        1357,      52.98] }
dataframe = pd.DataFrame(data1)

# Set the index for brics
dataframe.index = ["1", "2", "3", "4", "5"]
print(dataframe)


#input/output
'''input/output '''
'''writing the data and  reading the data '''

dataframe.to_csv('intermidet5_data1')
pd.read_csv('intermidet5_data1')


