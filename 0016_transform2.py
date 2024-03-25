transformed_df = df.iloc[:, 1:].transform(lambda x: (x - x.mean() / x.std()))

print(transformed_df)

"""
   number_of_sales  discount_rate
0       199.090524       0.658335
1       139.090524       8.658335
2        64.090524       5.658335
3        88.090524       3.658335
4        81.090524       2.658335
5       653.090524       7.658335

"""
