import numpy as np

import pandas as pd

np.random.seed(2024)

d1 = np.random.randint(1,20, size = (3,3))

d2 = np.random.randint(50,80, size = (3,3))

df1 = pd.DataFrame(d1, columns = ["c1", "c2", "c3"])

df2 = pd.DataFrame(d2, columns = ["c1", "c2", "c3"])

df = pd.concat([df1, df2], ignore_index = True)

print(df)

"""
   c1  c2  c3
0   9   1   1
1   5  10   2
2   4  11   3
3  50  55  78
4  67  65  73
5  60  64  65
"""
