import pandas as pd

#数据集：电信客户流失数据
# 上个月内离开的客户：该列称为Churn
# 每个客户已注册的服务：如电话、互联网、在线安全、电视和电影等
# 客户账户信息：他们成为客户的时间、合同、付款方式、每月费用和总费用
# 客户的人口统计信息：性别、年龄范围，是否有伴侣和家属

df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(5))