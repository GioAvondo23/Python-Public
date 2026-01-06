#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:20:18 2025

@author: gio_avondo
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# ===== Part A: Load & Inspect =====
df = pd.read_csv("data.csv", encoding = 'latin1')
x = False
if x == True:
    print(df, '\n\n')
    
    headers = list(df.columns) #tells you the column titles
    print(headers)
    
    print(df.head(2), '\n\n') #lists the top n rows
    print(df.tail(2), '\n\n') #lists the bottom n rows
    print(df.index, '\n\n') #tells you how many columns there are
    print(df[" Name "], '\n\n') #Outputs a specific column
    print(df.describe(include = 'all'), '\n\n') #brief statistical summary of relevant columns
    print(df.loc[0], '\n\n') #Outputs a specific row
    print(df[df["Customer ID"] < 1005], '\n\n') #Boolean Indexing
    print(df.shape, '\n\n') #Number of rows and collumns
    
    info = df.info() #non-null elements per column and datatype/memory (it's a health check)
    print(info, '\n\n')




# ===== Part B: Cleanse =====

# 1) Standardise column names
print(list(df.columns))
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(' ', '_')
)
print(list(df.columns), '\n\n')

# 2) Fix data types

df["signup_date"] = pd.to_datetime(df["signup_date"], errors = 'coerce', dayfirst = True)

cols = ['spend_(£)', 'discount_%', 'age', 'annual_income_(£)', 'loyalty_score']
df[cols] = df[cols].apply(
    lambda s: s.str.replace(r"[£$,%]", "", regex=True)
              .pipe(pd.to_numeric, errors="coerce")
)



# 3) Missing values
print((df.isna()|df.eq("")|df.eq(" ")).sum(), '\n\n') #outputs empty cells per column (remove .sum() for a dataframe of True/False outputs)
df.replace(" ", np.nan, inplace=True)

print(df.info(), '\n\n')
for col in df.columns:
    if df[col].dtype.kind in "biufc":  # numeric columns
        df[col] = df[col].fillna(df[col].median())
    else:  # non-numeric columns
        df[col] = df[col].fillna(f"Mode - {df[col].mode()[0]}")



# 4) Duplicates

num_dupes = df.duplicated().sum()
duplicated = df.duplicated()
df = df.drop_duplicates()
print(num_dupes, ' Duplicate removed', '\n\n')


# 5) Outliers (pick a numeric column)
q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3 - q1
print('Age IQR: ', (df["age"].quantile(0.75) - df["age"].quantile(0.25)), '\n\n')


lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
#df["age"] = df["age"].clip(lower, upper) #winsorising (cap the outliers)
df = df[(df["age"] >= lower) & (df["age"] <= upper)] #Outliers were removed since capping the ages would be innaccurate data


# ===== Part C: Munging / Feature Engineering =====

#Create Cleaned Categorical Column

df["country_clean"] = (
    df["country"]
    .str.strip()
    .str.upper()
)

#Derived Numerical Feature (Spending - Income Ratio)

df["spend_ratio"] = df["spend_(£)"] / df["annual_income_(£)"]

#Bin a Numeric Variable

bins = [0, 18, 25, 40, 60, 120]
labels = ["Child (0-18)", "Young (18-25)", "Adult (25-40)", "Mid (40-60)" , "Senior (60+)"]

df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

#Groupby Summary Statistics
summary = (
    df.groupby("country_clean")
      .agg(
          customers=("customer_id", "count"),
          avg_spend=("spend_(£)", "mean"),
          median_loyalty=("loyalty_score", "median")
      )
      .sort_values("avg_spend", ascending=False)
)

print(summary, '\n\n')

#Pivot Table 2D summary

pivot = pd.pivot_table(
    df,
    values="spend_(£)",
    index="country_clean",
    columns="age_group",
    aggfunc="mean",
    observed = False
)

print(pivot)



# ===== Part D: Final Checks & Save =====
print("\nINFO AFTER CLEANING:")   # ✅ required .info() section again
print(df.info())

print("\nMissing values after cleaning:")
print(df.isna().sum().sort_values(ascending=False))

print("\nFINAL HEAD:")
print(df.head(10))

df.to_csv("cleaned_data.csv", index=False)
print("\nSaved cleaned_data.csv")
