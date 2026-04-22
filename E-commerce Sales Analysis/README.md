# E-commerce Sales Analysis (Datetime Project)

## Project Overview

This project analyzes e-commerce sales data using Python (Pandas and NumPy) with a focus on **date-time operations**. The goal is to understand sales trends over time, identify high-performing periods, and extract meaningful insights from transactional data.

---

## Dataset Description

The dataset contains order-level information:

- Order_ID → Unique order identifier
- Customer → Customer name
- Amount → Order value (contains missing values)
- Order_Date → Date of order

---

## Steps Performed

### Data Cleaning

- Converted `Order_Date` to datetime format using `pd.to_datetime()`
- Handled missing values in `Amount` using mean imputation

---

### Feature Engineering (Datetime)

Extracted useful components from the date:

- Year
- Month
- Day
- Day_Name (e.g., Monday, Tuesday)

---

### Data Analysis

#### Monthly Sales

- Calculated total sales per month using `groupby()`

#### Best Performing Month

- Identified the month with highest sales using `idxmax()`

#### Sales by Day

- Analyzed total sales based on day of the week

---

### Data Filtering

- Filtered orders after a specific date (March 2024)

---

### Business Logic

- Created `Amount_Category` column:
  - High Value (≥ 2500)
  - Normal (< 2500)

---

## Key Learnings

- Working with datetime data in Pandas
- Extracting date components using `.dt`
- Handling missing values using `fillna()`
- Aggregating data using `groupby()`
- Identifying top-performing segments using `idxmax()`
- Applying conditional logic using `np.where()`

---

## Tools Used

- Python
- Pandas
- NumPy

---

## How to Run

1. Install required libraries:

   ```bash
   pip install pandas numpy
   ```

2. Run the Python script:

   ```bash
   python your_script_name.py
   ```

---

## Conclusion

This project demonstrates how to perform time-based data analysis using Pandas. It highlights the importance of datetime processing in real-world datasets and provides a foundation for more advanced time-series analysis.
