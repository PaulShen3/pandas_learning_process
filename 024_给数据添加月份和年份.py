import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df)

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month