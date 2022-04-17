import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.columns)
print(df.groupby(["Churn","PaymentMethod"])["MonthlyCharges"].mean())