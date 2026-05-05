# E-commerce Time Series Analysis with Pandas

## Overview

This project focuses on cleaning and analyzing a messy e-commerce dataset using Pandas.
It demonstrates real-world data preprocessing, time series feature engineering, and extraction of business insights.

---

## Objectives

- Clean inconsistent date formats and handle missing values
- Standardize categorical data (city, category)
- Handle invalid revenue values (negative and missing)
- Create time-based features
- Extract meaningful business insights

---

## Dataset Features

The dataset includes:

- `order_id`, `store_id`
- `order_date`, `ship_date`, `delivery_date`
- `category`, `city`
- `revenue`

---

## Data Cleaning Steps

### 1. Remove Duplicates

Duplicate rows based on `order_id` and `store_id` are removed.

### 2. Datetime Conversion

All date columns are converted using:

- `pd.to_datetime(errors="coerce")`
- Invalid values are converted to `NaT`

### 3. Missing Value Handling

- Rows with missing critical dates are removed
- Revenue is cleaned by:
  - Converting negative values to missing (`NaN`)
  - Filling missing values using median

### 4. Data Standardization

- Converted text to lowercase and removed extra spaces
- Mapped inconsistent values:
  - Categories → Electronics, Home, Fashion
  - Cities → Delhi, Mumbai

---

## Feature Engineering

### Delivery Time

```
Delivery Days = Delivery Date - Order Date
```

### Shipping Delay

```
Shipping Delay = Ship Date - Order Date
```

---

## Analysis Performed

### Top Performing City

Identified the city with the highest total revenue.

### Best Category

Determined the category generating the highest revenue.

### Time Metrics

- Delivery duration analysis
- Shipping delay analysis

---

## Tech Stack

- Python
- Pandas
- NumPy

---

## Key Learnings

- Handling messy real-world datasets
- Working with time series data
- Applying data cleaning best practices
- Feature engineering for business insights

---

## Future Improvements

- Add data visualization using Matplotlib or Seaborn
- Perform time-series resampling for trend analysis
- Detect anomalies in delivery times
- Build dashboards

---

## How to Run

```
pip install pandas numpy
python your_script.py
```

---

## Author

Sarthak Jain
