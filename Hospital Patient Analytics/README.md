# Hospital Patient Analytics (Pandas Project)

## Project Overview

This project analyzes hospital patient data using Python (Pandas and NumPy). It simulates real-world healthcare analytics by focusing on patient costs, hospital stays, and departmental performance.

The objective is to clean and transform data, merge multiple datasets, and generate insights that help understand treatment patterns and resource utilization.

---

## Dataset Description

### 1. Patients Table

- Patient_ID → Unique identifier for each patient
- Name → Patient name
- Age → Age of patient
- Gender → Gender of patient
- Dept_ID → Department reference
- Treatment_Cost → Cost of treatment (contains missing values)
- Days_Admitted → Number of days patient stayed in hospital

### 2. Departments Table

- Dept_ID → Unique department identifier
- Dept_Name → Name of department

### 3. Doctors Table

- Dept_ID → Department reference
- Doctor_Name → Assigned doctor

---

## Steps Performed

### Data Cleaning

- Handled missing values in `Treatment_Cost` using mean imputation

### Feature Engineering

- Created `Cost_per_day` column → Treatment_Cost / Days_Admitted
- Created `Patient_Category` column:
  - High Cost (≥ 40000)
  - Medium Cost (20000–40000)
  - Low Cost (< 20000)

### Data Merging

- Merged patients with departments using `Dept_ID`
- Merged the result with doctors to include doctor information

### Data Analysis (GroupBy)

- Average treatment cost per department
- Total number of patients per department
- Maximum days admitted per department

### Business Insights

- Identified patient with highest treatment cost
- Identified patient with longest hospital stay
- Identified patients with high cost and long stay

### Advanced Analysis

- Calculated department-wise average treatment cost
- Merged department averages back into main dataset
- Identified patients whose treatment cost is higher than their department average

---

## Key Learnings

- Handling missing data using `fillna()`
- Creating derived columns using arithmetic operations
- Applying conditional logic using `np.where()`
- Merging multiple datasets using `pd.merge()`
- Performing grouped analysis using `groupby()`
- Identifying top records using `idxmax()`
- Sorting and filtering data effectively
- Understanding how to merge aggregated data back into the original dataset

---

## Tools Used

- Python
- Pandas
- NumPy

---

## How to Use This Project

1. Clone the repository
2. Run the script in a Python environment
3. Analyze the outputs printed in the console
4. Modify the dataset to explore additional scenarios

---

## Conclusion

This project demonstrates practical data analysis techniques in a healthcare context using Pandas. It highlights how structured data processing and analysis can provide meaningful insights into hospital operations and patient management.
