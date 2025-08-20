#Step4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv('sample_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Basic stats
print("Total Revenue:", df['Revenue'].sum())
print("Total Units Sold:", df['Units Sold'].sum())

# Plot using seaborn
sns.set(style="whitegrid")
sns.lineplot(x='Date', y='Revenue', data=df, marker='o')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
