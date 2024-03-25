#groupby

df = pd.DataFrame({'items': ["X", "Y", "Z", "Y", "Z", "X"], 'number_of_sales': [200, 140, 65, 89, 82, 654]})

print(df)

print("************************************")

print(df.groupby("items").sum())

print("************************************")

print(df.groupby("items").mean())

"""
  items  number_of_sales
0     X              200
1     Y              140
2     Z               65
3     Y               89
4     Z               82
5     X              654
************************************
       number_of_sales
items                 
X                  854
Y                  229
Z                  147
************************************
       number_of_sales
items                 
X                427.0
Y                114.5
Z                 73.5

"""
