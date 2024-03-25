print(df.groupby("items").aggregate({"number_of_sales": "min", "discount_rate": "max"}))

"""
       number_of_sales  discount_rate
items                                
X                  200             10
Y                   89             11
Z                   65              8
"""
