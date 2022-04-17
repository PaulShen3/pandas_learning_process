import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))

#删除high和low这两列

df.drop(columns=["High","Low"],inplace = True)

print(df.head(3))

#练习
import pandas as pd
df = pd.read_csv("./00700.HK.csv")
print(df.head(3))
df.drop(columns=["High","Low"],inplace=True)
print(df.head(3))