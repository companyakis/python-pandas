print(df.groupby("items").aggregate([min, np.mean, np.median, max]))

"""
      number_of_sales                    discount_rate                
                  min   mean median  max           min mean median max
items                                                                 
X                 200  427.0  427.0  654             3  6.5    6.5  10
Y                  89  114.5  114.5  140             6  8.5    8.5  11
Z                  65   73.5   73.5   82             5  6.5    6.5   8
"""
