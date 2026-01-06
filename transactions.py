#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 13:42:33 2025

@author: gio_avondo
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#Part A: Load & Inspect Data

df = pd.read_csv("transactions.csv")

print(df.head(3), '\n\n')
print(df.shape, '\n\n')
print(df.info(), '\n\n')
print(df.describe(include = 'all'), '\n\n')

#Part B: Data Cleansing

#Column Name Standardisation

df.columns = (
    df.columns
      .str.replace(r"[£()]", "", regex=True)
      .str.strip()
      .str.lower()
      .str.replace(' ', '_')
)
print(list(df.columns), '\n\n')

#Fix Data Types + Monthly Features

df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors = 'coerce', dayfirst = True)
df['year'] = df['transaction_date'].dt.year
df['month'] = df['transaction_date'].dt.month



df['unit_price'] = (
    df['unit_price']
    .str.replace(r"[£$,%]", "", regex=True)
    .pipe(pd.to_numeric, errors="coerce")
)

#Missing Data + cleaned channel/category/Product column

df["channel"] = (
    df["channel"]
    .str.strip()
    .str.upper()
)

df['product'] = (df['product'].str.strip())
    
df["category"] = (
    df["category"]
    .str.strip()
    .str.capitalize()
)

df["returned"] = (
    df["returned"]
    .str.strip()
    .fillna('Unknown')
)
             
print((df.isna()|df.eq("")|df.eq(" ")).sum(), '\n\n')


df['quantity'] = (
    df['quantity']
    .abs()
    .fillna(df['quantity'].median())
)

df['transaction_date'] = df['transaction_date'].fillna("Unknown")

#Quantity/totals check

df['total'] = df['unit_price']*df['quantity']

#Duplicates

num_dupes = df.duplicated().sum()
duplicated = df.duplicated()
print('Duplicated row(s): \n', df[df.duplicated()], '\n\n')
df = df.drop_duplicates()
print(num_dupes, ' Duplicate(s) removed', '\n\n')

#Part C: Data Munging

#Net Revenue (Excludes Returned Transactions)

df['revenue'] = 0.0
df.loc[df["returned"] == "No", "revenue"] = df['total']

#Transaction Value

df['high_value'] = False
df.loc[df["total"] > 1000, "high_value"] = True

#Groupby Revenue/Returns by Category

returns_by_channel = (
    df.groupby("channel")
      .agg(
          return_count=("returned", lambda s: (s == "Yes").sum())
      )
)

revenue_by_category = (
    df.groupby("category")["revenue"]
      .sum()
      .reset_index() #If you want index shown
)

print(revenue_by_category, '\n\n')
print(returns_by_channel, '\n\n')

pivot = pd.pivot_table(
    df,
    values="total",
    index="category",
    columns="channel",
    aggfunc="sum",
    observed = False
)

print(pivot, '\n\n')#Note that groupby revenue and pivot table (total) are different to account for returns and unknown returns

spend_avg = df["revenue"].sum() / df["customer_id"].nunique()
avg_basket = df['quantity'].sum()/df['transaction_id'].nunique()
print('Average Basket Size: ', avg_basket)
print('Average Spend per Customer: ', spend_avg)
print('Number of Transactions: ', df['transaction_id'].nunique(), '\n\n')

# 7) Customer-level aggregation
customer_summary = (
    df.groupby("customer_id")
      .agg(
          total_spend=("revenue", "sum"),
          transactions=("transaction_id", "count"),
          avg_basket=("total", "mean")
      )
      .sort_values("total_spend", ascending=False)
)

print("\nCustomer Summary:")
print(customer_summary, '\n\n')


print(df, '\n\n')

print(df.info(), '\n\n')

print(df['total'].describe(), '\n\n')

print("\nMissing values after cleaning:")
print(df.isna().sum().sort_values(ascending=False))

df.to_csv("cleaned_transactions.csv", index=False)
print("\nSaved cleaned_transactions.csv")


