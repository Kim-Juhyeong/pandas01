import pandas as pd

df = pd.read_csv('./driver_license_status1.csv')

print(df)

grouped = df.groupby(['year','age2'])
average = grouped.mean()

for key, group in grouped:
    print(group.head())
    print(group.tail())
    print('\n')

average