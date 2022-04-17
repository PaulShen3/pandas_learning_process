import pandas as pd

df = pd.read_csv("./分布数据前100.csv",index_col=0)

print(df.head())
print(df.columns)

df.reset_index(inplace=True)
print(df.head())
print(df.columns)