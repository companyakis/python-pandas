#series_concat

s1 = pd.Series([2154, 4547, 7894, 6987], index = ["2021 q1", "2021 q2", "2021 q3", "2021 q4"])

s2 = pd.Series([3254, 5789], index = ["2022 q1", "2023 q2"])

s = pd.concat([s1, s2])

print(s)

"""
2021 q1    2154
2021 q2    4547
2021 q3    7894
2021 q4    6987
2022 q1    3254
2023 q2    5789
dtype: int64

"""
