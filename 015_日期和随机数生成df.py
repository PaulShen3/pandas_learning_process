import pandas as pd
import numpy as np

date_range = pd.date_range(start = '2021-01-01',periods=1000)

data = {
    'norm':np.random.normal(loc=0,scale=1,size=1000),  #loc=0,scale=1 标准正态分布
    'uniform':np.random.uniform(low=0,high=1,size=1000),   #均匀分布
    'binomial':np.random.binomial(n=1,p=0.2,size=1000)    #二项分布
}

df = pd.DataFrame(data = data,index = date_range)

print(df)

import pandas as pd
import numpy as np

date_range2 = pd.date_range(start='2022-04-14',periods=100)

data2 = {
    'normal':np.random.normal(loc=0,scale=1,size=100),
    'uniform':np.random.uniform(low=0,high=1,size=100),
    'binomial':np.random.binomial(n=1,p=0.2,size=100)
}

df2 = pd.DataFrame(data = data2,index=date_range2)
print(df2)