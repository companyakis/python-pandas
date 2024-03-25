df = pd.DataFrame({'items'          : ["X", "Y", "Z", "Y", "Z", "X"], 
                   'number_of_sales': [200, 140, 65, 89, 82, 654],
                   'discount_rate'  : [3, 11, 8, 6, 5, 10]
})

print(df)

print("*****************************************")

print(df.groupby("items").mean())

print("*****************************************")

print(df.groupby("items").min())

"""
  items  number_of_sales  discount_rate
0     X              200              3
1     Y              140             11
2     Z               65              8
3     Y               89              6
4     Z               82              5
5     X              654             10
*****************************************
       number_of_sales  discount_rate
items                                
X                427.0            6.5
Y                114.5            8.5
Z                 73.5            6.5
*****************************************
       number_of_sales  discount_rate
items                                
X                  200              3
Y                   89              6
Z                   65              5
"""
