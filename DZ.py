import pandas as pd

df = pd.read_csv('dz.csv')

group = df.groupby('City')['Salary'].mean()

print(group)