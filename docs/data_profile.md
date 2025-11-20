# Data Profile and Structure Review (Cynthia Shen)

This document summarizes the structural and integrity assessment of the two raw datasets, confirming requirements for the Data Cleaning and Standardization phase.

## 1. Calorie Supply Dataset (OWID/FAO)

Filename: `daily-per-capita-caloric-supply.csv`

### Schema Summary (Structure and Data Types)
* Total Rows: 13050 entries
* Data Types: `float64` (1), `int64` (1), `object` (2)

| Column | Non-Null Count | Dtype | Notes |
| :--- | :--- | :--- | :--- |
| Entity | 13050 | object | Country Name, requires standardization. |
| Code | 10449 | object | Country Code, contains nulls but is not used for analysis. |
| Year | 13050 | int64 | Used for merging. |
| Daily calorie supply per person | 13050 | float64 | Core value column. |

## 2. Adult Obesity Dataset (WHO/Kaggle)

Filename: `obesity-cleaned.csv`

### Schema Summary (Structure and Data Types)
* Total Rows: 24570 entries
* Data Types: `int64` (2), `object` (3)

| Column | Non-Null Count | Dtype | Notes |
| :--- | :--- | :--- | :--- |
| Unnamed: 0 | 24570 | int64 | Index column, will be dropped. |
| Country | 24570 | object | Country Name, requires standardization. |
| Year | 24570 | int64 | Used for merging. |
| Obesity (%) | 24570 | object | Requires cleaning (Numeric Extraction). |
| Sex | 24570 | object | Requires filtering. |

## 3. Standardization Requirements

Based on the profiling, two key standardization steps are necessary for data integration:

1.  **Filtering (`Sex` Column):** The data contains categories `['Both sexes', 'Male', 'Female']`. We must filter the dataset to only retain rows where `Sex` is **'Both sexes'** to match the analysis scope.
2.  **Numeric Extraction (`Obesity (%)` Column):** The column is stored as a string (`object`) because it contains confidence intervals.
    * Sample Value: `0.5 [0.2-1.1]`
    * Action: Extract the leading numeric value (e.g., `0.5`) and convert the resulting column to a `float` type for calculation.
3.  **Country Harmonization:** The country names between the two datasets must be mapped using the `COUNTRY_MAP` implemented in `clean_data.py` to ensure accurate merging.
