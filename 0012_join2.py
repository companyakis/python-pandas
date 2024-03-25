df1 = pd.DataFrame({"employee" : ["Mustafa", "Aygün", "Bilge", "Bumin", "Kutluk", "Kültigin"],
                    "deparment": ["Head Office", "Finance", "HR", "Audit", "Sales", "IT"]
})

df2 = pd.DataFrame({"employee" : ["Mustafa", "Aygün", "Bilge", "Bumin", "Kutluk", "Kültigin"],
                    "gross_monthly_salary_₺": [150000, 75000, 80000, 94000, 87500, 92000]
    
})


df = pd.merge(df1, df2)

print(df)

"""
   employee    deparment  gross_monthly_salary_₺
0   Mustafa  Head Office                  150000
1     Aygün      Finance                   75000
2     Bilge           HR                   80000
3     Bumin        Audit                   94000
4    Kutluk        Sales                   87500
5  Kültigin           IT                   92000
"""
