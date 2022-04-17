import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10,4),columns=list("ABCD"))
# df = pd.DataFrame(np.random.rand(10,4),columns=["A","B","C","D"])
print(df)
print()
print(df.loc[df['C'] > 0.8])