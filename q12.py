import pandas as pd

# Create a sample DataFrame
data = {'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Sales': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)

# Get the top 5 products by sales
top_5_products = df['Product'].value_counts().head(5)

print("The top 5 products by sales are:")
print(top_5_products)
