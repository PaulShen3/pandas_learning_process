import pandas as pd
import numpy as np

df = pd.DataFrame({
    'normal':np.random.normal(loc=0,scale=1,size=1000),
    'uniform':np.random.uniform(low=0,high=1,size=1000),
    'binomial':np.random.binomial(n=1,p=0.2,size=1000)
},
    index = pd.date_range(start='2021-01-01',periods=1000)
)

#在这里完成题目
df.head(100).to_csv("分布数据前100.csv")

