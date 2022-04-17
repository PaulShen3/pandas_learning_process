import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))

print(df["Churn"].value_counts())
