#conditional_selections

import numpy as np

import pandas as pd

data = np.random.randint(1,20, size = (6,5))

df = pd.DataFrame(data, columns = ["c1", "c2", "c3", "c4", "c5"])

print(df)

print("*************************")

print(df[:3][["c4", "c5"]]) # double [[]]

"""
   c1  c2  c3  c4  c5
0   8   9   5  15   4
1   5  18   9  19   6
2   6  15   1   6  17
3  19   2   3   7   2
4  17   5   6  19  15
5  12  12  19   8  16
*************************
   c4  c5
0  15   4
1  19   6
2   6  17
"""
