df = pd.DataFrame({'items'          : ["a", "b", "c", "a", "c", "b"], 
                   'number_of_sales': [200, 140, 65, 89, 82, 654],
                   'discount_rate'  : [3, 11, 8, 6, 5, 10]
})

print(df)

print("************************************")

print(df.groupby("items").apply(np.mean))

"""
  items  number_of_sales  discount_rate
0     a              200              3
1     b              140             11
2     c               65              8
3     a               89              6
4     c               82              5
5     b              654             10
************************************
       number_of_sales  discount_rate
items                                
a                144.5            4.5
b                397.0           10.5
c                 73.5            6.5
"""
