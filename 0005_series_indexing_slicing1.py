#series_indexing_slicing

s = pd.Series([2 * i + 3 for i in range(10)], index = [char for char in "abcdefghij"])

print(s)

print("--------------------")

print(s["c"])

print("--------------------")

print(s["a":"e"])

print("--------------------")

print(s[:"f"])

"""
a     3
b     5
c     7
d     9
e    11
f    13
g    15
h    17
i    19
j    21
dtype: int64
--------------------
7
--------------------
a     3
b     5
c     7
d     9
e    11
dtype: int64
--------------------
a     3
b     5
c     7
d     9
e    11
f    13
dtype: int64
"""
