import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.head(3))
print(df.info())

print()
print(df.corr())   #只能出来三行，因为相关性矩阵只会计算数字型字段