#Step1
# clean_data.py

import pandas as pd

# Load raw data
df = pd.read_csv('sample_sales_data.csv')  # Adjust path if needed

# ----- 1. Inspect the dataset -----
print("🔹 First few rows:")
print(df.head())

print("\n🔹 Dataset info:")
print(df.info())

print("\n🔹 Summary of missing values:")
print(df.isnull().sum())

# ----- 2. Handle missing values -----
# Option 1: Drop rows with any missing values
df = df.dropna()

# (Optional) If you'd prefer to fill missing values instead:
# df['Revenue'] = df['Revenue'].fillna(0)

# ----- 3. Fix data types -----
# Convert 'Date' column to datetime
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Invalid dates become NaT
    df = df.dropna(subset=['Date'])  # Drop rows where date conversion failed

# Convert 'Revenue' to numeric (if needed)
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
df = df.dropna(subset=['Revenue'])

# ----- 4. Remove duplicates -----
df = df.drop_duplicates()

# ----- 5. Save cleaned data -----
df.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Data cleaned and saved to 'cleaned_sales_data.csv'")