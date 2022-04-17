#把yes变成1，no变成0

import pandas as pd
df = pd.read_csv("Telco-Customer-Churn.csv")

print(df["Churn"].value_counts())

#把yes变1

df["Churn"] = df["Churn"].map({"Yes":1,"No":0})       #df.["字段名"].map({"变量名":"改后的变量名})
print()
print(df["Churn"].value_counts())