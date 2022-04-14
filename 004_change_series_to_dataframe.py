import pandas as pd

grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
data = pd.Series(grades)
df = pd.DataFrame(data,columns = ['grade'])   #需要给一个列名，不然列名自动变成0
print(df)


# import pandas as pd
#
# grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
#
# data = pd.Series(data = grades)
#
# df = pd.DataFrame(data,columns=['grade'])
#
# print(df)