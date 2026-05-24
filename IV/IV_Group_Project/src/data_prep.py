"""Shared data loading and preprocessing for all three systems."""

import pandas as pd


def load_and_prepare(filepath: str) -> pd.DataFrame:
    """Read the weather CSV, clean it up, and add columns we need for the dashboards."""
    df = pd.read_csv(filepath)

    df['day'] = pd.to_datetime(df['day'])

    # Handle missing values
    df['summary'] = df['summary'].fillna('No description')
    df['desc'] = df['desc'].replace('', pd.NA).fillna('unknown')
    df['cloudCover'] = df['cloudCover'].fillna(df['cloudCover'].median())

    # Extra columns for grouping and analysis
    df['tempRange'] = df['tempMax'] - df['tempMin']
    df['month'] = df['day'].dt.month
    df['year'] = df['day'].dt.year
    df['monthName'] = df['day'].dt.strftime('%b')
    df['dayOfYear'] = df['day'].dt.dayofyear
    df['avgTemp'] = (df['tempMax'] + df['tempMin']) / 2

    season_map = {
        12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn',
    }
    df['season'] = df['month'].map(season_map)

    return df


if __name__ == "__main__":
    data = load_and_prepare("data/clean_weather_data.csv")
    print(f"Loaded {len(data)} rows, {len(data.columns)} columns")
    print(f"Columns: {list(data.columns)}")
    print(f"Date range: {data['day'].min()} to {data['day'].max()}")
    print(f"Desc values: {data['desc'].unique()}")
    print(data.head())
