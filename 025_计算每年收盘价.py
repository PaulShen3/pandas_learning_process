import pandas as pd

df = pd.read_csv("./00700.HK.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Month'].dt.month
print(df)

avg = df.groupby("Year")["Close"].mean  #Close是收盘价
print (avg)


