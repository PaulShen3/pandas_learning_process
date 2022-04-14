import pandas as pd

# date_range = pd.date_range(start = '2021-10-01',end = '2021-10-31')  #默认按天递增，并且包含最后一天
date_range = pd.date_range(start = '2021-10-01',periods=31)  #默认按天递增，取31个数

print(date_range)


#
# print()
# import pandas as pd
#
# date_range2 = pd.date_range(start='2022-04-14',end='2022-09-01')
# print(date_range2)