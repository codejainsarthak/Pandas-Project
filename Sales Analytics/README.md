# Sales & Orders Analytics (Pandas Mini Project)

## Project Overview

This project analyzes a small sales dataset using Python (Pandas and NumPy) to simulate real-world business analytics tasks.

The goal is to clean the data, merge datasets, perform aggregations, and extract meaningful insights such as:

* Total sales
* Customer behavior
* Product performance
* Monthly trends

---

## Dataset Description

### 1. Orders Table

* Order_ID → Unique order identifier
* Customer → Customer name
* Product_ID → Product reference
* Quantity → Number of items purchased
* Price → Price per unit (contains missing values)
* Month → Month of order

### 2. Products Table

* Product_ID → Unique product identifier
* Product_Name → Name of product
* Category → Product category

---

## Steps Performed

### Data Cleaning

* Handled missing values in `Price` using mean imputation

### Feature Engineering

* Created `Total` column → Quantity × Price
* Created `Order_Category` column:

  * High (≥ 3000)
  * Medium (1500–3000)
  * Low (< 1500)

### Data Merging

* Merged Orders and Products using `Product_ID`

### Data Analysis (GroupBy)

* Total sales per product
* Total sales per customer
* Average order value per customer
* Monthly sales analysis

### Business Insights

* Identified product with highest sales
* Identified month with highest sales

---

## Key Learnings

* Data cleaning using `fillna()`
* Creating new columns using arithmetic operations
* Conditional logic using `np.where()`
* Data merging using `pd.merge()`
* Aggregation using `groupby()`
* Finding top performers using `idxmax()`

---

## Not Covered in This Project (Future Improvements)

This project focuses on core Pandas fundamentals. The following important concepts are not included:

* `groupby().transform()` for row-level comparison
* `pivot_table()` for advanced summarization
* Time-based analysis using datetime functions
* Advanced joins (left, right, outer, cross in depth)
* Handling duplicates and outliers
* Visualization (Matplotlib / Seaborn)
* Performance optimization and vectorization best practices
* Working with large datasets (chunking, memory optimization)

---

## Conclusion

This project demonstrates foundational data analysis skills using Pandas. It is suitable as a beginner-to-intermediate level project and serves as a base for more advanced analytics and real-world data science workflows.
