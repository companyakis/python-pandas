np.random.seed(101)

d1 = np.random.randint(0, 10, 6) #(10, size = 6)
d2 = np.random.randint(10, 30, 6)
d3 = np.random.randint(40, 60, 6)

a_dict = {"col1": d1, "col2": d2, "col3": d3}

nums = pd.DataFrame(a_dict)

nums.index = ["row1", "row2", "row3", "row4", "row5", "row6"]

print(nums)

print("----------------")

nums.drop("row1" , axis = 0, inplace = True)

print(nums)

"""
      col1  col2  col3
row1     1    18    57
row2     6    10    59
row3     7    24    55
row4     9    15    48
row5     8    22    59
row6     4    18    59
----------------
      col1  col2  col3
row2     6    10    59
row3     7    24    55
row4     9    15    48
row5     8    22    59
row6     4    18    59
"""



