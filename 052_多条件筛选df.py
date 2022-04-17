import numpy as np
import pandas as pd

np.random.seed(66)

df = pd.DataFrame(np.random.rand(10,4),columns=list("ABCD"))
print(df)


print(df[(df["C"]>0.3) & (df["D"] < 0.7)])

