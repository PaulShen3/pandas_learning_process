import pandas as pd

df = pd.read_csv("./00700.HK.csv")

print(df)

df_new = df[["Date","Open","Close","Volume"]]   #只要这几列
print(df_new.head(3))      #只包含前三列

#练习
import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df)

df_new = df[["Date","Open","Close","Volume"]]
print(df_new.head(3))