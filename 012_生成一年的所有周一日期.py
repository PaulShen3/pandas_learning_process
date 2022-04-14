import pandas as pd

# date_range = pd.date_range(start='2021-01-01',end = '2021-12-31',freq='W-MON')

date_range = pd.date_range(start='2021-01-01',periods=52,freq='W-MON') #取周几就用英文首字母前三位就行


print(date_range)

print()

import pandas as pd

date_range2 = pd.date_range(start='2022-04-14',end='2022-09-01',freq='W-FRI')

print(date_range2)