dict = {"mustafa": 10, "bilge": 45, "kağan": 37}

s = pd.Series(dict)

print(s)

print(s["bilge"])

"""
mustafa    10
bilge      45
kağan      37
dtype: int64
45
"""
