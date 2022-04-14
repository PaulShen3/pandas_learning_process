import pandas as pd

grades = {'语文':80,'数学':90,'英语':85,'计算机':100}
data = pd.Series(grades)


data = data.append(pd.Series({'物理':88,'化学':95}))


data['生物']=88
data['地理']=96

print(data)