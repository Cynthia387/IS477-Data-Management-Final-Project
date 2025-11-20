**Update on tasks:**

At this point, we have completed all the main preparation tasks outlined in our project plan, and our progress is on schedule.

We first created the full repository structure described in our plan. The folders /data/raw, /scripts were all set up as planned. We uploaded our two raw datasets into /data/raw/ and removed placeholder files like .gitkeep, and cleaned the structure so that everything is easy to navigate. This gives us a clear starting point for later steps such as cleaning, integration, and analysis.

Next, we completed the data acquisition work. For the calorie supply dataset from Our World in Data , we created a Python script called acquire_data.py in the /scripts folder. This script automatically downloads the Our World in Data CSV file using the requests library, creates any necessary folders, saves the dataset into /data/raw, and computes its SHA-256 hash to support data integrity. The obesity dataset cannot be downloaded programmatically because it is from Kaggle which requires us to log in in order to download it, so we uploaded it manually and documented this limitation. Even though it was uploaded manually, we still computed its SHA-256 hash to ensure reproducibility and to follow the project requirements.

We also wrote a second script, verify_checksums.py, which verifies the integrity of all raw datasets using the hashes stored in a checksums.txt file located at the root of the repository. This script reads each file’s expected hash, compares it to the actual hash on disk, and reports whether the file matches or is missing. This step satisfies the requirement of having scripts that help others reproduce our exact data and verify that nothing has changed. We are currently working on writing clear documentation that explains how someone else can acquire our datasets including instructions for downloading the Our World in Data file, manually obtaining the Kaggle file and verifying file integrity using the provided SHA-256 checksums. This documentation will be added to the /docs folder in the next milestone. 

Since the initial setup, we have successfully completed all core data preparation tasks (Profiling, Cleaning, and Integration). This phase included analyzing the datasets for standardization needs, developing scripts/clean_data.py to fix country name discrepancies and clean core variables, and creating scripts/integrate_data.py to merge the two resulting clean datasets into the final analysis-ready file, data/processed/calorie_obesity.csv. The detailed findings are documented in docs/data_profile.md.

**Team contributions:**

**Tracie Huynh thuyn3:** For team contributions during this milestone, I completed most of the technical setup and scripting tasks. I created the repository structure, uploaded the raw datasets, wrote the data acquisition script acquire_data.py, implemented SHA-256 integrity functions, created the checksum file checksums.txt, wrote the verification script verify_checksums.py, cleaned up folder issues, and documented the data collection and acquisition steps. I also helped drafting this milestone report and made sure that we are on track. Also, I tested all of my scripts inside Visual Studio Code to make sure they run correctly and produce the expected outputs. I also checked the raw datasets inside VS Code to confirm their structure and make sure they are ready for cleaning and integration in the next milestone. I also spent time fixing path issues and making sure our directory layout matches the project requirements. 

**Cynthia Shen xs49:** My primary focus has been the **Data Profiling, Cleaning, and Integration** stages. Firstly, I collaborate with the initial GitHub repository setup. Then I successfully profiled the raw datasets, documented the findings in **`docs/data_profile.md`**, and developed **`scripts/clean_data.py`** to handle critical standardization needs. This included implementing the necessary `COUNTRY_MAP` and logic for filtering the 'Both sexes' data and extracting numeric obesity rates. I subsequently developed and executed **`scripts/integrate_data.py`**, which successfully merged the two cleaned datasets (`clean_obesity.csv` and `clean_calories.csv`) on country and year, producing the final analysis-ready file, **`data/processed/calorie_obesity.csv`**. 

**Timeline & Updates**
| Date | Task | Lead | Status |
| :--- | :--- | :--- | :--- |
| Oct 17 – Oct 19 | Setup & Acquisition | T, C | **Completed** |
| Oct 20 – Oct 24 | Data Profiling & Structure Review | C, T | **Completed** |
| Oct 25 – Oct 29 | Data Cleaning & Standardization | Cynthia | **Completed** |
| Oct 30 – Nov 3 | Integration & Validation | C, T | **Completed** |
| Nov 4 – Nov 8 | Exploratory Analysis (EDA) | Tracie | **In Progress** |
| Nov 9 – Nov 13 | Data Quality & Ethical Review | Tracie | On Track |
| **Nov 14 – Nov 18** | **Status Report (Milestone 3)** | T, C | **Finish** |
| Nov 19 – Nov 25 | Workflow Automation | Cynthia | On Track |
| Nov 26 – Dec 1 | Final Analysis & Visualization | T, C | On Track |
| Dec 2 – Dec 3 | Final Assembly & Internal Review | C, T | On Track |
| Dec 10 | Final Submission | Both | On Track |
