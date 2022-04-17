import pandas as pd

df = pd.read_csv("./00700.HK.csv")

print(df["Close"].min())

df["Close"].argmin()  #返回最小值所在的df的索引
df.loc[[df["Close"].argmin()]]   #传入索引筛选出最小值所在数据行
print(df.loc[[df["Close"].argmin()]])   #再多加一个[]返回df，否则返回series

#练习
import pandas as pd
df = pd.read_csv("./00700.HK.csv")
print(df["Close"].min())

df["Close"].argmin()
min_loc = df.loc[["Close".argmin()]]
print(min_loc)