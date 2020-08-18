

import pandas as pd




temp_series=pd.Series([['A','B','C'],['a','b','c'],['apple','bus','cat']]);
print(temp_series.head())


print(type(temp_series))
print(temp_series.shape)

print(type(temp_series.iloc[0]))


print(temp_series.loc[1])

