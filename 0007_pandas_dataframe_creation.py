#pandas_dataframe_creation

import pandas as pd

import numpy as np

data = np.array([[2021, 2022, 2023], [43.4, 28.84, 62.17], [110, 97, 121]])

df = pd.DataFrame(data, columns = ["year", "growing rate", "number of employees"])

print(df)

print("----------------")

print(df.info())

print("----------------")

print(df.describe())

print("----------------")

print(df.columns)

print("----------------")

print(df.head(2))

print("----------------")

print(df.tail(2))

print("----------------")

print(df.shape)

print("----------------")

print(df.ndim)

print("----------------")

print(df.size)

print("----------------")

print(df.axes)

"""
     year  growing rate  number of employees
0  2021.0       2022.00              2023.00
1    43.4         28.84                62.17
2   110.0         97.00               121.00
----------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   year                 3 non-null      float64
 1   growing rate         3 non-null      float64
 2   number of employees  3 non-null      float64
dtypes: float64(3)
memory usage: 200.0 bytes
None
----------------
              year  growing rate  number of employees
count     3.000000      3.000000             3.000000
mean    724.800000    715.946667           735.390000
std    1123.035939   1131.588675          1115.490868
min      43.400000     28.840000            62.170000
25%      76.700000     62.920000            91.585000
50%     110.000000     97.000000           121.000000
75%    1065.500000   1059.500000          1072.000000
max    2021.000000   2022.000000          2023.000000
----------------
Index(['year', 'growing rate', 'number of employees'], dtype='object')
----------------
     year  growing rate  number of employees
0  2021.0       2022.00              2023.00
1    43.4         28.84                62.17
----------------
    year  growing rate  number of employees
1   43.4         28.84                62.17
2  110.0         97.00               121.00
----------------
(3, 3)
----------------
2
----------------
9
----------------
[RangeIndex(start=0, stop=3, step=1), Index(['year', 'growing rate', 'number of employees'], dtype='object')]

"""
