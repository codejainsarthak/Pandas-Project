import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\PYTHON\pandas final\time.csv")

print(df)
df = df.drop_duplicates(subset=["order_id" , "store_id"])
print(df)
df["order_date"] = pd.to_datetime(df["order_date"], errors= "coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors= "coerce")
df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors= "coerce")
print(df[["order_date" , "ship_date", "delivery_date"]])
print(df.isna().sum())

df =df.dropna(subset=["order_date" , "ship_date" , "delivery_date"])
print(df)
df["category"] = df["category"].str.lower().str.strip()
df["city"] = df["city"].str.lower().str.strip()


print(df[["city" , "category"]])


cate_map = {
    "elec": "Electronics",
    "home": "Home",
    "fashion" : "Fashion",
    "electronics": "Electronics"
}

city_map = {
    "mumbai" : "Mumbai",
    "delhi" : "Delhi"
}

df["category"] = df["category"].replace(cate_map)
df["city"] = df["city"].replace(city_map)

print(df[["city" , "category"]])

print(df["revenue"])
print(df["revenue"].describe)

df["revenue"] = df["revenue"].mask(df["revenue"] < 0)
df["revenue"] = df["revenue"].fillna(df["revenue"].median())

print(df[["revenue" , "category"]])
top_city = df.groupby("city")["revenue"].sum().idxmax()
print(top_city)

best_category = df.groupby("category")["revenue"].sum().idxmax()
print(best_category)
df["delivery_days"] = (df["delivery_date"] - df["order_date"]).dt.days

df["shipping_delay"] = (df["ship_date"] - df["order_date"]).dt.days
print(df["shipping_delay"])

print(df["delivery_days"])