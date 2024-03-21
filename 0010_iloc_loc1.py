import pandas as pd
import numpy as np

data = np.random.randint(0, 50, size = (10, 4))

df = pd.DataFrame(data, columns = ["quarter1", "quarter2", "quarter3", "quarter4"])

print(df)

print("*****************************************")

print(df.iloc[:4])

"""
   quarter1  quarter2  quarter3  quarter4
0         8        33        39        37
1         6        18        41        41
2        15         3        46         8
3        28         5        42        44
4        27        35        34        45
5         6        41        31         5
6        13         9        17        17
7        45        10         6        49
8        34        31        48        37
9        46        32        40        38
*****************************************
   quarter1  quarter2  quarter3  quarter4
0         8        33        39        37
1         6        18        41        41
2        15         3        46         8
3        28         5        42        44
"""
