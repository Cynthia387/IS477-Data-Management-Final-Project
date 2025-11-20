import pandas as pd
import os
import re

# 1. CONFIGURATION AND PATHS
RAW_DIR = os.path.join("data", "raw")
CLEAN_DIR = os.path.join("data", "clean")
os.makedirs(CLEAN_DIR, exist_ok=True)

WHO_OBESITY_RAW = os.path.join(RAW_DIR, "obesity-cleaned.csv")
OWID_CALORIES_RAW = os.path.join(RAW_DIR, "daily-per-capita-caloric-supply.csv")

# 2. Country Harmonization Map
# Maps long names (Obesity data) to short names (Calorie data)
COUNTRY_MAP = {
    # WHO/UN Long Names to OWID/FAO Common Names
    'Syrian Arab Republic': 'Syria',
    "Côte d'Ivoire": "Cote d'Ivoire", # Mapping to Calorie name (List 2)
    "Democratic People's Republic of Korea": 'North Korea',
    'Viet Nam': 'Vietnam',
    'Micronesia (Federated States of)': 'Micronesia (country)',
    'United Republic of Tanzania': 'Tanzania',
    'Democratic Republic of the Congo': 'Democratic Republic of Congo',
    'Brunei Darussalam': 'Brunei',
    'Iran (Islamic Republic of)': 'Iran',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Timor-Leste': 'East Timor',
    'Cabo Verde': 'Cape Verde',
    'Republic of Moldova': 'Moldova',
    'Republic of North Macedonia': 'North Macedonia',
    'Republic of Korea': 'South Korea',
    'Venezuela (Bolivarian Republic of)': 'Venezuela',
    "Lao People's Democratic Republic": 'Laos',
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'United States of America': 'United States',
    'Russian Federation': 'Russia',

    # Other fixes
    'Hong Kong SAR, China': 'Hong Kong',
    'Macao SAR, China': 'Macao',
    'Taiwan, Province of China': 'Taiwan',
}

# 3. Cleaning

def clean_obesity_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filters, cleans, and standardizes the WHO Obesity data."""
    print("Cleaning Obesity Data...")
    df_clean = df.copy()
    
    # 3a. Filter to keep only 'Both sexes'
    df_clean = df_clean[df_clean['Sex'] == 'Both sexes']
    
    # 3b. Extract numeric obesity rate (removes confidence interval)
    df_clean['Obesity_Rate'] = df_clean['Obesity (%)'].str.extract(r'(\d+\.?\d*)')
    df_clean['Obesity_Rate'] = pd.to_numeric(df_clean['Obesity_Rate'])
    
    # 3c. Apply country standardization and rename
    df_clean = df_clean.rename(columns={'Country': 'Entity'})
    df_clean['Entity'] = df_clean['Entity'].replace(COUNTRY_MAP)
    df_clean = df_clean[['Entity', 'Year', 'Obesity_Rate']] # Final columns selection

    return df_clean

def clean_calorie_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and standardizes the OWID Calorie data."""
    print("Cleaning Calorie Data...")
    df_clean = df.copy()

    # 3a. Rename the main value column
    df_clean = df_clean.rename(columns={
        'Daily calorie supply per person': 'Calories_per_person'
    })

    # 3b. Drop 'Code' column and apply country standardization
    df_clean = df_clean.drop(columns=['Code'])
    df_clean['Entity'] = df_clean['Entity'].replace(COUNTRY_MAP)

    return df_clean

# 4. Execution
def main():
    try:
        # Load Raw Data
        df_obesity_raw = pd.read_csv(WHO_OBESITY_RAW)
        df_calories_raw = pd.read_csv(OWID_CALORIES_RAW)

        # Clean and Save
        df_obesity_clean = clean_obesity_data(df_obesity_raw)
        df_calories_clean = clean_calorie_data(df_calories_raw)

        df_obesity_clean.to_csv(os.path.join(CLEAN_DIR, "clean_obesity.csv"), index=False)
        df_calories_clean.to_csv(os.path.join(CLEAN_DIR, "clean_calories.csv"), index=False)
        print(f"\nSUCCESS: Cleaned files saved to {CLEAN_DIR}.")
        
    except FileNotFoundError as e:
        print(f"\nERROR: File not found: {e}. Ensure acquire_data.py has run successfully and files are in data/raw.")

if __name__ == "__main__":
    main()