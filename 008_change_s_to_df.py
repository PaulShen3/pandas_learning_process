# import pandas as pd
#
# grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
# data = pd.Series(grades)
#
# df = data.reset_index()
# df.columns = ['course','grade']
#
# print(df)
#
#
#
#
# grade = {'政治':64,'英语':76,'数学三':117,'432统计学':141}
#
# data1 = pd.Series(grade)
#
# df1 = data1.reset_index()
# df1.columns = ['project','grade']
#
# print(df1)

import pandas as pd
cp3_2022 = {'得分':14.7,'篮板':4.4,'助攻':10.8,'抢断':1.9,'盖帽':0.3}

data_cp3 = pd.Series(cp3_2022)
print(data_cp3)

df2 = data_cp3.reset_index()
df2.columns = ['data_name','data']

print(df2)