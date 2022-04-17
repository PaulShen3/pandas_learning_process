import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))


#对列重命名，比如Date变成D
#方法一：直接覆盖
df.columns = ["D",'O','H','L','C','V']
print(df)

#方法二：df.rename

df.rename(columns = {"Date":"D","Open":"O","High":"H"},
          inplace=True)
print(df)


df.rename(columns = {"Date":"D"},inplace=True)