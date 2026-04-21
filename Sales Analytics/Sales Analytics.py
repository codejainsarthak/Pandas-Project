import pandas as pd
import numpy as np

# Orders Data 
orders = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "Customer": ["Amit", "Neha", "Raj", "Amit", "Simran", "Raj", "Karan", "Neha"],
    "Product_ID": [1, 2, 1, 3, 2, 3, 1, 2],
    "Quantity": [2, 1, 3, 2, 1, 2, 5, 2],
    "Price": [500, 1000, None, 1500, 1000, None, 500, 1000],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Apr"]
})

# Product Data
products = pd.DataFrame({
    "Product_ID": [1, 2, 3],
    "Product_Name": ["Laptop", "Phone", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics"]
})

# print(orders)
# print(products)

df = pd.merge(orders,products,on="Product_ID",how="inner")

df["Price"] = df["Price"].fillna(df["Price"].mean())


df["Total"] = df["Price"] * df["Quantity"]


df["Order_Category"] = np.where(df["Total"]>=3000,"High",(np.where((df["Total"]<3000) & (df["Total"] >1500),"Medium","Low")))

sales_per_product = df.groupby("Product_Name")["Total"].sum()
print(sales_per_product)

sales_per_customer = df.groupby("Customer")["Total"].sum()
print(sales_per_customer)

average_per_customer = df.groupby("Customer")["Total"].mean()
print(average_per_customer)

sales_per_month = df.groupby("Month")["Total"].sum()
print(sales_per_month)

highest_sales_month = df.groupby("Month")["Total"].sum().idxmax()

highest_sales_product = df.groupby("Product_Name")["Total"].sum().idxmax()
