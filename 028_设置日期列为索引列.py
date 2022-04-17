import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))    #只要前三行的数据

#把date变成索引列

df.set_index("Date",inplace=True)


#练习
import pandas as pd

df = pd.read_csv("./00700.HK.csv")

df.set_index("Date",inplace=True)