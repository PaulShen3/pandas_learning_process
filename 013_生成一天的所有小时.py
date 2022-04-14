import pandas as pd

date_range = pd.date_range(start = '2021-10-01',periods=24,freq='H') #H就是小时
# date_range = pd.date_range(start = '2021-10-01',end = '2021-10-02',freq='H',closed = 'left') #H就是小时

print(date_range)

# print()
#
# import pandas as pd
#
# date_range2 = pd.date_range(start='2022-04-14',periods=48,freq='H')
# print(date_range2)