import pandas as pd

df = pd.DataFrame(
    {
        "姓名":['小张','小王','小李','小赵'],
        "性别":['男','女','男','女'],
        "年龄":[18,19,20,21]
    }
)

print(df)

print()
import pandas as pd

df2 = pd.DataFrame({
    "姓名":['Paul','Lebron','Booker'],
    "年龄":[36,37,25],
    "得分":[14,30,25]
})


print(df2)