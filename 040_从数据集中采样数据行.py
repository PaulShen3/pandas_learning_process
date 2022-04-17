import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.sample(10))

df.sample(10).to_csv("sample10.csv")