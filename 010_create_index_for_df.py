#把姓名设置为索引列

import pandas as pd

# df = pd.DataFrame(
#     {
#         "姓名":['小张','小王','小李','小赵'],
#         "性别":['男','女','男','女'],
#         "年龄":[18,19,20,21]
#     }
# )

data = {
        "姓名":['小张','小王','小李','小赵'],
        "性别":['男','女','男','女'],
        "年龄":[18,19,20,21]
}

df = pd.DataFrame(data)

df.set_index("姓名",inplace = True)    #inplace = True就是直接修改df，不加的话会返回一个新的df
print(df)


# import pandas as pd
#
# data2 = pd.DataFrame({
#         "姓名":['Paul','Lebron','Booker'],
#         "年龄":[36,37,25],
#         "得分":[14,30,25]
# })
#
# data2.set_index("姓名",inplace=True)
# print(data2)