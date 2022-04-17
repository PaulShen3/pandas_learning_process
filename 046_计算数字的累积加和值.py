import pandas as pd
import numpy as np

#每个数字等于前面所有数字的和

np.random.seed(66)

s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1,s2],axis=1)
df.columns = ['col1','col2']

#
print(df.cumsum())  #cumsum()累计加和函数