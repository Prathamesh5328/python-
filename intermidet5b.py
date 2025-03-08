import pandas as pd 
data1 = {
         "country"   : ["Brazil",   "Russia", "India",     "China",   "South Africa"],
         "capital"   : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
         "area"      : [ 8.516,      17.10,    3.286,       9.597,     1.221],
         "population": [ 200.4,      143.5,    1252,        1357,      52.98] }
dataframe = pd.DataFrame(data1)
dataframe.index = ["1", "2", "3", "4", "5"]



#data exploration 
'''the basics information to explore using the pandas '''
print(dataframe.head(3 ))#this will be printing starting 3 roes of the data 
print(dataframe.tail(3))#this will be printing ending  3 roes of the data
print(dataframe.shape)#this will be printing shape of the data
print(dataframe.info)#this will be printing information of the data

'''discriptive statistics '''
print(dataframe.describe())#this will print all statistic discription of the data
print(dataframe.mean)
print(dataframe.mode)
print(dataframe.median)
# print(dataframe.corr())
