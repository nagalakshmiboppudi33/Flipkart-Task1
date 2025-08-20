#Step2
import pandas as pd

# Load CSV file
csv_data = pd.read_csv('sample_sales_data.csv')

# Comment these out if you don't have the files
# excel_data = pd.read_excel('sales_data.xlsx')
# json_data = pd.read_json('sales_data.json')

# Combine only the CSV for now
combined = csv_data  # just one dataframe

# Save combined data
combined.to_csv('combined_sales_data.csv', index=False)

print("Combined data saved. Only CSV used because others are missing.")
print(combined.head())
