import pandas as pd
import numpy as np

np.random.seed(66)

df = pd.DataFrame(np.random.rand(10,4),columns=list("ABCD"))
print(df)

#开始循环遍历
for index , row in df.head(5).iterrows():     #这里for index,row in df.iterrows():就可以打印全部列表
    print(row)