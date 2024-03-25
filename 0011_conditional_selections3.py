print(df[(df.c5 > 15) | (df.c2 < 15)])

print("*************************")

print(df[(df.c5 > 15) | (df.c2 < 15)][["c2", "c3"]].iloc[:3])

"""
   c1  c2  c3  c4  c5
0   8   9   5  15   4
2   6  15   1   6  17
3  19   2   3   7   2
4  17   5   6  19  15
5  12  12  19   8  16
*************************
   c2  c3
0   9   5
2  15   1
3   2   3
"""