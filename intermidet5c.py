import pandas as pd 
data1 = {"country"   : ["Brazil",   "Russia", "India",     "China",   "South Africa"],
         "capital"   : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
         "area"      : [ 8.516,      17.10,    3.286,       9.597,     1.221],
         "population": [ 200.4,      143.5,    1422,        1357,      52.98] }
dataframe = pd.DataFrame(data1)
dataframe.index = ["1", "2", "3", "4", "5"]

#sorting and filtering data 
'''sorting....'''
'''sorts the data by its name '''
df2 = dataframe.sort_values('area', axis= 0 , ascending= True, na_position= 'last' )
print(df2)#this will print the data in ascending order by taking the area in reference 

df3 = dataframe.sort_values('population', axis= 0 ,ascending=  True, na_position= 'last' )
print(df3)#this will print the data in ascending order by taking the population in reference 

'''filtering ....'''
df4 =  dataframe[dataframe['country'] == 'India']
print(df4)
print(df4.shape)
df5 =  dataframe[dataframe['area'] > 5 ]
print(df5)
print(df5.shape)