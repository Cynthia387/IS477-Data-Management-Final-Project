# Data Dictionary

This document describes the main datasets used in the project, including their fields and meanings. Our analysis is based on three levels of data:

1. Raw source datasets (from Our World in Data and WHO/Kaggle)  
2. Cleaned datasets used for integration  
3. The final integrated dataset used for analysis and visualization  

## 1. Raw Datasets

### 1.1 `data/raw/daily-per-capita-caloric-supply.csv` (Our World in Data / FAO)

Source: Our World in Data – “Daily supply of calories per person” (based on FAO Food Balances and historical research).

Each row represents the average daily calorie supply for one country in one year.

- **Entity**  
  Name of the country or region (e.g., "United States", "Vietnam").

- **Code**  
  Short country code (e.g., "USA", "VNM"). Some entries are missing.  
  This column is not used in our analysis and is dropped during cleaning.

- **Year**  
  Calendar year of observation (integer).

- **Daily calorie supply per person**  
  Average number of kilocalories available per person per day in that country and year.  
  This measures calories available for consumption, not necessarily calories actually eaten.

### 1.2 `data/raw/obesity-cleaned.csv` (WHO / Kaggle)

Source: Kaggle – “Obesity Among Adults by Country (1975–2016)” (based on WHO Global Health Observatory).

Each row represents an obesity estimate for one country, one year, and one sex category.

- **Country**  
  Official country name used by WHO (e.g., "United States of America", "Viet Nam").

- **Year**  
  Calendar year of observation (integer).

- **Sex**  
  Sex category for the estimate: "Male", "Female", or "Both sexes".  
  For this project, we only keep "Both sexes" in the cleaned dataset.

- **Obesity (%)**  
  Obesity prevalence as a percentage of the adult population.  
  In the raw data, this is stored as a text string that includes a confidence interval  
  (for example: `"23.4 [21.1–25.6]"`).  
  In cleaning, we extract only the numeric percentage.

- **(Unnamed index column)**  
  Extra index column created during file export.  
  This is removed during cleaning.

## 2. Cleaned Datasets

### 2.1 `data/clean/clean_calories.csv`

Created by: `scripts/clean_data.py` from `daily-per-capita-caloric-supply.csv`.

Each row is a cleaned calorie record for a country and year.

- **Entity**  
  Standardized country name (after applying the COUNTRY_MAP to harmonize names  
  across sources, e.g., mapping "United States of America" to "United States").

- **Year**  
  Calendar year of observation.

- **Calories_per_person**  
  Cleaned and renamed version of "Daily calorie supply per person".  
  Numeric kilocalories available per person per day.

### 2.2 `data/clean/clean_obesity.csv`

Created by: `scripts/clean_data.py` from `obesity-cleaned.csv`.

Each row is a cleaned obesity record for “Both sexes” in a given country and year.

- **Entity**  
  Standardized country name (mapped from WHO country names such as  
  "Viet Nam", "United States of America", etc.).

- **Year**  
  Calendar year of observation.

- **Obesity_Rate**  
  Numeric obesity prevalence (percentage of adults with BMI ≥ 30).  
  Extracted from the original "Obesity (%)" text column using a regular expression.

## 3. Integrated Dataset

### 3.1 `data/processed/calorie_obesity.csv`

Created by: `scripts/integrate_data.py` by merging `clean_calories.csv` and `clean_obesity.csv` on Entity and Year.

Each row represents one country–year pair for which we have both calorie supply and obesity prevalence.

- **Entity**  
  Standardized country name used consistently across both input datasets.

- **Year**  
  Calendar year of observation within the overlapping period (1975–2016).

- **Calories_per_person**  
  Daily kilocalories available per person in that country and year.

- **Obesity_Rate**  
  Percentage of adults classified as obese in that country and year.

This integrated dataset is the main input for all analysis and visualizations in `scripts/analyze_data.py`.
