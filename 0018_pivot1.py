#pivot

df_titanic = sns.load_dataset("titanic")

print(df_titanic.columns)

print("************************************")

print(df_titanic.survived.value_counts())

print("************************************")

print(df_titanic["class"].value_counts())

print("************************************")

print(df_titanic.groupby("sex")["survived"].sum())

print("************************************")

pivot_survived_class = df_titanic.pivot_table("survived", index = "sex", columns = "class")

print(pivot_survived_class)

"""
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object')
************************************
0    549
1    342
Name: survived, dtype: int64
************************************
Third     491
First     216
Second    184
Name: class, dtype: int64
************************************
sex
female    233
male      109
Name: survived, dtype: int64
************************************
class      First    Second     Third
sex                                 
female  0.968085  0.921053  0.500000
male    0.368852  0.157407  0.135447
"""
