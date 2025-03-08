import pandas as pd 
df1 = pd.DataFrame({'category' : ['A','A','B','B','A','A','B','B'],
                    'value' :    [ 10,15,20,25,30,35,40,45]})
df1.index = ['1','2','3','4','5','6','7','8']

# coustem aggregation 
def coustem_agg(x):
    return x.max() - x.min()


group1 = df1.groupby('category')
result = group1['value'].agg(['max','min'])
result1 = group1['value'].agg(coustem_agg)
print(result) 
print(result1)