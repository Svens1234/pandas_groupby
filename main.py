import numpy as np
import pandas as pd
dict = {'Company': ['COMP1', 'COMP1', 'COMP2', 'COMP2', 'COMP3', 'COMP3'],
        'Months': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN'],
        'Salary': [2000, 1500, 3000, 5000, 2500, 3500 ]}

df = pd.DataFrame(dict)
print(df)
print(df.groupby('Company'))
print(df.groupby('Company').mean())
groupby_comp = df.groupby('Company')
print(groupby_comp.mean())
print(groupby_comp.sum())
print(groupby_comp.std())   #среднее квадратичное отклонение
print(type(groupby_comp.sum()))
print(groupby_comp.sum().loc['COMP3'])
print(df.groupby('Company').sum().loc['COMP3'])
print(df.groupby('Company').count())
print(df)
print(df.groupby('Company').max())
print(df.groupby('Company').min())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['COMP2'])
comp2 = df.groupby('Company').describe().transpose()['COMP2']
print(type(comp2))

