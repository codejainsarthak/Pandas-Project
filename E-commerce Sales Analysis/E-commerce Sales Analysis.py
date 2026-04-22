import pandas as pd
import numpy as np

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Customer": ["Amit", "Neha", "Raj", "Simran", "Amit", "Raj", "Neha", "Karan"],
    "Amount": [2000, 1500, None, 3000, 2500, None, 1800, 2200],
    "Order_Date": [
        "2024-01-05", "2024-01-15", "2024-02-10", "2024-02-20",
        "2024-03-05", "2024-03-18", "2024-04-01", "2024-04-10"
    ]
}

df = pd.DataFrame(data)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])


df["Amount"] = df["Amount"].fillna(df["Amount"].mean())

print(df)


df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Day"] = df["Order_Date"].dt.day
df["Day_Name"] = df["Order_Date"].dt.day_name()

sales_per_month = df.groupby("Month")["Amount"].sum()

filter_data = df[df["Order_Date"]> "31-03-2024" ]

highest_sales_month = df.groupby("Month")["Amount"].sum().idxmax()
sales_per_dayname = df.groupby("Day_Name")["Amount"].sum()


df["Amount_Category"] = np.where(df["Amount"] >= 2500,"High Value" , "Normal")

print(df)
