print(df[df.c2 > 10])

print("*************************")

print(df[(df.c1 > 10) & (df.c4 < 15)])

"""
   c1  c2  c3  c4  c5
1   5  18   9  19   6
2   6  15   1   6  17
5  12  12  19   8  16
*************************
   c1  c2  c3  c4  c5
3  19   2   3   7   2
5  12  12  19   8  16
"""
