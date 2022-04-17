import pandas as pd
import numpy as np

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10,4),columns=list("ABCD"))

df.iloc[3,1] = np.nan      #iloc[a,b] 这边a是索引行的位置，b是索引列的位置，np.nan就是设置空值
df.loc[8,'D'] = np.nan     #loc[a,"B"] 这边a还是所银行的位置，”B“是列名
print(df)

df2 = df.dropna()  #这会把整行都删掉
print(df2)