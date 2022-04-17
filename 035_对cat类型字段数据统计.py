import pandas as pd

#导入数据集
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))

#填充TotalCharges的缺失值
median = df["TotalCharges"] [df["TotalCharges"] != " "].median()
df.loc[df["TotalCharges"] == " ",'TotalCharges'] = median
df["TotalCharges"] = df["TotalCharges"].astype(float)

#将分类列转换成Categorical类型
number_columns = ["tenure", "MonthlyCharges", "TotalCharges"]
for column in number_columns:
    df[column] = df[column].astype(float)

for column in set(df.columns) - set(number_columns):  # set函数可以用 “-” 的形式把两个集合相减
    df[column] = pd.Categorical(df[column])

print(df.info())

#对cat类型字段数据统计
print(df.describe(include=["category"]))

#unique是有几种，top是出现最频繁的，freq是出现了多少次