#截断：如果一个数小于-1，就让他等于-1，如果一个数大于1，就让他等于1
import numpy as np
import pandas as pd

np.random.seed(66)
s1 = pd.Series(np.random.rand(20))  #生成0-1之间的随机数
s2 = pd.Series(np.random.randn(20))  #生成正态分布随机数

#concat默认是行方向堆叠，如果需要行堆叠则为：df = pd.concat([s1,s2]),如果要列方向就加一个axis=1
df = pd.concat([s1,s2],axis=1)  #列方向堆叠

df.columns = ["col1","col2"]  #修改列名

df['col3'] = df["col2"].map(lambda x:1 if x>=0 else -1)

df["col4"] = df["col2"].clip(-1.0,1.0)   #clip就是截断函数
print(df)