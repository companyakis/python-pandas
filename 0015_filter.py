#filter

df = pd.DataFrame({'items'          : ["X", "Y", "Z", "Y", "Z", "X"], 
                   'number_of_sales': [200, 140, 65, 89, 82, 654],
                   'discount_rate'  : [3, 11, 8, 6, 5, 10]
})

print(df.groupby("items").std())

print("*****************************************")

def df_filter_max(i):
    return i["discount_rate"].max() > 10

print(df.groupby("items").filter(df_filter_max))

print("*****************************************")

def df_filter_std(i):
    return i["number_of_sales"].std() > 100

print(df.groupby("items").filter(df_filter_std))

"""
       number_of_sales  discount_rate
items                                
X           321.026479       4.949747
Y            36.062446       3.535534
Z            12.020815       2.121320
*****************************************
  items  number_of_sales  discount_rate
1     Y              140             11
3     Y               89              6
*****************************************
  items  number_of_sales  discount_rate
0     X              200              3
5     X              654             10
"""
