import pandas as pd

s = pd.Series(data = ["001",'002','003','004'],
              index=list("abcd"))
print(s)

s = s.astype(int)  #是一个int类型
# s = s.map(int)     #是一个函数

print(s)

import pandas as pd

s = pd.Series(data = ['001','002','003','004'],
              index = list("abcd"))

s = s.map(int)

print(s)