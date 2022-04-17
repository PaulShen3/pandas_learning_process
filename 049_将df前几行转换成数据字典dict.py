import pandas as pd
import numpy as np

np.random.seed(66)

s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1,s2],axis=1)
df.columns = ['col1','col2']

#把前五行编程dict
print(df.head(5).to_dict())