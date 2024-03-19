s = pd.Series([2 * i + 3 for i in range(10)], index = [char for char in "abcdefghij"])

print(s.index)

print("--------------------")

print("x" in s)

print("--------------------")

print("d" in s)

print("--------------------")

print(s[["a", "i"]])

"""
Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')
--------------------
False
--------------------
True
--------------------
a     3
i    19
dtype: int64
"""
