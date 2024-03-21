df_new = df.copy()

df_new.index = ["row" +str(i) for i in range(10)]

print(df_new)

print("*****************************************")

print(df_new.loc[:"row3"])

"""
      quarter1  quarter2  quarter3  quarter4
row0         8        33        39        37
row1         6        18        41        41
row2        15         3        46         8
row3        28         5        42        44
row4        27        35        34        45
row5         6        41        31         5
row6        13         9        17        17
row7        45        10         6        49
row8        34        31        48        37
row9        46        32        40        38
*****************************************
      quarter1  quarter2  quarter3  quarter4
row0         8        33        39        37
row1         6        18        41        41
row2        15         3        46         8
row3        28         5        42        44
"""
