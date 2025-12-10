**Title:** Calorie Supply and Obesity Trends Analysis Project

**Contributors:**
Tracie Huynh (thuyn3): Data acquisition, repository structure, integrity verification, exploratory analysis, data quality review
Cynthia Shen (xs49):

**Summary:**

For this project, we set out to explore a simple but important question: Does the amount of calories available in a country relate to how common obesity is among its adult population? Obesity has become a global health concern and people often assume that having more food or more calories automatically leads to higher obesity rates. We wanted to test whether that assumption actually appears in real data. To do this, we combined two datasets from trusted international organizations which are the FAO calorie supply dataset from Our World in Data and the WHO obesity dataset found on Kaggle. Because the datasets differ in structure, naming conventions, time ranges and formats, much of our work centered on data cleaning, standardization, integrity verification and reproducibility before performing any analysis.
Our motivation came from noticing how steadily both calorie supply and obesity rates have been rising over the past several decades. At the global level, people now have more calories available to them than at any other time in history. Meanwhile, obesity rates have more than doubled since the 1970s. Although calories alone can’t explain obesity for factors like lifestyle, physical activity, food quality, income and urbanization also matter but we were curious whether the broad global trends show a relationship.Therefore, we centered our project on three main research questions:

- Is there a relationship between the average daily calorie supply per person and the adult obesity rate in each country?

- Do countries that have more calories available per person tend to have higher obesity rates?

- How has the relationship between calorie supply and obesity rates changed across different years or regions?
  
To start, we manually downloaded both datasets. The OWID dataset is openly accessible and covers 1961 to 2022. On the other hand, the Kaggle dataset is based on WHO data and covers 1975 to 2016. Since Kaggle requires user authentication, programmatic downloading was not allowed. To ensure reproducibility, we generated SHA-256 checksums for both files and created a verification script so anyone using our repository can confirm that they have the correct copies of the data. This helps avoid issues where files accidentally change or are downloaded incorrectly. 
Next came data profiling and cleaning. This stage revealed several mismatches, especially in country names such as “United States” vs. “United States of America,” or “Côte d’Ivoire” vs. “Ivory Coast” for example. We created a COUNTRY_MAP to standardize names across both datasets. We also filtered the obesity dataset to use only “Both sexes” data and converted any non-numeric values into proper numeric format. Once both datasets were clean and consistent, we merged them using country-year pairs, resulting in a final integrated dataset called calorie_obesity.csv.
With the merged dataset ready, we were finally able to start exploring the relationship between calorie supply and obesity rates. Our early findings suggest that there is generally a positive relationship with countries that have more calories available per person and also tend to have higher obesity rates. This pattern is especially strong in high-income countries, which often appear at the high end of both variables. However, the relationship isn’t perfect or universal. Several middle-income countries, for example, show rising obesity rates that don’t match their calorie supply levels, suggesting that other factors like changes in diet composition, processed food availability, or lifestyle are also playing major roles.

**Data Profile:**

Our project uses two official, country-level datasets that allow us to examine how national calorie supply relates to adult obesity rates over time. Both datasets come from authoritative international organizations and contain aggregated statistics, which minimizes ethical or privacy concerns.

## 1. FAO Food Balance Sheets – Daily Per Capita Calorie Supply  
The calorie dataset originates from the Food and Agriculture Organization’s FAOSTAT Food Balance Sheets. It reports average dietary energy available per person per day for countries worldwide. Key variables include:

- Country/Area  
- ISO Code  
- Year  
- Food supply (kcal/capita/day)

The dataset is generally clean and numeric, though some country names required standardization for integration.

## 2. WHO Global Health Observatory – Adult Obesity Prevalence  
Obesity data comes directly from the World Health Organization’s Global Health Observatory (GHO). The dataset provides annual obesity prevalence (BMI ≥ 30) by country, year, and sex. Variables include:

- Country  
- Year  
- Sex  
- Obesity prevalence (%)

Because the FAO dataset is not sex-disaggregated, we use the “Both sexes” category for consistency. Some values include confidence intervals, which required parsing to extract numeric prevalence rates.

## 3. Organization and Storage  
To maintain transparency and reproducibility, we keep a clear separation between raw and processed data:

- `data/raw/` – original downloaded files from FAO and WHO  
- `data/processed/` – cleaned and merged datasets created by our scripts  

This structure makes it easy to trace how each processed file was derived.

## Integration Considerations  
Although both datasets contain country-year indicators, they differ in naming conventions, coverage, and formatting. To integrate them, we:

- Standardized country names via a controlled mapping  
- Filtered data to overlapping years  
- Parsed and cleaned obesity values  
- Selected the “Both sexes” category  
- Dropped unused or inconsistent fields  
- Merged datasets by country and year  

The final integrated dataset, `data/processed/calorie_obesity.csv`, is the basis for our analysis and visualizations.

**Data Quality:**

Before doing any analysis, we first checked the quality of the two datasets we used: the Daily Per Capita Caloric Supply dataset from OWID from FAO and the Adult Obesity dataset from WHO found on Kaggle. Because these two datasets were created by different organizations and collected in different ways, our profiling step found several problems such as different column formats, different meanings for similar fields, missing values and data that didn’t line up. The goal of this step was to spot these issues and decide how to clean and standardize both datasets so we could merge them in a reliable way.

All of our assessments were performed using our custom profiling script which can be found in scripts/profile_data.py, which examined schema details, inspected variable formats, checked unique categories, compared country naming conventions and reported elements requiring standardization. Based on these findings, we implemented the necessary cleaning logic in our clean_data.py script. 

The first part of the assessment focused on evaluating the basic structure and completeness of the OWID/FAO calorie dataset. When we loaded the dataset, we found that it contained 13,050 rows and four columns which are Entity, Code, Year, and Daily calorie supply per person. The dataset was mostly complete, with no missing values in the Entity, Year, or calorie supply columns. The only field that contained missing entries was the Code column, which had more than 1,600 null values. Because the Code column was not needed for merging or analysis and added unnecessary noise, we decided to drop it entirely during the cleaning stage.Other than this column, the dataset was well-structured and all of the data types looked correct. The calorie values were stored as floating-point numbers, and the Year column was stored as an integer. Since this dataset had a clean and consistent structure, we think it served as a good foundation for integration in later phases.

On the other hand, the WHO/Kaggle obesity dataset had more complicated quality problems even though it didn’t have any missing values.This dataset includes 24,570 rows and five columns which are Country, Year, Obesity (%), Sex and an extra unnamed index column. The unnamed column came from the original file export and served no purpose so we removed it. The more significant issue was the format of the Obesity (%) column. The values were stored as strings rather than numbers because each value contained not only a percentage but also a confidence interval. For example, a single entry might appear as “0.5 [0.2–1.1]”. This format made the entire column incompatible with any numerical analysis. To correct this, we extracted the leading numeric value using a regular expression and converted the result into a proper numeric field called Obesity_Rate. This step fixed the validity issue in the dataset by making sure the obesity rates were stored as real numbers instead of text.

The obesity dataset also contained multiple entries for different sex categories, including “Male,” “Female,” and “Both sexes.” Since the calorie dataset does not break values down by sex and only reports national averages, we needed to make sure the two datasets were measuring the same kind of population.. For this reason, we restricted the obesity dataset to include only rows where Sex is “Both sexes.” This step helped keep the concepts consistent and prevented biased results that could happen if we mixed obesity rates broken down by gender with calorie data that only reflects the whole population.

**Findings:**

After cleaning and merging the two datasets, we analyzed how daily calorie supply is related to adult obesity rates over time and across countries. We implemented scripts/analyze_data.py to perform our main analysis and produce visualizations. The script loads data/processed/calorie_obesity.csv, computes global and yearly Pearson correlations between daily calories and adult obesity rates and writes the yearly correlation table to results/yearly_correlation.csv. It also generates multiple figures from scatter plots to country-level time trends and saves them in results/figures/. Overall, the results show a clear pattern that is countries that have more calories available per person usually have higher obesity rates. However, the strength of this relationship is not the same everywhere. Some countries show a very strong connection while others show a weaker one.

We first looked at the yearly correlation between calories and obesity for all countries combined. The values stayed mostly between 0.58 and 0.65, which means the relationship is moderately strong and very consistent across the years. This tells us that, in general, when people have access to more calories, obesity tends to increase as well. The correlation does not jump around too much which suggests the relationship has been stable for a long time.

To understand this better, We focused on four specific countries which are Vietnam, the United States, the United Kingdom and Japan. These countries were chosen because they represent different economic levels, diets and lifestyles.

For Vietnam, calorie supply increased a lot from the 1970s to 2015 from under 2,000 calories to almost 2,900. Obesity also increased, but very slowly from less than 0.3% to a little above 2%. This shows the relationship exists but it is much weaker compared to richer countries. Vietnam is still in an early stage of the “nutrition transition” meaning obesity rates are still low even though calories are rising.
The United States showed one of the strongest relationships. Daily calories increased from around 3,050 to almost 3,900 and obesity rose sharply from around 12 to 15% to more than 36%. The U.S. clearly shows that when a country has very high calorie availability for many years, obesity tends to increase quickly.

The United Kingdom showed a similar pattern even though not as extreme. Calories rose from about 3,100 to around 3,450 and obesity increased from around 10% to more than 27%. This still matches the overall trend which is that more calories tends to lead to more obesity.

Finally, Japan was a special case. Calories increased until around the late 1980s but then slowly decreased. Even though calories went down, obesity still increased from under 1% to around 4%. This suggests that calories alone cannot explain obesity in every country. Cultural habits, physical activity and types of food might also play an important role.

The scatterplots also help support the relationship. When we look at all countries together, the points form a clear upward trend. This means that as daily calories increase, obesity rates also tend to rise even though the exact number may be different from country to country.

In conclusion, our findings show a strong overall pattern which is that higher calorie supply is linked with higher obesity rates. However, the relationship is not exactly the same in every country. Some places, like the U.S. and U.K., show a very strong connection while others like Vietnam and Japan, show slower or more complicated changes. But across the world, the general trend remains as calorie availability rises, adult obesity rates tend to rise too.

**Future work:**

Although our project provides an initial understanding of how calorie supply relates to adult obesity, several directions could meaningfully strengthen both the analytical and data-curation components of the work.

## 1. Incorporate Additional Determinants and Build Richer Models  

Calorie supply alone cannot explain global obesity trends. Future expansions could integrate additional explanatory variables such as diet composition (e.g., sugar or ultra-processed food intake), physical inactivity rates, income or GDP, food price indices, and urbanization. Including these features would allow us to move beyond simple correlations toward multivariate models that more accurately reflect the complexity of obesity. With a richer dataset, we could apply more advanced approaches such as panel regression, mixed-effects models, or country-specific trajectory modeling to identify long-term drivers and quantify the relative importance of calories compared to other factors.

## 2. Improve Country Harmonization and Temporal Consistency  

Our current country-mapping approach corrects most straightforward naming inconsistencies, but it does not fully address historical changes such as country splits, mergers, or renamings. A more robust system—potentially built from ISO country codes, historical lookup tables, or authoritative geopolitical datasets—would improve comparability over long time periods and avoid mismatched records. Additionally, aligning datasets using explicit versioned mappings or controlled vocabularies would make the integrated dataset more stable and reusable for future projects.

## 3. Strengthen Automation, Metadata, and Reproducibility  

There are several steps still requires manual execution. A valuable extension would be to automate the entire process using a Snakemake pipeline, Makefile, or a unified `run_all.py` script. This would allow the full workflow—from raw data to final visualizations—to be reproduced with a single command. We could also improve metadata practices by adding a more detailed data dictionary and adopting standards such as DataCite or schema.org. Publishing the curated dataset in an archival repository would further enhance discoverability, ensure long-term preservation, and make our work easier for others to build upon.


**Reproducing:**

## 1. Clone the repository & Install dependencies
git clone https://github.com/Cynthia387/IS477-Data-Management-Final-Project.git
cd IS477-Data-Management-Final-Project

We recommend using a virtual environment.
pip install -r requirements.txt

## 2. Generate processed data

Run the profiling and cleaning scripts:

python scripts/profile_data.py
python scripts/clean_data.py

These scripts perform the following tasks:

'profile_data.py'
Reads the raw FAO and WHO datasets, checks their structure, summarizes missing values and data types, and writes profiling outputs to results/profile/.

'clean_data.py'
Performs all data-cleaning and integration steps required before analysis.  
  Specifically, the script:
  - Parses obesity prevalence values that appear with confidence intervals and extracts numeric estimates  
  - Harmonizes country names using a controlled mapping to ensure the FAO and WHO datasets align  
  - Filters the WHO dataset to the “Both sexes” category for consistency  
  - Removes unused or inconsistent columns (e.g., redundant codes or indices)  
  - Ensures numeric types are correctly formatted and handles missing years  
  - Merges the FAO and WHO datasets on matching country and year fields  

The key output of this script is:
data/processed/calorie_obesity.csv
which is the integrated dataset used for all subsequent analysis.

## 3. Run the analysis
python scripts/analyze_data.py
This script generates summary tables and visualizations and saves them to the results/ directory.

## 4. Verify outputs

The outputs produced (figures, summary tables, and integrated dataset) should match the descriptions and examples in the Findings section of this report. These steps fully reproduce our workflow end-to-end.

**References:**

## 1. Datasets and Data Sources:

 - **Food and Agriculture Organization of the United Nations (FAO)**. (2024). Food supply and nutrition data. FAO. (Primary source used in the OWID calorie dataset.)

 - **World Health Organization (WHO).**  :Global Health Observatory (GHO) – Obesity prevalence (BMI ≥ 30). Retrieved from  https://www.who.int/data/gho, API access: https://ghoapi.azureedge.net/api/

 - Harris, B., et al. (2015). Historical research contributing to long-term food supply estimates used in the OWID dataset.

 - Floud, R., et al. (2011). The Changing Body: Health, Nutrition, and Human Development in the Western World since 1700. (Referenced by FAO/OWID for historical nutrition data.)

 - Jonsson, U. (1998). Research on global nutrition patterns incorporated into the OWID dataset.

 - Grigg, D. (1995). Historical studies on food consumption used in the OWID dataset.

 - Fogel, R. (2004). The Escape from Hunger and Premature Death. (Used as part of the long-term nutrition series compiled by OWID.)

 - Food and Agriculture Organization of the United Nations. (2000). Early FAO nutrition dataset used in OWID reconstruction.

 - Food and Agriculture Organization of the United Nations. (1949). Foundational global food supply records included in OWID’s long-term dataset.

 - USDA Economic Research Service (ERS). (2015). U.S. food supply data incorporated into OWID’s harmonized dataset.

 - Ritchie, H., & Roser, M. (2023). Diet Compositions and Calorie Supply. Our World in Data. Retrieved from https://ourworldindata.org/diet-compositions (OWID performed major harmonization, processing, and compilation of all FAO and historical sources listed above.)

## 2. Softwares and tools:
 - pandas (Version 2.x). https://pandas.pydata.org/
 - Matplotlib (Version 3.x). https://matplotlib.org/
 - NumPy (Version 1.x). https://numpy.org/
 - Python (Version 3.x). https://www.python.org/





