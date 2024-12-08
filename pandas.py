import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./driver_license_status1.csv')

grouped_df = df.groupby(['year', 'age2'])[['Class1 Heavy','Class1 Ordinary','Class2 Ordinary','Class2 small']].sum().reset_index()

grouped

age2_20 = grouped_df[grouped_data['age2'] == 20]
age2_30 = grouped_df[grouped_data['age2'] == 30]

plt.figure(figsize=(12, 6))

for column in ['Class1 Heavy','Class1 Ordinary','Class2 Ordinary','Class2 small']:
    plt.plot(age2_20['year'], age2_20[column], label=f'age2=20, {column}')
    plt.plot(age2_30['year'], age2_30[column], linestyle='--', label=f'age2=30, {column}')

plt.title('Changes in License Holders by Year and Age Group (age2=20 & age2=30)')
plt.xlabel('Year')
plt.ylabel('Number of License Holders')
plt.legend()
plt.grid(True)
plt.show()