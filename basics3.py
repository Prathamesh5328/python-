#pandas basics
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
data = pd.DataFrame(dict)

# Set the index for brics
data.index = ["1", "2", "3", "4", "5"]
print(data)

# Print out brics with new index values
# print(data.iloc[['3']])



