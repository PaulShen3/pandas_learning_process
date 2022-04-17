import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.head(3))

median = df["TotalCharges"] [df["TotalCharges"] != " "].median()
df.loc[df["TotalCharges"] == " ",'TotalCharges'] = median
df["TotalCharges"] = df["TotalCharges"].astype(float)

#
print(df.columns)
#把三列变成数字类型，其他的列变成categrical类型

number_columns = ["tenure","MonthlyCharges","TotalCharges"]

for column in number_columns:
    df[column] = df[column].astype(float)

for column in set(df.columns) - set(number_columns):  #set函数可以用 “-” 的形式把两个集合相减
    df[column] = pd.Categorical(df[column])

print(df.info())