#加载csv文件到df，记得恢复索引列

import pandas as pd
df = pd.read_csv("分布数据前100.csv",index_col=0)

print(df.info())
print(df.head(10))