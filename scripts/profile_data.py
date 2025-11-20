import pandas as pd
import os

# 1. Prepare & Setup
RAW_DATA_DIR = os.path.join("data", "raw")
OWID_CALORIES_FILE = os.path.join(RAW_DATA_DIR, "daily-per-capita-caloric-supply.csv")
WHO_OBESITY_FILE = os.path.join(RAW_DATA_DIR, "obesity-cleaned.csv") 

# 2. Data Loading & Profiling
def run_profiling():
    try:
        df_cal = pd.read_csv(OWID_CALORIES_FILE)
    except FileNotFoundError:
        print(f"\n[ERROR] Calorie file not found. Run acquire_data.py.")
        df_cal = pd.DataFrame({'Entity': []}) 

    df_obesity = pd.read_csv(WHO_OBESITY_FILE)
    
    print("\n--- A. CALORIE DATA SUMMARY ---")
    df_cal.info()
    
    print("\n--- B. OBESITY DATA SUMMARY ---")
    df_obesity.info()
    
    # 3. Cleaning Checks
    
    # Sex Check for documentation
    print(f"\nObesity Sex categories: {df_obesity['Sex'].unique()}")
    
    # Obesity Rate Check for documentation
    print(f"Obesity Rate Sample: {df_obesity.head(1)['Obesity (%)'].iloc[0]}")
    
    # 4. Country mapping check
    country_list_obesity = set(df_obesity['Country'].unique())
    country_list_cal = set(df_cal['Entity'].unique()) if not df_cal.empty else set() 

    diff_obesity_only = country_list_obesity - country_list_cal
    diff_cal_only = country_list_cal - country_list_obesity
    
    print("\n========================================================")
    print("--- COUNTRY MAPPING LISTS (Required for clean_data.py) ---")
    print("========================================================")
    
    print(f"\n[LIST 1: Names in OBESITY data ONLY] (Total: {len(diff_obesity_only)})")
    print(diff_obesity_only)
    
    print(f"\n[LIST 2: Names in CALORIE data ONLY] (Total: {len(diff_cal_only)})")
    print(diff_cal_only)
    
    print("\nACTION: Use these lists to build the COUNTRY_MAP.")

if __name__ == "__main__":
    run_profiling()