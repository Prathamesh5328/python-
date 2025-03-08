#pandas 
#groupby and aggrecation 
'''groupby...
   sytex...
grouped = df.groupby ( by, axis = 0, level = None ,as_index = True , sort = True , group_key = True ,squeeze = False , observed = False ) '''

import pandas as pd 
df = pd.DataFrame({'category' : ['A','A','B','B','B'],
                    'value' : [ 10,20,30,40,50]})
df.index = ['1','2','3','4','5']



#1. call 
group = df.groupby('category')
print(group)

'''sum(),min(),max(),mean()'''
group_sum = group['value'].sum()
print(group_sum)
group_mean = group['value'].mean()
print(group_mean)
group_min = group['value'].min()
print(group_min)
group_max = group['value'].max()
print(group_max)

#multiple agg function 
aggrigated = group['value'].agg(['mean','median','max','min', 'sum',])
print(aggrigated)

