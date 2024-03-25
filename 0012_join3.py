df1 = pd.DataFrame({"employee" : ["Mustafa", "Aygün", "Bilge", "Bumin", "Kutluk", "Kültigin"],
                    "id"       : [1, 2, 14, 17, 21, 46],
                    "deparment": ["Head Office", "Finance", "HR", "Audit", "Sales", "IT"]
})

df2 = pd.DataFrame({"id"       : [1, 2, 14, 17, 21, 46],
                    "gross_monthly_salary_₺": [150000, 75000, 80000, 94000, 87500, 92000]
})



df3 = pd.DataFrame({"deparment": ["Head Office", "Finance", "HR", "Audit", "Sales", "IT"],
                    "group_director": ["Mustafa Buyukdereli", "Kağan Yolaçıkan", "Bengü Arslan", "Hakan Onkardeş", "Esmer Ay", "Nurbilge Tarakçı"]
    
})


merged1 = pd.merge(df1, df2)

print(merged1)

print("*******************************************************")

merged2 = pd.merge(merged1, df3)

print(merged2)

"""
   employee  id    deparment  gross_monthly_salary_₺
0   Mustafa   1  Head Office                  150000
1     Aygün   2      Finance                   75000
2     Bilge  14           HR                   80000
3     Bumin  17        Audit                   94000
4    Kutluk  21        Sales                   87500
5  Kültigin  46           IT                   92000
*******************************************************
   employee  id    deparment  gross_monthly_salary_₺       group_director
0   Mustafa   1  Head Office                  150000  Mustafa Buyukdereli
1     Aygün   2      Finance                   75000      Kağan Yolaçıkan
2     Bilge  14           HR                   80000         Bengü Arslan
3     Bumin  17        Audit                   94000       Hakan Onkardeş
4    Kutluk  21        Sales                   87500             Esmer Ay
5  Kültigin  46           IT                   92000     Nurbilge Tarakçı
"""
