print(df_new.loc["row0", "quarter3"]) # 39

print(df_new.loc["row5", "quarter2"]) # 41

print(df_new.loc[: "row4", "quarter2": ])

"""
      quarter2  quarter3  quarter4
row0        33        39        37
row1        18        41        41
row2         3        46         8
row3         5        42        44
row4        35        34        45
"""
