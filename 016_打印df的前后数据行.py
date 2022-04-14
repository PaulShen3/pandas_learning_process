#df.head打印前几行，df.tail打印后几行

import pandas as pd
import numpy as np

date_range = pd.date_range(start = '2021-01-01',periods=1000)

df = pd.DataFrame(data = {
    'norm':np.random.normal(loc=0,scale=1,size=1000),  #loc=0,scale=1 标准正态分布
    'uniform':np.random.uniform(low=0,high=1,size=1000),   #均匀分布
    'binomial':np.random.binomial(n=1,p=0.2,size=1000)    #二项分布
    },
    index = pd.date_range(start = '2021-01-01',periods=1000))

print(df.head(10))
print()      #打印个空格空出来
print(df.tail(5))


