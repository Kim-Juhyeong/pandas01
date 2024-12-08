import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./driver_license_status1.csv')

grouped_df = df.groupby(['year', 'age2'])[['Class1 Heavy','Class1 Ordinary','Class2 Ordinary','Class2 small']].sum().reset_index()

#grouped

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

license_types = ['Class1 Heavy','Class1 Ordinary','Class2 Ordinary','Class2 small']
growth_rates_by_type = {}

for license_type in license_types:
    pivot_data = grouped_data.pivot(index='year', columns='age2', values=license_type)
    growth_rate = pivot_data.pct_change() * 100
    growth_rates_by_type[license_type] = growth_rate

combined_growth_rates = pd.concat(growth_rates_by_type, axis=1)
combined_growth_rates.columns = pd.MultiIndex.from_tuples([(col, age_group) for col in license_types for age_group in ['age2=20', 'age2=30']])

for license_type in license_types:
    growth_rate = growth_rates_by_type[license_type]
    
    growth_rate.plot(
        kind='bar',
        figsize=(10, 6),
        title=f'Annual Growth Rates for {license_type}',
        xlabel='Year',
        ylabel='Growth Rate (%)',
        grid=True
    )
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(['0%','age2=20', 'age2=30'], title='Age Group')
    plt.tight_layout()
    plt.show()

