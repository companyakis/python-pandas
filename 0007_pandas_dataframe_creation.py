#pandas_dataframe_creation

import pandas as pd

import numpy as np

data = np.array([[2021, 2022, 2023], [43.4, 28.84, 62.17], [110, 97, 121]]).T

df = pd.DataFrame(data, columns = ["year", "growing rate", "number of employees"]).astype("int64")

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
0  2021            43                  110
1  2022            28                   97
2  2023            62                  121
----------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column               Non-Null Count  Dtype
---  ------               --------------  -----
 0   year                 3 non-null      int64
 1   growing rate         3 non-null      int64
 2   number of employees  3 non-null      int64
dtypes: int64(3)
memory usage: 200.0 bytes
None
----------------
         year  growing rate  number of employees
count     3.0      3.000000             3.000000
mean   2022.0     44.333333           109.333333
std       1.0     17.039171            12.013881
min    2021.0     28.000000            97.000000
25%    2021.5     35.500000           103.500000
50%    2022.0     43.000000           110.000000
75%    2022.5     52.500000           115.500000
max    2023.0     62.000000           121.000000
----------------
Index(['year', 'growing rate', 'number of employees'], dtype='object')
----------------
   year  growing rate  number of employees
0  2021            43                  110
1  2022            28                   97
----------------
   year  growing rate  number of employees
1  2022            28                   97
2  2023            62                  121
----------------
(3, 3)
----------------
2
----------------
9
----------------
[RangeIndex(start=0, stop=3, step=1), Index(['year', 'growing rate', 'number of employees'], dtype='object')]
"""
