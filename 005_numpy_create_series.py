import numpy as np
import pandas as pd

s = pd.Series(
    np.arange(10,100,10),
    index = np.arange(101,110),
    dtype = 'float'
    #数值：10~90  间隔10
    #索引：101~109，间隔1
    #类型：float64
)
print(s)


# import pandas as pd,numpy as np
#
# s = pd.Series(
#     np.arange(10,100,10),
#     index = np.arange(101,110),
#     dtype = 'float'
# )
#
# print(s)