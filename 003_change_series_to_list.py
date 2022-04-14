import pandas as pd

grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
data = pd.Series(grades)

numbers = data.tolist()  #tolist是变成list
print(numbers)


# import pandas as pd
#
# grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
#
# data = pd.Series(grades)
#
# numbers = data.tolist()
#
# print(numbers)