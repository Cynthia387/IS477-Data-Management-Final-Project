**Overview:**
The overall goal of this project is to explore the relationship between the average daily calorie supply and adult obesity rates across different countries and years. For this project, we will use data from two trusted sources which are the “Total daily supply of calories per person (1961-2022)” dataset from Our World in Data (based on the UN Food and Agriculture Organization FAO data) and the “Obesity Among Adults by Country (1975-2016)” dataset from Kaggle (based on World Health Organization WHO data). 
These two datasets come from different, trustworthy sources and have different structures making them suitable for integration and analysis. Together, they will help us see how the total amount of calories available per person per day in a country is related to the percentage of adults who are classified as obese in that country.

**Research questions:**
As mentioned above, this project focuses on understanding the connection between food energy supply and obesity levels across different countries. Therefore, our main research questions are:

- Is there a relationship between the average daily calorie supply per person and the adult obesity rate in each country?

- Do countries that have more calories available per person tend to have higher obesity rates?

- How has the relationship between calorie supply and obesity rates changed across different years or regions?

**Team:**
**Tracie Huynh:** I will take the lead on finding and preparing the datasets we will use for this project. Once the data is collected, I’ll help Cynthia with cleaning, organizing, and integrating the two datasets into a single and organized file for analysis. I’ll also create visualizations that help show patterns or relationships between calorie supply and obesity rates in different countries and years. In addition, I’ll document each step of our workflow so that our process is clear and easy to follow. I will make sure that we stay on schedule and that our project follows all the course’s requirements and rules. I will also help write and organize the final report to make sure it is complete and clearly explained and ready to submit on time.
**Cynthia Shen:** I will be responsible for data integration, cleaning, and reproducibility. After Tracie collects the datasets, I will assess their structure, check schema compatibility, standardize field names, and harmonize country and year variables. I will develop data quality checks (completeness, validity, consistency) and handle missing values systematically. Once both datasets are standardized, I will merge them into a single analysis-ready dataset and document the process. I will also be responsible for workflow automation and reproducibility, including organizing the GitHub repository, writing clear markdown documentation, creating requirements.txt, and ensuring all steps can be reproduced in Jupyter using versioned scripts. In addition, I will co-lead data validation and metadata documentation, maintain progress tracking in Git commits, and help write the methods, data, and results sections of the report to ensure clarity and compliance with course requirements.

**Dataset:**
The **first dataset** is called **“Total Daily Supply of Calories per Person (1961-2022)”** from Our World in Data which is based on data from the Food and Agriculture Organization (FAO). It shows the average number of calories available per person per day in each country and year. One thing to remember is this data measures how much food energy people have access to not how much they actually eat. The file is in CSV format and includes columns for country, year, and total calories per person per day. It was downloaded manually by us from the Our World in Data website and is openly available under a Creative Commons license. Since it does not include any personal or sensitive information, we believe there are no ethical concerns when using it.
The **second dataset** is called **“Obesity Among Adults by Country (1975-2016)”** from Kaggle which is based on the World Health Organization (WHO) data. It includes the percentage of adults who are obese (with a BMI of 30 or higher) in each country and year. It is also a CSV file with columns for country, year, and obesity rate. It was also downloaded manually by us from Kaggle and is publicly available so there are no privacy or ethical issues.

**Timeline:**

- Oct 17 – Oct 19	Setup & Acquisition	Create GitHub repository, define folder structure (data/raw, data/clean, scripts, results), and document licensing for both datasets. Download datasets from OWID (FAO) and Kaggle (WHO). Record SHA-256 checksums and metadata.	Tracie (download & metadata), Cynthia (repo setup)

- Oct 20 – Oct 24	Data Profiling & Structure Review	Inspect datasets in Jupyter (using pandas), summarize key columns, missing values, and data types. Produce initial profiling notebook and write short summary (docs/data_profile.md).	Cynthia (profiling & schema notes), Tracie (summary visual checks)

- Oct 25 – Oct 29	Data Cleaning & Standardization	Clean field names, normalize country and year formats, handle missing or outlier values, and document all transformations. Save interim cleaned datasets to data/clean/.	Cynthia

- Oct 30 – Nov 3	Integration & Validation	Merge datasets on country and year for 1975–2016, validate merged entries, and generate coverage report (number of valid countries and years). Output data/processed/calorie_obesity.csv.	Cynthia (merge logic), Tracie (validation check)

- Nov 4 – Nov 8	Exploratory Analysis (EDA)	Conduct initial EDA on integrated dataset: compute descriptive stats, correlation matrix, and create preliminary visualizations (global and regional trends). Identify insights to refine research questions.	Tracie

- Nov 9 – Nov 13	Data Quality Assessment & Ethical Review	Assess data completeness, identify anomalies (e.g., calorie <800 or >5500, obesity >60%), and verify compliance with data licenses. Add findings to docs/data_quality.md.	Cynthia

- Nov 14 – Nov 18	Status Report (Milestone 3)	Write and finalize StatusReport.md summarizing progress: dataset handling, integration, EDA visuals, and challenges. Include dataset references and repository links.	Tracie (EDA visuals & interpretation), Cynthia (methods & workflow summary)

- Nov 19 – Nov 25	Workflow Automation & Reproducibility	Create Jupyter-based workflow or run_all.sh to automate the full pipeline (clean → integrate → analyze → visualize). Add environment files (requirements.txt) and metadata records.	Cynthia

- Nov 26 – Dec 1	Final Analysis & Visualization Refinement	Conduct final analytical comparisons (e.g., time-series regression or correlation tests). Finalize high-quality figures and write visual captions.	Tracie (analysis & plots), Cynthia (statistical checks)

- Dec 2 – Dec 3	Final Assembly & Internal Review	Draft README.md (overview, data lifecycle, findings, reproducibility steps), proofread report, test workflow, and tag final release on GitHub.	Cynthia & Tracie

- Dec 10	Final Submission	Submit GitHub release URL and Box folder link via Canvas.	Both

**Constraints:**

- Temporal mismatch: The FAO calorie dataset covers 1961–2022, while the WHO obesity dataset stops at 2016. To maintain alignment, we will analyze only the overlapping period 1975–2016.

- Country naming differences: Variations such as “Côte d’Ivoire” vs. “Ivory Coast” or “Russian Federation” vs. “Russia” will require manual mapping to standard ISO-3 codes.

- Data meaning limitation: Calorie supply measures availability, not actual consumption; obesity rates measure population health outcomes. This limits causal interpretation—our findings will describe correlation, not causation.

- Data coverage gaps: Some countries have missing records or inconsistent time intervals. These will reduce sample size and may bias results toward well-documented countries.


**Gaps and Future Considerations:**

- Lag effects: We plan to test whether obesity rates correlate more strongly with calorie supply from previous years (e.g., a 3-year lag), but this depends on remaining time after the main analysis.

- Regional grouping: We have not yet finalized which classification system (UN M49 or World Bank regions) to use for aggregating regional trends. This decision will be made during EDA.

- Data licensing: We must still confirm and cite the exact license text from Our World in Data (FAO-based) and Kaggle (WHO-based) in our final report.

- Quality validation: Additional manual validation may be needed to verify countries with extreme calorie or obesity values, ensuring they are not due to data errors.
