import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(5))

#正确设置数据列的类型
print(df.info())

print(df["TotalCharges"].value_counts())   #出来11列空白值导致数据列类型不是float，可以使用中位数填补空白值

#把空白值改成中位数
median = df["TotalCharges"][df["TotalCharges"] != " "].median()
df.loc[df["TotalCharges"] == " ","TotalCharges" ] = median

#修改数据类型
df["TotalCharges"] = df["TotalCharges"].astype(float)
print()
#再次验证
print(df["TotalCharges"].value_counts())