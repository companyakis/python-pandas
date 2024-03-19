import pandas as pd

l = [i for i in range(10)]

pd_s = pd.Series(l)

print(pd_s)

print("--------------------")

print(type(pd_s))

print("--------------------")

print(pd_s.axes)

print("--------------------")

print(pd_s.dtype)

print("--------------------")

print(pd_s.size)

print("--------------------")

print(pd_s.ndim)

print("--------------------")

print(pd_s.head(2))

print("--------------------")

print(pd_s.tail(3))

"""
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64
--------------------
<class 'pandas.core.series.Series'>
--------------------
[RangeIndex(start=0, stop=10, step=1)]
--------------------
int64
--------------------
10
--------------------
1
--------------------
0    0
1    1
dtype: int64
--------------------
7    7
8    8
9    9
dtype: int64
"""
