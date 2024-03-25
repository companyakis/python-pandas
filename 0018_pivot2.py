#cut and pivot

titanic_ages = pd.cut(df_titanic["age"], [0, 18, 100])

print(titanic_ages.describe())

print("************************************")

pivot_age_survived_sex = df_titanic.pivot_table("survived", ["sex", titanic_ages], "class")

print(pivot_age_survived_sex)

"""
count           714
unique            2
top       (18, 100]
freq            575
Name: age, dtype: object
************************************
class                First    Second     Third
sex    age                                    
female (0, 18]    0.909091  1.000000  0.511628
       (18, 100]  0.972973  0.900000  0.423729
male   (0, 18]    0.800000  0.600000  0.215686
       (18, 100]  0.375000  0.071429  0.133663

"""
