new_df = df.copy()

temp_df = new_df.drop("row2", axis = 0)

print(temp_df)

print("----------------")

print(new_df)

"""
      col1  col2  col3
row1     5    23    59
row3     3    25    46
row4     2    25    57
row5     5    10    45
row6     9    12    57
----------------
      col1  col2  col3
row1     5    23    59
row2     8    27    47
row3     3    25    46
row4     2    25    57
row5     5    10    45
row6     9    12    57

"""
