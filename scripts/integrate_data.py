import pandas as pd
import os

# 1. Path Configurations
CLEAN_DIR = os.path.join("data", "clean")
PROCESSED_DIR = os.path.join("data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

CLEAN_OBESITY_FILE = os.path.join(CLEAN_DIR, "clean_obesity.csv")
CLEAN_CALORIES_FILE = os.path.join(CLEAN_DIR, "clean_calories.csv")
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "calorie_obesity.csv")


def integrate_data():
    """Loads clean data and performs the final merge and validation."""
    print("Starting data integration...")
    
    # the two cleaned datasets
    df_obesity = pd.read_csv(CLEAN_OBESITY_FILE)
    df_calories = pd.read_csv(CLEAN_CALORIES_FILE)
    
    # 2. Merge datasets
    # Merge on the standardized 'Entity' (Country) and 'Year'
    df_merged = pd.merge(
        df_obesity,
        df_calories,
        on=['Entity', 'Year'],
        how='inner' # Inner join: Only keep countries present in both datasets
    )
    
    # 3. Valitaion & Cleanup
    print(f"Merge complete. Initial rows: {df_obesity.shape[0]} (Obesity) + {df_calories.shape[0]} (Calories)")
    print(f"Final merged rows: {df_merged.shape[0]}")
    
    # Remove any rows where core values might still be missing (should be rare)
    df_merged = df_merged.dropna()
    
    # 4. save file
    df_merged.to_csv(OUTPUT_FILE, index=False)
    print(f"SUCCESS: Final integrated data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    integrate_data()