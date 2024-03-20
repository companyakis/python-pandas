df.index = ["row1", "row2", "row3", "row4", "row5", "row6"]

print(df[: "row3"])

print("----------------")

print(df["row4": "row5"])

"""
      col1  col2  col3
row1     5    23    59
row2     8    27    47
row3     3    25    46
----------------
      col1  col2  col3
row4     2    25    57
row5     5    10    45
"""
