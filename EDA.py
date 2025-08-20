#Step3
import pandas as pd

df = pd.read_csv('sample_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

print("Monthly Sales Revenue:\n", df.groupby('Month')['Revenue'].sum())
print("\nMonthly Sales by Product:\n", df.groupby(['Month', 'Product'])['Revenue'].sum())
print("\nTotal Sales by Product:\n", df.groupby('Product')['Revenue'].sum())
