import pandas as pd
import numpy as np

df = pd.DataFrame({
    'normal':np.random.normal(loc=0,scale=1,size=1000),
    'uniform':np.random.uniform(low=0,high=1,size=1000),
    'binoimal':np.random.binomial(n=1,p=0.2,size=1000)
},
index=pd.date_range(start='2021-01-01',periods=1000))
print(df)
print(df["binoimal"].value_counts())