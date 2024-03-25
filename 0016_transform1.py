#transform

df = pd.DataFrame({'items'          : ["a", "b", "c", "d", "e", "f"], 
                   'number_of_sales': [200, 140, 65, 89, 82, 654],
                   'discount_rate'  : [3, 11, 8, 6, 5, 10]
})

print(df)

print("************************************")

# a * 2
transformed_df = df.iloc[:, 1:].transform(lambda x: 2 * x)

print(transformed_df)

"""
  items  number_of_sales  discount_rate
0     a              200              3
1     b              140             11
2     c               65              8
3     d               89              6
4     e               82              5
5     f              654             10
************************************
   number_of_sales  discount_rate
0              400              6
1              280             22
2              130             16
3              178             12
4              164             10
5             1308             20

"""
