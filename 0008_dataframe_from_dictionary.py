d1 = np.random.randint(0, 10, 6) #(10, size = 6)

d2 = np.random.randint(10, 30, 6)

d3 = np.random.randint(40, 60, 6)

a_dict = {"col1": d1, "col2": d2, "col3": d3}

df = pd.DataFrame(a_dict)

print(df)

"""
   col1  col2  col3
0     5    23    59
1     8    27    47
2     3    25    46
3     2    25    57
4     5    10    45
5     9    12    57
"""
