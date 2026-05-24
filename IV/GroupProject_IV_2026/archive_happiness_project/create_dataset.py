"""
Script to create the World Happiness dataset for IV Project
This creates a synthetic but realistic dataset based on World Happiness Report structure
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define countries by region
regions = {
    'Western Europe': ['Finland', 'Denmark', 'Norway', 'Iceland', 'Netherlands',
                       'Switzerland', 'Sweden', 'Austria', 'Luxembourg', 'United Kingdom',
                       'Ireland', 'Germany', 'Belgium', 'France', 'Spain', 'Italy'],
    'North America': ['Canada', 'United States', 'Mexico', 'Costa Rica', 'Panama'],
    'Australia and New Zealand': ['Australia', 'New Zealand'],
    'Middle East and North Africa': ['Israel', 'United Arab Emirates', 'Saudi Arabia',
                                      'Qatar', 'Kuwait', 'Bahrain', 'Jordan', 'Morocco', 'Egypt'],
    'Latin America and Caribbean': ['Chile', 'Brazil', 'Argentina', 'Uruguay', 'Colombia',
                                     'Ecuador', 'Peru', 'Paraguay', 'Bolivia', 'Venezuela'],
    'Eastern Europe': ['Czech Republic', 'Poland', 'Lithuania', 'Russia', 'Latvia',
                       'Romania', 'Serbia', 'Bulgaria', 'Ukraine', 'Belarus'],
    'Southeast Asia': ['Singapore', 'Thailand', 'Philippines', 'Indonesia', 'Vietnam',
                       'Malaysia', 'Myanmar', 'Cambodia', 'Laos'],
    'East Asia': ['Taiwan', 'Japan', 'South Korea', 'China', 'Hong Kong', 'Mongolia'],
    'South Asia': ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Afghanistan'],
    'Sub-Saharan Africa': ['Mauritius', 'Nigeria', 'South Africa', 'Kenya', 'Tanzania',
                          'Uganda', 'Ethiopia', 'Ghana', 'Senegal', 'Rwanda']
}

# Years to include
years = [2020, 2021, 2022, 2023, 2024]

# Create dataset
data = []

for year in years:
    for region, countries in regions.items():
        # Base values for region (different regions have different base happiness)
        region_base = {
            'Western Europe': 7.2,
            'North America': 7.0,
            'Australia and New Zealand': 7.3,
            'Middle East and North Africa': 6.0,
            'Latin America and Caribbean': 6.1,
            'Eastern Europe': 5.8,
            'Southeast Asia': 5.9,
            'East Asia': 6.4,
            'South Asia': 4.5,
            'Sub-Saharan Africa': 4.2
        }

        base_happiness = region_base[region]

        for country in countries:
            # Add some variance to happiness score
            happiness = base_happiness + np.random.normal(0, 0.5)
            happiness = np.clip(happiness, 1, 10)

            # Generate correlated variables
            gdp_per_capita = happiness * 0.15 + np.random.normal(0, 0.05)
            gdp_per_capita = np.clip(gdp_per_capita, 0.2, 2.0)

            social_support = happiness * 0.12 + np.random.normal(0, 0.04)
            social_support = np.clip(social_support, 0.3, 1.0)

            healthy_life_expectancy = happiness * 0.08 + np.random.normal(0, 0.03)
            healthy_life_expectancy = np.clip(healthy_life_expectancy, 0.2, 0.9)

            freedom = happiness * 0.11 + np.random.normal(0, 0.05)
            freedom = np.clip(freedom, 0.1, 0.8)

            generosity = np.random.normal(0.15, 0.08)
            generosity = np.clip(generosity, -0.1, 0.5)

            corruption = 1 - (happiness * 0.08) + np.random.normal(0, 0.04)
            corruption = np.clip(corruption, 0.1, 0.9)

            # Add year trend (slight improvement over years)
            year_factor = (year - 2020) * 0.02
            happiness += year_factor

            data.append({
                'Country': country,
                'Region': region,
                'Year': year,
                'Happiness_Score': round(happiness, 3),
                'GDP_per_Capita': round(gdp_per_capita, 4),
                'Social_Support': round(social_support, 4),
                'Healthy_Life_Expectancy': round(healthy_life_expectancy, 4),
                'Freedom': round(freedom, 4),
                'Generosity': round(generosity, 4),
                'Corruption_Perception': round(corruption, 4)
            })

# Create DataFrame
df = pd.DataFrame(data)

# Add derived attributes
df['Population_Category'] = pd.cut(
    np.random.randint(1, 1400, len(df)),
    bins=[0, 10, 50, 200, 1500],
    labels=['Small', 'Medium', 'Large', 'Very Large']
)

# Save to CSV
df.to_csv('world_happiness_data.csv', index=False)

print(f"Dataset created successfully!")
print(f"Total records: {len(df)}")
print(f"Countries: {df['Country'].nunique()}")
print(f"Years: {df['Year'].nunique()}")
print(f"Regions: {df['Region'].nunique()}")
print(f"\nFirst few rows:")
print(df.head(10))
print(f"\nDataset shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
