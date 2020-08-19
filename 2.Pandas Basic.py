

import pandas as pd
import numpy as np



temp_series=pd.Series([['A','B','C'],['a','b','c'],['apple','bus','cat']]);
print(temp_series.head())


print(type(temp_series))
print(temp_series.shape)

print(type(temp_series.iloc[0]))


print(temp_series.loc[1])

data_arr=np.random.random((90,5))
print(data_arr.shape)
data_col=['A','B','C','D','E']
print(data_col)

df_data=pd.DataFrame(data_arr,columns=data_col);
print(df_data.head())
print(df_data.shape)