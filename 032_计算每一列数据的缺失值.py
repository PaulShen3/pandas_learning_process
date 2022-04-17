import pandas as pd

#数据集准备
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))

#计算每一列数据缺失值
print(df.isnull())
print(df.isnull().sum())   #如果大于0就代表有多少缺失值，如果全是0酒泉市false，没有缺失值

#练习
import pandas as pd
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))
print(df.isnull())
print(df.isnull().sum())