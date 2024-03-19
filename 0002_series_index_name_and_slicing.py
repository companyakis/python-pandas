#series_index_name_and_slicing

s = pd.Series([2021, 2022, 2023, 2024], index = ["Year1", "Year2", "Year3", "Year4"])

print(s)

print("--------------------")

print(s["Year2"])

print("--------------------")

print(s["Year2" : ])

"""
Year1    2021
Year2    2022
Year3    2023
Year4    2024
dtype: int64
--------------------
2022
--------------------
Year2    2022
Year3    2023
Year4    2024
dtype: int64

"""
