#update_series

s = pd.Series([i for i in range(8)])

print(s)

print("--------------------")

s[2] = 1001

print(s)

"""
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
dtype: int64
--------------------
0       0
1       1
2    1001
3       3
4       4
5       5
6       6
7       7
dtype: int64

"""
